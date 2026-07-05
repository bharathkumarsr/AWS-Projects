# Amazon EventBridge Scheduler
## Purpose

Automates IAM compliance execution.

### Schedule Name:

IAM-Daily-Audit

### Schedule Type:

Rate Based

### Configuration:

rate(1 day)

### Target:

IAM-Audit Lambda Function

## Why Used:

* Fully automated execution
* No manual intervention
* Continuous compliance monitoring

```
Workflow:

Every 24 Hours
        ↓
EventBridge
        ↓
Lambda
        ↓
IAM Audit
        ↓
SNS Alerts
        ↓
S3 Report
        ↓
CloudWatch Logs
```
