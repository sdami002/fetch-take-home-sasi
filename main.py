from sqs_reader import read_sqs_messages
from data_transformer import mask_pii
from db_loader import load_to_db

def main():
    messages = read_sqs_messages()
    if messages:
        print("Messages received:", messages)  # Debug line
        masked_data = mask_pii(messages)
        print("Masked Data:", masked_data)  # Debug line
        load_to_db(masked_data)
    else:
        print("No messages received from SQS.")

if __name__ == "__main__":
    main()
