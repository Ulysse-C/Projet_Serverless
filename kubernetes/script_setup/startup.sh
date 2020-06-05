#kubeless instalation
export RELEASE=$(curl -s https://api.github.com/repos/kubeless/kubeless/releases/latest | grep tag_name | cut -d '"' -f 4)
kubectl create ns kubeless
kubectl create -f https://github.com/kubeless/kubeless/releases/download/$RELEASE/kubeless-$RELEASE.yaml
#kubeless CLI
export OS=$(uname -s| tr '[:upper:]' '[:lower:]')
curl -OL https://github.com/kubeless/kubeless/releases/download/$RELEASE/kubeless_$OS-amd64.zip && \
  unzip kubeless_$OS-amd64.zip && \
  sudo mv bundles/kubeless_$OS-amd64/kubeless /usr/local/bin/
#Kafka
export RELEASE=$(curl -s https://api.github.com/repos/kubeless/kafka-trigger/releases/latest | grep tag_name | cut -d '"' -f 4)
kubectl create -f https://github.com/kubeless/kafka-trigger/releases/download/$RELEASE/kafka-zookeeper-$RELEASE.yaml
#Elastic
kubectl apply -f https://download.elastic.co/downloads/eck/1.1.2/all-in-one.yaml
cat <<EOF | kubectl apply -f -
apiVersion: elasticsearch.k8s.elastic.co/v1
kind: Elasticsearch
metadata:
  name: quickstart
spec:
  version: 7.7.0
  nodeSets:
  - name: default
    count: 1
    config:
      node.master: true
      node.data: true
      node.ingest: true
      node.store.allow_mmap: false
EOF
#Kibana
cat <<EOF | kubectl apply -f -
apiVersion: kibana.k8s.elastic.co/v1
kind: Kibana
metadata:
  name: quickstart
spec:
  version: 7.7.0
  count: 1
  elasticsearchRef:
    name: quickstart
EOF
#functions files
mkdir project_serverless_functions
cd project_serverless_functions
curl https://raw.githubusercontent.com/Ulysse-C/Projet_Serverless/master/kubernetes/code/KtoES.py?token=APRSKMSTHGBNRRSDWYMJERS64NDNG >> KafkatoES.py
curl https://raw.githubusercontent.com/Ulysse-C/Projet_Serverless/master/kubernetes/code/fromWebtoKafka.js?token=APRSKMW2YQ6USPMC45DQVGS64NDNK >> WebtoKafka.js
curl https://raw.githubusercontent.com/Ulysse-C/Projet_Serverless/master/kubernetes/code/package.json?token=APRSKMT5IMLJZ2KF6AYV6EC64NOF6 >> package.json
curl https://raw.githubusercontent.com/Ulysse-C/Projet_Serverless/master/kubernetes/code/requirements.txt?token=APRSKMQ43WFHRE2AHM3DVT264NDNQ >> requirements.txt
curl https://raw.githubusercontent.com/Ulysse-C/Projet_Serverless/master/kubernetes/script_setup/functions.sh?token=APRSKMTXAQ4V3O6CSP3G6PC64NVZU >> setup_functions.sh
curl https://raw.githubusercontent.com/Ulysse-C/Projet_Serverless/master/kubernetes/script_setup/getdatas.sh?token=APRSKMUQCP7I6C4X6CHG22264NW6M >> useful_data.sh
