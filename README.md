# Employee Management System

A complete, production-ready **Employee Management System** built with Django and Bootstrap 5. This project provides a clean, modern interface for managing employee records with full CRUD functionality, search, authentication, and a professional dashboard.

## 📋 Project Overview

The Employee Management System (EMS) is a web application that allows organizations to manage their employee data efficiently. It features secure authentication, a statistics-driven dashboard, and complete employee record management (create, read, update, delete, and search).

## ✨ Features

### Authentication
- Secure login / logout using Django's built-in authentication system
- `@login_required` protection on all internal views
- Automatic redirect of unauthenticated users to the login page

### Dashboard
- Total employee count
- Employees added in the last 30 days
- Department count overview
- Recently added employees table
- Quick action cards (Add Employee, Employee List, Search Employee)

### Employee Management (CRUD)
- **Add Employee** — create new employee records with full validation
- **View Employees** — paginated, sortable employee list
- **Update Employee** — edit existing employee details
- **Delete Employee** — remove records with a confirmation step
- **Search Employee** — search by Employee ID, Name, or Department

### UI/UX
- Modern, responsive Bootstrap 5 interface
- Professional blue color theme
- Navbar, collapsible sidebar, cards, tables, forms, buttons, and alerts
- Delete confirmation prompts
- Auto-dismissing success/error alert messages
- Loading spinner on navigation
- Custom 404 error page

## 🛠️ Technologies

- **Backend:** Python 3, Django 5
- **Database:** SQLite
- **Frontend:** Bootstrap 5, HTML5, CSS3, JavaScript
- **Icons:** Bootstrap Icons
- **Version Control:** Git

## 📁 Folder Structure

```
employee_management/
├── employee_management/       # Project configuration
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── employees/                 # Main application
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   ├── apps.py
│   └── migrations/
├── templates/
│   ├── base.html
│   ├── 404.html
│   ├── registration/
│   │   └── login.html
│   └── employees/
│       ├── dashboard.html
│       ├── employee_list.html
│       ├── employee_add.html
│       ├── employee_update.html
│       ├── employee_delete.html
│       └── employee_search.html
├── static/
│   ├── css/style.css
│   ├── js/script.js
│   └── images/
├── requirements.txt
├── README.md
├── manage.py
└── .gitignore
```

## 🚀 Installation

### 1. Extract the project and navigate into it
```bash
cd employee_management
```

### 2. Create a virtual environment
```bash
python -m venv venv
```

Activate it:
- **Windows:** `venv\Scripts\activate`
- **macOS / Linux:** `source venv/bin/activate`

### 3. Install requirements
```bash
pip install -r requirements.txt
```

### 4. Run migrations
```bash
python manage.py migrate
```

### 5. Create a superuser
```bash
python manage.py createsuperuser
```

### 6. Run the development server
```bash
python manage.py runserver
```

Visit **http://127.0.0.1:8000/** and log in with the superuser credentials you created. The Django admin panel is available at **http://127.0.0.1:8000/admin/**.

## 📸 Screenshots

_Add screenshots of the Dashboard, Employee List, Add/Update forms, and Search page here after running the project locally._

## 🔮 Future Enhancements

- Role-based access control (Admin, HR, Manager)
- Export employee data to CSV / PDF
- Employee profile photo upload
- Email notifications on employee creation/update
- Attendance and leave management modules
- REST API using Django REST Framework
- Dark mode theme toggle

## 📄 License

This project is provided as-is for educational and internal business use.
