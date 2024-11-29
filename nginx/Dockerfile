FROM nginx:alpine

COPY ./default.conf /etc/nginx/conf.d/

COPY entrypoint.sh /

RUN chmod +x /entrypoint.sh

CMD ["/entrypoint.sh"]
