# 💾 Amazon Elastic Block Store (Amazon EBS)

## Overview

Amazon Elastic Block Store (Amazon EBS) is a high-performance block storage service designed for use with Amazon EC2 instances. EBS provides persistent storage, meaning data remains available even if an EC2 instance is stopped or restarted.

In this project, Amazon EBS was used to store both the operating system and business data. The EBS volumes were protected using AWS Backup and successfully restored during the Disaster Recovery process.

---

# Purpose

Amazon EBS was used to:

- Store the Amazon Linux operating system.
- Store the Nginx web application.
- Store business-critical data separately from the operating system.
- Provide persistent storage for EC2.
- Demonstrate backup and disaster recovery using AWS Backup.

---

# Why Amazon EBS?

Amazon EBS provides durable and reliable block storage for EC2 instances.

Key advantages include:

- Persistent Storage
- Low Latency
- High Performance
- Point-in-Time Snapshots
- Easy Volume Expansion
- Integration with AWS Backup
- Supports Encryption
- Independent Lifecycle from EC2

---

# Architecture

```text
                  Backup-WebServer (EC2)
                           │
          ┌────────────────┴────────────────┐
          │                                 │
     Root EBS Volume                  Data EBS Volume
        10 GB (gp3)                     20 GB (gp3)
          │                                 │
    Operating System                 Business Data
    Amazon Linux                     HR Files
    Nginx                            Finance Reports
    Configuration                    Logs
```

---

# Configuration Used

## Root Volume

| Property | Value |
|----------|-------|
| Volume Type | gp3 |
| Size | 10 GB |
| Device Name | /dev/xvda |
| Purpose | Operating System |

The root volume contains:

- Amazon Linux 2023
- Nginx Web Server
- System Configuration
- Installed Packages
- Boot Files
- Application Files

---

## Additional Data Volume

| Property | Value |
|----------|-------|
| Volume Name | Backup-Data-Volume |
| Volume Type | gp3 |
| Size | 20 GB |
| Device Name | /dev/sdf |
| Mount Point | /backup-data |

Purpose:

- Store business files
- Separate application data from the operating system
- Demonstrate persistent storage
- Backup important business information

---

# File System

The additional EBS volume was formatted using the XFS file system.

Command:

```bash
sudo mkfs.xfs /dev/nvme1n1
```

---

# Mounting the Volume

A mount point was created.

```bash
sudo mkdir /backup-data
```

Mounted using

```bash
sudo mount /dev/nvme1n1 /backup-data
```

Verification

```bash
df -h
```

---

# Persistent Mount

To ensure the volume automatically mounts after every reboot, the UUID of the volume was added to:

```
/etc/fstab
```

UUID obtained using:

```bash
sudo blkid
```

Configuration example:

```text
UUID=<Volume-UUID>   /backup-data   xfs   defaults,nofail   0   2
```

Verification:

```bash
sudo mount -a
```

This ensures business data remains available after instance restarts.

---

# Business Data Structure

The additional EBS volume stored sample business data.

```text
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

This structure simulates enterprise application data.

---

# Volume Verification

The attached volumes were verified using:

```bash
lsblk
```

Example:

```text
nvme0n1   10G   Root Volume

nvme1n1   20G   Data Volume
```

Mounted file systems verified using:

```bash
df -h
```

---

# Why Separate Business Data?

Instead of storing everything on the root volume, a dedicated EBS volume was attached.

Benefits include:

- Independent storage management
- Easier backup
- Faster disaster recovery
- Better scalability
- Simplified storage expansion
- Reduced risk of data loss during OS maintenance

This follows enterprise storage best practices.

---

# Integration with AWS Backup

The EC2 instance, along with its attached EBS volumes, was protected using AWS Backup.

Backup workflow:

```text
Amazon EC2

↓

Root EBS Volume

↓

Data EBS Volume

↓

AWS Backup

↓

Recovery Point

↓

Restore

↓

New EBS Volumes

↓

New EC2 Instance
```

AWS Backup automatically created snapshots of the EBS volumes as part of the EC2 backup process.

---

# Disaster Recovery

During the restore process:

- AWS Backup created new EBS volumes from snapshots.
- Attached the restored volumes to the new EC2 instance.
- Restored both the operating system and business data.
- Verified successful recovery.

After restoration:

```text
Original Root Volume

↓

Snapshot

↓

Restored Root Volume

↓

New EC2 Instance
```

and

```text
Original Data Volume

↓

Snapshot

↓

Restored Data Volume

↓

Business Data Available
```

---

# Volume Type (gp3)

The project used **General Purpose SSD (gp3)** volumes.

Advantages:

- High performance
- Low latency
- Independent IOPS configuration
- Cost-effective
- Suitable for production workloads

---

# Best Practices Followed

- Used separate EBS volumes for OS and business data.
- Used gp3 SSD volumes.
- Used XFS file system.
- Configured persistent mounting using `/etc/fstab`.
- Verified storage before backup.
- Included EBS volumes in Disaster Recovery testing.

---

# Project Implementation

As part of this project:

- Created a 20 GB EBS volume.
- Attached the volume to the EC2 instance.
- Formatted it using XFS.
- Mounted it at `/backup-data`.
- Configured automatic mounting through `/etc/fstab`.
- Stored sample business data.
- Protected the EC2 instance and attached EBS volumes using AWS Backup.
- Successfully restored the EBS volumes during Disaster Recovery.

---

# Learning Outcomes

Through implementing Amazon EBS, the following concepts were learned:

- Amazon EBS Fundamentals
- Persistent Storage
- Block Storage
- Volume Attachment
- Linux Disk Management
- XFS File System
- UUID Configuration
- `/etc/fstab`
- Volume Mounting
- Storage Best Practices
- AWS Backup Integration
- Disaster Recovery

---

# Interview Questions

### Q1. What is Amazon EBS?

Amazon Elastic Block Store (EBS) is a persistent block storage service used with Amazon EC2 instances. It provides durable, high-performance storage for operating systems, applications, and data.

---

### Q2. Why did you attach a second EBS volume?

The second EBS volume was used to store business data separately from the operating system. This improves storage management, simplifies backups, and aligns with enterprise best practices.

---

### Q3. Why did you use the XFS file system?

XFS is a high-performance journaling file system that is well suited for large files, scalability, and enterprise workloads. Amazon Linux 2023 also uses XFS by default for its root filesystem.

---

### Q4. Why did you configure `/etc/fstab`?

The `/etc/fstab` file ensures the EBS volume is automatically mounted after every reboot, preventing manual intervention and ensuring application availability.

---

### Q5. What happened to the EBS volumes during the restore process?

AWS Backup created snapshots of the EBS volumes as part of the EC2 backup. During restoration, new EBS volumes were created from those snapshots and attached to the restored EC2 instance.

---

### Q6. What is the difference between Root Volume and Data Volume?

| Root Volume | Data Volume |
|-------------|-------------|
| Contains Operating System | Contains Business Data |
| Required for booting | Stores application files and user data |
| Mounted automatically | Mounted manually and configured in `/etc/fstab` |
| Usually smaller | Can be expanded independently |

---

# Conclusion

Amazon EBS provided persistent and reliable storage for both the operating system and business data in this project. By separating application data onto a dedicated 20 GB EBS volume, formatting it with XFS, and configuring automatic mounting, the storage architecture followed enterprise best practices. AWS Backup protected the EC2 instance and its attached EBS volumes, allowing successful restoration during the Disaster Recovery exercise and demonstrating how persistent storage supports business continuity in AWS.
