PASSWORD=$(kubectl get secret quickstart-es-elastic-user -o go-template='{{.data.elastic | base64decode}}')
echo "PASSWORD: $PASSWORD" 
kubectl get svc -n kubeless kafka
