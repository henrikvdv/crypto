build docker image:
docker build -t cryptoapp:latest -f docker/Dockerfile .

run docker image:
docker run -p 8501:8501 cryptoapp:latest
open in chrome browser:
http://localhost:8501/


minikube start
docker login

(base) henrik-@Henriks-Air ~ % kubectl create secret generic regcred \
    --from-file=.dockerconfigjson=.docker/config.json \
    --type=kubernetes.io/dockerconfigjson



docker build -t henrikvdv/cryptoapp:latest .
docker login
docker push henrikvdv/cryptoapp:latest
minikube start
kubectl create deployment kubernetes-crypto-aaa --image=henrikvdv/cryptoapp:latest
kubectl scale deploy kubernetes-crypto-aaa --replicas=4
kubectl describe po


kubectl delete deployment kubernetes-crypto-aaa

kubectl port-forward deploy/kubernetes-crypto-aaa 8501:8501 #todo remove and find how to open port when creating deployment
? kubectl set image deployments/kubernetes-crypto-aaa cryptoapp=henrikvdv/cryptoapp:latest




