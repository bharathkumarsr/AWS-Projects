# Amazon CloudWatch

## Overview

Amazon CloudWatch is a fully managed monitoring and observability service provided by AWS. It enables developers and system administrators to monitor applications, collect logs, track performance metrics, create alarms, and troubleshoot issues across AWS resources.

In this project, Amazon CloudWatch is used to capture and store AWS Lambda execution logs, monitor the serverless workflow, and assist in debugging and troubleshooting during file processing.

---

# Purpose in This Project

Amazon CloudWatch is responsible for:

- Capturing AWS Lambda execution logs.
- Recording successful and failed executions.
- Monitoring serverless application performance.
- Assisting in debugging runtime errors.
- Providing operational visibility into the entire workflow.

---

# Service Used

- Amazon CloudWatch

---

# Log Group Created

| Property | Value |
|----------|-------|
| Log Group | /aws/lambda/ServerlessEventProcessor |
| Source | AWS Lambda |
| Log Retention | Never Expire (Default) |

---

# Why CloudWatch Was Used

CloudWatch provides centralized monitoring and logging for AWS resources.

Instead of manually debugging the Lambda function, CloudWatch automatically records:

- Function execution
- Errors
- Execution duration
- Request IDs
- Memory usage
- Initialization time
- Custom application logs

This significantly simplifies monitoring and troubleshooting.

---

# Workflow

```text
User Uploads File
        │
        ▼
Amazon S3 Bucket
        │
ObjectCreated Event
        │
        ▼
AWS Lambda
        │
Execution Logs
        │
        ▼
Amazon CloudWatch
```

---

# How It Works

### Step 1

A user uploads a file into Amazon S3.

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

Lambda writes execution logs using Python's print() statements.

Example

```python
print("========== Lambda Started ==========")
print(f"Bucket : {bucket}")
print(f"Object Key : {object_key}")
```

---

### Step 5

CloudWatch automatically stores the logs inside the Lambda Log Group.

---

### Step 6

Developers can review the logs to verify successful execution or identify failures.

---

# Log Structure

CloudWatch creates the following hierarchy:

```
Log Group
│
└── Log Stream
      │
      ├── START RequestId
      ├── Application Logs
      ├── END RequestId
      └── REPORT
```

---

# Example Logs

```
========== Lambda Started ==========

Bucket : bharath-serverless-pipeline-luffy

Object Key : employee-list.csv

Writing item to DynamoDB...

Item successfully stored.

Publishing SNS Notification...

SNS Notification Sent Successfully

========== Lambda Completed ==========
```

---

# Lambda Runtime Logs

CloudWatch automatically records runtime information.

Example

```
START RequestId:
xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx

END RequestId:
xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx

REPORT RequestId:
Duration: 425 ms

Memory Size: 128 MB

Max Memory Used: 72 MB
```

---

# Debugging

CloudWatch was used during project development to identify and resolve issues such as:

- HeadObject 404 errors
- Incorrect S3 object keys
- Lambda execution failures
- SNS notification issues
- DynamoDB write failures
- IAM permission problems

The detailed logs helped quickly locate and fix runtime errors.

---

# Monitoring Benefits

CloudWatch provides visibility into:

- Function Invocations
- Execution Duration
- Error Rate
- Throttles
- Concurrent Executions
- Memory Usage
- Log Events

---

# CloudWatch Metrics

AWS Lambda automatically publishes metrics such as:

- Invocations
- Errors
- Duration
- Throttles
- Concurrent Executions
- Iterator Age (if applicable)

These metrics help monitor application performance over time.

---

# Security

CloudWatch logs are protected using IAM permissions.

Only authorized users and AWS services can access or manage log groups.

The Lambda execution role uses the following managed policy:

```
AWSLambdaBasicExecutionRole
```

This policy allows Lambda to:

- Create Log Groups
- Create Log Streams
- Write Log Events

---

# IAM Permissions Required

Example IAM Policy

```json
{
  "Effect": "Allow",
  "Action": [
    "logs:CreateLogGroup",
    "logs:CreateLogStream",
    "logs:PutLogEvents"
  ],
  "Resource": "*"
}
```

---

# AWS Services Integrated

Amazon CloudWatch integrates with:

- AWS Lambda
- Amazon S3
- Amazon DynamoDB
- Amazon SNS
- AWS IAM

---

# Benefits of Amazon CloudWatch

- Fully Managed Monitoring
- Centralized Logging
- Real-Time Metrics
- Error Tracking
- Performance Monitoring
- Automatic Log Collection
- Easy Troubleshooting
- Operational Visibility
- Seamless AWS Integration

---

# Project Outcome

Amazon CloudWatch successfully captured all Lambda execution logs, enabling monitoring and troubleshooting throughout the Serverless Event Processing Pipeline.

It provided detailed visibility into application behavior, helping identify and resolve runtime issues during development and testing.

---

# Key Learning Outcomes

- Configured CloudWatch logging for AWS Lambda.
- Monitored Lambda executions.
- Analyzed execution logs.
- Identified runtime errors.
- Debugged AWS service integrations.
- Understood Log Groups and Log Streams.
- Monitored Lambda performance metrics.
- Implemented production-grade observability.

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
         Execution Logs
                   │
                   ▼
        Amazon CloudWatch
         (Logs & Monitoring)
```

---

# Real-World Use Cases

Amazon CloudWatch is widely used for:

- Application Monitoring
- Infrastructure Monitoring
- Serverless Observability
- Performance Analysis
- Security Monitoring
- Incident Investigation
- CI/CD Monitoring
- Automated Alerting
- DevOps Operations
- Cloud Resource Monitoring

---

# Interview Questions

### Why did you use Amazon CloudWatch?

Amazon CloudWatch provides centralized logging and monitoring for AWS resources. It was used to monitor Lambda execution, troubleshoot errors, and verify successful processing of uploaded files.

---

### What is the difference between a Log Group and a Log Stream?

- **Log Group:** A collection of logs for a specific AWS resource (for example, `/aws/lambda/ServerlessEventProcessor`).
- **Log Stream:** A sequence of log events generated by a single execution environment within a log group.

---

### Which IAM policy allows Lambda to write logs?

The **AWSLambdaBasicExecutionRole** managed policy grants permissions to create log groups, create log streams, and write log events.

---

### How did CloudWatch help during this project?

CloudWatch helped identify and resolve issues such as S3 `HeadObject` errors, Lambda runtime exceptions, IAM permission problems, and SNS notification failures by providing detailed execution logs.

---

# Conclusion

Amazon CloudWatch is the monitoring and observability component of this Serverless Event Processing Pipeline. It automatically captures AWS Lambda execution logs, runtime metrics, and error details, enabling efficient monitoring, debugging, and performance analysis. By integrating CloudWatch with Lambda and other AWS services, the project demonstrates production-ready logging, operational visibility, and best practices for serverless application monitoring.
