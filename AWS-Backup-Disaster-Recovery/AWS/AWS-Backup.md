# 🔄 AWS Backup

## Overview

AWS Backup is a fully managed backup service that centralizes and automates data protection across AWS services. It enables organizations to create, manage, monitor, and restore backups from a single console without developing custom backup scripts.

In this project, AWS Backup was used to protect the **Backup-WebServer EC2 instance**, including its attached Amazon EBS volumes. A backup was created manually, stored in a Backup Vault, and later restored to validate the Disaster Recovery process.

---

# Purpose

AWS Backup was used to:

- Protect the EC2 instance.
- Backup attached EBS volumes.
- Generate Recovery Points.
- Store backups securely in a Backup Vault.
- Restore infrastructure during Disaster Recovery.
- Validate business continuity.

---

# Why AWS Backup?

AWS Backup provides centralized backup management for multiple AWS services.

Key benefits include:

- Fully Managed Backup Service
- Centralized Backup Management
- Automated Backup Scheduling
- Backup Monitoring
- Secure Recovery Points
- Point-in-Time Restore
- Backup Retention Policies
- Disaster Recovery Support

---

# Architecture

```text
              Backup-WebServer (EC2)
                       │
         ┌─────────────┴─────────────┐
         │                           │
   Root EBS Volume            Data EBS Volume
         │                           │
         └─────────────┬─────────────┘
                       │
                 AWS Backup
                       │
                 Backup Vault
                       │
                Recovery Point
                       │
                 Restore Process
                       │
             Restored EC2 Instance
```

---

# AWS Resources Protected

The following resources were protected:

| Resource | Purpose |
|----------|----------|
| Amazon EC2 | Compute Instance |
| Root EBS Volume | Operating System |
| Data EBS Volume | Business Data |

AWS Backup automatically included the attached EBS volumes while backing up the EC2 instance.

---

# Configuration Used

| Property | Value |
|----------|-------|
| Backup Type | On-Demand Backup |
| Protected Resource | Backup-WebServer |
| Resource Type | Amazon EC2 |
| Backup Vault | Backup-DR-Vault |
| Retention Period | 30 Days |
| Region | ap-south-1 |

---

# Backup Workflow

The backup process followed these steps:

```text
EC2 Instance

↓

AWS Backup

↓

Creates EBS Snapshots

↓

Stores Metadata

↓

Creates Recovery Point

↓

Stores in Backup Vault
```

AWS Backup captures:

- EC2 configuration
- Root EBS Volume
- Attached EBS Volumes
- Instance metadata
- Boot configuration

---

# Backup Vault

The backup was stored inside:

```
Backup-DR-Vault
```

The Backup Vault acts as a secure repository for Recovery Points.

It stores:

- Recovery Points
- Backup Metadata
- Backup History

---

# Recovery Point

After the backup completed successfully, AWS Backup created a Recovery Point.

Example:

```
image/ami-xxxxxxxxxxxxxxxx
```

The Recovery Point contains:

- EC2 Image (AMI)
- Root Volume Snapshot
- Data Volume Snapshot
- Instance Configuration

This Recovery Point is used to restore the workload.

---

# Disaster Recovery Process

The Recovery Point was restored using AWS Backup.

Restore workflow:

```text
Recovery Point

↓

Restore Job

↓

Creates New AMI

↓

Creates New EBS Volumes

↓

Launches New EC2 Instance

↓

Application Restored
```

---

# Validation Performed

After restoration, the following validations were completed:

- EC2 instance launched successfully.
- Root EBS volume restored.
- Data EBS volume restored.
- Nginx service was available.
- Business data remained intact.
- Application was accessible after assigning an Elastic IP.

This confirmed a successful Disaster Recovery.

---

# Backup Monitoring

AWS Backup provides monitoring through:

- Backup Jobs
- Restore Jobs
- Protected Resources
- Recovery Points

In this project, backup and restore jobs were monitored from the AWS Backup console.

---

# Benefits

Using AWS Backup provides:

- Centralized backup management
- Reduced operational effort
- Consistent backup policies
- Faster recovery
- Improved business continuity
- Simplified disaster recovery
- Native integration with AWS services

---

# Best Practices

- Use Backup Plans for automated backups.
- Store backups in dedicated Backup Vaults.
- Regularly test restore procedures.
- Monitor backup and restore jobs.
- Configure appropriate retention periods.
- Enable encryption for sensitive workloads.
- Apply least-privilege IAM permissions.

---

# Project Implementation

As part of this project:

- Created an AWS Backup Vault.
- Selected the EC2 instance as the protected resource.
- Performed an On-Demand Backup.
- Generated a Recovery Point.
- Verified successful backup completion.
- Restored the Recovery Point.
- Launched a new EC2 instance.
- Verified restored EBS volumes.
- Confirmed application functionality.

---

# Learning Outcomes

Through implementing AWS Backup, the following concepts were learned:

- AWS Backup Service
- Protected Resources
- Backup Vaults
- Recovery Points
- Backup Jobs
- Restore Jobs
- EC2 Backup
- EBS Snapshot Integration
- Disaster Recovery
- Business Continuity Planning

---

# Interview Questions

### Q1. What is AWS Backup?

AWS Backup is a fully managed service that centralizes and automates backups for supported AWS resources, enabling secure backup storage and simplified recovery.

---

### Q2. Why was AWS Backup used in this project?

AWS Backup was used to protect the EC2 instance and its attached EBS volumes, generate Recovery Points, and demonstrate a complete Disaster Recovery workflow.

---

### Q3. What resources were backed up?

The backup included:

- Amazon EC2 Instance
- Root EBS Volume
- Additional EBS Data Volume

---

### Q4. What is a Recovery Point?

A Recovery Point is a backup copy stored in a Backup Vault that contains all the information required to restore a protected resource to a previous state.

---

### Q5. Does AWS Backup create snapshots?

Yes. For Amazon EC2, AWS Backup creates Amazon EBS snapshots and stores metadata required to restore the instance.

---

### Q6. What happened during the restore process?

AWS Backup created:

- A new Amazon Machine Image (AMI)
- New EBS volumes from snapshots
- A new EC2 instance using the restored configuration

The restored instance was then verified by checking the application and business data.

---

### Q7. What is the difference between AWS Backup and manual EBS snapshots?

| AWS Backup | Manual EBS Snapshot |
|-------------|---------------------|
| Centralized management | Individual snapshot management |
| Supports backup policies | Manual process |
| Creates Recovery Points | Creates only volume snapshots |
| Supports restore workflows | Volume restore only |
| Tracks backup and restore jobs | No centralized monitoring |

---

# Conclusion

AWS Backup served as the core data protection service in this project by safeguarding the EC2 instance and its attached EBS volumes. The service created Recovery Points stored in a Backup Vault, enabling a successful restore of the infrastructure during the Disaster Recovery exercise. This implementation demonstrates how AWS Backup simplifies backup management, improves business continuity, and provides a reliable recovery mechanism for production workloads.
