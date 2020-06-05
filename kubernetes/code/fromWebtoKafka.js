const { Kafka } = require('kafkajs')
const https = require('https');
const xmlParser = require('xml2json');

module.exports =  {
	tokafka: async function  (event, context) {
		const kafka = new Kafka({
		  clientId: 'fromWebtoKafka',
		  brokers: ['XX.X.X.XXX:9092']
		})
		
		const date = Date.now()
		const dateTimeFormat = new Intl.DateTimeFormat('en', { year: 'numeric', month: '2-digit', day: '2-digit' }) 
		const [{ value: month },,{ value: day },,{ value: year }] = dateTimeFormat .formatToParts(date ) 
		const d1 = `${day}/${month}/${year }`
		https.get('https://rte-france.com/getEco2MixXml.php?type=mix&&dateDeb='+d1+'&dateFin='+d1+'&mode=NORM', async (resp) => {
		  let data = '';
		  resp.on('data', async (chunk) => {
		    data += chunk;
		  });
		  resp.on('end', async () => {
		    const producer = kafka.producer()
		    console.log("Sending");
		    await producer.connect()
			await producer.send({
			  topic: 'rte-france',
			  messages: [
			    { value: xmlParser.toJson(data) },
			  ],
			})

			await producer.disconnect()
			  });	
			}).on("error", async (err) => {
			  console.log("Error: " + err.message);
			});	
	}
}
