# 🚨 Disaster Recovery (DR)

## Overview

Disaster Recovery (DR) is the process of restoring IT infrastructure, applications, and business data after an unexpected event such as hardware failure, accidental deletion, cyberattacks, or natural disasters. The primary goal of Disaster Recovery is to minimize downtime and ensure business continuity.

In this project, Disaster Recovery was demonstrated by restoring an Amazon EC2 instance and its attached Amazon EBS volumes using **AWS Backup Recovery Points**. After restoration, the application and business data were verified to ensure the environment was fully operational.

---

# Project Objective

The objective of this project was to:

- Protect an EC2 instance using AWS Backup.
- Simulate infrastructure failure.
- Restore the infrastructure from a Recovery Point.
- Verify application availability.
- Validate business continuity.

---

# Disaster Recovery Architecture

```text
                  Production Environment

                  Backup-WebServer (EC2)
                          │
        ┌─────────────────┴─────────────────┐
        │                                   │
   Root EBS Volume                    Data EBS Volume
        │                                   │
        └─────────────────┬─────────────────┘
                          │
                     AWS Backup
                          │
                   Backup-DR-Vault
                          │
                   Recovery Point
                          │
                    Restore Process
                          │
          ┌───────────────┴────────────────┐
          │                                │
   New Root EBS Volume              New Data EBS Volume
          │                                │
          └───────────────┬────────────────┘
                          │
             Restored Backup-WebServer
                          │
                  Assign Elastic IP
                          │
                 Verify Nginx Website
```

---

# Disaster Scenario

Assume the production EC2 instance becomes unavailable due to:

- Accidental instance deletion
- Operating system corruption
- EBS volume failure
- Human error
- Malware or ransomware attack
- Hardware failure
- AWS Availability Zone issues

Without backups, recovering the application and business data would be extremely difficult.

---

# Disaster Recovery Workflow

```text
Production EC2

↓

AWS Backup

↓

Recovery Point Created

↓

Infrastructure Failure

↓

Restore Recovery Point

↓

Launch New EC2 Instance

↓

Attach Restored EBS Volumes

↓

Assign Elastic IP

↓

Verify Application

↓

Business Restored
```

---

# AWS Services Used

| AWS Service | Purpose |
|-------------|---------|
| Amazon VPC | Network isolation |
| Public Subnet | Hosts EC2 instance |
| Internet Gateway | Internet connectivity |
| Route Table | Traffic routing |
| Security Group | Firewall rules |
| Amazon EC2 | Application server |
| Amazon EBS | Persistent block storage |
| Amazon S3 | Business document storage |
| AWS Backup | Backup management |
| Backup Vault | Stores Recovery Points |
| Recovery Point | Restore source |
| Elastic IP | Restore public access after recovery |

---

# Disaster Recovery Steps Performed

## Step 1 – Created Infrastructure

Configured:

- Custom VPC
- Public Subnet
- Internet Gateway
- Route Table
- Security Group
- EC2 Instance
- Additional 20 GB EBS Volume

---

## Step 2 – Configured Application

Installed:

- Amazon Linux 2023
- Nginx Web Server

Created business data under:

```text
/backup-data
```

---

## Step 3 – Protected Infrastructure

Using AWS Backup:

- Selected EC2 instance
- Created On-Demand Backup
- Stored backup in **Backup-DR-Vault**
- Generated Recovery Point

---

## Step 4 – Simulated Recovery

Instead of waiting for an actual disaster, the Recovery Point was restored.

AWS Backup automatically:

- Created a new AMI
- Created new EBS volumes
- Launched a new EC2 instance

---

## Step 5 – Assigned Elastic IP

The restored EC2 instance received a new public IP by default.

To maintain application accessibility:

- An Elastic IP was allocated.
- The Elastic IP was associated with the restored EC2 instance.

This provided a consistent public endpoint for accessing the application.

---

## Step 6 – Validation

After restoration, the following checks were performed:

- EC2 instance running
- Root volume restored
- Data volume restored
- `/backup-data` available
- Nginx service running
- Website accessible via browser
- Business data intact

All validations completed successfully.

---

