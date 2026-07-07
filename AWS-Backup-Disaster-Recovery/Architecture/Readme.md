# ☁️ AWS Backup & Disaster Recovery Project

> **Enterprise-Level AWS Backup & Disaster Recovery Implementation**
>
> Designed and implemented a production-inspired Backup & Disaster Recovery (DR) solution on AWS using Amazon EC2, EBS, Amazon S3, and AWS Backup. This project demonstrates how organizations protect workloads, automate backups, and recover infrastructure after failures.

---

# 📌 Project Overview

Business continuity is one of the most critical aspects of modern cloud infrastructure. Hardware failures, accidental deletions, ransomware attacks, and human errors can lead to data loss and service downtime.

This project demonstrates how to build a reliable Disaster Recovery solution using AWS native services.

The implementation includes:

- Custom AWS Networking
- Linux EC2 Server
- Persistent EBS Storage
- Amazon S3 Object Storage
- Automated AWS Backup
- Backup Vault
- Recovery Points
- Disaster Recovery Restore
- Business Data Recovery

The project follows industry best practices by separating operating system storage from business data and automating backups using AWS Backup.

---

# 🎯 Project Objectives

- Design a secure AWS infrastructure.
- Deploy an application server on Amazon EC2.
- Store business data on a separate EBS volume.
- Configure Amazon S3 for document storage.
- Enable Versioning and Encryption.
- Configure centralized backups using AWS Backup.
- Create automated backup policies.
- Generate Recovery Points.
- Restore infrastructure after disaster.
- Validate successful recovery.

---

# 🏗️ Solution Architecture

```
                          Internet
                              │
                     Internet Gateway
                              │
                 Backup-DR-VPC (10.0.0.0/16)
                              │
                 Public Subnet (10.0.1.0/24)
                              │
                    Backup-WebServer (EC2)
                              │
          ┌───────────────────┴───────────────────┐
          │                                       │
     Root EBS Volume                        Data EBS Volume
      (Amazon Linux)                      (/backup-data)
          │                                       │
          │                         HR
          │                         Finance
          │                         Logs
          │                         Config Files
          │
          └───────────────┐
                          │
                   Amazon S3 Bucket
                Versioning Enabled
                Server Side Encryption
                          │
                          ▼
                     AWS Backup
                          │
                  Backup Vault
                          │
                  Backup Plan
                          │
                  Daily Backup Rule
                          │
                  Recovery Point
                          │
                   Disaster Recovery
                          │
                 Restored EC2 Instance
```

---

# 🛠️ AWS Services Used

| Service | Purpose |
|----------|----------|
| Amazon VPC | Isolated cloud network |
| Public Subnet | Internet accessible subnet |
| Internet Gateway | Internet connectivity |
| Route Table | Routes internet traffic |
| Security Group | Virtual firewall |
| Amazon EC2 | Linux application server |
| Amazon EBS | Persistent block storage |
| Amazon S3 | Object storage |
| AWS Backup | Centralized backup management |
| Backup Vault | Stores recovery points |
| Backup Plan | Backup policy |
| Recovery Point | Backup image |
| Elastic IP | Public access after restore |

---

# 📚 Architecture Explanation

## 1. Amazon VPC

A custom Virtual Private Cloud (VPC) was created to isolate the infrastructure from other AWS environments.

### Configuration

- CIDR Block
```
10.0.0.0/16
```

### Purpose

- Secure network isolation
- Custom networking
- Better security
- Enterprise architecture

---

## 2. Public Subnet

A public subnet was created inside the VPC.

### Configuration

```
10.0.1.0/24
```

### Purpose

Hosts internet-facing resources like EC2.

---

## 3. Internet Gateway

Attached to the VPC to provide internet connectivity.

### Purpose

Allows

- SSH
- HTTP
- HTTPS

traffic.

---

## 4. Route Table

Configured with

```
0.0.0.0/0
↓
Internet Gateway
```

### Purpose

Allows outbound internet communication.

---

## 5. Security Group

Acts as a firewall.

### Inbound Rules

| Port | Purpose |
|-------|----------|
|22|SSH|
|80|HTTP|
|443|HTTPS|

### Outbound

Allow All

---

# 💻 Amazon EC2

Amazon Linux 2023 instance used as the application server.

### Configuration

Instance Type

```
t3.micro
```

Hosted

- Nginx Web Server
- Demo Website

### Purpose

Represents the production server.

---

# 💽 Amazon EBS

Two EBS volumes were used.

---

## Root Volume

Stores

- Operating System
- Installed Packages
- Nginx
- Application

---

## Additional Data Volume

20 GB

Mounted at

```
/backup-data
```

Contains

```
HR

Finance

Logs

Configuration
```

### Why Separate Volume?

Enterprise applications separate operating system from business data.

Benefits

