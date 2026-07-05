# File: IAM.md

# AWS IAM (Identity and Access Management)

## Service Purpose

AWS IAM is used to securely manage identities, authentication, authorization, and permissions within an AWS account.

In this project, IAM serves two purposes:

1. The target of the security audit.
2. The authorization layer that enables Lambda to perform IAM compliance checks.

---

# Why IAM Was Used

The goal of this project is to automate IAM security compliance validation.

The Lambda function audits:

* IAM users
* MFA status
* AdministratorAccess privileges
* Access key age
* Password policy compliance

This helps identify security risks such as:

* Users without MFA
* Excessive privileges
* Long-lived credentials
* Non-compliant access controls

---

# IAM Users Created

## developer-test

Purpose:

* Test user for MFA compliance validation.

Configuration:

* MFA: Disabled
* AdministratorAccess: No
* Access Keys: Not configured

---

## admin-test

Purpose:

* Test user for privilege escalation detection.

Configuration:

* MFA: Disabled
* AdministratorAccess: Enabled
* Access Keys: Configured

---

# IAM Execution Role

Role Name:

```text
Lambda-IAM-Audit-Role
```

Trusted Entity:

```json
{
  "Version":"2012-10-17",
  "Statement":[
    {
      "Effect":"Allow",
      "Principal":{
        "Service":"lambda.amazonaws.com"
      },
      "Action":"sts:AssumeRole"
    }
  ]
}
```

---

# Attached Policies

## AWS Managed Policy

```text
AWSLambdaBasicExecutionRole
```

Purpose:

Allows Lambda to:

* Create CloudWatch Log Groups
* Create CloudWatch Log Streams
* Write CloudWatch Logs

---

## Custom Policy

Policy Name:

```text
IAM-Audit-Lambda-Policy
```

Policy JSON:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "IAMAuditPermissions",
            "Effect": "Allow",
            "Action": [
                "iam:ListUsers",
                "iam:ListRoles",
                "iam:ListMFADevices",
                "iam:ListAccessKeys",
                "iam:GetAccountPasswordPolicy",
                "iam:ListAttachedUserPolicies",
                "iam:GetUser"
            ],
            "Resource": "*"
        },
        {
            "Sid": "S3Permissions",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:GetObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::iam-audit-reports-bharath-796231892525-ap-south-1-an",
                "arn:aws:s3:::iam-audit-reports-bharath-796231892525-ap-south-1-an/*"
            ]
        },
        {
            "Sid": "SNSPermissions",
            "Effect": "Allow",
            "Action": [
                "sns:Publish"
            ],
            "Resource": "*"
        },
        {
            "Sid": "CloudWatchPermissions",
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "*"
        }
    ]
}
```

---

# Security Principle Used

This project follows the:

```text
Principle of Least Privilege (PoLP)
```

The Lambda function only receives permissions required for:

* IAM auditing
* S3 uploads
* SNS notifications
* CloudWatch logging

AdministratorAccess was intentionally avoided.

---

# IAM Compliance Checks Implemented

## MFA Validation

API Used:

```python
iam.list_mfa_devices()
```

Validation:

```text
MFA Enabled ?
    YES -> Compliant
    NO  -> Generate SNS Alert
```

---

## AdministratorAccess Detection

API Used:

```python
iam.list_attached_user_policies()
```

Validation:

```text
AdministratorAccess attached ?
    YES -> Critical Alert
    NO  -> Compliant
```

---

## Access Key Audit

API Used:

```python
iam.list_access_keys()
```

Validation:

```text
Access Key Age > 90 Days ?
    YES -> Compliance Alert
    NO  -> Compliant
```
