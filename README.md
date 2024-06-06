# Sentiment Analysis

## Description

Sentiment Analysis is a simple Django web application that allows users to analyze the sentiment of a given text input. The app utilizes an AI-powered sentiment analysis model ([TextBlob](https://github.com/sloria/TextBlob)) to determine whether the text is positive, negative, or neutral, as well as its level of subjectivity.

## Features

- **Sentiment Analysis:** Determines the polarity (positive, negative, or neutral) and subjectivity of the input text.
- **Results Visualization:** Displays the analysis results in a clear and organized table.
- **User-Friendly Interface:** Easy to use thanks to Bootstrap for layout and styling.
- **Multilingual Support:** The user interface is available in Italian and English (with the potential to add more languages in the future).
- **Microservices Architecture:** Built on a microservices architecture for scalability and maintainability.

## Architecture

The application follows a microservices architecture, consisting of two main components:

- **Backend ([sas-backend-server](https://github.com/giandonatoinverso/sas-backend-server)):** Django web service which handles the application logic, interaction with the sentiment analysis model, and communication with the database.
- **Database ([sas-db](https://github.com/giandonatoinverso/sas-db)):** Stores the results of the sentiment analysis in a MySql database

## Installation with Docker Compose

1. **Prerequisites:**
   - Docker and Docker Compose installed on your system.
   - A `.env` file in the project's root directory containing the necessary environment variables (e.g., MySQL root password).

2. **Start the application:**
   ```bash
   docker compose build --no-cache && docker-compose --env-file production.env up -d
   ```
3. **Accessing the Application**
   - Open your web browser and navigate to *http://localhost:8000* (or the address specified in your docker-compose.yml).

## Usage

1. **Enter Text**: Type or paste the text you want to analyze into the textarea.
2. **Click "Analyze"**: The app will process the text and display the results in the table below.

## Customization

- **Language**: Multi-language support with .po files
- **Styling**: Customization of the appearance of the application by modifying the style.css file

## Building and Publishing

This project includes a *taskfile.yml* script that simplifies the process of building and publishing a new version of the Docker image.

To build and publish the Docker image, run the following command:

```bash
task publish-docker
```

## Deployment on AWS

- AWS VPC
  - Dedicated VPC to ensure security and resource isolation

- Amazon Route 53
  - DNS Management

- AWS ECS on Fargate
  - Container management for *sas-db*, *sas-backend-server* and *sas-client*

- AWS Elastic Load Balancer
  - Application Load Balancer (ALB) for distributing HTTP traffic between containers *sas-backend-server* and *sas-client*

- AWS CloudWatch
  - Log monitoring, alarm definition and container performance monitoring
  