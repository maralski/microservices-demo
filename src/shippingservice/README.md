# Shipping Service

The Shipping service provides price quote, tracking IDs, and the impression of order fulfillment & shipping processes.

## Local

Run the following command to restore dependencies to `vendor/` directory:

    dep ensure --vendor-only

## Build

From `src/shippingservice`, run:

```
docker build -t shippingservice .
```

## Test

```
go test .
```

## Running docker image

```
docker run \
-p 50051:50051 \
-e PORT=50051 \
-e NEW_RELIC_LICENSE_KEY=$NEW_RELIC_LICENSE_KEY \
-e NEW_RELIC_APP_NAME="shippingservice" \
-e NEW_RELIC_LOG=stdout \
-e NEW_RELIC_LOG_LEVEL=debug \
shippingservice
```