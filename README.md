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

Step 2: Clone the Repository
Clone the repository to your local machine:

sh
```
git clone https://github.com/sdami002/fetch-take-home-sasi.git
cd fetch-take-home-sasi
```

Step 3: Set Up Docker and LocalStack
Ensure Docker is installed and running on your machine. Start the Docker containers for LocalStack and PostgreSQL:

sh
```
docker-compose up
```
### While docker is running, Open a new prompt and follow next steps.

### Step 4: Python Environment Setup [Optional]
Create and activate a Python virtual environment, then install the required dependencies:

sh
```
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

Step 5: Configure AWS CLI
Configure AWS CLI to use LocalStack:

sh
```
aws configure --profile localstack
```
Use the following details:
```
AWS Access Key ID: test
AWS Secret Access Key: test
Default region name: us-east-1
Default output format: json
```

Step 6: Create SQS Queue
Create an SQS queue using AWS CLI:

sh
```
awslocal sqs create-queue --queue-name login-queue
```

Step 7: Create PostgreSQL Table
Connect to your PostgreSQL database and create the user_logins table:

sh
```
psql -d postgres -U postgres -p 5432 -h localhost -W
```
Run the following SQL command:

sql
```
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

Step 8: Send a Test Message to SQS
Create a message.json file with the following content:

json
```

{
    "user_id": "123",
    "device_id": "device123",
    "ip": "192.168.1.1",
    "device_type": "mobile",
    "locale": "en_US",
    "app_version": 1,
    "create_date": "2024-07-03"
}
```
Send the test message to the SQS queue:

sh
```
awslocal sqs send-message --queue-url http://localhost:4566/000000000000/login-queue --message-body file://message.json
```
Step 9: Run the Main Script
Run the ETL process:

sh
```
python main.py
```

Step 10: Verify Data in PostgreSQL
Connect to PostgreSQL and query the user_logins table:

sh
```
psql -d postgres -U postgres -p 5432 -h localhost -W
```
Run the following SQL command:

sql
```
SELECT * FROM user_logins;

```
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
```
# Additional Questions
### How would you deploy this application in production?
```
To deploy this application in production, I would containerize the application using Docker and deploy it on a cloud service like AWS ECS or Kubernetes. For the SQS and PostgreSQL services, I would use managed services like AWS SQS and Amazon RDS.
```

### What other components would you want to add to make this production ready?
```
Monitoring and Logging: Use services like AWS CloudWatch and ELK Stack for monitoring and logging.
Error Handling: Implement robust error handling and retries for SQS message processing.
CI/CD Pipeline: Set up a CI/CD pipeline using tools like Jenkins, GitHub Actions, or AWS CodePipeline.
Security: Ensure all secrets and sensitive information are securely managed using AWS Secrets Manager or similar tools.
```
### How can this application scale with a growing dataset?
```
The application can scale horizontally by running multiple instances of the ETL process, which can read from the SQS queue and process messages in parallel. Using AWS SQS and Amazon RDS ensures that the messaging and database services can scale independently based on the load.
```

### How can PII be recovered later on?
```
To recover PII later on, you can store the mapping of original values to masked values in a secure and access-controlled database or use a reversible encryption method. Ensure that access to the mapping data is strictly controlled and audited.
```

### What are the assumptions you made?
```
The SQS queue and PostgreSQL database are accessible and configured correctly.
The masking of PII data should be deterministic, meaning the same input will always produce the same masked output.
The ETL process will handle message retries and error logging.
By following above detailed steps and explanations, you should be able to complete the take-home project successfully. If you encounter any issues or have further questions, feel free to ask!
```
## Decisions and Explanations
### How will you read messages from the queue?
```
Messages will be read from the SQS queue using the boto3 library, which provides an easy-to-use API to interact with AWS services, including SQS. The receive_message method of the SQS client will be used to poll the queue for new messages.
```
### What type of data structures should be used?
```
The JSON data from the SQS queue will be read into Python dictionaries, which provide a flexible and efficient way to manage the data. Lists will be used to collect multiple records for batch processing.
```
### How will you mask the PII data so that duplicate values can be identified?
```
PII data such as device_id and ip will be masked using a hashing function like SHA-256. This ensures that the same input value always produces the same hashed output, making it possible to identify duplicates. The hashlib library will be used for this purpose.
```

### What will be your strategy for connecting and writing to Postgres?
```
The psycopg2 library will be used to connect to the PostgreSQL database and execute SQL commands. A connection will be established at the beginning of the data load process, and data will be inserted using the INSERT SQL command. The connection will be closed once all data is processed to ensure resources are freed and to maintain database integrity.
```
### Where and how will your application run?
```
The application will run inside Docker containers, which will be orchestrated using Docker Compose. This setup allows for a consistent and isolated environment that includes LocalStack for SQS and PostgreSQL for the database. The entire ETL process, including reading from the queue, transforming the data, and loading it into the database, will be handled by a Python script executed within this environment.
```
