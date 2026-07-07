# 💻 Amazon EC2 (Elastic Compute Cloud)

## Overview

Amazon Elastic Compute Cloud (Amazon EC2) is a web service that provides secure, resizable virtual servers in the cloud. It allows users to launch Linux or Windows instances on demand without investing in physical hardware.

In this project, Amazon EC2 was used to host the application server that was later protected using **AWS Backup** and restored as part of the Disaster Recovery process.

---

# Purpose

Amazon EC2 was used to:

- Host the web application.
- Simulate a production application server.
- Store business data on an attached EBS volume.
- Demonstrate AWS Backup and Disaster Recovery.
- Validate infrastructure restoration after failure.

The EC2 instance acts as the primary workload that is protected throughout this project.

---

# Configuration Used

| Property | Value |
|----------|-------|
| Instance Name | Backup-WebServer |
| Operating System | Amazon Linux 2023 |
| Instance Type | t3.micro |
| Architecture | x86_64 |
| Virtualization | HVM |
| VPC | Backup-DR-VPC |
| Subnet | Public-Subnet-1 |
| Security Group | Backup-DR-SG |
| Key Pair | Backup-DR.pem |
| Root Volume | 10 GB (gp3) |
| Additional Volume | 20 GB (gp3) |

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
              Backup-WebServer (EC2)
                        │
          ┌─────────────┴─────────────┐
          │                           │
     Root EBS Volume          Data EBS Volume
       10 GB (gp3)             20 GB (gp3)
```

---

# Operating System

The instance was launched using:

```
Amazon Linux 2023
```

### Why Amazon Linux?

Amazon Linux is an AWS-optimized Linux distribution that provides:

- Better AWS integration
- Regular security updates
- High performance
- Long-term support
- Native AWS CLI support

---

# Instance Type

The following instance type was selected:

```
t3.micro
```

Specifications:

- 2 vCPUs
- 1 GB RAM
- Burstable Performance
- General Purpose

### Why t3.micro?

It is suitable for:

- Development
- Testing
- Small web applications
- Learning environments
- AWS Free Tier eligible (varies by account)

---

# Storage Configuration

## Root Volume

The root EBS volume stores:

- Operating System
- Installed Packages
- Nginx
- Configuration Files
- System Logs

Configuration:

```
10 GB
gp3
```

---

## Additional EBS Volume

A second EBS volume was attached.

Configuration:

```
20 GB
gp3
```

Mounted at:

```
/backup-data
```

Used to store:

- HR Files
- Finance Reports
- Application Logs
- Configuration Files

Separating business data from the operating system follows enterprise storage best practices.

---

# Web Server

Nginx was installed on the EC2 instance.

Installation:

```bash
sudo dnf install nginx -y
```

Service Management:

```bash
sudo systemctl enable nginx
sudo systemctl start nginx
```

Verification:

```bash
systemctl status nginx
```

Purpose:

- Host a demo website
- Validate application availability
- Test Disaster Recovery after restore

---

# Business Data

Sample business data was created under:

```
/backup-data
```

Example:

```text
/backup-data

├── HR
├── Finance
├── Logs
└── Config
```

This simulated enterprise application data stored separately from the operating system.

---

# Network Configuration

The EC2 instance was deployed in:

| Component | Value |
|----------|-------|
| VPC | Backup-DR-VPC |
| Subnet | Public-Subnet-1 |
| Internet Access | Enabled |
| Public IP | Assigned |
| Security Group | Backup-DR-SG |

This allowed:

- SSH access
- HTTP access
- AWS service communication

---

# SSH Access

The EC2 instance was accessed securely using a Key Pair.

Connection:

```bash
ssh -i Backup-DR.pem ec2-user@<Public-IP>
```

Purpose:

- Linux administration
- Package installation
- File management
- Backup validation
- Restore verification

---

# Role in AWS Backup

The EC2 instance was the primary resource protected by AWS Backup.

Workflow:

```text
EC2 Instance

↓

AWS Backup

↓

Backup Vault

↓

Recovery Point

↓

Restore

↓

New EC2 Instance
```

AWS Backup created an EC2 recovery point, which was later restored to launch a new EC2 instance.

---

# Disaster Recovery Validation

After creating the backup:

- Recovery Point was generated.
- Restore operation was initiated.
- A new EC2 instance was created.
- Root and data volumes were restored.
- Nginx application was verified.
- Business data was successfully recovered.

This confirmed that the backup strategy worked as expected.

---

# Best Practices Followed

- Used Amazon Linux 2023.
- Used gp3 EBS volumes.
- Separated OS and application data.
- Restricted access using Security Groups.
- Used SSH Key Pair authentication.
- Protected the instance using AWS Backup.
- Verified successful recovery after restore.

---

# Project Implementation

As part of this project:

- Launched an Amazon EC2 instance.
- Configured networking within a custom VPC.
- Attached a 20 GB EBS data volume.
- Installed and configured Nginx.
- Created sample business data.
- Configured AWS Backup protection.
- Performed an on-demand backup.
- Restored the EC2 instance from the Recovery Point.
- Validated successful Disaster Recovery.

---

# Learning Outcomes

Through implementing Amazon EC2, the following concepts were learned:

- EC2 Instance Deployment
- Amazon Linux Administration
- SSH Connectivity
- Web Server Deployment
- EBS Integration
- Linux Storage Management
- AWS Backup Integration
- Disaster Recovery Validation
- Infrastructure Restoration

---

# Interview Questions

### Q1. What is Amazon EC2?

Amazon EC2 is a cloud computing service that provides resizable virtual servers for hosting applications and workloads.

---

### Q2. Why did you use EC2 in this project?

EC2 was used as the primary application server to demonstrate AWS Backup, Recovery Points, and Disaster Recovery.

---

### Q3. Why was Amazon Linux 2023 selected?

Amazon Linux 2023 provides AWS optimization, security updates, long-term support, and seamless integration with AWS services.

---

### Q4. Why was a separate EBS volume attached?

Separating business data from the operating system simplifies backup, improves data management, and allows independent recovery of application data.

---

### Q5. What happened during the restore process?

AWS Backup created a new EC2 instance using the Recovery Point. New EBS volumes were created from snapshots, the operating system and application were restored, and the business data became available again.

---

### Q6. How did you verify that the restore was successful?

The restored EC2 instance was launched successfully, the attached EBS volumes were available, the Nginx web application was accessible, and the business data stored in `/backup-data` was intact.

---

# Conclusion

Amazon EC2 served as the core compute resource for this AWS Backup & Disaster Recovery project. It hosted the web application, stored business data on attached EBS volumes, and acted as the primary workload protected by AWS Backup. By successfully restoring the EC2 instance from a Recovery Point and validating application functionality, the project demonstrated a complete backup and disaster recovery workflow aligned with enterprise cloud operations and AWS best practices.
