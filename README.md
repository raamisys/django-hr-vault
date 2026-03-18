# 🔐 HR Vault System (Django)

A secure HR management system built with Django that demonstrates **data-at-rest protection**, **user-based access control**, and **admin verification**.

---

## 🚀 Features

* 🔐 **Encrypted Sensitive Data**

  * Bank account numbers and salaries are encrypted in the database
* 👤 **User-Based Ownership**

  * Each record is linked to the user who created it
* 🔒 **Authentication Required**

  * Only logged-in users can access employee records
* 📋 **Employee Management**

  * Add and view employee records
* 🛠️ **Admin Panel Integration**

  * Manage records via Django Admin
  * Verify encrypted data directly from the database
* 🌐 **Smart Routing**

  * Homepage redirects based on authentication status

---

## 🧱 Tech Stack

* Python 3.x
* Django 4.x
* SQLite (default database)
* django-cryptography (for field-level encryption)

---

## 📁 Project Structure

```
hr_vault/
├── hr_vault/          # Main app
│   ├── models.py      # EmployeeRecord model (with encryption)
│   ├── views.py       # Add & list views (protected)
│   ├── admin.py       # Admin configuration
│   ├── urls.py        # App routes
│   └── templates/
│       └── hr_vault/
│           ├── add_employee.html
│           └── employee_list.html
│
├── config/            # Project settings
│   ├── settings.py
│   └── urls.py
│
├── db.sqlite3         # Database
└── manage.py
```

---

## 🧩 Model Overview

### `EmployeeRecord`

| Field               | Description        |
| ------------------- | ------------------ |
| employee_name       | Employee name      |
| department          | Department         |
| bank_account_number | 🔐 Encrypted       |
| annual_salary       | 🔐 Encrypted       |
| added_by            | ForeignKey to User |
| created_at          | Timestamp          |

---

## 🔐 Encryption (Data at Rest)

Sensitive fields are encrypted using:

```python
from django_cryptography.fields import encrypt
```

```python
bank_account_number = encrypt(models.CharField(max_length=100))
annual_salary = encrypt(models.DecimalField(...))
```

* Data is **encrypted before saving**
* Automatically **decrypted when accessed in Django**
* Stored as unreadable ciphertext in the database

---

## 🔒 Access Control

Views are protected using:

```python
from django.contrib.auth.decorators import login_required
```

* Unauthenticated users are redirected to login
* Only authorized users can create and view records

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd hr_vault
```

---

### 2. Create virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 5. Create superuser

```bash
python manage.py createsuperuser
```

---

### 6. Run the server

```bash
python manage.py runserver
```

---

## 🌐 Usage

* Visit: `http://127.0.0.1:8000/`
* Login via `/login/`
* Access employee records at `/hr/`
* Add new records at `/hr/add/`
* Admin panel: `/admin/`

---

## 🧪 Verification

### ✅ Django Admin

* View and manage employee records
* Decrypted values shown for usability

### ✅ Database Inspection

* Open `db.sqlite3` using:

  * DB Browser for SQLite
  * VS Code SQLite extension

👉 Encrypted fields will appear like:

```
gAAAAABlYxk3kF8k...
```

---

## ⚠️ Security Notes

* Do NOT change `SECRET_KEY` after encryption (data may become unreadable)
* Encrypted fields are secure at rest but still accessible in app logic
* Consider masking sensitive data in UI for production use

---

## 📄 License

This project is for educational purposes.
