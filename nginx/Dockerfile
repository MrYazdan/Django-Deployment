FROM nginx:alpine

COPY ./default.conf /etc/nginx/conf.d/

ENTRYPOINT nginx-debug -g 'daemon off;'
