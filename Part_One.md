# Project Serverless, Part One
Simple setup for updating a Aws DynamoDB with lambda functions and Sqs

### What you will know
![global schema](images/rapport1.png)

### Sqs & Dynamo DB
Nothing more than the basic creation of Aws, note somewhere the name and the arn of the services you just created.

### Roles
You will need to create two new roles with IAM for your lambda functions, so you will chose the use case "Lambda".
Both will need the policy : AWSLambdaBasicExecutionRole

then, for the one putting in the sqs, the policy : AmazonSQSFullAccess  (but I think it is possible to limit the permissions to the sqs we are using only)

And, for the lambda function interacting with the dynamo DB, add a inline policy, for the service dynamoDB, select the actions "PutItem" and "GetItem", finally, chose the dynamoDB you want to interact with as ressource, with it arn.

### lambda functions
here, the dynamo table has two Items,and the name "Test", id and numberGeneated, you can change the name and the amount if you do it everywere (the two functions and the Dynamo DB).

### Event
For a lambda function triggered with a timer, use the service CloudWatch, in Event/Rules, create a new rule with the trigger you want, for this example, chose schedule and the time you want, on the right pannel, add your lambda function as target.
For the moment, the input in the database is independent of the trigger, but that will come later.

### Note
All the code is available in the **Code_Part_One** folder.