# Feedback App

A FastAPI application for managing feedback entries, using SQLAlchemy for database operations and pytest for testing.

## Overview

This project implements a simple API for managing feedback entries. It allows users to create feedback entries with scores and comments, and retrieve them from the database.

## Features

- Create new feedback entries with scores and comments.
- Retrieve all feedback entries.
- Handle validation and error cases for feedback creation.

## Technologies Used

- FastAPI: A modern, fast (high-performance), web framework for building APIs with Python.
- SQLAlchemy: A SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- pytest: A testing framework for Python that makes it easy to write simple tests.
- Vue2: A progressive JavaScript framework for building user interfaces. It is used here for the frontend.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/erpan011J/simple-feedback-app.git
   cd simple-feedback-app
   ```

2. **Build and run the Docker containers:**

   ```bash
   docker-compose up --build -d
   ```

3. **Access the application:**

   - The feedback form can be accessed at http://localhost:8080/.


## Testing
   - To run tests using pytest:
     
   ```bash
   docker exec feedback_app_backend pytest
   ```
    
## API Documentation

    Once the application is running, you can access the API documentation (Swagger UI) at http://localhost:8000/docs
