# Automated AWS IAM Audit & Compliance Architecture

## Architecture Diagram

```text
                 Amazon EventBridge
                          |
                          v
                    AWS Lambda
                          |
                ------------------
                |        |       |
                v        v       v
             AWS IAM    S3      SNS
                          |
                          v
                    CloudWatch
```

---

## Workflow

1. EventBridge triggers Lambda.
2. Lambda performs IAM security auditing.
3. IAM users, roles, and policies are analyzed.
4. Compliance reports are generated.
5. Reports are uploaded to S3.
6. Security alerts are sent through SNS.
7. Logs are stored in CloudWatch.

---

## Technology Stack

* AWS IAM
* AWS Lambda
* Amazon S3
* Amazon SNS
* Amazon EventBridge
* Amazon CloudWatch
* Python
* Boto3

---

## Security Controls

* MFA validation
* Password policy checks
* Access key rotation
* Administrator access detection
* Root account monitoring
* Least privilege enforcement

---

## Project Benefits

* Automated compliance monitoring
* Reduced manual auditing effort
* Improved cloud security posture
* Real-time security alerting
* Enterprise-grade IAM governance
