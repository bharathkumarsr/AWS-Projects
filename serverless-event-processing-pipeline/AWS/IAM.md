# AWS Identity and Access Management (IAM)

## Overview

AWS Identity and Access Management (IAM) is a security service that enables secure access control to AWS resources. IAM allows administrators to define who can access AWS services and what actions they are permitted to perform using users, groups, roles, and policies.

In this project, IAM is used to securely grant the AWS Lambda function permission to interact with Amazon S3, DynamoDB, Amazon SNS, and Amazon CloudWatch without exposing AWS credentials.

---

# Purpose in This Project

IAM is responsible for:

- Providing secure access to AWS resources.
- Granting AWS Lambda the required permissions.
- Following the Principle of Least Privilege.
- Eliminating the need to hardcode AWS credentials.
- Securing communication between AWS services.

---

# IAM Service Used

- AWS IAM

---

# IAM Role Created

| Property | Value |
|----------|-------|
| Role Name | ServerlessPipelineLambdaRole |
| Trusted Entity | AWS Lambda |
| Role Type | Service Role |

---

# Why IAM Role Was Used

AWS Lambda cannot access other AWS services by default.

To perform operations such as:

- Reading files from Amazon S3
- Writing metadata into DynamoDB
- Publishing notifications to Amazon SNS
- Writing execution logs into CloudWatch

Lambda must assume an IAM Role that explicitly grants these permissions.

---

# Attached IAM Policies

The following AWS Managed Policies were attached to the Lambda execution role.

| Policy | Purpose |
|---------|---------|
| AWSLambdaBasicExecutionRole | Allows Lambda to create and write CloudWatch logs |
| AmazonS3ReadOnlyAccess | Allows Lambda to read uploaded objects from S3 |
| AmazonDynamoDBFullAccess | Allows Lambda to insert metadata into DynamoDB |
| AmazonSNSFullAccess | Allows Lambda to publish notifications to SNS |

---

# Trust Relationship

The IAM role trusts the Lambda service.

Example Trust Policy

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

This trust relationship allows AWS Lambda to assume the execution role during function execution.

---

# Permissions Granted

## Amazon S3

Purpose

- Read uploaded files
- Retrieve object metadata

Actions

- s3:GetObject
- s3:HeadObject

---

## Amazon DynamoDB

Purpose

- Store processed file metadata

Actions

- dynamodb:PutItem
- dynamodb:GetItem
- dynamodb:UpdateItem

---

## Amazon SNS

Purpose

- Publish email notifications

Action

- sns:Publish

---

## Amazon CloudWatch

Purpose

- Store Lambda execution logs

Actions

- logs:CreateLogGroup
- logs:CreateLogStream
- logs:PutLogEvents

---

# IAM Workflow

```text
AWS Lambda Starts
        │
        ▼
Assumes IAM Role
        │
        ▼
Receives Temporary Credentials
        │
        ▼
Access Amazon S3
        │
        ▼
Write to DynamoDB
        │
        ▼
Publish to SNS
        │
        ▼
Write Logs to CloudWatch
```

---

# Authentication Flow

```text
AWS Lambda
      │
      ▼
Assume IAM Role
      │
      ▼
Temporary Security Credentials
      │
 ┌────┼───────────────┐
 ▼    ▼               ▼
S3 DynamoDB        SNS
      │
      ▼
CloudWatch
```

---

# Security Best Practices Followed

- No AWS Access Keys stored in the Lambda code.
- Used IAM Role instead of IAM User credentials.
- Lambda automatically receives temporary credentials.
- Enabled least-privilege access using IAM policies.
- CloudWatch logging enabled for auditing.
- S3 bucket kept private using IAM permissions.

---

# Benefits of Using IAM Roles

- Improved Security
- Temporary Credentials
- No Hardcoded Secrets
- Centralized Access Management
- Fine-Grained Permissions
- Automatic Credential Rotation
- Easy Integration with AWS Services
- Supports Least Privilege Principle

---

# AWS Services Integrated

- AWS Lambda
- Amazon S3
- Amazon DynamoDB
- Amazon SNS
- Amazon CloudWatch

---

# Project Outcome

The IAM execution role securely enabled the Lambda function to access all required AWS services without embedding AWS credentials in the application code.

This ensured secure, scalable, and production-ready communication between AWS services while following AWS security best practices.

---

# Key Learning Outcomes

- Created an IAM Role for AWS Lambda.
- Configured a trust relationship with the Lambda service.
- Attached AWS Managed Policies.
- Understood IAM Roles vs IAM Users.
- Implemented secure authentication using temporary credentials.
- Granted permissions to access Amazon S3, DynamoDB, SNS, and CloudWatch.
- Applied the Principle of Least Privilege.
- Built a secure serverless architecture.

---

# Architecture

```text
               AWS Lambda
                    │
         Assume IAM Execution Role
                    │
                    ▼
      Temporary Security Credentials
                    │
      ┌─────────────┼──────────────┐
      ▼             ▼              ▼
 Amazon S3     DynamoDB       Amazon SNS
                    │
                    ▼
             Amazon CloudWatch
```

---

# Real-World Use Cases

AWS IAM Roles are widely used for:

- Serverless Applications
- EC2 Instance Profiles
- ECS Task Roles
- EKS IAM Roles for Service Accounts (IRSA)
- Cross-Account AWS Access
- CI/CD Pipelines
- Cloud Automation
- Secure API Integrations
- AWS Security and Governance

---

# Interview Questions

### Why did you use an IAM Role instead of storing AWS credentials in Lambda?

IAM Roles provide temporary security credentials automatically, eliminating the need to hardcode AWS Access Keys and improving security.

---

### Why is AWSLambdaBasicExecutionRole required?

It allows the Lambda function to create log groups, log streams, and write logs to Amazon CloudWatch for monitoring and troubleshooting.

---

### What is the Principle of Least Privilege?

It is the security practice of granting only the minimum permissions required for a service or user to perform its tasks.

---

# Conclusion

AWS Identity and Access Management (IAM) is the security foundation of this Serverless Event Processing Pipeline. By using an IAM execution role, the Lambda function securely accessed Amazon S3, DynamoDB, Amazon SNS, and CloudWatch without storing AWS credentials. This approach follows AWS security best practices and demonstrates secure access management in a production-ready serverless application.
