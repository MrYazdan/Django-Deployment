FROM nginx:alpine

COPY ./certs /
COPY ./default.conf /etc/nginx/

ENTRYPOINT nginx-debug -g 'daemon off;'
