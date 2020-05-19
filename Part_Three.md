# Project Serverless, Part Three
Simple setup for a Kibana dashboard with ElasticSearch Service

### What you will know
![global schema](images/rapport3.png)

### From DynamoDB to ElasticSearch Service
The dynamoDB already created is used as trigger for a new lambda function, to send the ElasticSearch Service (ES), this function needs a role, with access to the DynamoDB, and the ES

### ElasticSearch Service
At the creation of the ES, you will need to chose the identification method to allow peoples, including you, to access the ES and the kibana, when the ES is online, you can access to the kibana with the link under the arn, in the overview pannel.

### Kibana Dashboard
Connect to your Elasticsearch data with the connection with their index, then use the pannels on the left side to create dashboard and visualisations 
