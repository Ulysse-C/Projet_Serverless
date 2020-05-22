import json
import logging
import boto3
from botocore.exceptions import ClientError

from random import randint



def lambda_handler(event, context):
    QueueName = 'CreditCardTransaction'
    # Set up logging
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s: %(asctime)s: %(message)s')


    n = randint (1,10);
    # Send some SQS messages
    response = send_sqs_message(QueueName,n)


    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }
    
    
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