# frontend

Run the following command to restore dependencies to `vendor/` directory:

    dep ensure --vendor-only

## Building docker image

From `src/frontend/`, run:

```
docker build -t frontend .
```

## Running docker image

```
docker run \
-p 8080:8080 \
-e PORT=8080 \
-e PRODUCT_CATALOG_SERVICE_ADDR=productcatalogservice:3550 \
-e CURRENCY_SERVICE_ADDR=currencyservice:7000 \
-e CART_SERVICE_ADDR=cartservice:7070 \
-e RECOMMENDATION_SERVICE_ADDR=recommendationservice:8080 \
-e SHIPPING_SERVICE_ADDR=shippingservice:50051 \
-e CHECKOUT_SERVICE_ADDR=checkoutservice:5050 \
-e AD_SERVICE_ADDR=recommadservice:9555 \
-e NEW_RELIC_LICENSE_KEY=$NEW_RELIC_LICENSE_KEY \
-e NEW_RELIC_APP_NAME="frontend" \
-e NEW_RELIC_LOG=stdout \
-e NEW_RELIC_LOG_LEVEL=debug \
frontend
```