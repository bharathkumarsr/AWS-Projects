# Dockerized NGINX Deployment

## Objective

Deploy a web application using Docker and NGINX.

---

## Deployment

Pulled image:

```bash
docker pull nginx
```

Started container:

```bash
docker run -d \
--name enterprise-nginx \
-p 80:80 \
nginx
```

---

## Validation

```bash
docker ps
```

Accessed:

```text
http://PUBLIC-IP
```

Successfully displayed:

```text
Welcome to nginx!
```

---

## Why NGINX?

- Lightweight
- High performance
- Reverse proxy support
- Container friendly
