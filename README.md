# Notification Service Documentation

## Overview
This documentation provides an overview of the components, Docker configurations, and FastAPI endpoints implemented in the `notification_service` for the BQP Assignment platform. The service is designed to manage notifications related to new posts and comments, enabling automated communication via email and potentially other channels.

## Directory Structure

    /notification_service
    ├── /compose
    │   └── /local
    │       ├── Dockerfile             # Dockerfile to build the Docker image
    │       └── start                  # Startup script to launch the FastAPI server
    ├── /src
    │   ├── database.py                # Defines database models for articles
    │   ├── main.py                    # FastAPI application entry point
    │   ├── requirements.txt           # Lists Python dependencies
    │   ├── utils.py                   # Contains utility functions for notification handling
    │   └── /config
    │       ├── .env                   # Stores environment variables
    │       └── constants.py           # (Optional) Stores constants used across the application
    └── local.yml                      # Docker Compose configuration for local development

## Components

### Docker Configuration
- **File**: `local.yml`
- **Description**: Configures the Docker environment for the notification service, setting up the necessary service parameters, exposed ports, and volume mappings for development.

### Dockerfile
- **Location**: `compose/local/Dockerfile`
- **Purpose**: Builds the Docker image for the service, installing required Python packages and setting up the environment.

### Startup Script
- **File**: `compose/local/start`
- **Purpose**: Executes the FastAPI application using Uvicorn with specified host and port configurations. It ensures that the service reloads automatically during development when changes are detected.

## Source Code Files

### Main Application (FastAPI)
- **File**: `src/main.py`
- **Functionality**:
  - Entry point for the FastAPI application.
  - Defines endpoints for sending notifications about new posts and comments.

### Database Configuration
- **File**: `src/database.py`
- **Functionality**:
  - Establishes database connections using SQLAlchemy.
  - Defines ORM models for the articles used in notifications.

### Utility Functions
- **File**: `src/utils.py`
- **Functionality**:
  - Functions for sending email notifications to users about new posts and comments.

### Python Requirements
- **File**: `src/requirements.txt`
- **Details**: Includes all necessary Python libraries such as FastAPI, Uvicorn, Pydantic, SendGrid, Twilio, and others required to run the notification service.

## Configuration Files

### Environment Variables
- **File**: `src/config/.env`
- **Contains**:
  - Google client credentials for integration with Google services (if required).
  - Other sensitive keys and secrets required for the operation of the service.

### Constants
- **File**: `src/config/constants.py`
- **Description**: This file can store constant values used throughout the application, although it is optional and currently empty.

## Setup and Deployment
To deploy the notification service locally using Docker:
1. Navigate to the service directory:
    ```bash
    cd /path/to/notification_service
    ```
2. Build and run the Docker container:
    ```bash
    docker-compose -f local.yml up --build
    ```

This setup ensures that the notification service is properly configured and ready for integration with other services or for standalone functionality as part of the BQP Assignment platform.
