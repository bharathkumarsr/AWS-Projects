# 🌐 Amazon VPC (Virtual Private Cloud)

## Overview

Amazon Virtual Private Cloud (Amazon VPC) is a networking service that allows you to create a logically isolated virtual network within AWS. It gives complete control over IP addressing, subnets, routing, internet access, and network security for cloud resources.

In this project, a custom VPC was created to host the entire Backup & Disaster Recovery infrastructure instead of using the default VPC. This reflects how production environments are typically designed.

---

# Why Amazon VPC?

A Virtual Private Cloud is the foundation of almost every AWS infrastructure deployment.

Using a custom VPC provides:

- Network isolation
- Secure communication between resources
- Custom IP addressing
- Internet connectivity control
- Fine-grained routing
- Better security architecture
- Scalability for future expansion

Instead of placing resources into the AWS Default VPC, a dedicated VPC was designed specifically for this Disaster Recovery project.

---

# Architecture

```
                    AWS Cloud
                         │
                 Backup-DR-VPC
                 10.0.0.0/16
                         │
        ┌────────────────────────────────┐
        │                                │
   Public Subnet                  Future Private Subnet
   10.0.1.0/24                      10.0.2.0/24
        │
        │
   Backup-WebServer
        │
        │
 Internet Gateway
        │
     Internet
```

---

# Configuration

| Property | Value |
|----------|-------|
| VPC Name | Backup-DR-VPC |
| CIDR Block | 10.0.0.0/16 |
| DNS Resolution | Enabled |
| DNS Hostnames | Enabled |
| Tenancy | Default |

---

# CIDR Block

The VPC was configured using

```
10.0.0.0/16
```

This provides

```
65,536 IP Addresses
```

The address range starts from

```
10.0.0.0
```

to

```
10.0.255.255
```

This allows multiple subnets to be created in the future.

---

# Why /16?

Using a /16 CIDR block is a common enterprise practice because it provides enough IP addresses for future expansion without needing to redesign the network.

Benefits include:

- Multiple public subnets
- Multiple private subnets
- High Availability
- Multi-AZ deployments
- Scalable architecture

---

# DNS Resolution

DNS Resolution was enabled.

Purpose:

Allows EC2 instances inside the VPC to resolve domain names into IP addresses.

Without DNS Resolution:

- yum update fails
- dnf install fails
- Package downloads fail
- Internet hostname resolution does not work properly

---

# DNS Hostnames

DNS Hostnames were enabled.

Purpose:

Automatically assigns internal DNS names to EC2 instances.

Example

```
ip-10-0-1-76.ap-south-1.compute.internal
```

This is useful for:

- Internal communication
- Service discovery
- Load Balancers
- Route 53 integration

---

# Why a Custom VPC?

Using the default VPC is convenient for learning but is generally avoided in production environments.

A custom VPC provides:

- Better security
- Controlled networking
- Custom routing
- Dedicated infrastructure
- Easier compliance with organizational standards

This project follows that best practice.

---

# Network Isolation

The VPC acts as a secure boundary around all cloud resources.

Resources inside the VPC include:

- Amazon EC2
- Amazon EBS
- Security Groups
- Route Tables
- Internet Gateway

Only resources inside this VPC can communicate directly unless additional networking configurations such as VPC Peering or VPNs are established.

---

# High-Level Traffic Flow

```
Internet

↓

Internet Gateway

↓

Route Table

↓

Public Subnet

↓

EC2 Instance

↓

Application
```

---

# Components Inside the VPC

The following AWS resources were deployed inside the VPC:

- Public Subnet
- Route Table
- Internet Gateway
- Security Group
- EC2 Instance
- Root EBS Volume
- Data EBS Volume

Together, these components form the production network where the application runs.

---

# Security Considerations

The VPC improves security by:

- Isolating infrastructure from other AWS customers
- Allowing custom routing policies
- Restricting inbound traffic using Security Groups
- Supporting future implementation of private subnets and NAT Gateways

This creates a secure foundation for the Backup & Disaster Recovery solution.

---

# Real-World Use Cases

Organizations use Amazon VPC for:

- Hosting production web applications
- Running Kubernetes clusters
- Database deployments
- Disaster Recovery environments
- DevOps CI/CD infrastructure
- Multi-tier application architectures

In this project, Amazon VPC serves as the secure network foundation for the Disaster Recovery environment.

---

# What Was Implemented in This Project?

✔ Created a custom VPC

✔ Configured CIDR block (10.0.0.0/16)

✔ Enabled DNS Resolution

✔ Enabled DNS Hostnames

✔ Deployed networking resources inside the VPC

✔ Hosted EC2 instance within the VPC

✔ Connected the VPC to the internet using an Internet Gateway

✔ Configured routing through a Route Table

✔ Used the VPC as the network foundation for AWS Backup and Disaster Recovery

---

# Learning Outcomes

Through implementing Amazon VPC in this project, the following concepts were learned:

- VPC Design
- CIDR Planning
- Public Networking
- Internet Connectivity
- DNS Configuration
- Network Isolation
- AWS Routing
- Enterprise Network Architecture
- Secure Cloud Infrastructure
- Production Networking Best Practices

---

# Conclusion

Amazon VPC is the foundation of this AWS Backup & Disaster Recovery project. It provides a secure, isolated, and scalable networking environment where all cloud resources operate. By creating a custom VPC with proper DNS configuration, internet connectivity, and routing, the infrastructure follows AWS networking best practices and closely resembles a real-world production environment.
