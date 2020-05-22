import json
import logging
import requests
import xmltodict
import boto3
from botocore.exceptions import ClientError
from datetime import date


def send_sqs_message(QueueName, msg_body):
    sqs = boto3.resource('sqs')
    queue = sqs.get_queue_by_name(QueueName = QueueName)
    # Send the SQS message
    data = {
        "Records": [
            {
              "body": msg_body
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


def lambda_handler(event, context):
    d1 = date.today().strftime("%d/%m/%Y")
    message = requests.get("https://rte-france.com/getEco2MixXml.php?type=mix&&dateDeb="+d1+"&dateFin="+d1+"&mode=NORM")
    QueueName = 'trial'
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s: %(asctime)s: %(message)s')
    jsonmessage = json.dumps(xmltodict.parse(message.text))
    msg = send_sqs_message(QueueName,jsonmessage)
    if msg is not None:
        logging.info(f'Sent SQS message ID: {msg["MessageId"]}')
    return {
        'statusCode': 200,
        'body': msg
    }