# Rectangle Intersection API

Welcome to my Rectangle Intersection API project! This project implements a web API that takes two pairs of doubles representing a line segment and searches an internal database to return a list of rectangles that intersect the input segment by any of the edges.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Setup](#setup)
- [Running the Application](#running-the-application)
- [API Usage](#api-usage)
- [Running Tests](#running-tests)
- [Dockerization](#dockerization)
- [Environment Variables](#environment-variables)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project demonstrates a simple Flask-based API that handles geometric computations. It checks whether a given line segment intersects with any rectangles stored in the database.

## Features

- Accepts two pairs of doubles representing a line segment.
- Searches an internal database for rectangles.
- Returns a list of rectangles that intersect the input segment.
- Uses SQLAlchemy for ORM.
- Dockerized for easy deployment.
- Includes unit and integration tests.

## Project Structure

Here's how the project is structured:

```
/rubicomp/
|-- app/
|   |-- __init__.py
|   |-- api.py
|   |-- models.py
|   |-- utils.py
|-- tests/
|   |-- __init__.py
|   |-- test_api.py
|   |-- test_models.py
|-- venv/
|-- .gitignore
|-- requirements.txt
|-- README.md
|-- config.py
|-- run.py
|-- Dockerfile
|-- .dockerignore
|-- docker-compose.yml
|-- .env
```

## Setup

### Prerequisites

Make sure you have the following installed:

- Python 3.9+
- Docker (optional for Docker setup)
- Docker Compose (optional for Docker setup)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Verdiyev/rubicomp.git
   cd rubicomp
   ```

2. Set up a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `.\venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:

   Create a `.env` file in the root directory with the following content:

   ```dotenv
   SECRET_KEY=your_generated_secret_key
   DATABASE_URL=sqlite:///rectangles.db
   ```

## Running the Application

### Running Locally

1. Make sure your virtual environment is activated.
2. Run the application:

   ```bash
   flask run
   ```

   The API will be available at `http://localhost:5000`.

### Running with Docker

1. Build the Docker image:

   ```bash
   docker-compose build
   ```

2. Run the Docker container:

   ```bash
   docker-compose up
   ```

   The API will be available at `http://localhost:5000`.

## API Usage

### Endpoint: `/intersect`

- **Method**: `POST`
- **Description**: Returns rectangles that intersect the given line segment.
- **Request Payload**:

  ```json
  {
      "x1": float,
      "y1": float,
      "x2": float,
      "y2": float
  }
  ```

- **Response**:

  ```json
  [
      {
          "id": int,
          "x1": float,
          "y1": float,
          "x2": float,
          "y2": float
      },
      ...
  ]
  ```

### Example

You can use `curl` to test the endpoint:

```bash
curl -X POST http://localhost:5000/intersect -H "Content-Type: application/json" -d '{"x1": 0, "y1": 0, "x2": 1, "y2": 1}'
```

## Running Tests

1. Make sure your virtual environment is activated.
2. Run the tests using `pytest`:

   ```bash
   pytest tests/
   ```

## Dockerization

The project includes a `Dockerfile` and `docker-compose.yml` for easy Docker deployment. Follow the instructions in the "Running with Docker" section to build and run the Docker container.

## Environment Variables

The application uses environment variables for configuration. The `.env` file should include:

- `SECRET_KEY`: A secret key for Flask sessions and security.
- `DATABASE_URL`: The database connection URL.

## Contributing

Feel free to contribute! Here's how you can help:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License.
```

You can copy and paste this entire string directly into your README.md file. It should maintain the formatting and structure. If you need any more adjustments or further help, feel free to ask!
