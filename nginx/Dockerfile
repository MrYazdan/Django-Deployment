FROM nginx:alpine

COPY ./certs /
COPY ./default.conf /etc/nginx/

RUN nginx-debug -g 'daemon off;'