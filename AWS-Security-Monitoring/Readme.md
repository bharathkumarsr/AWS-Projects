# 🛡️ AWS Security Monitoring Project

> **A Real-Time AWS Security Monitoring and Compliance Project using CloudTrail, CloudWatch, SNS, and AWS Config**

---

# 📌 Project Overview

Organizations running workloads in AWS must continuously monitor user activities, detect suspicious behavior, generate real-time alerts, and ensure that cloud resources comply with security best practices.

This project demonstrates how to build an **AWS-native Security Monitoring Solution** that performs:

- Continuous API activity logging
- Security event monitoring
- Real-time email notifications
- Compliance monitoring
- Configuration auditing

The solution uses multiple AWS services integrated together to create an automated security monitoring pipeline similar to what many organizations use in production environments.

---

# 🎯 Project Objectives

- Monitor AWS account activities.
- Capture every API call made in the AWS account.
- Detect failed AWS Console login attempts.
- Generate CloudWatch metrics from CloudTrail logs.
- Trigger alarms when suspicious activity occurs.
- Send email notifications using Amazon SNS.
- Continuously evaluate AWS resources for compliance.
- Detect security misconfigurations automatically.

---

# 🏗️ Architecture

```
                IAM User
                    │
                    ▼
             AWS Management Console
                    │
                    ▼
               AWS CloudTrail
                    │
        ┌───────────┴────────────┐
        ▼                        ▼
 CloudTrail S3 Bucket     CloudWatch Logs
                                   │
                                   ▼
                           Metric Filter
                                   │
                                   ▼
                          CloudWatch Alarm
                                   │
                                   ▼
                             Amazon SNS
                                   │
                                   ▼
                           Email Notification

                    AWS Resources
             (EC2 • EBS • S3 • IAM)
                    │
                    ▼
               AWS Config
                    │
                    ▼
          Compliance Evaluation
```

---

# 🚀 AWS Services Used

| AWS Service | Purpose |
|-------------|----------|
| IAM | Secure access management |
| EC2 | Test server for monitoring |
| S3 | Store CloudTrail and AWS Config logs |
| CloudTrail | Record AWS API activities |
| CloudWatch Logs | Store and analyze CloudTrail logs |
| Metric Filters | Detect failed console login events |
| CloudWatch Alarms | Generate alerts |
| SNS | Send email notifications |
| AWS Config | Monitor compliance of AWS resources |

---

# 🔹 Why Each AWS Service Was Used

---

# 1️⃣ AWS IAM (Identity and Access Management)

## Why we used IAM

IAM provides secure authentication and authorization for AWS resources.

It allows administrators to:

- Create users
- Assign permissions
- Follow least-privilege access
- Improve account security

### In this project

IAM was used to:

- Create IAM users
- Test Console Login events
- Generate CloudTrail logs
- Simulate authentication activities

---

# 2️⃣ Amazon EC2

## Why we used EC2

EC2 provides virtual machines inside AWS.

### In this project

EC2 was used as the infrastructure resource that AWS Config evaluates for compliance.

Examples:

- Security Group monitoring
- EBS volume encryption validation

---

# 3️⃣ Amazon S3

## Why we used S3

CloudTrail and AWS Config require durable storage.

### In this project

Two buckets were created:

### Bucket 1

```
bharath-security-cloudtrail-logs
```

Purpose:

Store CloudTrail log files.

---

### Bucket 2

```
bharath-aws-config-logs-2026
```

Purpose:

Store AWS Config snapshots and configuration history.

---

# 4️⃣ AWS CloudTrail

## Why we used CloudTrail

CloudTrail records every API call made inside AWS.

Examples include:

- Login events
- EC2 creation
- IAM changes
- S3 access
- Security Group modifications

CloudTrail is the foundation of AWS auditing.

### In this project

CloudTrail was configured to:

- Capture Management Events
- Send logs to S3
- Deliver logs to CloudWatch Logs

Without CloudTrail, security event monitoring would not be possible.

---

# 5️⃣ Amazon CloudWatch Logs

## Why we used CloudWatch Logs

CloudWatch Logs stores application and AWS service logs.

### In this project

CloudTrail logs were streamed into CloudWatch Logs.

This allowed searching and analyzing events in near real time.

---

# 6️⃣ CloudWatch Metric Filter

## Why we used Metric Filters

CloudWatch cannot generate alarms directly from log text.

Metric Filters convert log patterns into numerical metrics.

### In this project

We created a metric filter:

```
FailedConsoleLoginCount
```

Filter Pattern:

