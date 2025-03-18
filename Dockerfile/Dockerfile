FROM nginx:1.19.10-alpine

RUN apk add --no-cache tini

RUN chmod -R 755 /usr/share/nginx/html && \
    chown -R nginx:nginx /var/cache/nginx /var/log/nginx /etc/nginx

COPY nginx.conf /etc/nginx/nginx.conf

USER nginx

EXPOSE 8080

ENTRYPOINT ["/sbin/tini", "--"]
CMD ["nginx", "-g", "daemon off;"]