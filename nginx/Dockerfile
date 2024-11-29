FROM nginx:stable-alpine

USER root

RUN apk add --update openssl bash

COPY ./default.conf /etc/nginx/conf.d/
COPY ./entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

CMD ["/entrypoint.sh"]

