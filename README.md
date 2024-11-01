
# Flask-BankingAPI
This project is a RESTful API built with Flask to manage financial data. It includes features for user and account management, transaction processing, budget tracking, and bill scheduling, providing users with tools for efficient personal financial management.

## Technologies Used
- **Flask** - Python web framework for building the API.
- **MySQL** - Database for storing user, account, transaction, budget, and bill data.
- **Flask SQLAlchemy** - ORM for database interactions.
- **JWT** - For secure authentication and authorization.
- **Docker** - Containerization for easy deployment.
- **Swagger** - API documentation and testing.

## Getting Started

### Prerequisites
- **Python 3.12** installed
- **MySQL** server setup
- **Docker** installed (optional for containerized setup)
- **Postman** or similar API testing tool for testing endpoints

### Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/Flask-FinancialManagementAPI
   ```

2. **Install requirements**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Create `.env` file**:
   ```bash
   MYSQL_DATABASE_URI=your-mysql-database-url
   JWT_SECRET_KEY=your-jwt-secret-key
   ```

4. **Run database migrations**:
   ```bash
   flask db upgrade
   ```

5. **Start the Flask application**:
   ```bash
   flask run
   ```

   The application will run at `http://localhost:5000`.

## Usage

- **User Management**:
  - `POST /users`: Register a new user.
  - `GET /users/me`: Retrieve profile of authenticated user.
  - `PUT /users/me`: Update profile information.

- **Account Management**:
  - `GET /accounts`: Retrieve all accounts of authenticated user.
  - `POST /accounts`: Create a new account.
  - `GET /accounts/:id`: Get specific account details (authorized user only).
  - `PUT /accounts/:id`: Update account details (authorized user only).
  - `DELETE /accounts/:id`: Delete an account (authorized user only).

- **Transaction Management**:
  - `GET /transactions`: List all transactions of user’s accounts (optional filters).
  - `POST /transactions`: Create a new transaction.
  - `GET /transactions/:id`: Get specific transaction details (authorized user only).

- **Budgeting**:
  - `POST /budgets`: Set a budget for a category.
  - `GET /budgets`: List all user’s budgets.
  - `PUT /budgets/:id`: Update budget information.

- **Bill Management**:
  - `POST /bills`: Schedule a bill payment.
  - `GET /bills`: List scheduled bill payments.
  - `PUT /bills/:id`: Update bill details.
  - `DELETE /bills/:id`: Cancel a bill payment.

- **Two-Factor Authentication (2FA)**:
  - `POST /auth/enable-2fa`: Enables 2FA, generating a 2FA secret and QR code.
  - `POST /auth/verify-2fa`: Verifies the 2FA code during login or sensitive operations.

#### Deployment Link
> [!IMPORTANT]
> Access the API documentation here:
https://your-deployment-link.com/apidocs/#