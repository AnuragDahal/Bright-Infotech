# MongoDB User Management System

This project is a basic user management system implemented with MongoDB. It includes the following routes:

## User Routes

- `GET /user`: Fetch all users
- `POST /user`: Create a new user
- `PATCH/email` : Update the email 
- `DELETE/email`: Delete the user through email


## Authentication Routes

- `POST /auth/login`: Log in a user
- `POST /auth/logout`: Log out a user

## Security Features

- Cookie-based authentication: After a successful login, the user receives a cookie that authenticates them for subsequent requests.
- Password hashing: User passwords are hashed before they are stored in the database, adding an extra layer of security.

## Setup

1. Clone the repository: `git clone https://github.com/username/repository.git`
2. Install the dependencies: `pip install -r reqiurements.txt`
                            ` pip3 install -r requirement.txt`
3. Start the server: `uvicorn main:app --reload`

## Usage

To fetch all users, send a GET request to `/user`. To create a new user, send a POST request to `/user` with the user data in the request body.

To log in a user, send a POST request to `/auth/login` with the username and password in the request body. To log out a user, send a POST request to `/auth/logout`.
