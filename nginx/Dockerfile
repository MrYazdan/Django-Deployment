FROM nginx:alpine

COPY ./default.conf /etc/nginx/conf.d/

RUN chmod +x /entrypoint.sh

CMD ["/entrypoint.sh"]
