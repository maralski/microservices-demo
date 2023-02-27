# checkoutservice

Run the following command to restore dependencies to `vendor/` directory:

    dep ensure --vendor-only

## Building docker image

From `src/checkoutservice/`, run:

```
docker build -t checkoutservice .
```

## Running docker image

```
docker run \
-p 5050:5050 \
-e PORT=5050 \
-e NEW_RELIC_LICENSE_KEY=$NEW_RELIC_LICENSE_KEY \
-e NEW_RELIC_APP_NAME="checkoutservice" \
-e NEW_RELIC_LOG=stdout \
-e NEW_RELIC_LOG_LEVEL=debug \
checkoutservice
```