```
($.eventName="ConsoleLogin")
&&
($.responseElements.ConsoleLogin="Failure")
```

Whenever a failed login occurred,

CloudWatch increased the custom metric.

---

# 7️⃣ CloudWatch Alarm

## Why we used CloudWatch Alarm

CloudWatch Alarms monitor metrics.

When a threshold is exceeded,

they trigger automated actions.

### In this project

Alarm Name

```
FailedConsoleLoginAlarm
```

Condition

```
FailedConsoleLoginCount >= 1
```

When the metric reached one failed login,

the alarm entered the ALARM state.

---

# 8️⃣ Amazon SNS (Simple Notification Service)

## Why we used SNS

SNS provides real-time notifications.

### In this project

CloudWatch Alarm published a message to SNS.

SNS immediately sent an email notification whenever:

- Failed Console Login occurred

This enables security teams to react quickly.

---

# 9️⃣ AWS Config

## Why we used AWS Config

CloudTrail answers:

> **Who changed something?**

AWS Config answers:

> **Is the current configuration secure?**

AWS Config continuously evaluates AWS resources against predefined compliance rules.

### Rules Implemented

- encrypted-volumes
- restricted-common-ports
- root-account-mfa-enabled
- s3-bucket-public-read-prohibited
- s3-bucket-public-write-prohibited
- vpc-sg-open-only-to-authorized-ports

AWS Config automatically detected:

- Unencrypted EBS Volumes
- Open Security Groups
- Public S3 Buckets
- Missing MFA (if applicable)

This provides continuous compliance monitoring.

---

# 🔄 Project Workflow

```
User Login
      │
      ▼
CloudTrail records API event
      │
      ▼
CloudWatch Logs receives log
      │
      ▼
Metric Filter checks

Failed Login?

      │
      ▼
CloudWatch Metric

      │
      ▼
CloudWatch Alarm

      │
      ▼
Amazon SNS

      │
      ▼
Email Notification
```

---

# AWS Config Workflow

```
AWS Resources

EC2
EBS
IAM
S3

        │

        ▼

AWS Config

        │

Evaluates Rules

        │

        ▼

Compliant
or

Non-Compliant
```

---

# 🔐 Security Monitoring Implemented

✅ CloudTrail Logging

✅ CloudWatch Log Monitoring

✅ Failed Console Login Detection

✅ Custom Metric Filters

✅ CloudWatch Alarm

✅ SNS Email Notification

✅ Continuous Compliance Monitoring

---

# 📊 Compliance Rules Implemented

| Rule | Purpose |
|------|----------|
| encrypted-volumes | Detect unencrypted EBS volumes |
| restricted-common-ports | Detect insecure ports |
| root-account-mfa-enabled | Verify MFA on root account |
| s3-bucket-public-read-prohibited | Prevent public bucket read access |
| s3-bucket-public-write-prohibited | Prevent public bucket write access |
| vpc-sg-open-only-to-authorized-ports | Detect overly permissive security groups |

---

# 📈 Project Outcome

Successfully built an automated AWS Security Monitoring solution capable of:

- Capturing AWS API activities
- Detecting failed login attempts
- Generating security alerts
- Sending email notifications
- Evaluating AWS resource compliance
- Identifying security misconfigurations

---

# 💼 Real-World Use Cases

This architecture is commonly used for:

- Cloud Security Monitoring
- Security Operations Center (SOC)
- Compliance Auditing
- Threat Detection
- Governance
- DevSecOps
- AWS Infrastructure Monitoring

---

# 🛠️ Skills Demonstrated

- AWS IAM
- Amazon EC2
- Amazon S3
- AWS CloudTrail
- Amazon CloudWatch
- CloudWatch Logs
- Metric Filters
- CloudWatch Alarms
- Amazon SNS
- AWS Config
- Cloud Security
- Compliance Monitoring
- Security Event Detection
- AWS Logging
- Cloud Governance

---

# 📚 Key Learnings

- Implemented centralized AWS activity logging.
- Built real-time security monitoring using CloudWatch.
- Generated custom metrics from CloudTrail logs.
- Configured automated email alerts using SNS.
- Implemented continuous compliance monitoring using AWS Config.
- Understood the difference between event monitoring and compliance monitoring.
- Learned how multiple AWS security services integrate to create an enterprise-grade monitoring solution.

---

# 👨‍💻 Author

**Bharath Kumar S R**

**Role:** DevOps Engineer

**Technologies:** AWS • Linux • Docker • Kubernetes • Terraform • Jenkins • CI/CD • Cloud Security

---

⭐ If you found this project useful, feel free to star the repository!
