kubeless function deploy webtokafka --runtime nodejs12 --from-file WebtoKafka.js --handler WebtoKafka.tokafka -d package.json
kubeless function deploy kafkatoes --runtime python3.7 --from-file KafkatoES.py --handler KafkatoES.handler -d requirements.txt
kubeless topic create rte-france
sleep 3s
kubeless trigger kafka create toes --function-selector created-by=kubeless,function=kafkatoes --trigger-topic rte-france
kubeless trigger cronjob create tokafka --function webtokafka --schedule "*/30 * * * *"
