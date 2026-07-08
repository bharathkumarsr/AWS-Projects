# 📧 Amazon Simple Notification Service (Amazon SNS)

## 📌 Overview

Amazon Simple Notification Service (Amazon SNS) is a fully managed messaging and notification service that enables applications and AWS services to send notifications to subscribers through multiple communication protocols such as Email, SMS, HTTP/HTTPS, AWS Lambda, Amazon SQS, and mobile push notifications.

In this project, Amazon SNS was used to deliver **real-time email notifications** whenever a security event was detected by Amazon CloudWatch.

---

# 🎯 Objective

The objective of implementing Amazon SNS in this project was to:

- Send real-time security alerts.
- Notify administrators when suspicious activities occur.
- Integrate with CloudWatch Alarms.
- Improve incident response time.
- Automate security notifications.

---

# 🏗️ What We Implemented

During this project, Amazon SNS was configured as the notification service for the AWS Security Monitoring pipeline.

The implementation included:

- Created an SNS Topic
- Added an Email Subscription
- Verified the email subscription
- Connected CloudWatch Alarm to SNS
- Tested email notifications

---

# Architecture

```text
AWS Console Login

        │

        ▼

AWS CloudTrail

        │

        ▼

CloudWatch Logs

        │

        ▼

Metric Filter

        │

        ▼

CloudWatch Alarm

        │

        ▼

Amazon SNS Topic

        │

        ▼

Administrator Email
```

---

# Implementation Steps

## Step 1 - Create an SNS Topic

Created a Standard SNS Topic.

Example

```
Topic Name

SecurityAlerts
```

Purpose

The topic acts as a communication channel between CloudWatch Alarms and notification subscribers.

---

## Step 2 - Choose Topic Type

Selected

```
Standard Topic
```

Purpose

Provides high availability, scalability, and reliable message delivery.

---

## Step 3 - Create Email Subscription

Added an Email subscription.

Protocol

```
Email
```

Endpoint

```
your-email@example.com
```

Purpose

Receive security alerts directly in the administrator's mailbox.

---

## Step 4 - Confirm Subscription

AWS sent a confirmation email.

Clicked

```
Confirm Subscription
```

Purpose

Activate the subscription so Amazon SNS can deliver notifications.

---

## Step 5 - Integrate with CloudWatch Alarm

Opened

```
FailedConsoleLoginAlarm
```

Configured Alarm Action

```
Send Notification
```

Selected SNS Topic

```
SecurityAlerts
```

Purpose

Whenever the alarm enters the **ALARM** state, CloudWatch automatically publishes a message to Amazon SNS.

---

## Step 6 - Generate Test Event

Generated a failed AWS Console login.

CloudWatch Alarm changed to

```
ALARM
```

Amazon SNS immediately sent an email notification.

Verified the email was successfully received.

---

# Workflow

```text
Failed Console Login

        │

        ▼

CloudTrail

        │

        ▼

CloudWatch Logs

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

# Why Amazon SNS Was Used

Amazon SNS enables automated notifications whenever important events occur.

Without SNS,

administrators would need to continuously monitor the AWS Console.

SNS provides immediate notifications, allowing security teams to respond quickly to suspicious activities.

---

# Why SNS Instead of Manual Monitoring?

Manual monitoring has several limitations:

- Requires continuous observation.
- Delays incident detection.
- Increases operational effort.
- Can miss critical security events.

Amazon SNS automates notifications, ensuring that security alerts are delivered instantly.

---

# Technical Features Used

## Standard Topic

Configured a Standard SNS Topic.

Benefits

- High throughput
- Reliable delivery
- Low latency
- Supports multiple subscribers

---

## Email Protocol

Configured Email as the notification protocol.

Benefits

- Easy to implement
- Immediate alert delivery
- Suitable for administrators and security teams

---

## CloudWatch Alarm Integration

Configured CloudWatch Alarm to publish messages directly to the SNS Topic.

This enables automated notifications without manual intervention.

---

## Subscription Confirmation

Verified ownership of the email address by confirming the subscription.

This prevents unauthorized email subscriptions.

---

# Security Best Practices Followed

- Used a dedicated SNS Topic for security alerts.
- Verified email subscription before enabling notifications.
- Integrated only trusted AWS services.
- Automated security event notifications.
- Reduced manual monitoring effort.

---

# Real-World Industry Usage

Amazon SNS is widely used for:

- Security alerts
- Cloud infrastructure monitoring
- Incident response
- DevOps notifications
- CI/CD pipeline notifications
- Backup completion alerts
- Auto Scaling notifications
- Application monitoring
- Compliance reporting

Organizations often integrate SNS with:

- AWS Lambda
- Amazon SQS
- CloudWatch
- EventBridge
- Security Hub
- GuardDuty

---

# Benefits

- Fully managed service
- Real-time notifications
- High availability
- Highly scalable
- Easy AWS integration
- Supports multiple protocols
- Improves incident response

---

# Key Learnings

During this implementation, the following concepts were learned:

- Creating Amazon SNS Topics.
- Configuring Email subscriptions.
- Confirming subscriptions securely.
- Integrating SNS with CloudWatch Alarms.
- Automating security notifications.
- Validating end-to-end alert delivery.

---

# Interview Questions

## Why did you use Amazon SNS in this project?

Amazon SNS was used to deliver real-time email notifications whenever a failed AWS Console login was detected. This ensured administrators were immediately informed of potential security incidents without manually monitoring the AWS Console.

---

## Why integrate SNS with CloudWatch?

CloudWatch detects security events but does not notify users directly. SNS acts as the notification service, delivering alerts through email or other supported protocols whenever a CloudWatch Alarm changes state.

---

## Why did you choose an Email subscription?

Email is simple to configure, easy to validate during testing, and is commonly used by administrators to receive operational and security alerts.

---

## What happens when a failed login occurs?

1. AWS CloudTrail records the failed login event.
2. CloudTrail sends the log to CloudWatch Logs.
3. The Metric Filter identifies the failed login.
4. CloudWatch increments the custom metric.
5. CloudWatch Alarm enters the **ALARM** state.
6. Amazon SNS publishes a notification.
7. The administrator receives an email alert.

---

# AWS Services Integrated with Amazon SNS

- AWS CloudTrail
- Amazon CloudWatch Logs
- CloudWatch Metric Filters
- CloudWatch Alarms
- AWS IAM

---

# Project Outcome

Successfully implemented Amazon SNS as the notification layer of the AWS Security Monitoring solution. A Standard SNS Topic with an Email subscription was configured and integrated with CloudWatch Alarms. When a failed AWS Console login was detected, CloudWatch automatically published a notification to Amazon SNS, which delivered an email alert to the administrator. This implementation demonstrates an automated and event-driven alerting mechanism commonly used in enterprise cloud security environments.
