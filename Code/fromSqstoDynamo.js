const AWS = require('aws-sdk');
AWS.config.update({region: "eu-west-3"});
exports.handler = async (event, context, callback) => {
    var j = 0;
    const ddb = new AWS.DynamoDB({apiVersion: "2012-10-08"});
    const documentClient = new AWS.DynamoDB.DocumentClient({region: "eu-west-3"});
    for(var {body} of event.Records){
        const obj = JSON.parse(body);
        for (var {body} of obj.Records){
            var bodyjson = JSON.parse(body);
            for(const {valeur} of bodyjson.liste.mixtr.type) {
                for (var i=0; i < valeur.length; i++) {
                    if (j<5) {
                        j++;
                        var val = valeur[i];
                        var periode = val["@periode"];
                        var text = val["#text"];
                        const params = {
                            TableName: "Number",
                            Item: {
                              id: periode,
                              periode: periode,
                              valeur: text
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
        }
    }
} 