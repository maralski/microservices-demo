## Building docker image

From `src/paymentservice/`, run:

```
docker build -t paymentservice .
```

## Running docker image

```
docker run \
-p 50051:50051 \
-e PORT=50051 \
-e NEW_RELIC_LICENSE_KEY=$NEW_RELIC_LICENSE_KEY \
-e NEW_RELIC_APP_NAME="paymentservice" \
-e NEW_RELIC_LOG=stdout \
-e NEW_RELIC_LOG_LEVEL=debug \
-e NEW_RELIC_NO_CONFIG_FILE=true \
paymentservice
```