# Fetch Rewards Data Engineering Takehome

This project is a data engineering task that processes messages from an SQS queue, masks PII data, and loads the data into a PostgreSQL database using Docker, LocalStack, and Python.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
  - [Step 1: Clone the Repository](#step-1-clone-the-repository)
  - [Step 2: Set Up Docker and LocalStack](#step-2-set-up-docker-and-localstack)
  - [Step 3: Configure AWS CLI](#step-3-configure-aws-cli)
  - [Step 4: Create SQS Queue](#step-4-create-sqs-queue)
  - [Step 5: Python Environment Setup](#step-5-python-environment-setup)
  - [Step 6: Create PostgreSQL Table](#step-6-create-postgresql-table)
  - [Step 7: Send a Test Message to SQS](#step-7-send-a-test-message-to-sqs)
  - [Step 8: Run the Main Script](#step-8-run-the-main-script)
  - [Step 9: Verify Data in PostgreSQL](#step-9-verify-data-in-postgresql)
- [Project Files](#project-files)
- [License](#license)

## Prerequisites

- Docker
- Docker Compose
- Python 3.6 or higher
- AWS CLI
- PostgreSQL (for local development)

## Project Structure

```plaintext
fetch-rewards-data-engineering-takehome/
├── .gitignore
├── docker-compose.yaml
├── requirements.txt
├── message.json
├── sqs_reader.py
├── data_transformer.py
├── db_loader.py
├── main.py
└── README.md
