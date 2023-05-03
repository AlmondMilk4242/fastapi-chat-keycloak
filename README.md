# FastAPI Chat System Backend

This is a Python FastAPI backend for a chat system. It includes the following features:
- Authentication using Keycloak
- Thread creation between two users
- Sending messages between users within a thread

## Getting Started
1. Clone this repository to your local machine.
2. Install the dependencies with `pip install -r requirements.txt`.
3. Run the server with `uvicorn main:app --reload`.

## Starting a Keycloak Instance Using Docker
1. Install [Docker](https://docs.docker.com/get-docker/) on your machine.
2. Pull the Keycloak image by running `docker pull jboss/keycloak`.
3. Run Keycloak in a container by running `docker run -p 8080:8080 jboss/keycloak`.
4. Access the Keycloak Admin Console at [http://localhost:8080/auth/admin](http://localhost:8080/auth/admin).

## API Endpoints
- `/threads` (POST): Create a new thread between two users.
- `/threads` (GET): Get all threads for a user.
- `/threads/{thread_id}` (DELETE): Delete a thread by ID.
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

## Setting Environment Variables
To use this project, you will need to set the following environment variables in a `.env` file located in the project directory:
- `DATABASE_URL=postgresql://postgres:db_password@your_db_instance:5432/postgres`
- `KEYCLOAK_JWKS_URL=http://localhost:8080/realms/my_realm/protocol/openid-connect/certs`


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

## Deploying with AWS Elastic Beanstalk and CI/CD Pipeline
This project uses a GitHub Actions CI/CD pipeline for building and deploying the application to AWS Elastic Beanstalk. To deploy the application, you need to set up the required environment variables in the GitHub Secrets for the repository.

For a complete overview of the pipeline, refer to the `.github/workflows/ci-cd.yml` file in the project repository. The pipeline builds a Docker image, pushes it to DockerHub, and deploys it to AWS Elastic Beanstalk.

To deploy the application to AWS Elastic Beanstalk, you will need to set up an environment with a Docker platform and configure the required environment variables, such as `DATABASE_URL` and `KEYCLOAK_JWKS_URL`.

For more information on deploying FastAPI applications with AWS Elastic Beanstalk, refer to the [official FastAPI deployment guide](https://fastapi.tiangolo.com/deployment/aws-ecs/).
