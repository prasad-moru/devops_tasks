FROM alpine:3.14 AS builder

RUN apk add --no-cache \
    curl \
    gcc \
    libc-dev \
    make \
    openssl-dev \
    pcre-dev \
    zlib-dev

RUN curl -fSL https://nginx.org/download/nginx-1.19.10.tar.gz -o nginx.tar.gz && \
    mkdir -p /usr/src/nginx && \
    tar -zxC /usr/src/nginx -f nginx.tar.gz && \
    rm nginx.tar.gz

WORKDIR /usr/src/nginx/nginx-1.19.10
RUN ./configure \
    --prefix=/usr/share/nginx \
    --sbin-path=/usr/sbin/nginx \
    --conf-path=/etc/nginx/nginx.conf \
    --error-log-path=/var/log/nginx/error.log \
    --http-log-path=/var/log/nginx/access.log \
    --pid-path=/var/run/nginx.pid \
    --lock-path=/var/run/nginx.lock \
    --user=nginx \
    --group=nginx \
    --with-threads \
    --with-file-aio \
    --with-http_ssl_module \
    --with-http_v2_module \
    --with-http_realip_module \
    --with-http_stub_status_module \
    --without-http_autoindex_module \
    --without-http_ssi_module && \
    make -j$(nproc) && \
    make install

FROM alpine:3.14

RUN addgroup -S nginx && \
    adduser -S -D -H -h /var/cache/nginx -s /sbin/nologin -G nginx nginx

RUN apk add --no-cache \
    pcre \
    openssl \
    tzdata \
    tini \
    ca-certificates && \
    mkdir -p /var/log/nginx /var/cache/nginx /etc/nginx/conf.d

COPY --from=builder /usr/sbin/nginx /usr/sbin/nginx
COPY --from=builder /usr/share/nginx /usr/share/nginx
COPY --from=builder /etc/nginx /etc/nginx

RUN mkdir -p /usr/share/nginx/html /etc/nginx/conf.d

COPY nginx.conf /etc/nginx/nginx.conf
COPY default.conf /etc/nginx/conf.d/default.conf

RUN chown -R nginx:nginx /usr/share/nginx /var/log/nginx /var/cache/nginx /etc/nginx && \
    chmod -R 755 /usr/share/nginx/html && \
    chmod -R 644 /usr/share/nginx/html/*

EXPOSE 8080

ENTRYPOINT ["/sbin/tini", "--"]

CMD ["nginx", "-g", "daemon off;"]

USER nginx