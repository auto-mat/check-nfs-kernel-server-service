FROM alpine:3.19.0

LABEL authors="Auto*Mat, z. s. auto-mat@auto-mat.cz"
LABEL maintainer="Auto*Mat, z. s. auto-mat@auto-mat.cz"

ENV DO_BASE_API_URL="https://api.digitalocean.com/v2"

RUN apk update && apk add --no-cache curl doctl python3 py3-requests; \
    curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"; \
    chmod +x ./kubectl; \
    mv ./kubectl /usr/local/bin/kubectl;
COPY ./check_host_nfs_service.sh /usr/local/bin
COPY ./check_floating_ip_is_assigned.py /usr/local/bin
CMD ["/bin/sh"]