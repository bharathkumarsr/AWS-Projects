# 📍 AWS Backup Recovery Points

## Overview

A **Recovery Point** is a backup copy of a protected AWS resource created by AWS Backup. It contains all the information required to restore the resource to a previous state after accidental deletion, hardware failure, or disaster.

In this project, a Recovery Point was created after performing an **On-Demand Backup** of the **Backup-WebServer EC2 instance**. This Recovery Point was later used to restore the EC2 instance and validate the Disaster Recovery process.

---

# Purpose

Recovery Points were used to:

- Store a recoverable copy of the EC2 instance.
- Protect attached Amazon EBS volumes.
- Restore infrastructure after failure.
- Validate Disaster Recovery.
- Ensure Business Continuity.

---

# Why Recovery Points?

Recovery Points provide a reliable restore source for protected resources.

Benefits include:

- Point-in-Time Recovery
- Secure Backup Storage
- Fast Infrastructure Restoration
- Disaster Recovery Support
- Business Continuity
- Centralized Backup Management

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
                 Restore Job
                       │
                       │
            Restored EC2 Instance
```

---

# Configuration Used

| Property | Value |
|----------|-------|
| Protected Resource | Backup-WebServer |
| Resource Type | Amazon EC2 |
| Backup Type | Image |
| Backup Method | On-Demand Backup |
| Backup Vault | Backup-DR-Vault |
| Retention | 30 Days |
| Region | ap-south-1 |

---

# Recovery Point Information

The Recovery Point generated in this project contained:

- EC2 Instance Configuration
- Amazon Machine Image (AMI)
- Root EBS Snapshot
- Additional EBS Snapshot
- Instance Metadata
- Boot Configuration

Example Recovery Point ID:

```text
image/ami-xxxxxxxxxxxxxxxx
```

---

# How Recovery Points Work

```text
EC2 Instance

↓

AWS Backup

↓

Creates Recovery Point

↓

Stores in Backup Vault

↓

Available for Restore
```

Once the backup is completed successfully, the Recovery Point becomes available for future restore operations.

---

# What Does the Recovery Point Contain?

For an Amazon EC2 backup, the Recovery Point includes:

### EC2 Configuration

- Instance Type
- AMI Information
- Networking Configuration
- Boot Configuration

---

### Root EBS Volume

Contains:

- Amazon Linux Operating System
- Installed Packages
- Nginx
- Configuration Files

---

### Additional EBS Volume

Contains:

- Business Documents
- HR Files
- Finance Reports
- Logs
- Application Configuration

---

# Recovery Point Lifecycle

```text
Create Backup

↓

Recovery Point Created

↓

Stored in Backup Vault

↓

Available for Restore

↓

Retention Period Ends

↓

Recovery Point Deleted
```

---

# Retention Period

The Recovery Point was configured with:

```
30 Days
```

This means:

- The backup remains available for restoration for 30 days.
- After the retention period expires, AWS Backup automatically deletes the Recovery Point unless the policy is changed.

---

# Restore Process

The Recovery Point was successfully used to restore the infrastructure.

```text
Recovery Point

↓

Restore Job

↓

Creates New AMI

↓

Creates New Root EBS

↓

Creates New Data EBS

↓

Launches New EC2

↓

Application Available
```

---

# Validation Performed

After restoration, the following validations were completed:

- EC2 instance launched successfully.
- Root EBS volume restored.
- Additional EBS volume restored.
- Nginx web server started successfully.
- Business data was available.
- Website was accessible after assigning an Elastic IP.

This confirmed that the Recovery Point was valid and complete.

---

# Monitoring Recovery Points

Recovery Points can be monitored from the AWS Backup Console.

Information available includes:

- Recovery Point ID
- Backup Status
- Resource Name
- Resource Type
- Backup Type
- Creation Time
- Retention Period
- Backup Vault

---

# Benefits

Recovery Points provide:

- Reliable Restore Source
- Secure Backup Storage
- Fast Disaster Recovery
- Business Continuity
- Backup History
- Infrastructure Recovery

---

# Best Practices

- Regularly verify Recovery Points.
- Test restore operations periodically.
- Configure appropriate retention periods.
- Store Recovery Points in dedicated Backup Vaults.
- Monitor backup job status.
- Protect Backup Vaults using IAM and Backup Vault Lock where required.

---

# Project Implementation

As part of this project:

- Created an On-Demand Backup.
- Generated a Recovery Point.
- Stored the Recovery Point in **Backup-DR-Vault**.
- Configured a 30-day retention period.
- Restored the EC2 instance using the Recovery Point.
- Verified successful application recovery.

---

# Learning Outcomes

Through implementing Recovery Points, the following concepts were learned:

- Recovery Point Creation
- EC2 Backup
- Backup Validation
- Infrastructure Restore
- Disaster Recovery
- Backup Retention
- AWS Backup Monitoring
- Business Continuity

---

# Interview Questions

### Q1. What is a Recovery Point in AWS Backup?

A Recovery Point is a backup copy of a protected AWS resource stored in a Backup Vault. It contains the data and metadata required to restore the resource.

---

### Q2. What did your Recovery Point contain?

The Recovery Point contained:

- EC2 Instance Configuration
- Amazon Machine Image (AMI)
- Root EBS Snapshot
- Additional EBS Snapshot
- Instance Metadata

---

### Q3. Where is a Recovery Point stored?

Recovery Points are stored inside an AWS Backup Vault.

---

### Q4. How was the Recovery Point created?

The Recovery Point was created by performing an **On-Demand Backup** of the EC2 instance using AWS Backup.

---

### Q5. What happened when you restored the Recovery Point?

AWS Backup:

- Created a new AMI
- Created new EBS volumes from snapshots
- Launched a new EC2 instance
- Restored the operating system, application, and business data

---

### Q6. Can a Recovery Point be used multiple times?

Yes. A Recovery Point can be used multiple times during its retention period to restore one or more copies of the protected resource.

---

### Q7. What happens after the retention period expires?

When the configured retention period ends, AWS Backup automatically deletes the Recovery Point unless the retention policy is modified.

---

# Conclusion

Recovery Points are the core restore mechanism in AWS Backup. In this project, the Recovery Point captured the complete state of the **Backup-WebServer**, including its configuration and attached EBS volumes. By successfully restoring the EC2 instance from the Recovery Point and validating the application and business data, the project demonstrated an effective Disaster Recovery workflow and highlighted the importance of Recovery Points in ensuring business continuity.
