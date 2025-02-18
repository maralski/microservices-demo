# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

FROM --platform=$BUILDPLATFORM python:3.12.8@sha256:e74938514dc67ad3eade8798aa929f5dd569e463758c83243636d4e1b54aa559 AS base

FROM base AS builder

# get packages
COPY requirements.in .
RUN pip install pip-tools
# This generates the requirements.txt file
RUN pip-compile requirements.in
RUN pip install -r requirements.txt

FROM base
# Enable unbuffered logging
ENV PYTHONUNBUFFERED=1
# Enable Profiler
ENV ENABLE_PROFILER=1

WORKDIR /email_server

# Grab packages from builder
COPY --from=builder /usr/local/lib/python3.12/ /usr/local/lib/python3.12/

# Add the application
COPY . .

# Install New Relic Python agent
ARG NEWRELIC_AGENT_VERSION
ENV NEWRELIC_AGENT_VERSION=${NEWRELIC_AGENT_VERSION:-10.6.0}
RUN pip install newrelic==$NEWRELIC_AGENT_VERSION

EXPOSE 8080
ENTRYPOINT [ "python", "email_server.py" ]
