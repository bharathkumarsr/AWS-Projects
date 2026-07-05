# Amazon SNS (Simple Notification Service)

## Overview

Amazon SNS (Simple Notification Service) is a fully managed messaging service provided by AWS that enables applications to send notifications to subscribers through multiple communication protocols such as Email, SMS, HTTP/HTTPS, Lambda, and SQS.

In this project, Amazon SNS is used to send an email notification whenever a file is successfully processed by the AWS Lambda function.

---

# Purpose in This Project

Amazon SNS is responsible for:

- Sending real-time email notifications.
- Alerting users after successful file processing.
- Decoupling the notification mechanism from the application logic.
- Providing reliable and scalable message delivery.

---

# Service Used

- Amazon Simple Notification Service (SNS)

---

# Topic Created

| Property | Value |
|----------|-------|
| Topic Type | Standard |
| Topic Name | FileProcessingNotifications |
| Region | ap-south-1 (Mumbai) |

---

# Topic ARN

```
arn:aws:sns:ap-south-1:<AWS_ACCOUNT_ID>:FileProcessingNotifications
```

---

# Subscription

An Email subscription was created and confirmed.

| Property | Value |
|----------|-------|
| Protocol | Email |
| Status | Confirmed |

---

# Why SNS Was Used

Instead of directly sending emails from the Lambda function using SMTP or third-party services, Amazon SNS provides a managed and highly available notification service.

Benefits include:

- No SMTP server configuration
- Automatic scalability
- High reliability
- Easy integration with AWS Lambda
- Low operational overhead

---

# Workflow

```text
User Uploads File
        │
        ▼
Amazon S3
        │
ObjectCreated Event
        │
        ▼
AWS Lambda
        │
File Processed Successfully
        │
        ▼
Amazon SNS
        │
        ▼
Email Notification
```

---

# How It Works

### Step 1

A user uploads a file into the Amazon S3 bucket.

Example

```
employee-list.csv
```

---

### Step 2

Amazon S3 generates an ObjectCreated event.

---

### Step 3

AWS Lambda is automatically invoked.

---

### Step 4

Lambda processes the uploaded file by:

- Reading S3 metadata
- Retrieving file size
- Retrieving content type
- Writing metadata into DynamoDB

---

### Step 5

After successful processing, Lambda publishes a message to the SNS topic.

Example

```python
sns.publish(
    TopicArn=SNS_TOPIC_ARN,
    Subject="Serverless Event Processing",
    Message=message
)
```

---

### Step 6

Amazon SNS receives the message and immediately delivers it to all confirmed subscribers.

---

### Step 7

The subscribed email address receives a notification.

Example Email

```
Subject:
Serverless Event Processing
```

Email Body

```
Serverless Event Processing

File processed successfully.

Bucket Name :
bharath-serverless-pipeline-luffy

File Name :
employee-list.csv

File Size :
120 Bytes

Status :
SUCCESS

Upload Time :
2026-07-06 10:15:35 UTC
```

---

# Lambda Integration

AWS Lambda publishes messages to the SNS topic using the Boto3 SDK.

Example

```python
sns.publish(
    TopicArn=SNS_TOPIC_ARN,
    Subject="Serverless Event Processing",
    Message=message
)
```

---

# IAM Permissions Required

The Lambda execution role requires permission to publish messages to the SNS topic.

Example IAM Policy

```json
{
  "Effect": "Allow",
  "Action": [
    "sns:Publish"
  ],
  "Resource": "arn:aws:sns:ap-south-1:<AWS_ACCOUNT_ID>:FileProcessingNotifications"
}
```

---

# Notification Flow

```text
AWS Lambda
     │
     ▼
Amazon SNS Topic
     │
     ▼
Email Subscription
     │
     ▼
User Inbox
```

---

# Benefits of Amazon SNS

- Fully Managed Service
- Highly Available
- Automatic Scalability
- Event-Driven Notifications
- Reliable Message Delivery
- Easy AWS Integration
- Multiple Subscriber Support
- Secure Communication
- Low Cost

---

# Security

The SNS topic is secured using IAM policies.

Only the Lambda execution role is allowed to publish messages.

The email subscriber must confirm the subscription before receiving notifications.

---

# AWS Services Integrated

- Amazon SNS
- AWS Lambda
- Amazon S3
- Amazon DynamoDB
- Amazon CloudWatch
- AWS IAM

---

# Project Outcome

Amazon SNS successfully delivered real-time email notifications whenever a file was uploaded and processed by the Lambda function.

This provides immediate visibility into processing events without requiring users to manually monitor the application.

---

# Key Learning Outcomes

- Created an Amazon SNS Standard Topic.
- Configured Email subscriptions.
- Confirmed SNS subscriptions.
- Integrated SNS with AWS Lambda.
- Published notifications using the Boto3 SDK.
- Implemented event-driven email alerts.
- Configured IAM permissions for secure message publishing.
- Built a real-time notification workflow.

---

# Architecture

```text
                Upload File
                     │
                     ▼
              Amazon S3 Bucket
                     │
          ObjectCreated Event
                     │
                     ▼
            AWS Lambda Function
                     │
        File Processed Successfully
                     │
                     ▼
              Amazon SNS Topic
                     │
                     ▼
           Email Notification Sent
                     │
                     ▼
                User Mailbox
```

---

# Real-World Use Cases

Amazon SNS is commonly used for:

- Application Alerts
- System Monitoring
- CI/CD Pipeline Notifications
- Security Alerts
- Backup Completion Notifications
- Cloud Automation
- Incident Management
- Serverless Applications
- Event-Driven Architectures

---

# Conclusion

Amazon SNS plays a critical role in this Serverless Event Processing Pipeline by providing reliable, scalable, and real-time email notifications. After the AWS Lambda function successfully processes an uploaded file, SNS delivers a notification to subscribed users, ensuring immediate visibility into system events. Its seamless integration with AWS services makes it an ideal solution for building automated, event-driven cloud applications.
