FROM nginx:alpine

COPY ./certs /
COPY ./default.conf /etc/nginx/conf.d/

ENTRYPOINT nginx-debug -g 'daemon off;'
