# bank-app

Simple Python + MongoDB full-stack demo with Docker Compose and Kubernetes manifests.

## Run locally (docker-compose)
1. docker-compose up --build
2. Frontend: http://localhost:3000
   Backend: http://localhost:5000

## Build & push images
# docker build & push examples
docker build -t bank-backend:local ./backend
docker tag bank-backend:local YOUR_REGISTRY/bank-backend:latest
docker push YOUR_REGISTRY/bank-backend:latest

docker build -t bank-frontend:local ./frontend
docker tag bank-frontend:local YOUR_REGISTRY/bank-frontend:latest
docker push YOUR_REGISTRY/bank-frontend:latest

## Deploy to k8s
kubectl create namespace bank-app
kubectl apply -f k8s/database/secret.yaml
kubectl apply -f k8s/database/service.yaml
kubectl apply -f k8s/database/statefulset.yaml
kubectl apply -f k8s/backend/deployment.yaml
kubectl apply -f k8s/backend/service.yaml
kubectl apply -f k8s/frontend/deployment.yaml
kubectl apply -f k8s/frontend/service.yaml

## Notes
- Replace <REGISTRY> in k8s manifests with your docker registry.
- Keep secrets out of git in production (use External Secrets / Vault).
