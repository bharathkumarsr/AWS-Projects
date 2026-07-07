# ✅ Restore Validation

## Overview

Restore Validation is the process of verifying that a restored infrastructure is fully functional after a backup recovery operation. A successful restore does not end when the EC2 instance is launched—it must be validated to ensure that the operating system, storage, applications, networking, and business data are working correctly.

In this project, Restore Validation was performed after restoring the **Backup-WebServer** from an **AWS Backup Recovery Point**. The restored environment was tested to confirm that it matched the original production environment.

---

# Objective

The objective of Restore Validation was to:

- Verify the EC2 instance launched successfully.
- Confirm EBS volumes were restored.
- Validate business data integrity.
- Verify network connectivity.
- Confirm the Nginx web application was accessible.
- Ensure the Disaster Recovery process was successful.

---

# Restore Validation Architecture

```text
           Recovery Point
                 │
                 │
           Restore Job
                 │
                 ▼
      Restored EC2 Instance
                 │
      ┌──────────┴──────────┐
      │                     │
 Root EBS Volume      Data EBS Volume
      │                     │
 Amazon Linux         Business Files
      │                     │
      └──────────┬──────────┘
                 │
          Nginx Web Server
                 │
          Elastic IP Address
                 │
           Browser Validation
```

---

# Validation Checklist

The following components were validated after the restore.

| Component | Status |
|-----------|--------|
| EC2 Instance Running | ✅ |
| Root EBS Volume Attached | ✅ |
| Data EBS Volume Attached | ✅ |
| Operating System Booted | ✅ |
| Business Data Restored | ✅ |
| Nginx Installed | ✅ |
| Nginx Service Running | ✅ |
| Website Accessible | ✅ |
| Elastic IP Associated | ✅ |
| SSH Access Working | ✅ |

---

# Step 1 – Verify EC2 Instance

Navigate to:

```
AWS Console

↓

EC2

↓

Instances
```

Verify:

- Instance State = Running
- Correct Instance Type
- Correct VPC
- Correct Subnet
- Security Group Attached

Expected Result:

```
Running
```

---

# Step 2 – Verify Root EBS Volume

Navigate to:

```
EC2

↓

Volumes
```

Verify:

- Root volume attached
- Status = In-use
- Correct Size (10 GB)

Expected:

```
Root Volume

↓

Attached

↓

In-use
```

---

# Step 3 – Verify Data Volume

Verify:

- Additional 20 GB volume attached
- Mounted correctly

Command:

```bash
lsblk
```

Expected Output:

```text
nvme0n1    10G

nvme1n1    20G
```

---

# Step 4 – Verify Mounted File Systems

Run:

```bash
df -h
```

Expected:

```text
Filesystem

/

backup-data
```

The `/backup-data` mount point should be available.

---

# Step 5 – Verify Business Data

Navigate to:

```bash
cd /backup-data
```

List files:

```bash
ls -l
```

Expected folders:

```text
HR

Finance

Logs

Config
```

All business files should be present.

---

# Step 6 – Verify Nginx Service

Check service status:

```bash
sudo systemctl status nginx
```

Expected:

```text
Active (running)
```

---

# Step 7 – Verify Website

Open browser:

```
http://Elastic-IP
```

Expected:

```
AWS Backup & Disaster Recovery

Website Successfully Restored
```

The application should load successfully.

---

# Step 8 – Verify Elastic IP

Navigate to:

```
EC2

↓

Elastic IP
```

Verify:

- Elastic IP allocated
- Associated with restored EC2

Purpose:

Provides a stable public IP after recovery.

---

# Step 9 – Verify SSH Connectivity

Connect:

```bash
ssh -i Backup-DR.pem ec2-user@Elastic-IP
```

Expected:

```
Connected Successfully
```

---

# Step 10 – Verify AWS Backup

Navigate to:

```
AWS Backup

↓

Restore Jobs
```

Verify:

```
Status

Completed
```

This confirms the restore operation completed successfully.

---

# Validation Workflow

```text
Recovery Point

↓

Restore Job

↓

New EC2

↓

Attach Root Volume

↓

Attach Data Volume

↓

Boot Linux

↓

Start Nginx

↓

Assign Elastic IP

↓

Validate Website

↓

Recovery Successful
```

---

# Validation Results

| Validation Item | Result |
|-----------------|--------|
| EC2 Running | ✅ Pass |
| Root Volume Restored | ✅ Pass |
| Data Volume Restored | ✅ Pass |
| Mount Points Available | ✅ Pass |
| Business Files Available | ✅ Pass |
| SSH Working | ✅ Pass |
| Nginx Running | ✅ Pass |
| Website Accessible | ✅ Pass |
| AWS Backup Restore Completed | ✅ Pass |

---

# Why Restore Validation is Important

Simply creating backups is **not enough**.

Organizations must verify that:

- Backups are usable.
- Applications start correctly.
- Data is intact.
- Users can access services.
- Business operations can resume.

Without validation, there is no guarantee that backups can actually be used during a real disaster.

---

# Best Practices

- Perform restore testing regularly.
- Verify both infrastructure and application functionality.
- Validate business data after every restore.
- Document the recovery process.
- Monitor restore jobs in AWS Backup.
- Test Disaster Recovery periodically.

---

# Project Implementation

During this project:

- Restored the EC2 instance from an AWS Backup Recovery Point.
- Verified the restored EC2 instance was running.
- Confirmed the root and data EBS volumes were attached.
- Validated the `/backup-data` mount point.
- Verified business files were intact.
- Checked that the Nginx service was active.
- Associated an Elastic IP with the restored instance.
- Confirmed website accessibility.
- Verified successful SSH connectivity.
- Completed the Disaster Recovery validation successfully.

---

# Learning Outcomes

This validation process provided practical experience with:

- EC2 Recovery Validation
- EBS Volume Verification
- Linux Storage Validation
- Nginx Service Validation
- Elastic IP Association
- AWS Backup Restore Jobs
- Disaster Recovery Testing
- Business Continuity Verification

---

# Interview Questions

### Q1. What is Restore Validation?

Restore Validation is the process of verifying that a restored system is fully operational after recovering it from a backup.

---

### Q2. What did you validate after restoring your EC2 instance?

I validated:

- EC2 instance status
- Root and data EBS volumes
- File system mounts
- Business data
- Nginx service
- Website accessibility
- Elastic IP association
- SSH connectivity
- AWS Backup restore status

---

### Q3. Why is Restore Validation important?

It confirms that backups are reliable and that applications, infrastructure, and business data can be successfully recovered during a disaster.

---

### Q4. How did you verify the EBS volumes?

Using:

```bash
lsblk

df -h
```

These commands confirmed the restored volumes were attached and mounted correctly.

---

### Q5. How did you verify the application?

I checked that the Nginx service was running using `systemctl status nginx` and accessed the application through the Elastic IP in a web browser.

---

### Q6. What was the final outcome of your validation?

The restored infrastructure functioned exactly as expected. The EC2 instance, EBS volumes, Nginx web server, and business data were successfully recovered, confirming that the Disaster Recovery process was successful.

---

# Conclusion

Restore Validation was the final and most critical phase of this AWS Backup & Disaster Recovery project. It confirmed that the restored EC2 instance, attached EBS volumes, operating system, application, and business data were fully operational. By validating infrastructure, networking, storage, and application functionality, the project demonstrated a complete end-to-end disaster recovery workflow aligned with enterprise best practices for business continuity and operational resilience.
