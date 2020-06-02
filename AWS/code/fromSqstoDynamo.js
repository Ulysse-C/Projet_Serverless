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
            const date = bodyjson.liste["date_debut"];
            for(const {valeur} of bodyjson.liste.mixtr.type) {
                if (j<1) {
                j++;
                for (var i=0; i < valeur.length; i++) {
                        var val = valeur[i];
                        var periode = val["@periode"];
                        var text = val["#text"];
                        const params = {
                            TableName: "Number",
                            Item: {
                              id: date + " " + periode,
                              periode: periode,
                              valeur: text
                            },
                            ConditionExpression: "attribute_not_exists(id)"
                        };
                        try {   
                            var data = await documentClient.put(params).promise();
                            console.log(data);
                        }catch(err) {
                        console.log(err);
                        }
                    }
                }
            }
        }
    }
};