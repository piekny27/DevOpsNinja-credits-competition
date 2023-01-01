mkdir -p target

kind load docker-image credits-competition-view:latest
kind load docker-image credits-competition-web:latest

kubectl delete all,configmap,ingress -l type=application --namespace=credits-competition
helm template ../helm-charts/application > target/application-final.yaml
kubectl --namespace=credits-competition apply -f target/application-final.yaml