# Jenkins Server Deployment

## Project Objective

Provision a dedicated Jenkins server to automate Continuous Integration and Continuous Deployment (CI/CD) for the production environment.

---

## Architecture Role

```
Developer
    │
    ▼
GitHub Repository
    │
    ▼
Jenkins Server
    │
    ▼
Docker Build
    │
    ▼
Application EC2 Instances
    │
    ▼
Application Load Balancer
```

---

## EC2 Configuration

| Parameter | Value |
|-----------|-------|
| Instance Name | prod-jenkins-server |
| Operating System | Red Hat Enterprise Linux |
| Instance Type | t3.flex.large |
| Storage | 20 GB GP3 |
| IAM Role | prod-ec2-role |
| Network | Production VPC |
| Subnet | Public Subnet |
| Public IP | Enabled |

---

## Security Group

### Inbound Rules

| Type | Port | Source |
|------|------|--------|
| SSH | 22 | My IP |
| Custom TCP | 8080 | My IP |

### Outbound Rules

| Type | Destination |
|------|-------------|
| All Traffic | 0.0.0.0/0 |

---

## Purpose

The Jenkins server is responsible for:

- Continuous Integration (CI)
- Continuous Deployment (CD)
- Docker image build automation
- GitHub integration using Webhooks
- Automated application deployment
- Pipeline execution
- Build monitoring

---

## Security Best Practices

- Dedicated Jenkins server
- Restricted SSH access
- Jenkins UI accessible only from My IP
- IAM Role attached to the EC2 instance
- IMDSv2 enabled for enhanced instance metadata security

---

## AWS Services Used

- Amazon EC2
- IAM
- Security Groups
- Amazon VPC
- CloudWatch
- SNS
- Application Load Balancer
- Auto Scaling Group

---

## Future Enhancements

- SSL using ACM
- Reverse Proxy with Nginx
- Route 53 DNS
- AWS WAF
- Docker Hub Integration
- SonarQube
- Trivy Security Scan
- ArgoCD
- Kubernetes Deployment

---

## Outcome

Successfully provisioned a dedicated Jenkins server using Red Hat Enterprise Linux on an Amazon EC2 t3.flex.large instance to support CI/CD automation in a production-style AWS environment.
