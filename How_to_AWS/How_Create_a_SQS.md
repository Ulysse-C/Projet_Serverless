# How to create a SQS

### From [aws console](https://eu-west-3.console.aws.amazon.com/sqs/home?region=eu-west-3)

*	chose  "Create New Queue"
*	chose a name and the type of the queue. Our example use a standard queue.
* your queue is now created.

#### Good to know

* A usefull stat of the monitoring section is the NumberOfMessagesDeleted. Messages successfully received by a lambda function
will be counted here.
* You can send a message directly from the SQS for debugging purposes. Just choose Queue Action >> Send a Message
* A SQS send thousands of message, even if not in use. You can can monitor your budget in the [billing section.](https://console.aws.amazon.com/billing/home?region=eu-west-3#/)(You have 1 000 000 free messages each month)
