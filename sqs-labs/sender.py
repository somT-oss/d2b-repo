import boto3

# Create an sqs client
sqs = boto3.client('sqs')

# URL of the sqs queue
queue_url = 'your-sqs-url'

# Send "[i]. Order [i] send out for processing" messages to the queue
# Where i is the current index of the message being sent out
for i in range(5):
    message = f"[{i + 1}]. Order {i + 1} sent out for processing."
    sqs.send_message(QueueUrl=queue_url, MessageBody=message)
    print(f"Sent: {message}")