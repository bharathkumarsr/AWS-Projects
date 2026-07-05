# File: Lambda.md

# AWS Lambda

## Service Purpose

AWS Lambda provides serverless compute that executes code without managing infrastructure.

---

# Why Lambda Was Used

Advantages:

* Serverless architecture
* Event-driven execution
* Automatic scaling
* Zero server maintenance
* Native AWS integration
* Cost optimization

---

# Lambda Configuration

Function Name:

```text
IAM-Audit
```

Runtime:

```text
Python 3.x
```

Architecture:

```text
x86_64
```

Memory:

```text
256 MB
```

Timeout:

```text
60 Seconds
```

Execution Role:

```text
Lambda-IAM-Audit-Role
```

---

# Python Libraries Used

```python
import boto3
import csv
import io
from datetime import datetime, timezone
```

Purpose:

* boto3 → AWS SDK
* csv → CSV report generation
* io → In-memory file handling
* datetime → Access key age calculation

---

# AWS SDK Clients

```python
iam = boto3.client('iam')
s3 = boto3.client('s3')
sns = boto3.client('sns')
```

---

# Lambda Workflow

Step 1:
Retrieve IAM users

```python
iam.list_users()
```

Step 2:
Validate MFA

```python
iam.list_mfa_devices()
```

Step 3:
Detect AdministratorAccess

```python
iam.list_attached_user_policies()
```

Step 4:
Audit access keys

```python
iam.list_access_keys()
```

Step 5:
Send SNS alerts

```python
sns.publish()
```

Step 6:
Generate CSV report

```python
csv.DictWriter()
```

Step 7:
Upload report to S3

```python
s3.put_object()
```

Step 8:
Store execution logs

```python
print()
```

---

# Lambda Output

Generated Report:

```csv
User,MFA Enabled,Admin Access,Access Key Age
developer-test,NO,NO,N/A
admin-test,NO,YES,0
```

---

# Security Alerts Generated

## MFA Alert

Severity:

```text
HIGH
```

## Administrator Access Alert

Severity:

```text
CRITICAL
```

## Access Key Alert

Severity:

```text
HIGH
```
