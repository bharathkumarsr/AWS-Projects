# 🛣️ Route Table

## Overview

An **Amazon VPC Route Table** is a networking component that controls how network traffic is directed within a VPC. It contains a set of routing rules (routes) that determine where traffic from a subnet should be sent based on its destination.

In this project, a **Public Route Table** was created and associated with the public subnet to provide internet connectivity to the EC2 instance through the Internet Gateway.

---

# Purpose

The Route Table was used to:

- Enable internet access for the EC2 instance.
- Route outbound traffic to the Internet Gateway.
- Allow inbound traffic from the internet to reach the EC2 instance.
- Control network traffic within the VPC.

Without a Route Table, resources inside the subnet would not know where to send traffic destined for external networks.

---

# Configuration Used

| Property | Value |
|----------|-------|
| Route Table Name | Backup-DR-Public-RT |
| Associated VPC | Backup-DR-VPC |
| Associated Subnet | Public-Subnet-1 |
| Destination | 0.0.0.0/0 |
| Target | Internet Gateway (Backup-DR-IGW) |

---

# Architecture

```text
                 Internet
                     │
             Internet Gateway
                     │
        Backup-DR-Public-RT
                     │
             Public-Subnet-1
                     │
          Backup-WebServer (EC2)
```

---

# Route Configuration

The following route was configured in the Route Table:

| Destination | Target | Purpose |
|-------------|--------|---------|
| 10.0.0.0/16 | Local | Communication within the VPC |
| 0.0.0.0/0 | Internet Gateway | Internet access |

### Local Route

```
Destination : 10.0.0.0/16
Target      : Local
```

This route is automatically created by AWS and enables communication between resources inside the same VPC.

---

### Internet Route

```
Destination : 0.0.0.0/0
Target      : Internet Gateway
```

This route sends all internet-bound traffic to the Internet Gateway.

---

# Subnet Association

The Route Table was associated with:

```
Public-Subnet-1
```

Only subnets associated with this Route Table can use the configured routes.

If the subnet is not associated with the Route Table, internet connectivity will not work.

---

# Traffic Flow

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

# Why It Was Required

The EC2 instance required internet connectivity for:

- SSH Remote Access
- Installing Nginx
- Downloading Linux packages
- System updates
- Accessing AWS services
- Serving web traffic

The Route Table provided the path for this traffic.

---

# Issue Encountered During Project

Initially, the EC2 instance could not be accessed through SSH.

### Cause

The Public Subnet was **not associated** with the correct Route Table.

Without this association, traffic destined for the internet had no valid route.

### Resolution

- Associated the Public Subnet with the Public Route Table.
- Verified that the route `0.0.0.0/0 → Internet Gateway` was present.
- SSH connectivity was restored successfully.

This demonstrated the importance of correct Route Table associations in AWS networking.

---

# Resources Using This Route Table

The following resources depended on this Route Table:

- Public-Subnet-1
- Backup-WebServer EC2 Instance

All outbound internet traffic from these resources followed the configured routes.

---

# Best Practices

- Create separate Route Tables for public and private subnets.
- Associate each subnet with the appropriate Route Table.
- Use Internet Gateway only for public subnets.
- Use NAT Gateway for internet access from private subnets.
- Keep routing simple and well documented.

---

# Project Implementation

As part of this project:

- Created **Backup-DR-Public-RT**
- Added the default Local route
- Added the route `0.0.0.0/0 → Internet Gateway`
- Associated the Route Table with **Public-Subnet-1**
- Verified internet connectivity from the EC2 instance

---

# Learning Outcomes

Through implementing the Route Table, the following concepts were learned:

- Amazon VPC Routing
- Public Route Tables
- Route Configuration
- Subnet Association
- Internet Connectivity
- Local Routing
- AWS Network Troubleshooting
- Traffic Flow in AWS

---

# Interview Questions

### Q1. What is a Route Table in AWS?

A Route Table is a set of routing rules that determines where network traffic from a subnet is directed.

---

### Q2. Why was a Route Table required in this project?

The Route Table directed internet-bound traffic from the EC2 instance to the Internet Gateway, enabling SSH access, package installation, and web application connectivity.

---

### Q3. What is the purpose of the `0.0.0.0/0` route?

It represents the default route for all IPv4 internet traffic and forwards it to the Internet Gateway.

---

### Q4. What happens if a subnet is not associated with the correct Route Table?

Resources in that subnet cannot use the routes defined in the Route Table. In this project, SSH failed until the Public Subnet was associated with the correct Route Table.

---

### Q5. What is the difference between the Local route and the Internet route?

| Local Route | Internet Route |
|-------------|----------------|
| Enables communication within the VPC | Enables communication with the public internet |
| Created automatically by AWS | Added manually by the user |
| Target = Local | Target = Internet Gateway |

---

# Conclusion

The Route Table is a critical networking component that determines how traffic flows within and outside the VPC. In this project, the Public Route Table enabled secure internet connectivity by routing traffic from the EC2 instance to the Internet Gateway. Proper Route Table configuration and subnet association were essential for successful SSH access, web application deployment, and the overall AWS Backup & Disaster Recovery implementation.
