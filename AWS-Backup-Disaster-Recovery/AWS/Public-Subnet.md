# 🌍 Public Subnet

## Overview

A **Public Subnet** is a subnet within an Amazon VPC that allows resources to communicate directly with the internet through an **Internet Gateway (IGW)**. Resources deployed in a public subnet can have a **public IPv4 address**, making them accessible for services such as SSH, web hosting, and APIs.

In this project, the **Backup-WebServer EC2 instance** was deployed inside a public subnet to enable secure remote administration and web application access.

---

# Why Public Subnet?

Public subnets are commonly used to host internet-facing resources, such as:

- Web Servers
- Bastion Hosts
- Load Balancers
- API Servers
- Reverse Proxy Servers

For this Backup & Disaster Recovery project, a public subnet was required so that the EC2 instance could:

- Be accessed via SSH
- Serve a web application (Nginx)
- Download software packages from the internet
- Communicate with AWS services

---

# Project Architecture

```text
                     Backup-DR-VPC
                     10.0.0.0/16
                            │
        ┌──────────────────────────────────────┐
        │                                      │
        │        Public Subnet                 │
        │         10.0.1.0/24                  │
        │                                      │
        │     Backup-WebServer (EC2)           │
        │           Amazon Linux               │
        │                                      │
        └──────────────────────────────────────┘
                            │
                    Route Table
                            │
                     Internet Gateway
                            │
                         Internet
```

---

# Configuration Used

| Property | Value |
|----------|-------|
| Subnet Name | Public-Subnet-1 |
| VPC | Backup-DR-VPC |
| CIDR Block | 10.0.1.0/24 |
| Availability Zone | ap-south-1a |
| Auto Assign Public IPv4 | Enabled |

---

# CIDR Block

The subnet was created with the following CIDR block:

```
10.0.1.0/24
```

This provides:

- **256 IP addresses**
- Approximately **251 usable private IP addresses** (AWS reserves 5 IPs per subnet)

---

# Availability Zone

The subnet was deployed in:

```
ap-south-1a
```

Using a specific Availability Zone ensures predictable resource placement and low latency between resources in the same AZ.

---

# Auto Assign Public IPv4

The **Auto Assign Public IPv4** option was enabled.

### Why?

Whenever a new EC2 instance is launched into this subnet, AWS automatically assigns a public IPv4 address.

Without a public IP:

- SSH access from the internet would not work.
- HTTP/HTTPS traffic from users would not reach the instance.
- The instance would require a Bastion Host, NAT Gateway, or VPN for external access.

---

# Route Configuration

The public subnet is associated with a route table containing the following route:

| Destination | Target |
|-------------|--------|
| 0.0.0.0/0 | Internet Gateway |

This route allows outbound and inbound internet traffic.

---

# Internet Connectivity Flow

```text
Internet

↓

Internet Gateway

↓

Route Table

↓

Public Subnet

↓

EC2 Instance
```

This routing path allows internet traffic to reach the EC2 instance.

---

# Resources Hosted

The following resources were deployed in this public subnet:

- Amazon EC2 (Backup-WebServer)
- Root EBS Volume
- Additional EBS Data Volume

These resources form the application server used for backup and disaster recovery testing.

---

# Why Was a Public Subnet Used?

The EC2 instance needed internet connectivity for:

- SSH administration
- Installing Nginx
- Downloading system updates
- Accessing AWS services
- Testing the web application

A public subnet simplifies these tasks during development and testing.

---

# Security Considerations

Although the subnet is public, security is enforced using **Security Groups**.

Allowed inbound traffic:

| Protocol | Port | Purpose |
|----------|------|----------|
| SSH | 22 | Remote Administration |
| HTTP | 80 | Web Application |
| HTTPS | 443 | Secure Web Traffic |

All other inbound traffic remains blocked.

---

# Public vs Private Subnet

| Public Subnet | Private Subnet |
|---------------|----------------|
| Has internet access | No direct internet access |
| Uses Internet Gateway | Uses NAT Gateway for outbound traffic |
| Suitable for Web Servers | Suitable for Databases |
| Can have Public IP | Only Private IP |

In this project, the public subnet was chosen because the EC2 instance needed to be directly accessible for deployment, testing, and demonstration.

---

# Enterprise Best Practices

In production environments:

- Public subnets host internet-facing resources such as Load Balancers and Bastion Hosts.
- Application servers and databases are usually deployed in private subnets.
- Security Groups and Network ACLs are configured to restrict unnecessary access.
- Multi-AZ deployments improve availability.

For this project, a single public subnet was sufficient to demonstrate backup and disaster recovery concepts.

---

# Advantages

- Direct internet connectivity
- Easy SSH access
- Supports web hosting
- Simplifies application deployment
- Enables software updates and package installation
- Suitable for demonstration and testing environments

---

# Project Implementation

As part of this project:

- Created **Public-Subnet-1**
- Configured CIDR block **10.0.1.0/24**
- Enabled Auto Assign Public IPv4
- Associated the subnet with the Public Route Table
- Deployed the Backup-WebServer EC2 instance
- Verified internet connectivity through SSH and HTTP

---

# Learning Outcomes

Through this implementation, the following concepts were learned:

- Amazon Subnets
- Public Networking
- CIDR Planning
- Availability Zones
- Internet Routing
- Public IP Address Assignment
- EC2 Deployment
- AWS Network Design
- Cloud Infrastructure Best Practices

---

# Interview Questions

### Q1. What is a Public Subnet?

A Public Subnet is a subnet associated with a route table that has a route to an Internet Gateway, allowing resources within the subnet to communicate with the internet.

---

### Q2. Why did you use a Public Subnet in this project?

The EC2 instance required internet access for SSH administration, software installation, AWS service communication, and hosting the Nginx web application.

---

### Q3. What happens if Auto Assign Public IPv4 is disabled?

The EC2 instance receives only a private IP address. It cannot be accessed directly from the internet unless an Elastic IP is associated later or connectivity is provided through a Bastion Host, VPN, or AWS Systems Manager Session Manager.

---

### Q4. Can a Public Subnet exist without an Internet Gateway?

Yes, but it will not function as a true public subnet because there is no route for internet traffic. Resources would remain isolated despite being in a subnet designated as "public."

---

# Conclusion

The **Public Subnet** provides the network environment where the application server operates. By configuring internet routing, enabling automatic public IP assignment, and deploying the EC2 instance within the subnet, the infrastructure supports secure remote administration, application hosting, and AWS Backup testing. This configuration mirrors common cloud networking practices used for internet-facing workloads while serving as the foundation for the Backup & Disaster Recovery solution.
