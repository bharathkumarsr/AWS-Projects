## Amazon CloudWatch
### Purpose

Stores execution logs and audit trails.

## Why Used:

* Monitoring
* Troubleshooting
* Compliance evidence
* Operational visibility

#### Log Group:

/aws/lambda/IAM-Audit

## Permissions:

```
    "Effect":"Allow",
    "Action":[
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
    ],
    "Resource":"*"
```
