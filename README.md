# Project Serverless

This project is the project of end of second year of engineering school.
The objective was to get data from [Rte](https://rte-france.com/fr/eco2mix/eco2mix) to display it, using serverless technologies, especialy lambda functions.
First using Aws services, then kubernetes.
Check [the wiki](https://github.com/Ulysse-C/Projet_Serverless/wiki) for a quick tutorial of technologies we use.

### Aws
There is three part in this exemple:

[1.](https://github.com/Ulysse-C/Projet_Serverless/blob/master/AWS/from_Random_to_DynamoDB.md) Saving randomly generated numbers into DynamoDB, passing through Sqs.

[2.](https://github.com/Ulysse-C/Projet_Serverless/blob/master/AWS/from_Web_to_DynamoDB.md) Getting data from Rte, putting it in a DynamoDB, and having a static dashboard in Amazon S3

[3.](https://github.com/Ulysse-C/Projet_Serverless/blob/master/AWS/from_Web_to_ElasticSearch_Service.md) Getting data from Rte, putting it in a ElasticSearch service, and having a kibana dynamic dashboard

### Kubernetes

[4.](https://github.com/Ulysse-C/Projet_Serverless/blob/master/kubernetes/from_Web_to_ElasticSearch.md) A kubernetes version of the Aws part Three, if you want a quick setup on your cluster, [there is a setup](https://github.com/Ulysse-C/Projet_Serverless/wiki/Project-quick-setup)
