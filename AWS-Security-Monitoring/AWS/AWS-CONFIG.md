# 🛡️ AWS Config

## 📌 Overview

AWS Config is a fully managed AWS governance and compliance service that continuously monitors, records, and evaluates the configuration of AWS resources. It helps organizations maintain visibility into their cloud infrastructure by tracking configuration changes, maintaining a historical record of resources, and evaluating resources against predefined or custom compliance rules.

Unlike AWS CloudTrail, which records **who performed an action**, AWS Config focuses on **the current configuration state of AWS resources** and determines whether they comply with security best practices.

In this project, AWS Config was implemented to continuously monitor the security posture of AWS resources such as Amazon EC2, Amazon EBS, Amazon S3, IAM resources, and Security Groups.

---

# 🎯 Project Objective

The objective of implementing AWS Config was to:

- Continuously record AWS resource configurations.
- Detect configuration changes automatically.
- Evaluate resources against AWS Managed Rules.
- Identify security misconfigurations.
- Maintain configuration history.
- Generate compliance reports.
- Improve governance and security posture.

---

# ❓ Why AWS Config?

CloudTrail answers:

> **Who made the change?**

AWS Config answers:

> **Is the current configuration secure?**

Example

CloudTrail tells us:

```
User Bharath modified Security Group sg-123456.
```

AWS Config tells us:

```
Security Group sg-123456 is NON-COMPLIANT because SSH is open to the Internet.
```

Both services complement each other.

---

# 🏗️ Architecture

```
             AWS Resources

EC2
EBS
Security Groups
S3
IAM

        │

        ▼

      AWS Config Recorder

        │

Records Configuration Changes

        │

        ▼

Configuration History

        │

        ▼

AWS Config Rules

        │

Evaluates Compliance

        │

 ┌──────────────┐
 │              │
 ▼              ▼

Compliant   Non-Compliant

        │

        ▼

Configuration Snapshots

        │

        ▼

Amazon S3
```

---

# 🏗️ What We Implemented

During this project, AWS Config was configured completely from scratch.

Implementation included:

- Enabled AWS Config Recorder
- Created AWS Config Service Role
- Created dedicated S3 Bucket
- Configured Delivery Channel
- Enabled Continuous Recording
- Configured Resource Recording
- Implemented AWS Managed Rules
- Evaluated AWS Resources
- Verified Compliance Status

---

# Implementation Steps

---

# Step 1 - Create S3 Bucket

Created dedicated bucket

```
bharath-aws-config-logs-2026
```

Purpose

Store:

- Configuration History
- Configuration Snapshots
- Compliance Data

---

# Step 2 - Configure AWS Config Recorder

Enabled

```
Customer Managed Recorder
```

Recording Strategy

```
Record all resource types
```

Recording Frequency

```
Continuous Recording
```

Purpose

Continuously monitor AWS resources whenever configuration changes occur.

---

# Step 3 - Configure Resource Recording

Selected

```
Record all supported resource types
```

Global IAM resources

Initially excluded

```
IAM Users

IAM Roles

IAM Groups

IAM Policies
```

Reason

AWS excludes globally recorded IAM resources by default to reduce unnecessary configuration items and cost.

---

# Step 4 - Configure IAM Role

Created

```
AWSServiceRoleForConfig
```

Purpose

Allow AWS Config to

- Read AWS resources
- Evaluate resources
- Write configuration history
- Deliver snapshots to S3

---

# Step 5 - Configure Delivery Channel

Configured

Amazon S3 Bucket

```
bharath-aws-config-logs-2026
```

Purpose

Store

- Configuration snapshots
- Configuration history
- Compliance information

---

# Step 6 - Start Recording

Started

```
Configuration Recorder
```

Status

```
Recording = ON
```

AWS Config immediately started monitoring supported AWS resources.

---

# Step 7 - Add AWS Managed Rules

Configured the following AWS Managed Rules.

---

# Rule 1

## encrypted-volumes

Purpose

Checks whether every Amazon EBS volume is encrypted.

If an EBS volume is not encrypted,

AWS Config marks it

```
NON-COMPLIANT
```

---

Why important?

Encryption protects data stored on EBS volumes from unauthorized access.

---

In this project

The root EBS volume attached to the EC2 instance was intentionally left unencrypted (default), allowing AWS Config to detect it as **Noncompliant** and demonstrate compliance monitoring.

---

# Rule 2

## restricted-common-ports

Purpose

Checks Security Groups for unrestricted access to commonly used ports.

Ports include

- SSH (22)
- RDP (3389)
- FTP
- Telnet

---

Why important?

Open administrative ports are one of the most common cloud security risks.

---

In this project

The Security Group allowing SSH from

```
0.0.0.0/0
```

was detected as **Noncompliant** because unrestricted SSH access is not recommended in production.

---

# Rule 3

## vpc-sg-open-only-to-authorized-ports

Purpose

Evaluates Security Groups to determine whether only approved ports are open.

---

Why important?

Prevents unauthorized network exposure.

---

In this project

AWS Config evaluated the EC2 Security Group and flagged it if open ports were accessible from untrusted sources.

---

# Rule 4

## root-account-mfa-enabled

Purpose

Checks whether MFA is enabled for the AWS Root Account.

---

Why important?

