FROM python:3.8-slim-buster

ARG service
ARG region
ARG action
ARG instance_id
ARG db_cluster_identifiers
ARG cluster_name
ARG start_desired_count
ARG stop_desired_count

ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY
ARG AWS_SESSION_TOKEN
ENV AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}
ENV AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}
ENV AWS_SESSION_TOKEN=${AWS_SESSION_TOKEN}

ENV service=${service}
ENV region=${region}
ENV action=${action}
ENV instance_id=${instance_id}
ENV db_cluster_identifiers=${db_cluster_identifiers}
ENV cluster_name=${cluster_name}
ENV start_desired_count=${start_desired_count}
ENV stop_desired_count=${stop_desired_count}

WORKDIR /app
COPY ./docker/startup.sh ./onOffService ./
RUN chmod +x startup.sh
CMD ./startup.sh
