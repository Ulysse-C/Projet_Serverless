

AWS.config.update({
  region: "eu-west-3",
  //endpoint: 'http://localhost:8000',
  // accessKeyId default can be used while using the downloadable version of DynamoDB.
  // For security reasons, do not store AWS Credentials in your files. Use Amazon Cognito instead.
  accessKeyId: "AKIA2CGGZDAJ2B2U3UQR",
  // secretAccessKey default can be used while using the downloadable version of DynamoDB.
  // For security reasons, do not store AWS Credentials in your files. Use Amazon Cognito instead.
  secretAccessKey: "59orOfYDge0u6d3RkA+elncpkENU9znK7RYC9Im+"
});

var docClient = new AWS.DynamoDB.DocumentClient();


function drawElectricity(){
  var params = {
    TableName: "Number",
  }

  var docClient = new AWS.DynamoDB.DocumentClient();
  docClient.scan(params, function(err, data) {
    if (err) console.log(err, err.stack); // an error occurred
    else{
      var recentTimes = [];
      var recentValues = [];
      var time_data;
      var consumption_data;

      data.Items.forEach(function(item) {
        time_data = item.periode;
        consumption_data = item.valeur;
        //dateHour = item.DateHour.toString();
        recentTimes.push(time_data);
        recentValues.push(consumption_data);
      });





      //Chart.js code
      var ctx = document.getElementById('myChart').getContext('2d');
      var chart = new Chart(ctx,{
        type: 'line',

        data:{
          labels : recentTimes,
          datasets : [{
            label: 'Consommation electrique',
            backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(255, 99, 132)',
            data : recentValues
          }]
        },

        options: {}
      });

    }});
}

function drawCO2(){
  var params = {
    TableName: "Number",
  }

  var docClient = new AWS.DynamoDB.DocumentClient();
  docClient.scan(params, function(err, data) {
    if (err) console.log(err, err.stack); // an error occurred
    else{
      var recentTimes = [];
      var recentValues = [];
      var time_data;
      var consumption_data;

      data.Items.forEach(function(item) {
        time_data = item.periode;
        consumption_data = item.valeur;
        //dateHour = item.DateHour.toString();
        recentTimes.push(time_data);
        recentValues.push(consumption_data);
      });





      //Chart.js code
      var ctx = document.getElementById('myChart').getContext('2d');
      var chart = new Chart(ctx,{
        type: 'bar',

        data:{
          labels : recentTimes,
          datasets : [{
            label: 'Consommation electrique',
            backgroundColor: 'rgb(127, 255, 212)',
            borderColor: 'rgb(127, 255, 212)',
            data : recentValues
          }]
        },

        options: {}
      });

    }});
}
