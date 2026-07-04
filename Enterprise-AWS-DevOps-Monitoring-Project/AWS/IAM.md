# IAM Configuration

## Objective

To implement secure access control using AWS IAM Roles and Policies
without storing AWS access keys inside EC2 instances.

---

## Resources Created

| Resource | Name |
|----------|------|
| IAM Role | EC2-S3-Role |
| Service | EC2 |
| Policy | AmazonS3FullAccess |

---

## Configuration Steps

### Created IAM Role

Role Name:

```text
EC2-S3-Role
```

Trusted Entity:

```json
{
  "Service": "ec2.amazonaws.com"
}
```

Attached Policy:

```text
AmazonS3FullAccess
```

---

## Why IAM Role?

Instead of storing AWS credentials on the server:

❌ Access Keys

We used:

✅ IAM Roles

Benefits:

- Temporary credentials
- Secure authentication
- Principle of least privilege
- Automatic credential rotation

---

## Validation

Executed:

```bash
aws sts get-caller-identity
```

Output confirmed EC2 instance assumed role successfully.

---

## Key Learning

IAM Roles provide secure authentication between AWS services without
requiring hardcoded credentials.
