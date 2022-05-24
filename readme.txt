build docker image:
docker build -t cryptoapp:latest -f docker/Dockerfile .

run docker image:
docker run -p 8501:8501 cryptoapp:latest
open in chrome browser:
http://localhost:8501/

kubernetes # todo: move this
minikube start


docker login

(base) henrik-@Henriks-Air ~ % kubectl create secret generic regcred \
    --from-file=.dockerconfigjson=.docker/config.json \
    --type=kubernetes.io/dockerconfigjson



docker build -t henrikvdv/cryptoapp:latest .
docker login
docker push henrikvdv/cryptoapp:latest
kubectl create deployment kubernetes-crypto-aaa --image=henrikvdv/cryptoapp:0.1
kubectl scale deploy kubernetes-crypto-aaa --replicas=4
kubectl describe po





