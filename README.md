# Django REST API Learnings  
**Advanced Concepts & Practical Implementations**  
*A learning path guided by [Coding for Entrepreneurs (CFE)](https://www.youtube.com/c/CodingForEntrepreneurs)*  

---

## 🚀 Overview  
This repository showcases my progression from Django fundamentals to advanced REST API development using Django REST Framework (DRF). Through CFE's course, I focused on building scalable, secure, and efficient APIs while documenting my journey on LinkedIn.  

---

## � Key Skills & Concepts  
### **Core Topics Explored**  
1. **CRUD Operations**  
   - Built RESTful APIs with full Create, Retrieve, Update, Delete functionality.  
   - Mastered serializers, model relationships, and DRF’s request-response flow.  

2. **Generic Views & Mixins**  
   - Implemented `GenericAPIView`, `ListCreateAPIView`, and `RetrieveUpdateDestroyAPIView` to reduce redundancy.  
   - Combined `mixins.CreateModelMixin` and `mixins.ListModelMixin` for flexible logic reuse.  

3. **Authentication & Permissions**  
   - Integrated **Token Authentication** and **JWT** for secure user access.  
   - Customized permissions using `@permission_classes` decorators and Django’s built-in permission classes.  

4. **Search Optimization**  
   - Utilized Django’s native search filters for basic queries.  
   - Enhanced performance with **Algolia Search API** for real-time, scalable search results.  

5. **Viewsets & Routers**  
   - Simplified URL routing with `ModelViewSet` and `DefaultRouter`.  
   - Reduced boilerplate code while maintaining endpoint clarity.  

---

## 💻 Projects & Code  
Explore my implementations of these concepts in dedicated repositories:  
- **JWT Authentication Workflow**  
- **Algolia-Powered Search Endpoints**  
- **Custom CRUD APIs with Dynamic Permissions**  

🔗 [GitHub Profile](https://github.com/yourusername)  

---

## 📚 LinkedIn Documentation  
I break down my learning process, challenges, and solutions in detailed LinkedIn posts. Follow my journey for tutorials and insights:  

👉 [LinkedIn Profile](https://www.linkedin.com/in/rishav-upadhaya)  
*Pro Tip: Check my posts for code snippets, screenshots, and practical tips!*  

---

## 🛠️ Quickstart Guide  
### Run These Projects Locally  
1. **Clone the Repository**  
   ```bash  
   git clone https://github.com/yourusername/django-rest-api-projects.git  
   cd django-rest-api-projects  
   ```  

2. **Install Dependencies**  
   ```bash  
   pip install -r requirements.txt  # Includes Django, DRF, JWT, Algolia  
   ```  

3. **Configure Environment**  
   - Add Algolia credentials in `settings.py`.  
   - Set up JWT in `urls.py` and `authentication.py`.  

4. **Run Migrations & Server**  
   ```bash  
   python manage.py migrate  
   python manage.py runserver  
   ```  

---

## 🙏 Acknowledgments  
- **Coding for Entrepreneurs**: For their project-driven DRF course.  
- **Algolia**: For simplifying search integration with their Django SDK.  

---

## 📜 License  
MIT License - See [LICENSE](LICENSE) for details.  
