#!/usr/bin/env bash

if [ -z "$NEW_RELIC_LICENSE_KEY" ]; then
  echo "NEW_RELIC_LICENSE_KEY is not set"
  exit 1
fi

kubectl delete namespace store > /dev/null 2>&1

echo Creating namespace
kubectl create namespace store

echo Creating NEW_RELIC_LICENSE_KEY secret
kubectl -n store create secret generic newrelic-key --from-literal=new-relic-license-key=$NEW_RELIC_LICENSE_KEY

echo Deploying redis
kubectl -n store apply -f kubernetes-manifests/redis.yaml

echo Deploying adservice
kubectl -n store apply -f kubernetes-manifests/adservice.yaml

echo Deploying cartservice
kubectl -n store apply -f kubernetes-manifests/cartservice.yaml

echo Deploying emailservice
kubectl -n store apply -f kubernetes-manifests/emailservice.yaml

echo Deploying currencyservice
kubectl -n store apply -f kubernetes-manifests/currencyservice.yaml

echo Deploying paymentservice
kubectl -n store apply -f kubernetes-manifests/paymentservice.yaml

echo Deploying productcatalogservice
kubectl -n store apply -f kubernetes-manifests/productcatalogservice.yaml

echo Deploying recommendationservice
kubectl -n store apply -f kubernetes-manifests/recommendationservice.yaml

echo Deploying shippingservice
kubectl -n store apply -f kubernetes-manifests/shippingservice.yaml

echo Deploying checkoutservice
kubectl -n store apply -f kubernetes-manifests/checkoutservice.yaml

echo Deploying frontend
kubectl -n store apply -f kubernetes-manifests/frontend.yaml

echo All services deployed