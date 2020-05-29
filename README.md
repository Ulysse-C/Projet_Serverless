# Project Serverless

This project is the project of end of second year of engineering school.
The objective was to get data from [Rte](https://rte-france.com/fr/eco2mix/eco2mix) to display it, using serverless technologies, especialy lambda functions.
First using Aws services, then kubernetes.

### Part One, Aws
There is three part in this exemple:

[1.](https://github.com/Ulysse-C/Projet_Serverless/tree/master/AWS/from_random_to_DynamoDB) Saving randomly generated numbers into DynamoDB, passing through Sqs.

[2.](https://github.com/Ulysse-C/Projet_Serverless/tree/master/AWS/from_Web_to_DynamoDB) Getting data from Rte, putting it in a DynamoDB, and having a static dashboard in Amazon S3

[3.](https://github.com/Ulysse-C/Projet_Serverless/tree/master/AWS/from_Web_to_ElasticSearch_Service) Getting data from Rte, putting it in a ElasticSearch service, and having a kibana dynamic dashboard

### Part Two,  Kubernetes
A kubernetes version of the Aws part Three.
