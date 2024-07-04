from sqs_reader import read_sqs_messages

def test_sqs_reader():
    messages = read_sqs_messages()
    for msg in messages:
        print(msg)

if __name__ == "__main__":
    test_sqs_reader()
