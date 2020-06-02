# Project Serverless, Part Three
Simple setup for a Kibana dashboard with ElasticSearch Service on AWS

### What you will know
![global schema](../../images/rapport3.png)

### From Sqs to ElasticSearch Service
The Sqs and the function used are the ones of **Part Two**.
The lambda function don't use the client 'elasticsearch-py' but classic requests instead. The values are included in the ElasticSearch only if they are new.

### ElasticSearch Service
At the creation of the ES, you will need to chose the identification method to allow peoples, including you, to access the ES and the kibana, when the ES is online, you can access to the kibana with the link under the arn, in the overview pannel.

### Kibana Dashboard
Connect your Elasticsearch data with the "Connect to your Elasticsearch index" option, then use the pannels on the left side to create dashboard and visualisations, verify that the type of your values are recognized by kibana (especialy date or number) to allow a smooth visualisation creation.