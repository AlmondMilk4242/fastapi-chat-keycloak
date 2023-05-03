# FastAPI Chat System Backend

This is a Python FastAPI backend for a chat system. It includes the following features:
- Authentication using Keycloak
- Thread creation between two users
- Sending messages between users within a thread

## Getting Started
1. Clone this repository to your local machine.
2. Install the dependencies with `pip install -r requirements.txt`.
3. Run the server with `uvicorn main:app --reload`.

## API Endpoints
- `/threads` (POST): Create a new thread between two users.
- `/threads/{thread_id}/messages` (GET): Get all messages within a thread.
- `/threads/{thread_id}/messages` (POST): Send a message within a thread.

## Project Structure
- `app/database.py`: Database configuration and setup.
- `app/auth/auth.py`: Keycloak authentication functions.
- `app/models/chat.py`: SQLAlchemy models for threads and messages.
- `app/schemas/chat.py`: Pydantic schemas for threads and messages.
- `app/service/chat.py`: CRUD functions for threads and messages.
- `app/routers/chat.py`: API endpoints for threads and messages.
- `main.py`: FastAPI application startup and configuration.

## Technologies Used
- Python 3.9
- FastAPI
- SQLAlchemy
- Pydantic
- Keycloak
- Docker
- AWS

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
