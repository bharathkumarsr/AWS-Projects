# 🔐 Amazon EC2 Security Group

## Overview

An **Amazon EC2 Security Group** is a virtual firewall that controls inbound and outbound traffic for AWS resources. It operates at the **instance level** and allows only explicitly permitted traffic to reach an EC2 instance.

In this project, a Security Group was configured to secure the **Backup-WebServer** while allowing only the required protocols for administration and web application access.

---

# Purpose

The Security Group was used to:

- Allow administrators to connect using SSH.
- Allow users to access the web application over HTTP.
- Support secure HTTPS communication.
- Protect the EC2 instance from unauthorized network access.
- Restrict unnecessary inbound traffic.

Without a Security Group, the EC2 instance would not accept any inbound traffic.

---

# Configuration Used

| Property | Value |
|----------|-------|
| Security Group Name | Backup-DR-SG |
| Associated VPC | Backup-DR-VPC |
| Resource Protected | Backup-WebServer EC2 Instance |

---

# Architecture

```text
                   Internet
                       │
               Internet Gateway
                       │
                Public Route Table
                       │
                 Public Subnet
                       │
          ┌──────────────────────────┐
          │ Backup-WebServer (EC2)   │
          │                          │
          │  Security Group          │
          │      Backup-DR-SG        │
          └──────────────────────────┘
```

---

# Inbound Rules

The following inbound rules were configured:

| Type | Protocol | Port | Source | Purpose |
|------|----------|------|---------|----------|
| SSH | TCP | 22 | My IP / Anywhere (Demo) | Remote Administration |
| HTTP | TCP | 80 | 0.0.0.0/0 | Web Application Access |
| HTTPS | TCP | 443 | 0.0.0.0/0 | Secure Web Traffic |

---

## SSH (Port 22)

```
Protocol : TCP
Port     : 22
```

### Purpose

Allows administrators to remotely connect to the EC2 instance using SSH.

Used for:

- Server Administration
- Package Installation
- Configuration Changes
- Backup Validation
- Disaster Recovery Testing

---

## HTTP (Port 80)

```
Protocol : TCP
Port     : 80
```

### Purpose

Allows users to access the Nginx web application using a web browser.

Example:

```
http://<Public-IP>
```

---

## HTTPS (Port 443)

```
Protocol : TCP
Port     : 443
```

### Purpose

Supports secure encrypted web traffic.

Although SSL certificates were not configured in this project, opening port 443 prepares the infrastructure for secure HTTPS communication.

---

# Outbound Rules

The default outbound rule was retained.

| Type | Protocol | Port | Destination |
|------|----------|------|-------------|
| All Traffic | All | All | 0.0.0.0/0 |

### Purpose

Allows the EC2 instance to initiate outbound connections for:

- Software installation
- Linux updates
- AWS API communication
- DNS resolution
- Internet access

---

# Traffic Flow

```text
SSH Client

↓

Security Group

↓

EC2 Instance
```

```text
Web Browser

↓

HTTP/HTTPS

↓

Security Group

↓

Nginx Web Server
```

---

# How Security Groups Work

Security Groups are **stateful**.

This means:

- If inbound traffic is allowed, the response is automatically allowed.
- Return traffic does not require additional outbound rules.

Example:

```
Client

↓

HTTP Request

↓

EC2

↓

HTTP Response

↓

Allowed Automatically
```

---

# Resources Protected

The Security Group protected:

- Backup-WebServer EC2 Instance

The following services were accessible through it:

- SSH
- HTTP
- HTTPS

---

# Why It Was Required

The EC2 instance needed controlled network access for:

- Remote administration
- Application deployment
- Browser access
- Backup validation
- Disaster Recovery testing

The Security Group ensured that only approved traffic reached the server.

---

# Best Practices

- Allow only required ports.
- Restrict SSH access to trusted IP addresses whenever possible.
- Avoid exposing unnecessary services.
- Use separate Security Groups for different application tiers.
- Regularly review and remove unused rules.

---

# Project Implementation

As part of this project:

- Created **Backup-DR-SG**
- Attached it to the Backup-WebServer EC2 instance
- Allowed inbound SSH (22)
- Allowed inbound HTTP (80)
- Allowed inbound HTTPS (443)
- Retained the default outbound rule allowing all outbound traffic
- Verified connectivity using SSH and a web browser

---

# Learning Outcomes

Through implementing the Security Group, the following concepts were learned:

- AWS Security Groups
- Stateful Firewalls
- Inbound Rules
- Outbound Rules
- EC2 Network Security
- Application Access Control
- Secure Cloud Networking
- AWS Best Practices

---

# Interview Questions

### Q1. What is a Security Group?

A Security Group is a stateful virtual firewall that controls inbound and outbound network traffic for AWS resources such as EC2 instances.

---

### Q2. Why did you use a Security Group in this project?

The Security Group protected the EC2 instance by allowing only the required ports for SSH administration and web application access while blocking all other inbound traffic.

---

### Q3. Which ports were opened?

| Port | Purpose |
|------|----------|
| 22 | SSH Administration |
| 80 | HTTP Web Traffic |
| 443 | HTTPS Secure Web Traffic |

---

### Q4. What is the difference between a Security Group and a Network ACL?

| Security Group | Network ACL |
|----------------|-------------|
| Stateful | Stateless |
| Applied to EC2 instances | Applied to Subnets |
| Supports Allow rules only | Supports Allow and Deny rules |
| Return traffic is automatically allowed | Return traffic must be explicitly allowed |

---

### Q5. What would happen if port 22 was not allowed?

SSH connections to the EC2 instance would fail, preventing administrators from remotely managing the server.

---

### Q6. Why was HTTPS (443) opened even though SSL was not configured?

Port 443 was opened to prepare the infrastructure for future HTTPS support. In production environments, HTTPS is typically enabled using SSL/TLS certificates.

---

# Conclusion

The **Backup-DR-SG** Security Group served as the primary network security layer for the EC2 instance. It allowed secure administrative access through SSH and enabled web traffic over HTTP and HTTPS while blocking all unnecessary inbound connections. By implementing a minimal and controlled rule set, the project followed AWS security best practices and ensured secure access throughout the Backup & Disaster Recovery lifecycle.
