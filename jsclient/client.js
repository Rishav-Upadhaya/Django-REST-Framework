const contentContainer = document.getElementById("content-container");
const loginForm = document.getElementById("login-form");
const searchForm = document.getElementById("search-form");
const baseEndpoint = "http://localhost:8000/api";

// Improved form handling
if (loginForm) {
  loginForm.addEventListener("submit", handleLogin);
}

if (searchForm) {
  searchForm.addEventListener("submit", handleSearch);
}

function handleLogin(event) {
  event.preventDefault();
  const loginEndpoint = `${baseEndpoint}/token/`;
  let loginFormData = new FormData(loginForm);
  let loginObjectData = Object.fromEntries(loginFormData);
  let bodyStr = JSON.stringify(loginObjectData);

  const options = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: bodyStr,
  };

  fetch(loginEndpoint, options)
    .then((response) => {
      if (!response.ok) {
        throw new Error(`Login failed: ${response.status}`);
      }
      return response.json();
    })
    .then((authData) => {
      handleAuthData(authData, getProductList);
    })
    .catch((err) => {
      console.error("Login error:", err);
      if (contentContainer) {
        contentContainer.innerHTML = `<div class="error">${err.message}</div>`;
      }
    });
}

// Improved token refresh
function refreshToken() {
  const refreshEndpoint = `${baseEndpoint}/token/refresh/`;
  const refresh = localStorage.getItem("refresh");

  if (!refresh) {
    return Promise.reject("No refresh token available");
  }

  return fetch(refreshEndpoint, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      refresh: refresh,
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      localStorage.setItem("access", data.access);
      return data.access;
    });
}

function validateJWTToken() {
  const endpoint = `${baseEndpoint}/token/verify/`;
  const token = localStorage.getItem("access");

  if (!token) {
    return Promise.reject("No token found");
  }

  const options = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      token: token,
    }),
  };

  return fetch(endpoint, options)
    .then((response) => {
      if (!response.ok) {
        return refreshToken();
      }
      return token;
    })
    .catch((err) => {
      console.error("Token validation failed:", err);
      return refreshToken();
    });
}

// Improved search functionality
function handleSearch(event) {
  event.preventDefault();
  let formData = new FormData(searchForm);
  let data = Object.fromEntries(formData);
  let searchParams = new URLSearchParams(data);
  const endpoint = `${baseEndpoint}/search/?${searchParams}`;

  validateJWTToken()
    .then((token) => {
      const options = {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Token ${token}`,
        },
      };
      return fetch(endpoint, options);
    })
    .then((response) => response.json())
    .then((data) => {
      if (data.code === "token_not_valid") {
        throw new Error("Invalid token");
      }
      displaySearchResults(data);
    })
    .catch((err) => {
      console.error("Search error:", err);
      if (contentContainer) {
        contentContainer.innerHTML = `<div class="error">Search failed: ${err.message}</div>`;
      }
    });
}

function displaySearchResults(data) {
  if (!contentContainer) return;

  if (data && data.hits && data.hits.length > 0) {
    const htmlStr = data.hits
      .map((result) => `<li class="search-result">${result.title}</li>`)
      .join("");
    contentContainer.innerHTML = `<ul class="results-list">${htmlStr}</ul>`;
  } else {
    contentContainer.innerHTML = "<p>No results found</p>";
  }
}

function handleAuthData(authData, callback) {
  localStorage.setItem("access", authData.access);
  localStorage.setItem("refresh", authData.refresh);
  if (callback) {
    callback();
  }
}

function writeToContainer(data) {
  if (contentContainer) {
    contentContainer.innerHTML =
      "<pre>" + JSON.stringify(data, null, 4) + "</pre>";
  }
}

function getFetchOptions(method, body) {
  return {
    method: method === null ? "GET" : method,
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${localStorage.getItem("access")}`,
    },
    body: body ? body : null,
  };
}

function getProductList() {
  const endpoint = `${baseEndpoint}/products/`;
  const options = getFetchOptions();
  fetch(endpoint, options)
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      const validData = isTokenNotValid(data);
      if (validData) {
        writeToContainer(data);
      }
    });
}

function isTokenNotValid(jsonData) {
  if (jsonData.code && jsonData.code === "token_not_valid") {
    alert("Please login again");
    return false;
  }
  return true;
}

// Initialize Algolia search only if dependencies are loaded
if (
  typeof algoliasearch !== "undefined" &&
  typeof instantsearch !== "undefined"
) {
  const searchClient = algoliasearch(
    "AK967P1YKC",
    "da48ccd56faf08f687d4e25ff36e5103"
  );

  const search = instantsearch({
    indexName: "cfe_Product",
    searchClient,
  });

  search.addWidgets([
    instantsearch.widgets.searchBox({
      container: "#searchbox",
    }),

    instantsearch.widgets.clearRefinements({
      container: "#clear-refinements",
    }),

    instantsearch.widgets.refinementList({
      container: "#user-list",
      attribute: "user",
    }),
    instantsearch.widgets.refinementList({
      container: "#public-list",
      attribute: "public",
    }),

    instantsearch.widgets.hits({
      container: "#hits",
      templates: {
        item: `
                    <div>
                        <div>{{#helpers.highlight}}{ "attribute": "title" }{{/helpers.highlight}}</div>
                        <div>{{#helpers.highlight}}{ "attribute": "body" }{{/helpers.highlight}}</div>
                        
                        <p>{{ user }}</p><p>\${{ price }}
                    
                    
                    </div>`,
      },
    }),
  ]);

  search.start();
}
