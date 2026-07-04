# Amazon EC2 Configuration

## Objective

Provision a Linux server to host containerized enterprise applications.

---

## Instance Details

| Parameter | Value |
|-----------|---------|
| Name | DevOps-Docker-Server |
| Instance Type | t3.micro |
| OS | Amazon Linux 2023 6.18 |
| Region | ap-south-1 |
| Storage | 8 GB |

---

## Security Group

| Port | Protocol | Purpose |
|------|---------|----------|
| 22 | TCP | SSH |
| 80 | TCP | HTTP |
| 443 | TCP | HTTPS |

---

## IAM Role Attached

```text
EC2-S3-Role
```

---

## Validation

```bash
hostnamectl

aws sts get-caller-identity

curl ifconfig.me
```

---

## Why EC2?

- Flexible compute
- Scalable
- Supports container workloads
- Integrates with AWS ecosystem
