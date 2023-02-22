## Building docker image

From `src/emailservice/`, run:

```
docker build -t emailservice .
```

Can pass `NEWRELIC_AGENT_VERSION` as `--build-arg` to pip install particular version.

## Running docker image

```
 docker run \
 -p 8080:8080 \
 -e NEW_RELIC_LICENSE_KEY=$NEW_RELIC_LICENSE_KEY \
 -e NEW_RELIC_APP_NAME="emailservice" \
 -e NEW_RELIC_LOG=stderr \
 -e NEW_RELIC_LOG_LEVEL=debug \
 emailservice
```

