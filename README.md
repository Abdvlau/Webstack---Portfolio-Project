# URL Shortener API

A simple backend-only API to shorten URLs and redirect to the original URLs using FastAPI and MongoDB.

## Tech Stack
- **Framework:** FastAPI
- **Database:** MongoDB (MongoEngine)
- **Server:** Uvicorn
- **Containerization:** Docker
- **Documentation:** Swagger UI (integrated with FastAPI)

## Features
- **Shorten URLs:** Convert long URLs into short, unique identifiers.
- **Redirect URLs:** Redirect users from short URLs to the original long URLs.
- **Click Tracking:** Track the number of times a short URL has been accessed.
- **Error Handling:** Returns appropriate error responses for invalid URLs or expired short links.

## Setup Instructions

### Prerequisites
- Docker installed on your machine.
- A MongoDB instance (local or cloud) available.

### Steps to Run Locally
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd url-shortener-api

2. **Configure Environment Variables**: 
Create a .env file and add your MongoDB connection string
MONGO_URI=mongodb://<username>:<password>@<host>:<port>/<database>

3. **Build and Run with Docker**:
docker build -t url-shortener-app .
docker run -d -p 8000:8000 url-shortener-app

4. **Access the API**:
Visit http://localhost:8000/docs to view and test the API via Swagger UI.


### Running Without Docker

1. **Install Dependencies**:
pip install -r requirements.txt

2. **Run the Application**:
uvicorn app.main:app --reload


### API Endpoints Documentation

**Base URL**
The base URL for all endpoints is: http://localhost:8000


**Endpoints**

1. **POST /shorten**
Shortens a given long URL.

Request: 

{
  "original_url": "https://example.com"
}

Response:

{
  "short_url": "http://localhost:8000/{short_code}"
}

2. **GET /{short_code}**
Redirects to the original URL for a given short code.

Response:
302 Redirect to the original URL.


3. **GET /stats/{short_code}**
Retrieves the click count for a specific short URL.

Response:

{
  "original_url": "https://example.com",
  "clicks": 25
}

### Project Architecture

main.py: Entry point of the application.
app/routers/url.py: Contains API routes for URL shortening, redirection, and statistics.
app/models.py: MongoDB models using MongoEngine.
app/schemas.py: Pydantic schemas for request validation.
app/utils.py: Contains utility functions, including URL generation and validation.

### Usage Guidelines

Use the /shorten endpoint to generate a shortened URL.
Access the short URL to redirect to the original URL.
Use the /stats/{short_code} endpoint to get click statistics for a short URL.
