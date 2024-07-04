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
Setup Instructions
Step 1: Clone the Repository
Clone the repository to your local machine:

sh
Copy code
git clone https://github.com/sdami002/fetch-take-home-sasi.git
cd fetch-take-home-sasi
Step 2: Set Up Docker and LocalStack
Setup Instructions
Step 1: Clone the Repository
Clone the repository to your local machine: no need to break like this need completetluy in  continues
ChatGPT
markdown
Copy code
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

bash
Copy code

## Setup Instructions

### Step 1: Clone the Repository
Clone the repository to your local machine:
```sh
git clone https://github.com/yourusername/fetch-rewards-data-engineering-takehome.git
cd fetch-rewards-data-engineering-takehome
Step 2: Set Up Docker and LocalStack
Ensure Docker is installed and running on your machine. Start the Docker containers for LocalStack and PostgreSQL:

sh
Copy code
docker-compose up
Step 3: Configure AWS CLI
Configure AWS CLI to use LocalStack:

sh
Copy code
aws configure --profile localstack
Use the following details:

AWS Access Key ID: test
AWS Secret Access Key: test
Default region name: us-east-1
Default output format: json
Step 4: Create SQS Queue
Create an SQS queue using AWS CLI:

sh
Copy code
awslocal sqs create-queue --queue-name login-queue
Step 5: Python Environment Setup
Create and activate a Python virtual environment, then install the required dependencies:

sh
Copy code
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
Step 6: Create PostgreSQL Table
Connect to your PostgreSQL database and create the user_logins table:

sh
Copy code
psql -d postgres -U postgres -p 5432 -h localhost -W
Run the following SQL command:

sql
Copy code
CREATE TABLE user_logins (
    user_id VARCHAR(128),
    device_type VARCHAR(32),
    masked_ip VARCHAR(256),
    masked_device_id VARCHAR(256),
    locale VARCHAR(32),
    app_version INTEGER,
    create_date DATE
);
Step 7: Send a Test Message to SQS
Create a message.json file with the following content:

json
Copy code
{
    "user_id": "123",
    "device_id": "device123",
    "ip": "192.168.1.1",
    "device_type": "mobile",
    "locale": "en_US",
    "app_version": 1,
    "create_date": "2024-07-03"
}
Send the test message to the SQS queue:

sh
Copy code
awslocal sqs send-message --queue-url http://localhost:4566/000000000000/login-queue --message-body file://message.json
Step 8: Run the Main Script
Run the ETL process:

sh
Copy code
python main.py
Step 9: Verify Data in PostgreSQL
Connect to PostgreSQL and query the user_logins table:

sh
Copy code
psql -d postgres -U postgres -p 5432 -h localhost -W
Run the following SQL command:

sql
Copy code
SELECT * FROM user_logins;
Project Files
docker-compose.yaml: Docker Compose configuration file for setting up LocalStack and PostgreSQL.
requirements.txt: Python dependencies file.
message.json: Sample message to be sent to the SQS queue.
sqs_reader.py: Script to read messages from the SQS queue.
data_transformer.py: Script to mask PII data.
db_loader.py: Script to load data into the PostgreSQL database.
main.py: Main script to orchestrate the ETL process.
README.md: Project documentation.
