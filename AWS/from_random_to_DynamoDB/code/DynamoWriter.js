const AWS = require('aws-sdk');
AWS.config.update({region: "eu-west-3"});
exports.handler = async (event, context, callback) => {
    const ddb = new AWS.DynamoDB({apiVersion: "2012-10-08"});
    const documentClient = new AWS.DynamoDB.DocumentClient({region: "eu-west-3"});
    for(const {messageId, body} of event.Records){
        const obj = JSON.parse(body);
        for(const {idMessage, number} of obj.Records){
            const params = {
            TableName: "Test",
            Item: {
              id: idMessage,
              numberGeneated: number
            }
            }
            try {
                const data = await documentClient.put(params).promise();
                console.log(data);
            }catch(err) {
                console.log(err);
            }
        }
    }
} 