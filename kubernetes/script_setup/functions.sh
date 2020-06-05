kubeless function deploy webtokafka --runtime nodejs12 --from-file WebtoKafka.js --handler WebtoKafka.tokafka -d package.json
kubeless function deploy kafkatoes --runtime python3.7 --from-file KafkatoES.py --handler KafkatoES.handler -d requirements.txt
sleep 3s
kubeless trigger kafka create toes --function-selector created-by=kubeless,function=kafkatoes --trigger-topic ret-france
kubeless trigger cronjob create tokafka --function webtokafka --schedule "*/30 * * * *"