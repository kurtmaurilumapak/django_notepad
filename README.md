# Project: Django Notepad

## **Description**
This project implements a secure note-taking system using Django for both the client and server applications. The project includes:
- Middleware-based encryption and decryption of note data.
- REST API for secure communication between the client and server.
- A user-friendly web interface for adding and viewing notes.

## **Features**
- **User Authentication**: Login, registration, and logout functionality.
- **Add Notes**: Securely add notes from the client app.
- **Encryption & Decryption**: Middleware ensures notes are encrypted on the client and decrypted on the server.
- **Note Storage**: Notes are stored securely in a PostgreSQL database.

---

## **Installation Instructions**

### **1. Set Up Python Version**
This project requires Python **3.12.0**. Ensure you have this version installed before proceeding.

You can verify your Python version with:
```bash
python --version
```

---

### **2. Clone the Repository**
```bash
# Clone the repository to your local machine
git clone https://github.com/kurtmaurilumapak/django_notepad.git
cd django_notepad
```

---

### **3. Set Up Virtual Environments for Client and Server**

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
2. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
3. Install dependencies:
   ```bash
   pip install django
   pip install djangorestframework
   pip install djangorestframework-simplejwt
   pip install psycopg2-binary
   pip install cryptography
   pip install requests
   ```
### **4. Set Up PostgreSQL Database**
1. Install PostgreSQL:
   - Download and install PostgreSQL from [https://www.postgresql.org/download/](https://www.postgresql.org/download/).

2. Create a database for the server app:
   ```sql
   CREATE DATABASE notepad;
   ```
3. Update the `DATABASES` configuration in `server_app/settings.py` and for `client_app/settings.py` for session:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'notepad',
           'USER': '<your_username>',
           'PASSWORD': '<your_password>',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

---

### **5. Apply Migrations**

#### **Server App**
1. Navigate to the `server_app` directory:
   ```bash
   cd server_app
   ```
2. Run migrations to set up the database schema:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

## **Running the Applications**

### **1. Start the Server App**
1. Navigate to the `server_app` directory:
   ```bash
   cd server_app
   ```
2. Run the server on port `8000`:
   ```bash
   python manage.py runserver 8000
   ```

### **2. Start the Client App**
1. Navigate to the `client_app` directory:
   ```bash
   cd client_app
   ```
2. Run the client on port `8001`:
   ```bash
   python manage.py runserver 8001
   ```

---

## **Usage**

### **1. Access the Client App on Different Device**
Make sure you are on the same network where you run the server_app and client_app, and make sure you allow python on firewall inbound rules.
- Open a browser and navigate to:
  ```
  http://<ip-of-the-device-where-you-run-the-server_app-and-client_app>:8001/
  ```

### **2. Register or Login**
- Use the registration page to create a new account.
- Log in with your credentials.

### **3. Add Notes**
- Use the "Add Note" form on the home page to create a new note.
- Notes are encrypted before being sent to the server.

### **4. View Notes**
- Saved notes are displayed on the home page.
