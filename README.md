# Project Serverless

This project is the project of end of second year of engineering school.
Using Aws services

### Part One
A Lambda function write a random number in a Sqs, and another one take the value from the Sqs to a DynamoDB.

### Part Two
An extension of **Part One**, but now the first Lambda take data from a website (Rte) and the Data in the Dynamo is used to host a dashboard in S3.

### Part Three
An extension of **Part Two**, the data in the dynamo is pushed in an ElasticSeatch Service by a lambda to allow the use of a kibana dashboard
