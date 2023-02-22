## Building docker image

From `src/cartservice/`, run:

```
docker build -t cartservice .
```

## Running docker image

```
 docker run \
 -p 7070:7070 \
 -e NEW_RELIC_LICENSE_KEY=$NEW_RELIC_LICENSE_KEY \
 -e NEW_RELIC_APP_NAME="cartservice" \
 -e REDIS_ADDR="redis-cart:6379" \
 cartservice
```