- Easier backup
- Faster recovery
- Better scalability
- Independent restore

---

# 🗄️ File System

The new EBS volume was formatted using

```
XFS
```

Mounted permanently using

```
/etc/fstab
```

This ensures automatic mounting after reboot.

---

# ☁️ Amazon S3

Created an S3 bucket to simulate enterprise document storage.

### Stored

- HR Documents
- Finance Reports
- Configuration Files
- Logs

---

## Versioning

Enabled

Purpose

Recover previous versions if files are accidentally overwritten.

---

## Server Side Encryption

Enabled

AES-256

Purpose

Protect data at rest.

---

# 🔒 AWS Backup

AWS Backup provides centralized backup management.

Instead of manually creating snapshots, AWS Backup automates the entire process.

---

## Backup Vault

Created

```
Enterprise-Backup-Vault
```

Purpose

Stores all Recovery Points securely.

---

## Backup Plan

Created

```
Enterprise-Backup-Plan
```

Purpose

Defines

- Backup schedule
- Retention
- Lifecycle

---

## Backup Rule

Configured

Daily Backup

Retention

```
30 Days
```

Purpose

Automatically deletes backups after retention period.

---

## Resource Assignment

Protected resources

- EC2 Instance
- EBS Volumes

Purpose

Ensures infrastructure is backed up automatically.

---

# 📦 Recovery Point

After backup completion AWS Backup generated

```
Recovery Point
```

A Recovery Point is a restorable copy of infrastructure at a particular time.

---

# 🚨 Disaster Recovery

To validate the backup strategy,

the EC2 instance was restored from the Recovery Point.

AWS Backup performed

Recovery Point

↓

Created AMI

↓

Created new EBS Volumes

↓

Launched new EC2 Instance

↓

Application Restored

↓

Business Data Recovered

This successfully demonstrated Disaster Recovery.

---

# 🔄 Restore Validation

Validated

- EC2 launched successfully
- EBS volumes restored
- Business data available
- Nginx accessible
- Public access restored using Elastic IP

---

# 📁 Business Data Structure

```
/backup-data

├── HR
│     employees.csv
│
├── Finance
│     report.txt
│
├── Logs
│     application.log
│
└── Config
      application.conf
```

---

# 📸 Project Screenshots

```
screenshots/

01-vpc-created.png

02-public-subnet.png

03-route-table.png

04-security-group.png

05-ec2-running.png

06-nginx-homepage.png

07-ebs-volumes.png

08-mounted-volume.png

09-business-data.png

10-s3-bucket.png

11-s3-versioning.png

12-s3-files.png

13-backup-vault.png

14-backup-plan.png

15-resource-assignment.png

16-backup-job-completed.png

17-recovery-point.png

18-restore-job-completed.png

19-restored-ec2.png

20-restored-ebs.png
```

---

# 🔄 Project Workflow

```
Infrastructure Creation

↓

Deploy EC2

↓

Attach EBS

↓

Store Business Data

↓

Create S3 Bucket

↓

Enable Versioning

↓

Configure AWS Backup

↓

Create Backup Vault

↓

Create Backup Plan

↓

Backup EC2

↓

Recovery Point Created

↓

Restore EC2

↓

Validate Recovery
```

---

# 🌟 Key Features

- Custom VPC Architecture
- Public Networking
- Linux EC2 Deployment
- Separate Business Data Volume
- Persistent Storage
- Amazon S3 Versioning
- AES-256 Encryption
- Automated AWS Backup
- Backup Vault
- Daily Backup Policy
- Recovery Points
- EC2 Restore
- Business Continuity
- Disaster Recovery Testing

---

# 📖 Learning Outcomes

Through this project, I learned:

- AWS Networking Fundamentals
- EC2 Administration
- EBS Volume Management
- Linux File Systems (XFS)
- Persistent Mount Configuration
- Amazon S3 Versioning
- AWS Backup Architecture
- Recovery Point Management
- Backup Automation
- Disaster Recovery Planning
- Infrastructure Restoration
- Business Continuity Best Practices

---

# 🚀 Future Enhancements

- Cross-Region Backup
- Cross-Account Backup
- Backup Vault Lock
- Lifecycle transition to Cold Storage
- AWS Backup Audit Manager
- AWS Organizations Backup Policies
- Amazon SNS Backup Notifications
- AWS Lambda Backup Automation
- Terraform Infrastructure as Code
- CloudWatch Monitoring
- EventBridge Backup Alerts

---

# 🏆 Conclusion

This project demonstrates a complete enterprise-style AWS Backup & Disaster Recovery solution using native AWS services.

It showcases infrastructure deployment, storage management, centralized backup administration, disaster recovery validation, and business continuity planning. The implementation follows AWS best practices and reflects a practical workflow that cloud and DevOps engineers use to protect production workloads and ensure rapid recovery from failures.
