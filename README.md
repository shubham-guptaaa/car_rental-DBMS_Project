# Car Rental System

## Project Overview
This is a **Car Rental System** developed as part of our Database Management System (DBMS) project. The system provides a platform for users to rent cars efficiently and for admins to manage vehicle inventory and bookings seamlessly. The project leverages the **Django framework** for web development and **MySQL** as the backend database.

---

## Features

### User Module:
- User registration and login.
- Browsing available cars.
- Booking cars.
- Viewing booking history.

### Admin Module:
- Admin registration and login.
- Managing vehicle inventory (add, update, delete cars).
- Viewing and managing user bookings.

---

## Technologies Used
- **Backend Framework**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: MySQL
- **Version Control**: Git
---

## Installation and Setup

### Prerequisites:
1. Python (3.x)
2. MySQL Server
3. pip (Python package manager)

### Steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/shubham-guptaaa/car_rental-DBMS_Project.git
   ```
2. Navigate to the project directory:
   ```bash
   cd car-rental-system
   ```
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up the MySQL database:
   - Create a database named `car_rental`.
   - Update the `settings.py` file in the Django project to include your MySQL database credentials.

5. Apply database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
6. Run the development server:
   ```bash
   python manage.py runserver
   ```
7. Access the application in your browser at `http://127.0.0.1:8000/`.

---

## Screenshots
(Add screenshots of key features, such as the booking page, admin dashboard, etc.)

---

## Team Members
- **Aadya** (GitHub: [aadya2775](https://github.com/aadya2775))
- **Shubham Gupta** (GitHub: [shubham-guptaaa](https://github.com/shubham-guptaaa))

---

## License
This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgments
- Django and MySQL documentation.

---

## Contact
For any inquiries or feedback, feel free to reach out:
- **Your Email**: aadya2775@gmail.com
- **Teammate's Email**: shuvguptaaa@gmail.com

Thank you for checking out our project!

