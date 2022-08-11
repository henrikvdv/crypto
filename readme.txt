build docker image:
docker build -t cryptoapp:latest -f docker/Dockerfile .

run docker image:
docker run -p 8501:8501 cryptoapp:latest
open in chrome browser:
http://localhost:8501/

## kubernetes
open -a Docker
minikube start


docker login

# I guess only needed first time?
(base) henrik-@Henriks-Air ~ % kubectl create secret generic regcred \
    --from-file=.dockerconfigjson=.docker/config.json \
    --type=kubernetes.io/dockerconfigjson



docker build -t henrikvdv/cryptoapp:latest .
docker login
docker push henrikvdv/cryptoapp:latest
kubectl create deployment kubernetes-crypto-aaa --image=henrikvdv/cryptoapp:0.1

# or update (don't think it works yet):
kubectl set image deployment/kubernetes-crypto-aaa cryptoapp=henrikvdv/cryptoapp:latest

kubectl scale deploy kubernetes-crypto-aaa --replicas=4
kubectl describe po

kubectl port-forward deploy/kubernetes-crypto-aaa 8501:8501

# Access on localhost:8501
 kubectl delete deployment ...






