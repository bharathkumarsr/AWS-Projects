# AWS Lambda

## Overview

AWS Lambda is a fully managed serverless compute service that allows developers to run code without provisioning or managing servers. Lambda automatically executes code in response to AWS events, scales automatically based on workload, and charges only for the compute time consumed.

In this project, AWS Lambda serves as the core processing engine. It is automatically triggered whenever a new file is uploaded to the Amazon S3 bucket. The Lambda function extracts file metadata, stores it in Amazon DynamoDB, sends an email notification through Amazon SNS, and records execution logs in Amazon CloudWatch.

---

# Purpose in This Project

AWS Lambda is responsible for:

- Processing uploaded files automatically.
- Reading file metadata from Amazon S3.
- Storing metadata in Amazon DynamoDB.
- Publishing email notifications through Amazon SNS.
- Writing execution logs to Amazon CloudWatch.
- Enabling a fully automated serverless workflow.

---

# Lambda Function Details

| Property | Value |
|----------|-------|
| Function Name | ServerlessEventProcessor |
| Runtime | Python 3.x |
| Architecture | x86_64 |
| Invocation Type | Amazon S3 Event Notification |
| Execution Role | ServerlessPipelineLambdaRole |

---

# Why AWS Lambda Was Used

Instead of running a continuously active EC2 instance, AWS Lambda provides an event-driven and serverless approach.

Benefits include:

- No server management
- Automatic scaling
- Pay-per-use pricing
- High availability
- Native integration with AWS services
- Faster development and deployment

---

# Event Source

Amazon S3

Event Type

```
ObjectCreated
```

Whenever a new object is uploaded into the S3 bucket, Amazon S3 automatically invokes the Lambda function.

---

# Environment Variables

To avoid hardcoding resource names, Lambda uses environment variables.

| Variable | Value |
|----------|-------|
| TABLE_NAME | FileMetadata |
| SNS_TOPIC_ARN | Amazon SNS Topic ARN |

This approach improves maintainability and allows configuration changes without modifying the application code.

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
 ┌──────────────┼───────────────┐
 ▼              ▼               ▼
Read S3     Store Metadata    Publish SNS
Metadata    in DynamoDB       Notification
        │
        ▼
CloudWatch Logs
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

The Lambda function is automatically invoked.

---

### Step 4

Lambda retrieves:

- Bucket Name
- File Name
- File Size
- Content Type
- ETag

using the Amazon S3 API.

---

### Step 5

The extracted metadata is stored in the DynamoDB table.

---

### Step 6

Lambda publishes a success notification to Amazon SNS.

---

### Step 7

Amazon SNS sends an email notification to the subscribed user.

---

### Step 8

CloudWatch stores execution logs for monitoring and troubleshooting.

---

# Lambda Processing Flow

```text
Lambda Invoked
      │
      ▼
Read S3 Event
      │
      ▼
Retrieve Object Metadata
      │
      ▼
Store Metadata in DynamoDB
      │
      ▼
Publish SNS Notification
      │
      ▼
Write CloudWatch Logs
      │
      ▼
Return Success
```

---

# AWS Services Integrated

AWS Lambda integrates with:

- Amazon S3
- Amazon DynamoDB
- Amazon SNS
- Amazon CloudWatch
- AWS IAM

---

# IAM Role Used

Lambda uses the following execution role:

```
ServerlessPipelineLambdaRole
```

The IAM role provides secure permissions to:

- Read objects from Amazon S3
- Write items into DynamoDB
- Publish messages to SNS
- Write logs to CloudWatch

---

# Python SDK Used

AWS SDK for Python (Boto3)

Services initialized:

```python
import boto3

s3 = boto3.client("s3")
dynamodb = boto3.resource("dynamodb")
sns = boto3.client("sns")
```

---

# Metadata Stored

For every uploaded file, Lambda stores:

- File Name
- Bucket Name
- File Size
- Content Type
- ETag
- Upload Time
- Processing Status

---

# Logging

Lambda writes execution logs to Amazon CloudWatch.

Example Logs

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

# Error Handling

The Lambda function includes structured exception handling.

Features include:

- Try/Catch blocks
- CloudWatch error logging
- Stack trace generation
- Graceful failure response

This improves troubleshooting and operational reliability.

---

# Security Best Practices

- IAM Role used instead of AWS Access Keys
- Environment Variables used for configuration
- No hardcoded credentials
- Least Privilege permissions
- Private S3 bucket access
- CloudWatch logging enabled

---

# Benefits of AWS Lambda

- Fully Managed Service
- Serverless Architecture
- Automatic Scaling
- High Availability
- Event-Driven Processing
- Pay Only for Execution Time
- Easy AWS Integration
- No Infrastructure Management

---

# Project Outcome

AWS Lambda successfully automated the processing of uploaded files by extracting metadata, storing information in DynamoDB, sending notifications through Amazon SNS, and generating execution logs in CloudWatch.

This eliminated manual intervention and enabled a scalable event-driven workflow.

---

# Key Learning Outcomes

- Created an AWS Lambda function.
- Configured Lambda with Python runtime.
- Integrated Lambda with Amazon S3.
- Used environment variables.
- Accessed AWS services using Boto3.
- Stored metadata in DynamoDB.
- Published notifications to SNS.
- Implemented CloudWatch logging.
- Configured IAM execution roles.
- Built a production-ready serverless application.

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
       ┌─────────────┼──────────────┐
       ▼             ▼              ▼
 Amazon S3     Amazon DynamoDB   Amazon SNS
(Read Data)   (Store Metadata) (Send Email)
                     │
                     ▼
             Amazon CloudWatch
```

---

# Real-World Use Cases

AWS Lambda is widely used for:

- Serverless Applications
- File Processing
- Image Processing
- Event-Driven Architectures
- Data Transformation
- Log Processing
- CI/CD Automation
- Security Automation
- API Backends
- Scheduled Jobs

---

# Interview Questions

### Why did you choose AWS Lambda instead of Amazon EC2?

AWS Lambda eliminates server management, automatically scales based on workload, integrates natively with AWS services, and follows a pay-per-use pricing model, making it ideal for event-driven applications.

---

### Why use Environment Variables?

Environment variables allow configuration values such as table names and SNS topic ARNs to be managed outside the code, improving flexibility, security, and maintainability.

---

### What triggers the Lambda function?

Amazon S3 ObjectCreated event notifications automatically invoke the Lambda function whenever a new file is uploaded.

---

### Why is CloudWatch important?

Amazon CloudWatch captures execution logs, metrics, and errors, enabling monitoring, debugging, and operational visibility.

---

# Conclusion

AWS Lambda is the central processing component of this Serverless Event Processing Pipeline. It automatically responds to Amazon S3 upload events, retrieves file metadata, stores the information in Amazon DynamoDB, sends notifications using Amazon SNS, and records execution logs in Amazon CloudWatch. By leveraging serverless computing, the project demonstrates an automated, scalable, secure, and production-ready event-driven architecture following AWS best practices.
