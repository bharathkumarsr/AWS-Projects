# 🏦 AWS Backup Vault

## Overview

An **AWS Backup Vault** is a secure logical container used to store **Recovery Points** created by AWS Backup. It acts as a centralized repository where backups are securely stored until they are restored or expire based on the configured retention period.

In this project, a dedicated Backup Vault was created to securely store the backup of the **Backup-WebServer EC2 instance** and its attached Amazon EBS volumes.

---

# Purpose

The Backup Vault was used to:

- Store Recovery Points securely.
- Centralize backup storage.
- Organize backups.
- Support Disaster Recovery.
- Manage backup retention.
- Enable resource restoration.

---

# Why Backup Vault?

AWS Backup Vault provides:

- Centralized Backup Storage
- Secure Recovery Point Management
- Backup Organization
- Retention Management
- Backup Encryption
- Restore Management
- Backup Monitoring
- Disaster Recovery Support

---

# Architecture

```text
             Backup-WebServer (EC2)
                      │
                      │
                AWS Backup
                      │
                      │
             Backup-DR-Vault
                      │
                      │
             Recovery Point
                      │
                      │
           Restore EC2 Instance
```

---

# Configuration Used

| Property | Value |
|----------|-------|
| Backup Vault Name | Backup-DR-Vault |
| Region | ap-south-1 |
| Encryption | AWS Managed Key (Default) |
| Recovery Points | EC2 Recovery Point |
| Retention | 30 Days |

---

# How Backup Vault Works

The backup workflow is:

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
```

Instead of storing backups directly on the EC2 instance, AWS Backup stores them securely inside the Backup Vault.

---

# What is Stored in the Backup Vault?

The Backup Vault stores:

- Recovery Points
- Backup Metadata
- Backup History
- Backup Status
- Backup Information

For this project, the Recovery Point contained:

- EC2 Configuration
- Root EBS Snapshot
- Data EBS Snapshot
- AMI Metadata

---

# Recovery Point

After the backup completed successfully, AWS Backup generated a Recovery Point.

Example:

```text
image/ami-xxxxxxxxxxxxxxxx
```

This Recovery Point was stored inside:

```
Backup-DR-Vault
```

It was later used to restore the EC2 instance.

---

# Restore Workflow

```text
Recovery Point

↓

Backup Vault

↓

Restore Job

↓

Creates New AMI

↓

Creates New EBS Volumes

↓

Launches New EC2 Instance
```

The Backup Vault acts as the source for all restore operations.

---

# Monitoring

The Backup Vault allows administrators to monitor:

- Recovery Points
- Backup Jobs
- Restore Jobs
- Backup Status
- Retention Information

This provides complete visibility into backup operations.

---

# Backup Retention

The Recovery Point in this project was configured with:

```
30 Days
```

This means:

- The backup remains available for 30 days.
- It can be restored at any time during this period.
- After 30 days, AWS Backup automatically deletes the Recovery Point unless retention is modified.

---

# Security

AWS Backup Vault supports multiple security features:

- Encryption at Rest
- IAM Access Control
- Backup Vault Access Policies
- Backup Vault Lock (Optional)
- Cross-Account Backup Support

In this project, the Backup Vault used the default AWS-managed encryption.

---

# Backup Vault Lock

AWS Backup also supports **Backup Vault Lock**, which protects backups from being modified or deleted before the retention period expires.

Benefits include:

- Protection against accidental deletion
- Protection from ransomware attacks
- Compliance with regulatory requirements
- Immutable backups

Although Backup Vault Lock was not configured in this project, it is commonly implemented in production environments.

---

# Benefits

Using a Backup Vault provides:

- Secure Backup Storage
- Centralized Recovery Management
- Backup Organization
- Easy Restore Operations
- Retention Management
- Disaster Recovery Readiness

---

# Project Implementation

As part of this project:

- Created **Backup-DR-Vault**
- Stored the EC2 backup inside the vault
- Generated a Recovery Point
- Configured a 30-day retention period
- Used the Recovery Point to restore the EC2 instance
- Verified successful Disaster Recovery

---

# Learning Outcomes

Through implementing the Backup Vault, the following concepts were learned:

- Backup Vault
- Recovery Point Storage
- Backup Retention
- Backup Monitoring
- Restore Operations
- Backup Security
- Disaster Recovery
- Business Continuity

---

# Interview Questions

### Q1. What is an AWS Backup Vault?

An AWS Backup Vault is a secure storage container that holds Recovery Points created by AWS Backup for protected AWS resources.

---

### Q2. Why was a Backup Vault used in this project?

The Backup Vault securely stored the Recovery Point for the EC2 instance, allowing it to be restored during the Disaster Recovery process.

---

### Q3. What is stored inside a Backup Vault?

A Backup Vault stores:

- Recovery Points
- Backup Metadata
- Backup History
- Backup Status

For EC2 backups, it also stores references to the AMI and EBS snapshots required for restoration.

---

### Q4. Can a Recovery Point exist without a Backup Vault?

No. Every Recovery Point created by AWS Backup must be stored in a Backup Vault.

---

### Q5. What is Backup Vault Lock?

Backup Vault Lock is a feature that prevents backups from being modified or deleted before the configured retention period expires. It helps protect against accidental deletion and ransomware attacks.

---

### Q6. Can multiple backups be stored in the same Backup Vault?

Yes. A single Backup Vault can contain Recovery Points from multiple AWS resources, such as EC2 instances, EBS volumes, RDS databases, and EFS file systems.

---

### Q7. Is a Backup Vault the same as Amazon S3?

No.

| Backup Vault | Amazon S3 |
|--------------|-----------|
| Stores AWS Backup Recovery Points | Stores user-uploaded objects and files |
| Managed by AWS Backup | General-purpose object storage |
| Used for backup and restore operations | Used for application data, media, logs, and documents |

---

# Conclusion

The **Backup-DR-Vault** served as the secure repository for all Recovery Points generated during this project. By storing the EC2 backup and its associated metadata in a centralized vault, AWS Backup enabled reliable recovery of the infrastructure during the Disaster Recovery exercise. The Backup Vault also provided retention management, monitoring, and secure storage, making it an essential component of an enterprise backup strategy.
