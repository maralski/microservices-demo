#!/usr/bin/env bash

if [ -z "$NEW_RELIC_LICENSE_KEY" ]; then
  echo "NEW_RELIC_LICENSE_KEY is not set"
  exit 1
fi

kubectl delete namespace store
kubectl create namespace store
kubectl -n store create secret generic newrelic-key --from-literal=new-relic-license-key=$NEW_RELIC_LICENSE_KEY
kubectl -n store apply -f kubernetes-manifests/redis.yaml
kubectl -n store apply -f kubernetes-manifests/adservice.yaml
kubectl -n store apply -f kubernetes-manifests/cartservice.yaml
kubectl -n store apply -f kubernetes-manifests/emailservice.yaml
kubectl -n store apply -f kubernetes-manifests/currencyservice.yaml
kubectl -n store apply -f kubernetes-manifests/paymentservice.yaml
kubectl -n store apply -f kubernetes-manifests/productcatalogservice.yaml
kubectl -n store apply -f kubernetes-manifests/recommendationservice.yaml
kubectl -n store apply -f kubernetes-manifests/shippingservice.yaml
kubectl -n store apply -f kubernetes-manifests/checkoutservice.yaml
kubectl -n store apply -f kubernetes-manifests/frontend.yaml

# kubectl -n store apply -f kubernetes-manifests/checkoutservice.yaml
