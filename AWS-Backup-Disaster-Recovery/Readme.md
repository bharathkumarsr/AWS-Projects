# ☁️ AWS Backup & Disaster Recovery using AWS Backup

> A hands-on AWS project demonstrating how to design, protect, restore, and validate cloud infrastructure using AWS Backup and Disaster Recovery best practices.

![AWS](https://img.shields.io/badge/AWS-Cloud-orange)
![EC2](https://img.shields.io/badge/EC2-Compute-blue)
![EBS](https://img.shields.io/badge/EBS-Storage-green)
![AWS%20Backup](https://img.shields.io/badge/AWS-Backup-yellow)
![Disaster Recovery](https://img.shields.io/badge/Disaster-Recovery-red)

---

# 📖 Project Overview

Data loss and infrastructure failures are major challenges for every organization. Whether caused by accidental deletion, hardware failures, ransomware attacks, or system corruption, organizations require reliable backup and disaster recovery strategies to maintain business continuity.

This project demonstrates a complete **AWS Backup & Disaster Recovery** implementation by manually creating cloud infrastructure, protecting an EC2 instance using **AWS Backup**, generating recovery points, restoring the infrastructure, and validating the restored environment.

The project closely resembles enterprise backup workflows used by Cloud Engineers, DevOps Engineers, Infrastructure Engineers, and Site Reliability Engineers (SREs).

---

# 🎯 Project Objectives

The primary objectives of this project are:

- Design a secure AWS network
- Deploy a production-like EC2 Web Server
- Configure persistent storage using Amazon EBS
- Store business documents in Amazon S3
- Protect infrastructure using AWS Backup
- Generate Recovery Points
- Restore infrastructure after failure
- Validate Disaster Recovery
- Verify application availability
- Understand enterprise backup strategies

---

# 🏗 Project Architecture

```text
                                       Internet
                                           │
                                   Internet Gateway
                                           │
                                  Public Route Table
                                           │
                                  Public Subnet
                                           │
                              Security Group (22,80)
                                           │
                                 Backup-WebServer
                                   Amazon EC2
                                           │
                     ┌─────────────────────┴─────────────────────┐
                     │                                           │
               Root EBS Volume                           Data EBS Volume
                  10 GB gp3                                20 GB gp3
                     │                                           │
               Amazon Linux 2023                         Business Data
                     │
                   Nginx
                     │
         ───────────────────────────────────────────────
                     │
                 AWS Backup
                     │
              Backup-DR-Vault
                     │
              Recovery Point
                     │
               Restore Process
                     │
          Restored EC2 + Restored EBS
                     │
              Elastic IP Association
                     │
            Website Validation Successful

                 Amazon S3
        (Business Documents Storage)
```

---

# 🛠 AWS Services Used

| Service | Purpose |
|----------|----------|
| Amazon VPC | Creates isolated cloud network |
| Public Subnet | Hosts internet-facing resources |
| Internet Gateway | Enables Internet connectivity |
| Route Table | Routes Internet traffic |
| Security Group | Acts as virtual firewall |
| Amazon EC2 | Hosts web application |
| Amazon EBS | Persistent block storage |
| Amazon S3 | Object storage for business files |
| AWS Backup | Centralized backup management |
| Backup Vault | Stores Recovery Points |
| Recovery Point | Used for restoring infrastructure |
| Elastic IP | Provides static public IP after restore |

---

# 📂 Project Structure

```text
AWS-Backup-Disaster-Recovery/
│
├── README.md
│
├── docs/
│     ├── 01-VPC.md
│     ├── 02-Public-Subnet.md
│     ├── 03-Internet-Gateway.md
│     ├── 04-Route-Table.md
│     ├── 05-Security-Group.md
│     ├── 06-Amazon-EC2.md
│     ├── 07-Amazon-EBS.md
│     ├── 08-Amazon-S3.md
│     ├── 09-AWS-Backup.md
│     ├── 10-Backup-Vault.md
│     ├── 11-Backup-Plan.md
│     ├── 12-Recovery-Points.md
│     ├── 13-Disaster-Recovery.md
│     ├── 14-Restore-Validation.md
│     └── 15-Project-Learning.md
│
├── architecture/
│      ├── drawio/
│      ├── png/
│      └── diagrams/
│
├── screenshots/
│      ├── 01-vpc.png
│      ├── 02-subnet.png
│      ├── 03-igw.png
│      ├── 04-route-table.png
│      ├── 05-security-group.png
│      ├── 06-ec2.png
│      ├── 07-ebs.png
│      ├── 08-s3.png
│      ├── 09-backup-vault.png
│      ├── 10-backup-job.png
│      ├── 11-recovery-point.png
│      ├── 12-restore-job.png
│      ├── 13-restored-instance.png
│      ├── 14-restored-volumes.png
│      └── 15-nginx-validation.png
```

---

# 🌐 Network Architecture

## Custom VPC

```
10.0.0.0/16
```

Created a dedicated VPC to isolate all project resources.

---

## Public Subnet

```
10.0.1.0/24
```

Hosted the EC2 instance inside the public subnet.

---

## Internet Gateway

Provided Internet access for:

- SSH
- HTTP
- Package downloads
- AWS Services

---

## Route Table

Configured default route:

```
0.0.0.0/0

↓

Internet Gateway
```

---

## Security Group

Allowed:

| Port | Protocol | Purpose |
|-------|----------|----------|
|22|TCP|SSH|
|80|TCP|HTTP|

---

# 💻 Compute Layer

## Amazon EC2

Instance Details

| Property | Value |
|----------|-------|
| Name | Backup-WebServer |
| OS | Amazon Linux 2023 |
| Type | t3.micro |

Installed:

- Nginx
- Business Files
- Linux Utilities

---

# 💾 Storage Layer

## Root Volume

```
10 GB
gp3
```

Stores:

- Operating System
- Nginx
- Configuration

---

## Additional Volume

```
20 GB
gp3
```

Mounted:

```
/backup-data
```

Stores:

- HR
- Finance
- Logs
- Configuration Files

---

# 🪣 Amazon S3

Created an S3 bucket to demonstrate enterprise object storage.

Stored:

- Reports
- Business Documents
- Architecture Files

---

# 🔄 AWS Backup

Created:

- Backup Vault
- On-Demand Backup
- Recovery Point

Retention:

```
30 Days
```

Protected Resource:

```
Backup-WebServer
```

---

# 🚨 Disaster Recovery Workflow

```text
Launch EC2

↓

Configure Nginx

↓

Attach EBS

↓

Create Business Data

↓

AWS Backup

↓

Backup Vault

↓

Recovery Point

↓

Restore

↓

New EC2

↓

New EBS

↓

Assign Elastic IP

↓

Validate Website
```

---

# ✅ Restore Validation

The restored environment was verified by checking:

- EC2 Running
- SSH Connectivity
- Root Volume
- Data Volume
- Mount Points
- Business Data
- Nginx Status
- Website Accessibility

Everything was successfully restored.

---

# 📚 Linux Commands Used

```bash
lsblk

blkid

df -h

mkfs.xfs

mount

mkdir

systemctl

dnf install nginx

vi

echo

cat

ssh
```

---

# 🎓 Skills Gained

## AWS

- VPC
- EC2
- EBS
- S3
- AWS Backup
- Recovery Points
- Backup Vault
- Elastic IP

## Linux

- Storage Management
- Package Management
- File Systems
- SSH
- Service Management

## Networking

- CIDR
- Route Tables
- Internet Gateway
- Security Groups
- Public Networking

## Disaster Recovery

- Backup Strategy
- Infrastructure Restore
- Recovery Validation
- Business Continuity

---

# 📸 Screenshots Included

- VPC
- Subnet
- Route Table
- Internet Gateway
- Security Group
- EC2
- EBS
- S3 Bucket
- Backup Vault
- Backup Job
- Recovery Point
- Restore Job
- Restored EC2
- Restored EBS
- Elastic IP
- Nginx Validation

---

# 🚀 Future Enhancements

Future improvements include:

- AWS Backup Plan Automation
- Scheduled Daily Backups
- Backup Vault Lock
- Cross-Region Backup
- Cross-Account Backup
- Encrypted EBS Volumes
- IAM Backup Roles
- CloudWatch Monitoring
- SNS Notifications
- Terraform Automation
- Multi-AZ Disaster Recovery

---

# 💼 Real-World Use Cases

This project reflects backup and disaster recovery strategies used in:

- Banking
- Healthcare
- Insurance
- E-Commerce
- SaaS Platforms
- Enterprise Infrastructure
- Government Organizations

---

# 🎯 Learning Outcomes

By completing this project, I gained practical experience in:

- Designing AWS infrastructure
- Linux server administration
- Cloud networking
- Persistent storage management
- Backup and recovery
- Disaster Recovery planning
- Infrastructure validation
- Troubleshooting AWS services
- Applying cloud best practices

---

# 👨‍💻 Author

**Bharath Kumar S R**

**DevOps Engineer | AWS | Linux | Docker | Kubernetes | Terraform | CI/CD**

---

# ⭐ If you found this project useful, consider giving it a Star!