The Root Account has unrestricted permissions.

MFA significantly reduces the risk of account compromise.

---

# Rule 5

## s3-bucket-public-read-prohibited

Purpose

Checks whether any S3 bucket allows public read access.

---

Why important?

Public buckets may expose confidential data.

---

# Rule 6

## s3-bucket-public-write-prohibited

Purpose

Checks whether S3 buckets allow public write access.

---

Why important?

Public write permissions could allow attackers to upload malicious files.

---

# Compliance Results

AWS Config evaluated every supported AWS resource.

Example

```
EC2

↓

Security Group

↓

Rule Evaluation

↓

NON-COMPLIANT
```

Another example

```
Amazon EBS

↓

Encryption Check

↓

NON-COMPLIANT
```

---

# Workflow

```
AWS Resource

        │

Configuration Change

        │

        ▼

AWS Config Recorder

        │

        ▼

Configuration History

        │

        ▼

AWS Managed Rules

        │

        ▼

Compliance Evaluation

        │

 ┌────────────┐
 │            │

 ▼            ▼

PASS        FAIL

        │

        ▼

Compliance Dashboard
```

---

# Technical Features Used

## Configuration Recorder

Continuously records configuration changes for supported AWS resources.

---

## Delivery Channel

Delivers configuration snapshots to Amazon S3.

---

## Configuration History

Maintains historical records of every configuration change.

---

## Configuration Snapshots

Provides a point-in-time view of all recorded resources.

---

## AWS Managed Rules

Evaluates resources against AWS security best practices.

---

## Continuous Recording

Captures changes immediately after they occur.

---

# Security Best Practices Followed

- Enabled continuous recording.
- Used dedicated S3 bucket.
- Used AWS Service-Linked Role.
- Enabled compliance monitoring.
- Evaluated infrastructure automatically.
- Used AWS Managed Rules.
- Followed governance best practices.

---

# Difference Between CloudTrail and AWS Config

| AWS CloudTrail | AWS Config |
|----------------|------------|
| Records AWS API calls | Records AWS resource configurations |
| Shows who performed an action | Shows whether resources are compliant |
| Used for auditing | Used for compliance |
| Event-based | State-based |
| Stores logs | Stores configuration history |
| Supports forensic investigations | Supports governance and compliance |

---

# Real-World Industry Usage

AWS Config is commonly used for:

- Security Compliance
- CIS Benchmark Validation
- ISO 27001 Compliance
- PCI-DSS Compliance
- HIPAA Compliance
- Continuous Governance
- Infrastructure Auditing
- DevSecOps
- SOC Monitoring
- Enterprise Cloud Security

Large organizations use AWS Config to continuously validate thousands of AWS resources against internal security policies.

---

# Benefits

- Continuous compliance monitoring
- Automatic resource evaluation
- Configuration history
- Configuration snapshots
- Security governance
- Change tracking
- Native AWS integration
- Automated compliance reporting

---

# Key Learnings

During this implementation, the following concepts were learned:

- Configuring AWS Config from scratch.
- Creating Configuration Recorders.
- Configuring Delivery Channels.
- Understanding Service-Linked Roles.
- Recording AWS resource configurations.
- Implementing AWS Managed Rules.
- Detecting non-compliant resources.
- Understanding compliance versus auditing.
- Integrating AWS Config with Amazon S3.

---

# Interview Questions

## Why did you use AWS Config?

AWS Config continuously records AWS resource configurations and evaluates them against security and compliance rules. It helps identify misconfigured resources and ensures that infrastructure adheres to organizational security standards.

---

## Why use Continuous Recording?

Continuous recording captures every configuration change as it happens, providing up-to-date visibility into the environment and enabling immediate compliance evaluation.

---

## Why create a dedicated S3 bucket?

AWS Config requires an Amazon S3 bucket to store configuration snapshots and history. Using a dedicated bucket improves security, simplifies access control, and separates Config data from other AWS logs.

---

## Why did the `encrypted-volumes` rule become Noncompliant?

The attached Amazon EBS volume was not encrypted. AWS Config detected this and marked the resource as Noncompliant, demonstrating how managed rules identify security issues.

---

## Why did the `vpc-sg-open-only-to-authorized-ports` rule become Noncompliant?

The EC2 Security Group allowed SSH (port 22) from **0.0.0.0/0**, exposing the instance to the public internet. AWS Config flagged this as a security risk because production environments should restrict administrative access to trusted IP ranges.

---

## What is the difference between a Configuration Recorder and a Config Rule?

- **Configuration Recorder** records configuration changes for AWS resources.
- **Config Rules** evaluate those recorded configurations against predefined compliance policies.

---

# AWS Services Integrated

- Amazon EC2
- Amazon EBS
- Amazon S3
- AWS IAM
- AWS CloudTrail
- Amazon CloudWatch
- Amazon SNS

---

# Project Outcome

Successfully implemented AWS Config as the compliance and governance layer of the AWS Security Monitoring project. AWS Config continuously recorded infrastructure changes, stored configuration history in Amazon S3, and evaluated resources using AWS Managed Rules. The service identified security issues such as unencrypted EBS volumes and overly permissive Security Groups, demonstrating automated compliance monitoring and governance capabilities commonly used in enterprise AWS environments.
