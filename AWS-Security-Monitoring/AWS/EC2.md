# 🖥️ Amazon EC2 (Elastic Compute Cloud)

## 📌 Overview

Amazon Elastic Compute Cloud (Amazon EC2) is a scalable Infrastructure as a Service (IaaS) offering from AWS that provides secure, resizable virtual servers in the cloud. EC2 enables users to deploy applications, host websites, run databases, perform testing, and build enterprise infrastructure without managing physical hardware.

In this project, Amazon EC2 served as the primary compute resource that was monitored for security events and continuously evaluated for compliance using AWS CloudTrail and AWS Config.

---

# 🎯 Objective

The objective of implementing Amazon EC2 in this project was to:

- Deploy a secure virtual server in AWS.
- Generate AWS activity logs for monitoring.
- Configure Security Groups for network access.
- Validate AWS Config compliance rules.
- Demonstrate real-time security monitoring.
- Simulate production infrastructure.

---

# 🏗️ What We Implemented

During this project, an Amazon EC2 instance was launched and configured as the infrastructure resource for security monitoring.

The EC2 instance was used to demonstrate:

- AWS resource monitoring
- Security Group compliance
- EBS encryption compliance
- CloudTrail logging
- IAM authentication
- AWS Config resource evaluation

---

# Instance Configuration

| Property | Value |
|----------|-------|
| Service | Amazon EC2 |
| Instance Type | t2.micro |
| Region | ap-south-1 (Mumbai) |
| Operating System | Amazon Linux 2023 |
| Root Volume | Amazon EBS |
| Authentication | SSH Key Pair |
| Monitoring | AWS CloudTrail & AWS Config |

---

# Implementation Steps

## Step 1 - Launch EC2 Instance

Created an EC2 instance using the AWS Management Console.

Configuration:

```
Instance Type

t2.micro
```

Operating System

```
Amazon Linux 2023
```

Region

```
Mumbai (ap-south-1)
```

Purpose

Provide a compute resource for security monitoring and compliance evaluation.

---

## Step 2 - Create Key Pair

Created an SSH Key Pair.

Purpose

Securely authenticate while connecting to the EC2 instance.

AWS automatically generated a private key (.pem file).

---

## Step 3 - Configure Security Group

Created a custom Security Group.

Allowed inbound rules:

```
SSH (22)

Source

0.0.0.0/0
```

Purpose

Allow SSH connectivity to the EC2 instance for project testing.

> **Note:** In a production environment, SSH access should be restricted to trusted IP addresses or replaced with AWS Systems Manager Session Manager.

---

## Step 4 - Configure Storage

Amazon EBS Root Volume was automatically attached to the instance.

Purpose

Provide persistent block storage for the operating system.

AWS Config evaluated this EBS volume using the **encrypted-volumes** managed rule.

---

## Step 5 - Launch Instance

After reviewing the configuration,

the EC2 instance was launched successfully.

AWS automatically assigned:

- Instance ID
- Private IP
- Public IP
- Security Group
- EBS Volume

---

## Step 6 - Verify Instance Status

Verified that the instance entered the:

```
Running
```

state.

Confirmed:

- System Status Check
- Instance Status Check

Both passed successfully.

---

# How EC2 Was Used in This Project

The EC2 instance became part of the AWS Security Monitoring pipeline.

AWS services continuously monitored this resource.

```
EC2 Instance

      │

      ▼

CloudTrail

Records API Calls

      │

      ▼

CloudWatch Logs

      │

      ▼

Metric Filters

      │

      ▼

CloudWatch Alarm

      │

      ▼

SNS Email Notification
```

---

# AWS Config Evaluation

AWS Config continuously evaluated the EC2 instance for compliance.

Examples:

- Security Group configuration
- EBS encryption
- Attached resources
- Configuration changes

Example Rules

```
encrypted-volumes
```

```
vpc-sg-open-only-to-authorized-ports
```

These rules automatically detected security misconfigurations.

---

