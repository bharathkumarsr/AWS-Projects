# AWS Identity and Access Management (IAM)

## Overview

AWS Identity and Access Management (IAM) is the primary service used in this project to audit and secure AWS identities, permissions, and access controls.

The purpose of this project is to automate IAM security auditing and identify potential security risks and compliance violations.

---

## Why IAM Was Used

AWS IAM allows organizations to:

* Create and manage AWS users
* Create IAM roles
* Assign permissions
* Implement least privilege access
* Enforce security policies
* Enable Multi-Factor Authentication (MFA)

This project uses IAM to automatically validate security posture and compliance.

---

## What Was Implemented

The following IAM components were audited:

### IAM Users

* User enumeration
* MFA validation
* Console access verification
* Access key auditing

### IAM Roles

* Role inventory
* Unused role identification
* Permission validation

### IAM Policies

* Attached policy analysis
* Administrative access detection
* Wildcard permission detection

### Account Security

* Password policy validation
* Root account security checks

---

## Technical Implementation

Python Boto3 APIs used:

```python
iam.list_users()
iam.list_roles()
iam.list_access_keys()
iam.list_mfa_devices()
iam.get_account_password_policy()
iam.list_attached_user_policies()
```

---

## Security Checks

* Users without MFA
* Users with AdministratorAccess
* Access keys older than 90 days
* Password policy violations
* Unused IAM users
* Unused IAM roles
* Root account activity

---

## Outcome

AWS IAM auditing was fully automated to improve security visibility and compliance monitoring.
