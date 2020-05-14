# Project Serverless
Simple setup for updating a Aws DynamoDB with lambda functions and Sqs

### What you will know
![global schema](rapport1.png)

### Dashboard
The dashboard is a public webpage hosted in Amazon S3 service. The page access to the DynamoDB et scans the data via the Javascript AWS SDK. The data are displayed in colored and dynamic graphs made with Chart.js.

### lambda functions
```python
def send_sqs_message(QueueName, msg_body):
    sqs = boto3.resource('sqs')
    queue = sqs.get_queue_by_name(QueueName = QueueName)
    # Send the SQS message
    param = "name "
    param += str(msg_body)
    data = {
        "Records": [
    {
      "idMessage": param,
      "number": msg_body
    }
    ]
    }
    print(data)
    try:
        response = queue.send_message(MessageBody = json.dumps(data))
    except ClientError as e:
        logging.error(e)
        return None
    return response
```

