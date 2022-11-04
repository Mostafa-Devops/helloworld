FROM nginx:1.22.1

RUN rm -rf /etc/nginx/conf.d/default.conf
COPY ./helloworld_nginx.conf /etc/nginx/conf.d

EXPOSE 80
