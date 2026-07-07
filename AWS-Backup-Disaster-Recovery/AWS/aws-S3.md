# 🪣 Amazon Simple Storage Service (Amazon S3)

## Overview

Amazon Simple Storage Service (Amazon S3) is a highly durable, scalable, and secure object storage service provided by AWS. It is designed to store and retrieve any amount of data from anywhere over the internet.

In this project, Amazon S3 was used to store business documents separately from the EC2 instance, demonstrating how organizations keep critical files in highly durable object storage while using AWS Backup to protect compute resources.

---

# Purpose

Amazon S3 was used to:

- Store business documents
- Simulate enterprise file storage
- Demonstrate object storage in AWS
- Provide highly durable storage
- Separate application files from infrastructure
- Support business continuity

---

# Why Amazon S3?

Amazon S3 is one of the most widely used AWS services because it provides:

- 99.999999999% (11 9's) Durability
- High Availability
- Unlimited Storage Capacity
- Secure Object Storage
- Versioning Support
- Lifecycle Management
- Encryption Support
- Fine-Grained Access Control
- Integration with AWS Services

---

# Architecture

```text
                   Users

                     │

                 Internet

                     │

              Amazon S3 Bucket

                     │

         Business Documents

     ├── HR/
     ├── Finance/
     ├── Reports/
     └── Images/
```

---

# Configuration Used

| Property | Value |
|----------|-------|
| Bucket Name | backup-dr-storage (Example) |
| Region | ap-south-1 (Mumbai) |
| Object Ownership | Bucket Owner Enforced |
| Versioning | Disabled |
| Encryption | Default AWS Managed (Optional) |
| Public Access | Blocked |

---

# What is an Object?

Amazon S3 stores data as **Objects**.

Each object consists of:

- File
- Metadata
- Unique Object Key

Example:

```
Bucket

↓

finance-report.pdf
```

The object can be any file type:

- PDF
- Images
- Videos
- Logs
- ZIP Files
- CSV Files
- JSON Files

---

# Bucket Structure

Example folder organization used in this project:

```text
backup-dr-storage/

├── HR/
│      employees.csv
│
├── Finance/
│      annual-report.pdf
│
├── Reports/
│      backup-report.txt
│
└── Images/
       architecture.png
```

---

# Uploading Objects

Objects were uploaded directly into the S3 bucket.

Examples:

- Employee Records
- Financial Reports
- Project Documents
- Architecture Diagrams

These files simulate enterprise business data.

---

# Storage Class

The project used the default storage class:

```
S3 Standard
```

Advantages:

- High Availability
- Low Latency
- Frequent Access
- Multi-AZ Storage

---

# Data Durability

Amazon S3 automatically stores multiple copies of data across multiple Availability Zones within the Region.

This provides:

- 99.999999999% Durability
- Automatic Data Replication
- High Availability
- Protection against hardware failures

---

# Security

The following security measures were used:

- Block Public Access enabled
- Bucket Owner Enforced
- IAM-based access control
- Private bucket configuration

No public access was granted to the bucket.

---

# How S3 Differs from EBS

| Amazon S3 | Amazon EBS |
|------------|------------|
| Object Storage | Block Storage |
| Stores Files | Stores Disk Blocks |
| Accessed via API | Attached to EC2 |
| Highly Scalable | Fixed Volume Size |
| Stores Objects | Stores File Systems |
| Multi-AZ Durability | Single AZ Volume |

---

# Why S3 Was Used in This Project

The EC2 instance hosted the application and business data on EBS.

Amazon S3 was used to:

- Store business documents
- Store project artifacts
- Demonstrate AWS object storage
- Separate static files from compute resources

This reflects common enterprise architecture where applications run on EC2 while documents, backups, and media files are stored in S3.

---

# Real-World Use Cases

Amazon S3 is commonly used for:

- Website Assets
- Application Logs
- Backup Storage
- Disaster Recovery
- Data Lakes
- Media Storage
- Static Website Hosting
- Software Distribution
- Machine Learning Datasets

---

# Best Practices

- Block Public Access unless required.
- Use IAM Roles instead of Access Keys.
- Enable Server-Side Encryption.
- Enable Versioning for important data.
- Configure Lifecycle Policies for cost optimization.
- Follow least-privilege access principles.

---

# Project Implementation

As part of this project:

- Created an Amazon S3 bucket.
- Uploaded business documents.
- Organized files into folders.
- Kept the bucket private.
- Demonstrated secure object storage alongside EC2 and EBS.

---

# Learning Outcomes

Through implementing Amazon S3, the following concepts were learned:

- Object Storage
- Buckets and Objects
- Storage Classes
- Bucket Security
- IAM Permissions
- Public Access Block
- Data Durability
- Enterprise File Storage
- AWS Storage Services

---

# Interview Questions

### Q1. What is Amazon S3?

Amazon S3 is a highly durable and scalable object storage service that stores data as objects inside buckets.

---

### Q2. Why did you use Amazon S3 in this project?

Amazon S3 was used to securely store business documents separately from the EC2 instance, demonstrating object storage in an enterprise backup and disaster recovery environment.

---

### Q3. What is the difference between Amazon S3 and Amazon EBS?

| Amazon S3 | Amazon EBS |
|------------|------------|
| Object Storage | Block Storage |
| Accessed using APIs | Attached directly to EC2 |
| Unlimited Scalability | Fixed-size Volumes |
| Multi-AZ Durability | Single Availability Zone |

---

### Q4. What is a Bucket?

A bucket is a logical container in Amazon S3 that stores objects such as documents, images, videos, logs, and backups.

---

### Q5. What is an Object?

An object is the actual file stored in Amazon S3, consisting of the file data, metadata, and a unique object key.

---

### Q6. Why should Block Public Access be enabled?

Block Public Access prevents accidental exposure of sensitive data by ensuring that objects cannot be accessed anonymously over the internet.

---

# Conclusion

Amazon S3 provided secure, scalable, and highly durable object storage for this project. Business documents were stored in a private S3 bucket, demonstrating how enterprise applications separate static data from compute resources. By using Amazon S3 alongside Amazon EC2, Amazon EBS, and AWS Backup, the project reflects a common production architecture where object storage is used for secure file management and long-term data durability.
