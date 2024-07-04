import boto3
import json

def read_sqs_messages():
    sqs = boto3.client('sqs', endpoint_url='http://localhost:4566', region_name='us-east-1')
    try:
        response = sqs.receive_message(QueueUrl='http://sqs.us-east-1.localhost.localstack.cloud:4566/000000000000/login-queue', MaxNumberOfMessages=10)
        print("SQS Response:", response)  # Debug line
        messages = response.get('Messages', [])
        if not messages:
            print("No messages found.")
            return []
        parsed_messages = []
        for msg in messages:
            try:
                parsed_messages.append(json.loads(msg['Body']))
                print(f"Message received: {msg['Body']}")  # Debug line
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
                continue
        return parsed_messages
    except Exception as e:
        print(f"Error receiving SQS messages: {e}")
        return []
