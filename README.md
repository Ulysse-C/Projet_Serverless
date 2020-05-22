# Project Serverless

This project is the project of end of second year of engineering school.
Using Aws services

### Part One, from random to DynamoDB 
A Lambda function write a random number in a Sqs, and another one take the value from the Sqs to a DynamoDB.

### Part Two,  from Web to DynamoDB
An extension of **Part One**, but now the first Lambda take data from a website (Rte) and the Data in the Dynamo is used to host a dashboard in S3.

### Part Three, from Web to ElasticSearch Service
Another version of **Part Two**, instead of a dynamo, an ElasticSeatch Service is used to allow the use of a kibana dashboard
