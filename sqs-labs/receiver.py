import boto3

# Create an sqs client
sqs = boto3.client('sqs')

# URL of the sqs queue
queue_url = 'your-sqs-url'

# Receive and process messages from the queue 
while True:
    response = sqs.receive_message(QueueUrl=queue_url, MaxNumberOfMessages=1)
    if 'Messages' in response:
        message = response['Messages'][0]
        index = message['Body'][1]
        print(f"Processed order {index}.")
        # Delete the received message from the queue
        sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=message['ReceiptHandle'])
    else:
        print("No messages in the queue")
        break