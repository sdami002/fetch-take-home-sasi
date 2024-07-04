# Fetch Rewards Data Engineering Takehome
### This project is a data engineering task that processes messages from an SQS queue, masks PII data, and loads the data into a PostgreSQL database using Docker, LocalStack, and Python.

## Prerequisites

- Docker
- Docker Compose
- Python 3.6 or higher
- AWS CLI
- PostgreSQL (for local development)

## Project Structure

``` plaintext
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
```
## Setup Instructions
```
Step 1: Install Required Software
Docker: Install Docker from the official Docker website.
Docker Compose: Docker Compose is included with Docker Desktop.
Python: Install Python 3.6 or higher from the official Python website.
AWS CLI: Install the AWS CLI from the official AWS website.
PostgreSQL: Install PostgreSQL from the official PostgreSQL website.
```
```
Step 2: Clone the Repository
Clone the repository to your local machine:

sh
git clone https://github.com/sdami002/fetch-take-home-sasi.git
cd fetch-take-home-sasi
```
```
Step 3: Set Up Docker and LocalStack
Ensure Docker is installed and running on your machine. Start the Docker containers for LocalStack and PostgreSQL:

sh
docker-compose up
```
### While docker is running, Open a new prompt and follow next steps.

### Step 4: Python Environment Setup [Optional]
Create and activate a Python virtual environment, then install the required dependencies:
```
sh
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
### If you want to exit virtual environment use
```
deactivate
```
#### If you are unable to work in virtual environment just type deactivate and move to next steps.
### Next
```
pip install -r requirements.txt
```
```
Step 5: Configure AWS CLI
Configure AWS CLI to use LocalStack:

sh

aws configure --profile localstack
Use the following details:

AWS Access Key ID: test
AWS Secret Access Key: test
Default region name: us-east-1
Default output format: json
```
```
Step 6: Create SQS Queue
Create an SQS queue using AWS CLI:

sh

awslocal sqs create-queue --queue-name login-queue
```
```
Step 7: Create PostgreSQL Table
Connect to your PostgreSQL database and create the user_logins table:

sh

psql -d postgres -U postgres -p 5432 -h localhost -W
Run the following SQL command:

sql

CREATE TABLE user_logins (
    user_id VARCHAR(128),
    device_type VARCHAR(32),
    masked_ip VARCHAR(256),
    masked_device_id VARCHAR(256),
    locale VARCHAR(32),
    app_version INTEGER,
    create_date DATE
);
```
```
Step 8: Send a Test Message to SQS
Create a message.json file with the following content:

json

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

awslocal sqs send-message --queue-url http://localhost:4566/000000000000/login-queue --message-body file://message.json
```
```
Step 9: Run the Main Script
Run the ETL process:

sh

python main.py
```
```
Step 10: Verify Data in PostgreSQL
Connect to PostgreSQL and query the user_logins table:

sh

psql -d postgres -U postgres -p 5432 -h localhost -W
Run the following SQL command:

sql

SELECT * FROM user_logins;

```
Project Files
docker-compose.yaml: Docker Compose configuration file for setting up LocalStack and PostgreSQL.
requirements.txt: Python dependencies file.
message.json: Sample message to be sent to the SQS queue.
sqs_reader.py: Script to read messages from the SQS queue.
data_transformer.py: Script to mask PII data.
db_loader.py: Script to load data into the PostgreSQL database.
main.py: Main script to orchestrate the ETL process.
README.md: Project documentation
