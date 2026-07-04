# Docker Installation

## Objective

Install Docker Engine to deploy applications using containers.

---

## Installation

Updated packages:

```bash
sudo dnf update -y
```

Installed Docker:

```bash
sudo dnf install podman-docker -y
```

Started service:

```bash
sudo systemctl enable docker
sudo systemctl start docker
```

---

## Validation

```bash
docker --version

docker images

docker ps
```

---

## Why Docker?

- Containerization
- Portability
- Fast deployment
- Isolation
- Scalability

---

## Key Learning

Docker enables consistent deployment across environments.
