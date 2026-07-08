# 🛡️ AWS CloudTrail

## 📌 Overview

AWS CloudTrail is a fully managed auditing and governance service that records every API activity performed within an AWS account. It captures actions made through the AWS Management Console, AWS CLI, SDKs, and AWS services, providing a complete audit trail for security analysis, compliance, and troubleshooting.

In this project, AWS CloudTrail acted as the **foundation of the security monitoring solution** by recording all AWS account activities and delivering them to Amazon S3 and Amazon CloudWatch Logs for further analysis.

---

# 🎯 Objective

The objective of implementing AWS CloudTrail in this project was to:

- Record all AWS API activities.
- Capture AWS Console login events.
- Monitor account activity for security incidents.
- Deliver logs to Amazon S3 for long-term storage.
- Stream logs to CloudWatch Logs for real-time monitoring.
- Integrate with CloudWatch Alarms and Amazon SNS.
- Support compliance and forensic investigations.

---

# 🏗️ What We Implemented

During this project, a multi-service CloudTrail pipeline was configured.

The implementation included:

- Created a CloudTrail Trail
- Enabled Management Events
- Configured Multi-Region Trail
- Delivered logs to Amazon S3
- Sent logs to CloudWatch Logs
- Integrated with Metric Filters
- Triggered CloudWatch Alarms
- Generated Email Alerts using SNS

---

# Architecture

```text
AWS User Activity

        │

        ▼

AWS CloudTrail

 ┌──────────────┐
 ▼              ▼

Amazon S3    CloudWatch Logs

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
```

---

# Implementation Steps

## Step 1 - Create CloudTrail Trail

Created a new trail.

Example

```
Trail Name

SecurityMonitoringTrail
```

Purpose

The trail records every supported AWS API activity performed within the account.

---

## Step 2 - Configure Trail Type

Selected

```
Multi-region Trail
```

Purpose

Capture events occurring in every AWS Region instead of monitoring only one Region.

This follows AWS security best practices.

---

## Step 3 - Enable Management Events

Enabled

```
Management Events
```

Read Events

```
Enabled
```

Write Events

```
Enabled
```

Purpose

Capture activities such as

- Console Login
- EC2 Launch
- IAM User Creation
- Security Group Changes
- S3 Bucket Creation
- CloudWatch Configuration
- AWS Config Changes

---

## Step 4 - Configure S3 Bucket

Created

```
bharath-security-cloudtrail-logs
```

Configured CloudTrail to deliver log files into this bucket.

Purpose

Provide durable storage for audit logs.

---

## Step 5 - Enable CloudWatch Logs Integration

Created a CloudWatch Log Group.

Example

```
CloudTrailLogs
```

Configured CloudTrail to stream logs into CloudWatch Logs.

Purpose

Allow near real-time monitoring instead of waiting for log files in S3.

---

## Step 6 - Configure IAM Role

CloudTrail automatically used an IAM role with permissions to:

- Write logs to S3
- Publish logs to CloudWatch Logs

Purpose

Enable secure integration with AWS services.

---

## Step 7 - Start Logging

Verified

```
Logging = ON
```

CloudTrail immediately began recording AWS account activity.

---

## Step 8 - Validate Event History

Generated test events by:

- Logging into AWS
- Accessing EC2
- Accessing S3
- Opening IAM
- Performing Console Login tests

Verified that these events appeared in

```
CloudTrail → Event History
```

---

# What CloudTrail Recorded

Examples of recorded events:

- Console Login
- CreateBucket
- RunInstances
- StartInstances
- StopInstances
- CreateSecurityGroup
- AuthorizeSecurityGroupIngress
- CreateTrail
- PutMetricFilter
- PutMetricAlarm
- CreateTopic
- Subscribe

Every event contains:

- Event Name
- Username
- Event Time
- Source IP
- AWS Region
- Request Parameters
- Response Elements
- Event ID

---

# Why CloudTrail Was Used

CloudTrail provides complete visibility into AWS account activity.

It answers questions like:

- Who performed an action?
- What action was performed?
- When did it occur?
- Which AWS service was affected?
- From which IP address?
- Was the action successful?

Without CloudTrail, it would not be possible to audit user activities or detect unauthorized changes.

---

# Integration with CloudWatch

CloudTrail logs were streamed into CloudWatch Logs.

CloudWatch Metric Filters scanned these logs.

Filter Used

```
FailedConsoleLoginCount
```

Pattern

```
($.eventName = ConsoleLogin)
&&
($.responseElements.ConsoleLogin = "Failure")
```

