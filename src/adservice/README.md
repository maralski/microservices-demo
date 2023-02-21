# Ad Service

The Ad service provides advertisement based on context keys. If no context keys are provided then it returns random ads.

## Building locally

The Ad service uses gradlew to compile/install/distribute. Gradle wrapper is already part of the source code. To build Ad Service, run:

```
./gradlew installDist
```
It will create executable script src/adservice/build/install/hipstershop/bin/AdService

### Upgrading gradle version
If you need to upgrade the version of gradle then run

```
./gradlew wrapper --gradle-version <new-version>
```

## Building docker image

From `src/adservice/`, run:

```
docker build -t adservice .
```

Can pass `NEWRELIC_AGENT_DOWNLOAD` as `--build-arg` pointing to agent URL to download.

## Running docker image

```
docker run \
 -p 9555:9555 \
 -e NEW_RELIC_LICENSE_KEY=$NEW_RELIC_LICENSE_KEY \
 -e NEW_RELIC_APP_NAME="adservice" \
 -e NEW_RELIC_LOG_FILE_NAME=STDOUT \
 -e JAVA_OPTS="-javaagent:/app/newrelic/newrelic.jar" \
 adservice
```

