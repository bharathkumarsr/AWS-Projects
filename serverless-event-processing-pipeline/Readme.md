# 🚀 Serverless Event Processing Pipeline on AWS

> A fully automated, event-driven serverless application built using AWS services to process uploaded files, store metadata, send email notifications, and monitor execution logs without managing any servers.

![AWS](https://img.shields.io/badge/AWS-Serverless-orange)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Lambda](https://img.shields.io/badge/AWS-Lambda-yellow)
![DynamoDB](https://img.shields.io/badge/Database-DynamoDB-blue)
![SNS](https://img.shields.io/badge/Notification-SNS-green)
![CloudWatch](https://img.shields.io/badge/Monitoring-CloudWatch-red)

---

# 📖 Project Overview

Modern cloud applications require scalable and automated event processing without provisioning or managing infrastructure. AWS provides a serverless ecosystem that enables applications to respond to events automatically while minimizing operational overhead.

This project demonstrates how to build a **fully automated serverless event-driven architecture** using AWS managed services. Whenever a user uploads a file into an Amazon S3 bucket, the application automatically processes the upload, extracts file metadata, stores it in DynamoDB, sends an email notification via Amazon SNS, and records execution logs in Amazon CloudWatch.

The entire workflow operates without any manual intervention or server management.

---

# 🎯 Project Objectives

- Build a fully serverless application.
- Learn AWS event-driven architecture.
- Automate file processing.
- Store file metadata.
- Implement real-time notifications.
- Monitor application execution.
- Follow AWS security best practices.
- Eliminate infrastructure management.

---

# 🏗️ Architecture

```text
                     Upload File
                          │
                          ▼
                  Amazon S3 Bucket
                          │
          ObjectCreated Event Notification
                          │
                          ▼
                AWS Lambda Function
                          │
        ┌─────────────────┼──────────────────┐
        ▼                 ▼                  ▼
 Amazon S3         Amazon DynamoDB      Amazon SNS
(Read Metadata)    (Store Metadata)    (Email Alert)
                          │
                          ▼
                 Amazon CloudWatch
                (Logs & Monitoring)
```

---

# 🔄 Project Workflow

### Step 1

A user uploads a file into the Amazon S3 bucket.

↓

### Step 2

Amazon S3 generates an **ObjectCreated Event**.

↓

### Step 3

AWS Lambda is automatically invoked.

↓

### Step 4

Lambda retrieves:

- Bucket Name
- File Name
- File Size
- Content Type
- ETag

↓

### Step 5

Lambda stores the metadata inside Amazon DynamoDB.

↓

### Step 6

Lambda publishes a notification to Amazon SNS.

↓

### Step 7

Amazon SNS sends an email notification.

↓

### Step 8

CloudWatch records execution logs for monitoring and troubleshooting.

---

# 💡 Why This Project?

Traditional applications require continuously running servers that increase operational costs and maintenance efforts.

Using a serverless architecture provides:

- Automatic Scaling
- Reduced Infrastructure Management
- Lower Operational Cost
- Event-Driven Automation
- High Availability
- Better Security
- Faster Development

This project demonstrates real-world cloud-native application design following AWS best practices.

---

# ⭐ Key Features

- Fully Serverless Architecture
- Automatic File Processing
- Event-Driven Workflow
- Metadata Extraction
- Email Notifications
- Real-Time Monitoring
- Secure IAM Role-Based Access
- CloudWatch Logging
- Highly Scalable Design
- Production-Ready Implementation

---

# ☁️ AWS Services Used

| AWS Service | Purpose |
|-------------|----------|
| Amazon S3 | Stores uploaded files and triggers events |
| AWS Lambda | Processes uploaded files automatically |
| Amazon DynamoDB | Stores file metadata |
| Amazon SNS | Sends email notifications |
| Amazon CloudWatch | Captures execution logs and monitoring metrics |
| AWS IAM | Provides secure permissions between AWS services |

---

# 🛠️ Technology Stack

## Cloud Platform

- Amazon Web Services (AWS)

## Programming Language

- Python 3.x

## AWS SDK

- Boto3

## Database

- Amazon DynamoDB

## Storage

- Amazon S3

## Monitoring

- Amazon CloudWatch

## Notification Service

- Amazon SNS

## Identity & Security

- AWS IAM

---

# 📂 Project Structure

```
serverless-event-processing-pipeline/

│
├── lambda/
│     └── lambda_function.py
│
├── docs/
│     ├── README.md
│     ├── S3.md
│     ├── Lambda.md
│     ├── DynamoDB.md
│     ├── SNS.md
│     ├── IAM.md
│     └── CloudWatch.md
│
├── architecture/
│     ├── architecture.drawio
│     └── architecture.png
│
├── screenshots/
│     ├── s3-bucket.png
│     ├── lambda.png
│     ├── dynamodb.png
│     ├── sns.png
│     ├── cloudwatch.png
│     └── email-notification.png
│
└── README.md
```

---

# 🔒 Security Best Practices

- IAM Role-Based Authentication
- No Hardcoded AWS Credentials
- Least Privilege Principle
- Private Amazon S3 Bucket
- Environment Variables for Configuration
- CloudWatch Logging Enabled
- Secure AWS Service Integration

---

# 📊 Metadata Stored

For every uploaded file, the application stores:

- File Name
- Bucket Name
- File Size
- Content Type
- ETag
- Upload Time
- Processing Status

Example:

```json
{
  "FileName": "employee-list.csv",
  "Bucket": "bharath-serverless-pipeline-luffy",
  "FileSize": "1024",
  "ContentType": "text/csv",
  "ETag": "a1b2c3d4e5",
  "UploadTime": "2026-07-06 15:45:10 UTC",
  "Status": "Processed"
}
```

---

# 📧 Email Notification

After successful processing, Amazon SNS sends an email containing:

- Bucket Name
- File Name
- File Size
- Upload Time
- Processing Status

This enables real-time visibility into application activity.

---

# 📈 Monitoring

Amazon CloudWatch automatically records:

- Lambda Invocations
- Execution Duration
- Error Logs
- Memory Usage
- Runtime Information
- Debug Logs

This allows efficient monitoring and troubleshooting.

---

# 🚀 Benefits of This Architecture

- No Server Management
- Automatic Scaling
- Event-Driven Processing
- Highly Available
- Cost Efficient
- Secure by Design
- Production Ready
- Easy AWS Integration

---

# 🌍 Real-World Use Cases

- File Processing Systems
- Image Processing Pipelines
- Invoice Processing
- Audit Logging
- Document Management Systems
- Security Event Processing
- Data Ingestion Pipelines
- Serverless Applications
- Cloud Automation
- Enterprise Workflows

---

# 🎓 Skills Demonstrated

- AWS Serverless Architecture
- Amazon S3
- AWS Lambda
- Amazon DynamoDB
- Amazon SNS
- Amazon CloudWatch
- AWS IAM
- Python (Boto3)
- Event-Driven Design
- Cloud Security
- Monitoring & Logging
- Serverless Application Development
- AWS Integration
- Production Troubleshooting

---

# 🧠 Key Learnings

Through this project, I gained hands-on experience in:

- Designing event-driven architectures.
- Building serverless applications.
- Configuring Amazon S3 Event Notifications.
- Developing AWS Lambda functions using Python.
- Working with Amazon DynamoDB.
- Sending notifications through Amazon SNS.
- Monitoring applications using CloudWatch.
- Implementing secure IAM roles and permissions.
- Debugging production issues using CloudWatch Logs.
- Integrating multiple AWS managed services.

---

# 🔮 Future Enhancements

- Enable S3 Versioning.
- Add AWS Step Functions for orchestration.
- Archive metadata to Amazon S3.
- Generate processing reports.
- Integrate Amazon EventBridge.
- Implement Dead Letter Queue (DLQ).
- Add CloudWatch Alarms.
- Deploy using AWS CloudFormation or Terraform.
- Add CI/CD pipeline using GitHub Actions.
- Implement API Gateway for querying metadata.

---

# 📚 Documentation

Detailed documentation for each AWS service is available in the repository:

- 📄 S3.md
- 📄 Lambda.md
- 📄 DynamoDB.md
- 📄 SNS.md
- 📄 IAM.md
- 📄 CloudWatch.md

---

# 👨‍💻 Author

**Bharath Kumar S R**

Cloud | DevOps | AWS | Python | Kubernetes | Docker | Terraform | CI/CD

---

# ⭐ If you found this project useful

Please consider giving this repository a **Star ⭐**.
