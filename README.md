# Flask_auth_0.1 (with BluePrint)


# Flask Authentication with Blueprints

This project is a simple web application built with **Flask**, featuring user authentication and account management. It uses **Flask-Login**, **Flask-Bcrypt**, and **SQLAlchemy** for secure and organized data handling, and is structured using **Blueprints** for modularity and scalability.

---

## 📦 Key Features

- User registration (Sign Up) with form validation.
- User login and logout using Flask-Login.
- Password hashing with Flask-Bcrypt for security.
- Organized code structure using **Blueprints** for maintainability.
- SQLite database (easily replaceable with other databases).

---

## 🗂 Project Structure

```

Flask_auth_0.1/
│
├─ app/
│  ├─ **init**.py       # App initialization, DB and Bcrypt setup
│  ├─ models.py         # Database models
│  ├─ main/             # Main Blueprint
│  │  ├─ routes.py      # Main routes
│  │  └─ forms.py       # Web forms
│  └─ templates/        # HTML templates
│
├─ venv/                # Virtual environment (optional)
├─ requirements.txt     # Required libraries
└─ run.py               # App entry point

````

---

## ⚙️ Requirements

- Python 3.10+
- Flask
- Flask-Login
- Flask-Bcrypt
- Flask-WTF
- Flask-SQLAlchemy

Install dependencies using:

```bash
pip install -r requirements.txt
````

---

## 🚀 Running the Project

1. Set up a virtual environment (optional):

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
flask run
```

4. Open your browser and visit:

```
http://127.0.0.1:5000/
```

---

## 🔒 Security Notes

* Make sure to change the `SECRET_KEY` in `__init__.py` to a strong secret before deploying.
* Passwords are stored securely using **bcrypt**.
* The project can be extended to add email confirmation, password reset, and other security features.

---

## 📌 Contributing

* Create new branches for features or bug fixes.
* Follow the existing code style (PEP8).
* Submit a Pull Request after testing your changes.

---

## 📄 License

Open-source project — free to use and modify.

