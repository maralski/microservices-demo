## Building docker image

From `src/currencyservice/`, run:

```
docker build -t currencyservice .
```

## Running docker image

```
 docker run \
 -p 7000:7000 \
 -e PORT=7000 \
 -e NEW_RELIC_LICENSE_KEY=$NEW_RELIC_LICENSE_KEY \
 -e NEW_RELIC_APP_NAME="currencyservice" \
 -e NEW_RELIC_LOG=stdout \
 -e NEW_RELIC_LOG_LEVEL=debug \
 -e NEW_RELIC_NO_CONFIG_FILE=true \
 currencyservice
```

