# 🚀 AWS Highly Available DevOps Infrastructure

## 📌 Project Overview

This project demonstrates a production-inspired AWS infrastructure built using core AWS services and DevOps tools. The objective was to deploy a highly available, scalable, secure, and monitored web application environment.

The application is deployed on Docker containers running Nginx across multiple EC2 instances behind an Application Load Balancer. Auto Scaling ensures high availability, Jenkins is used for CI/CD automation, and Amazon CloudWatch monitors the infrastructure.

---

# 🏗 Architecture

(Insert Architecture Diagram Here)

---

# 📋 Project Workflow

```
User
   │
   ▼
Application Load Balancer
   │
   ▼
Target Group
   │
   ▼
Auto Scaling Group
   │
   ▼
EC2 Instances
   │
Docker Container
   │
Nginx Web Server
   │
HTML Application
```

Jenkins is responsible for deploying application updates to the EC2 instances, while CloudWatch continuously monitors the infrastructure.

---

# ☁ AWS Services Used

## 1. Amazon VPC

### Why Used

To create an isolated and secure network for the entire infrastructure.

### How it Works

All AWS resources are deployed inside a custom VPC, allowing complete control over networking, routing, and security.

---

## 2. Public Subnets

### Why Used

To host resources that require internet connectivity.

### Resources

- Bastion Host
- Jenkins Server
- Application Load Balancer

---

## 3. Private Subnets

### Why Used

To improve security by isolating application servers from direct internet access.

### Resources

- EC2 Application Servers

---

## 4. Internet Gateway

### Why Used

Allows resources in public subnets to communicate with the internet.

### Project Usage

- Access Jenkins UI
- Access Application Load Balancer
- Download Docker images
- Install software packages

---

## 5. Route Tables

### Why Used

Controls how network traffic flows inside the VPC.

### Project Usage

Routes internet traffic from public subnets through the Internet Gateway.

---

## 6. Security Groups

### Why Used

Acts as a virtual firewall for AWS resources.

### Project Usage

Application Server

- HTTP from ALB only
- SSH only from Bastion Host

Jenkins Server

- Port 8080
- SSH access

Application Load Balancer

- HTTP from Internet

Bastion Host

- SSH only from trusted IP

---

## 7. Bastion Host

### Why Used

Provides secure administrative access to private resources.

### Project Usage

Administrators connect to the Bastion Host before accessing private EC2 instances.

---

## 8. EC2 Instances

### Why Used

Hosts the application.

### Project Usage

Amazon Linux instances run Docker containers hosting the Nginx application.

---

## 9. Docker

### Why Used

Containerizes the application.

### Benefits

- Faster deployment
- Portability
- Easy application updates
- Consistent runtime environment

---

## 10. Nginx

### Why Used

Acts as the web server.

### Project Usage

Serves the HTML application running inside Docker containers.

---

## 11. Application Load Balancer (ALB)

### Why Used

Distributes incoming requests across multiple application servers.

### Benefits

- High Availability
- Load Distribution
- Health Checks
- Fault Tolerance

---

## 12. Target Group

### Why Used

Maintains the backend EC2 instances.

### Project Usage

The ALB forwards requests only to healthy targets.

Health Check

- Protocol: HTTP
- Path: /
- Success Code: 200

---

## 13. Auto Scaling Group

### Why Used

Automatically maintains the desired number of application servers.

### Configuration

Desired Capacity : 2

Minimum Capacity : 2

Maximum Capacity : 4

### Benefits

- Automatic Scaling
- High Availability
- Self-Healing Infrastructure

---

## 14. Launch Template

### Why Used

Defines the EC2 configuration used by the Auto Scaling Group.

Contains

- AMI
- Instance Type
- Security Groups
- Key Pair
- IAM Role
- User Data

---

## 15. IAM Role

### Why Used

Allows EC2 instances to securely access AWS services without storing credentials.

### Project Usage

Used for CloudWatch and Systems Manager integration.

---

## 16. Jenkins

### Why Used

CI/CD automation server.

### Project Usage

- Build application
- Deploy application
- Execute deployment jobs
- Integrate with GitHub Webhooks

---

## 17. CloudWatch Dashboard

### Why Used

Monitors infrastructure health.

### Metrics

- EC2 CPU Utilization
- ALB Metrics
- Network Traffic

---

## 18. CloudWatch Alarm

### Why Used

Generates alerts when CPU exceeds configured thresholds.

### Benefits

- Infrastructure Monitoring
- Performance Tracking

---

# 🔄 Request Flow

### Step 1

User accesses the Application Load Balancer.

↓

### Step 2

ALB receives the request.

↓

### Step 3

Target Group checks backend health.

↓

### Step 4

Healthy EC2 instance is selected.

↓

### Step 5

Docker container receives the request.

↓

### Step 6

Nginx serves the HTML application.

↓

### Step 7

Response is returned to the user.

Meanwhile,

CloudWatch continuously monitors EC2 instances, and the Auto Scaling Group maintains the required number of healthy instances.

---

# 🔐 Security Implementation

- Custom VPC
- Security Groups
- Bastion Host
- IAM Role
- Private Application Servers
- Least Privilege Access

---

# 📈 High Availability Features

- Multi Availability Zone Deployment
- Application Load Balancer
- Health Checks
- Auto Scaling Group
- Multiple Backend Servers
- CloudWatch Monitoring

---

# 📸 Screenshots

- Architecture Diagram
- VPC
- Public & Private Subnets
- Route Tables
- Internet Gateway
- Application Load Balancer
- Target Group
- Auto Scaling Group
- Launch Template
- CloudWatch Dashboard
- CloudWatch Alarm
- Jenkins Dashboard
- Docker Container
- Nginx Server 1
- Nginx Server 2

---

# 🛠 Tech Stack

- AWS EC2
- Amazon VPC
- IAM
- Security Groups
- Internet Gateway
- Route Tables
- Application Load Balancer
- Target Groups
- Auto Scaling Group
- Launch Template
- CloudWatch
- Docker
- Nginx
- Jenkins
- Git
- GitHub
- Linux
- Bash

---

# 🚀 Future Improvements

- Terraform
- Amazon ECR
- Amazon Route 53
- AWS Certificate Manager (HTTPS)
- AWS WAF
- Kubernetes (Amazon EKS)
- SonarQube
- Trivy
- Prometheus
- Grafana
- Argo CD

---

# 👨‍💻 Author

**Bharath Kumar S R**

DevOps Engineer

GitHub: https://github.com/<your-github>

LinkedIn: https://linkedin.com/in/<your-linkedin>
