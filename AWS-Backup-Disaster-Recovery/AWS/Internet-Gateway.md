# 🌐 Internet Gateway (IGW)

## Overview

An **Internet Gateway (IGW)** is a horizontally scaled, highly available AWS networking component that enables communication between resources inside a VPC and the public internet.

It serves as the gateway for inbound and outbound internet traffic.

In this project, an Internet Gateway was attached to the custom VPC to provide internet connectivity for the EC2 instance.

---

# Purpose

The Internet Gateway was used to:

- Enable SSH access to the EC2 instance.
- Allow HTTP/HTTPS traffic to the web server.
- Enable internet access for software installation and system updates.
- Allow communication with AWS public services.

Without an Internet Gateway, the EC2 instance would not have internet connectivity.

---

# Configuration Used

| Property | Value |
|----------|-------|
| Internet Gateway Name | Backup-DR-IGW |
| Attached VPC | Backup-DR-VPC |
| Route Table Association | Public Route Table |
| Route | 0.0.0.0/0 → Internet Gateway |

---

# Architecture

```text
                 Internet
                     │
                     │
          Internet Gateway (IGW)
                     │
              Backup-DR-VPC
                     │
            Public Route Table
                     │
             Public Subnet
                     │
             Backup-WebServer
```

---

# How It Works

1. An EC2 instance sends traffic destined for the internet.
2. The subnet's Route Table checks the destination.
3. Traffic matching `0.0.0.0/0` is forwarded to the Internet Gateway.
4. The Internet Gateway routes the traffic to the internet.
5. Response traffic follows the same path back to the EC2 instance.

---

# Route Table Configuration

The Public Route Table contains the following route:

| Destination | Target |
|-------------|--------|
| 0.0.0.0/0 | Internet Gateway |

This route enables all outbound internet traffic.

---

# Network Traffic Flow

```text
EC2 Instance

↓

Public Subnet

↓

Route Table

↓

Internet Gateway

↓

Internet
```

---

# Resources Using the Internet Gateway

The following resource depends on the Internet Gateway:

- Amazon EC2 (Backup-WebServer)

The EC2 instance used the Internet Gateway for:

- SSH Login
- Nginx Installation
- Package Updates
- Accessing AWS Services
- Serving the Web Application

---

# Why It Was Required in This Project

The Backup-WebServer needed internet access to:

- Connect through SSH
- Install software packages using `dnf`
- Download security updates
- Host a web application
- Communicate with AWS services

Without the Internet Gateway, none of these operations would have been possible from the internet.

---

# Security Considerations

The Internet Gateway itself does **not** filter traffic.

Security is enforced using:

- Security Groups
- Route Tables
- Network ACLs (optional)

Only ports **22**, **80**, and **443** were allowed through the Security Group.

---

# Key Features

- Highly Available
- Horizontally Scalable
- Managed AWS Service
- No Maintenance Required
- Supports IPv4 and IPv6 Traffic
- Enables Public Internet Connectivity

---

# Project Implementation

As part of this project:

- Created **Backup-DR-IGW**
- Attached the Internet Gateway to **Backup-DR-VPC**
- Updated the Public Route Table
- Added the route `0.0.0.0/0 → Internet Gateway`
- Verified internet connectivity using SSH and HTTP

---

# Learning Outcomes

Through implementing the Internet Gateway, the following concepts were learned:

- Internet Connectivity in AWS
- VPC Networking
- Public Routing
- Route Table Association
- Public Subnet Architecture
- EC2 Internet Access
- AWS Network Design

---

# Interview Questions

### Q1. What is an Internet Gateway?

An Internet Gateway is a VPC component that enables communication between resources inside a VPC and the public internet.

---

### Q2. Why was an Internet Gateway required in this project?

It allowed the EC2 instance to communicate with the internet for SSH access, software installation, package updates, and web application access.

---

### Q3. Does attaching an Internet Gateway automatically make an EC2 instance public?

No. The following are also required:

- A Public Subnet
- A Route Table with `0.0.0.0/0` pointing to the Internet Gateway
- A Public IP or Elastic IP assigned to the EC2 instance
- Security Group rules allowing the required traffic

---

### Q4. Can multiple VPCs share the same Internet Gateway?

No. An Internet Gateway can be attached to only one VPC at a time.

---

# Conclusion

The Internet Gateway provides the internet connectivity required for the EC2 instance in this project. By attaching it to the custom VPC and configuring the Route Table, the application server was able to communicate with external networks, enabling remote administration, application deployment, and successful validation of the AWS Backup & Disaster Recovery solution.