# Recovery Components

The Recovery Point restored:

### Compute

- Amazon EC2 Instance
- Instance Configuration

### Storage

- Root EBS Volume
- Additional EBS Volume

### Operating System

- Amazon Linux 2023

### Application

- Nginx Web Server

### Business Data

- HR Files
- Finance Reports
- Configuration Files
- Application Logs

---

# Recovery Time Objective (RTO)

**Recovery Time Objective (RTO)** defines the maximum acceptable time to restore services after a disaster.

For this demonstration:

- Restore completed within a few minutes.
- Application became available after assigning an Elastic IP and verifying services.

In production, the target RTO depends on business requirements and the criticality of the workload.

---

# Recovery Point Objective (RPO)

**Recovery Point Objective (RPO)** defines the maximum acceptable amount of data loss.

In this project:

- The restored data reflected the state of the EC2 instance at the time the On-Demand Backup was created.
- Any changes made after the backup would not be included in the restored environment.

---

# Benefits of Disaster Recovery

Implementing Disaster Recovery provides:

- Reduced downtime
- Business continuity
- Protection against data loss
- Faster infrastructure restoration
- Improved operational resilience
- Simplified recovery procedures
- Compliance with organizational policies

---

# Best Practices

- Automate backups using AWS Backup Plans.
- Test Disaster Recovery regularly.
- Enable Backup Vault Lock for immutable backups.
- Encrypt backups and EBS volumes.
- Monitor backup and restore jobs.
- Use multiple Availability Zones where applicable.
- Document recovery procedures.

---

# Project Implementation Summary

As part of this project:

- Built a custom AWS network.
- Deployed an EC2 web server.
- Attached an additional EBS volume.
- Installed and configured Nginx.
- Created business data.
- Performed an On-Demand Backup using AWS Backup.
- Generated a Recovery Point.
- Restored the EC2 instance.
- Restored the EBS volumes.
- Assigned an Elastic IP.
- Verified application functionality.
- Successfully completed Disaster Recovery validation.

---

# Learning Outcomes

Through this Disaster Recovery project, the following concepts were learned:

- Disaster Recovery Planning
- Business Continuity
- AWS Backup
- Recovery Points
- Backup Vaults
- EC2 Recovery
- EBS Restoration
- Infrastructure Recovery
- Elastic IP Management
- Application Validation

---

# Interview Questions

### Q1. What is Disaster Recovery?

Disaster Recovery (DR) is the process of restoring infrastructure, applications, and data after a failure or disaster to minimize downtime and maintain business continuity.

---

### Q2. How did you implement Disaster Recovery in this project?

I protected an EC2 instance using AWS Backup, created an On-Demand Backup, generated a Recovery Point, restored the instance from the Recovery Point, assigned an Elastic IP, and verified that the application and business data were successfully recovered.

---

### Q3. What resources were restored?

The restore process recreated:

- EC2 Instance
- Root EBS Volume
- Additional EBS Volume
- Operating System
- Nginx Web Server
- Business Data

---

### Q4. Why was an Elastic IP assigned after the restore?

The restored EC2 instance received a new public IP address. Assigning an Elastic IP provided a stable public IP, allowing users to access the application without changing the endpoint.

---

### Q5. What is the difference between RTO and RPO?

| RTO | RPO |
|-----|-----|
| Maximum acceptable downtime | Maximum acceptable data loss |
| Focuses on service restoration time | Focuses on data recovery point |

---

### Q6. How did you verify that the Disaster Recovery process was successful?

I verified that:

- The restored EC2 instance was running.
- The EBS volumes were attached.
- The `/backup-data` directory contained the expected files.
- Nginx was running successfully.
- The website was accessible through the Elastic IP.

---

# Conclusion

This project demonstrates a complete **AWS Backup and Disaster Recovery** workflow by protecting an EC2 instance, creating a Recovery Point, restoring the infrastructure, and validating application functionality. Using AWS Backup, Backup Vaults, Recovery Points, Amazon EC2, Amazon EBS, and Elastic IP, the project showcases a practical disaster recovery strategy that aligns with enterprise best practices for business continuity and cloud resilience.