# Why Amazon EC2 Was Used

Amazon EC2 provides a real AWS compute resource that generates infrastructure events and can be evaluated by AWS security services.

Without EC2,

AWS Config would have limited infrastructure to monitor.

The EC2 instance allowed us to demonstrate:

- Resource monitoring
- Configuration auditing
- Security Group validation
- EBS compliance

---

# Technical Features Used

## Amazon Linux 2023

Latest AWS-supported Linux operating system.

Benefits

- Secure
- Lightweight
- Optimized for AWS
- Long-term support

---

## Security Groups

Implemented as a virtual firewall.

Configured inbound SSH access.

AWS Config continuously evaluated Security Group compliance.

---

## Amazon EBS

Root storage attached to the EC2 instance.

AWS Config evaluated encryption status using the managed rule:

```
encrypted-volumes
```

---

## Key Pair Authentication

Used SSH Key Pair authentication instead of passwords.

Benefits

- Secure authentication
- Industry best practice
- Password-less login

---

# Security Monitoring Workflow

```
Administrator

        │

        ▼

Launch EC2

        │

        ▼

CloudTrail Logs API Activity

        │

        ▼

CloudWatch Logs

        │

        ▼

CloudWatch Monitoring

        │

        ▼

AWS Config Evaluates

Security Group

EBS Encryption

Configuration Changes
```

---

# Security Best Practices Followed

- Used IAM authentication.
- Used SSH Key Pair authentication.
- Configured Security Groups.
- Enabled CloudTrail logging.
- Enabled AWS Config monitoring.
- Followed least-privilege principles.

---

# Real-World Industry Usage

Amazon EC2 is widely used for:

- Web Servers
- Application Servers
- CI/CD Build Servers
- Jenkins Servers
- Kubernetes Worker Nodes
- Docker Hosts
- Monitoring Servers
- Database Servers
- API Servers
- Enterprise Applications

---

# Benefits

- Highly scalable
- On-demand provisioning
- Secure
- Flexible instance types
- Pay-as-you-go pricing
- Deep integration with AWS services
- Supports automation

---

# Key Learnings

During this implementation, the following concepts were learned:

- Launching Amazon EC2 instances.
- Configuring Security Groups.
- Using SSH Key Pair authentication.
- Understanding Amazon EBS storage.
- Monitoring EC2 using AWS CloudTrail.
- Evaluating EC2 compliance using AWS Config.
- Understanding Security Group best practices.

---

# Interview Questions

## Why did you use Amazon EC2 in this project?

Amazon EC2 provided a real compute resource that generated AWS API activity and allowed AWS Config to evaluate infrastructure compliance, such as Security Group configurations and EBS volume encryption.

---

## Why are Security Groups important?

Security Groups act as virtual firewalls that control inbound and outbound traffic to EC2 instances. They help protect instances by allowing only authorized network access.

---

## Why did AWS Config mark the Security Group as Noncompliant?

The managed rule **vpc-sg-open-only-to-authorized-ports** detected that SSH (port 22) was open to **0.0.0.0/0**. While this was acceptable for a lab environment, in production it should be restricted to trusted IP addresses or replaced with Systems Manager Session Manager.

---

## Why was the EBS volume marked Noncompliant?

The **encrypted-volumes** managed rule detected that the attached EBS volume was not encrypted. This demonstrates AWS Config's ability to identify security and compliance issues automatically.

---

# AWS Services Integrated with EC2

- AWS IAM
- Amazon EBS
- AWS CloudTrail
- Amazon CloudWatch Logs
- CloudWatch Alarms
- Amazon SNS
- AWS Config

---

# Project Outcome

Successfully deployed and configured an Amazon EC2 instance as the primary infrastructure resource for the AWS Security Monitoring project. The instance generated CloudTrail events, was continuously evaluated by AWS Config for Security Group and EBS compliance, and demonstrated how AWS-native services work together to provide real-time monitoring, compliance validation, and security visibility in a cloud environment.
