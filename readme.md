# FastAPI Firestore User Management

This project is a FastAPI-based application designed to manage users across multiple projects. It provides a unified API for creating, retrieving, updating, and deleting user information, with data stored in Google Cloud Firestore. Additionally, the application includes functionality to send email invitations with links to API documentation.

## Features

- **User Management**: Create, retrieve, update, and delete users.
- **Project Association**: Users are associated with specific projects via a `project_id`.
- **Email Invitations**: Send emails with links to Swagger UI and ReDoc API documentation.
- **Google Cloud Firestore**: Utilizes Firestore for data storage.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/aniketwdubey/FastAPI-Firestore-User-Management.git
   cd FastAPI-Firestore-User-Management
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables**:
   Create a `.env` file in the root directory and add the following variables:
   ```
   MAIL_USERNAME=your_email@gmail.com
   MAIL_PASSWORD=your_email_password
   MAIL_FROM=your_email@gmail.com
   RECIPIENT_EMAILS=email1@example.com,email2@example.com
   ```

## Running the Application

1. **Start the FastAPI Server**:
   ```bash
   uvicorn app.main:app --reload
   ```

2. **Access API Documentation**:
   - Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
   - ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## API Endpoints

- **Create User**: `POST /add_users`
- **Get Users**: `GET /get_users`
- **Update User**: `PATCH /update_users/{user_id}`
- **Delete User**: `DELETE /delete_users/{user_id}`
- **Send Invitation**: `POST /send_invite`


## Deployment

The application can be deployed on AWS EC2 or any other cloud service. Ensure that the necessary ports are open and the environment variables are set correctly.

## License

This project is licensed under the MIT License.
