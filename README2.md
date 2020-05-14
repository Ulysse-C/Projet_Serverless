# Project Serverless
Simple setup for updating a Aws DynamoDB with lambda functions and Sqs

### What you will know
![global schema](rapport2.png)

### Dashboard
The dashboard is a public webpage hosted in Amazon S3 service. The page access to the DynamoDB et scans the data via the Javascript AWS SDK. The data are displayed in colored and dynamic graphs made with Chart.js.

### From Web to SQS
The simplest lambda function. It requests data from RTE's website. The data are dumped in JSON and sent to the SQS.

### From SQS to DynamoDB
This functions parse the JSON data. Then for each value, it creates an add-request for the database and fills it.

### Note
All the code is available in the **Code** folder.
