const contentContainer = document.getElementById("content-container");
const loginForm = document.getElementById("login-form");
const baseEndpoint = "http://localhost:8000/api";
if (loginForm) {
  // handle this login form
  loginForm.addEventListener("submit", handleLogin);
}
function handleLogin(event) {
  event.preventDefault();
  const loginEndpoint = `${baseEndpoint}/token/`;
  let loginFormData = new FormData(loginForm);
  let loginObjectData = Object.fromEntries(loginFormData);
  let bodyStr = JSON.stringify(loginObjectData);
  //   console.log(bodyStr, loginObjectData, loginFormData, loginEndpoint);
  const options = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: bodyStr,
  };
  fetch(loginEndpoint, options)
    .then((response) => {
      console.log(response.status);
      return response.json();
    })
    .then((data) => {
      console.log("data", data);
      // handle success, maybe store token, etc.
    })
    .catch((err) => {
      console.log("err", err);
    });
}