Whenever a failed login occurred,

CloudWatch increased a custom metric.

---

# Integration with CloudWatch Alarm

Created Alarm

```
FailedConsoleLoginAlarm
```

Threshold

```
FailedConsoleLoginCount >= 1
```

Purpose

Generate an alarm whenever at least one failed AWS Console login occurs.

---

# Integration with Amazon SNS

Configured Amazon SNS Topic.

Example

```
SecurityAlerts
```

Whenever the CloudWatch Alarm entered the **ALARM** state,

SNS automatically sent an email notification.

---

# CloudTrail Workflow

```text
Administrator Login

        │

        ▼

CloudTrail Records API Event

        │

        ▼

CloudWatch Logs

        │

        ▼

Metric Filter

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

Email Alert
```

---

# Technical Features Used

## Multi-Region Trail

Captured AWS API activities across all AWS Regions.

---

## Management Events

Recorded both

- Read Events
- Write Events

for supported AWS services.

---

## Event History

Used to verify recorded API activities without downloading log files.

---

## S3 Log Delivery

Stored CloudTrail log files in

```
bharath-security-cloudtrail-logs
```

for long-term retention.

---

## CloudWatch Logs Integration

Enabled near real-time analysis of CloudTrail events.

---

# Security Best Practices Followed

- Enabled Multi-Region Trail.
- Enabled Management Events.
- Stored logs in a dedicated S3 bucket.
- Integrated CloudTrail with CloudWatch Logs.
- Used IAM roles for secure log delivery.
- Generated automated security alerts.
- Maintained an auditable activity history.

---

# Real-World Industry Usage

AWS CloudTrail is widely used for:

- Security Monitoring
- Incident Response
- Compliance Auditing
- Threat Detection
- SOC Operations
- DevSecOps
- Governance
- Change Tracking
- Forensic Investigations

Industries such as banking, healthcare, government, and e-commerce rely on CloudTrail to maintain secure and auditable AWS environments.

---

# Benefits

- Complete API auditing
- Near real-time monitoring
- Long-term log retention
- Integration with CloudWatch
- Compliance support
- Security investigation
- Native AWS integration

---

# Key Learnings

During this implementation, the following concepts were learned:

- Creating and configuring CloudTrail trails.
- Understanding Management Events.
- Configuring Multi-Region logging.
- Delivering logs to Amazon S3.
- Streaming logs to CloudWatch Logs.
- Monitoring AWS Console Login events.
- Integrating CloudTrail with CloudWatch Alarms and SNS.
- Building an end-to-end AWS security monitoring pipeline.

---

# Interview Questions

## Why did you use AWS CloudTrail?

CloudTrail records all AWS API activities, enabling auditing, monitoring, troubleshooting, and security investigations. It provides visibility into who performed an action, when it occurred, and which AWS resources were affected.

---

## Why did you enable a Multi-Region Trail?

A Multi-Region Trail captures events from all AWS Regions, ensuring complete visibility even if resources are created outside the primary Region.

---

## Why integrate CloudTrail with CloudWatch Logs?

CloudTrail stores logs in S3 for long-term retention, while CloudWatch Logs enables near real-time log analysis. This integration allows Metric Filters and Alarms to detect security events immediately.

---

## What is the difference between Event History and CloudTrail Logs?

- **Event History** provides a recent view of management events directly in the AWS Console.
- **CloudTrail Logs** are stored in Amazon S3 for long-term auditing and compliance and can also be streamed to CloudWatch Logs for monitoring.

---

## How did CloudTrail contribute to this project?

CloudTrail captured AWS Console login events and API calls. These logs were analyzed by CloudWatch Metric Filters, which generated custom metrics. CloudWatch Alarms monitored those metrics and Amazon SNS sent email alerts whenever suspicious activity, such as a failed console login, was detected.

---

# AWS Services Integrated with CloudTrail

- AWS IAM
- Amazon EC2
- Amazon S3
- Amazon CloudWatch Logs
- CloudWatch Metric Filters
- CloudWatch Alarms
- Amazon SNS
- AWS Config

---

# Project Outcome

Successfully implemented AWS CloudTrail as the auditing foundation of the AWS Security Monitoring solution. CloudTrail captured AWS API activities, delivered logs to Amazon S3 for secure storage, streamed events to CloudWatch Logs for real-time analysis, and integrated with CloudWatch Alarms and Amazon SNS to provide automated detection and notification of security events. This implementation demonstrates a production-style monitoring pipeline commonly used in enterprise AWS environments.
