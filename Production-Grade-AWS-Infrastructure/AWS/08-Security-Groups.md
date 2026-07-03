# Security Groups

## Objective

Create security groups to control traffic between the internet, load balancer, bastion host, and EC2 application servers.

## Security Groups

### 1. prod-alb-sg

**Inbound**

- HTTP (80) from 0.0.0.0/0
- HTTPS (443) from 0.0.0.0/0

**Outbound**

- All Traffic

---

### 2. prod-app-sg

**Inbound**

- HTTP (80) from prod-alb-sg
- SSH (22) from prod-bastion-sg

**Outbound**

- All Traffic

---

### 3. prod-bastion-sg

**Inbound**

- SSH (22) from My Public IP

**Outbound**

- All Traffic

---

## Outcome

- Internet users can access only the Application Load Balancer.
- Application servers are protected inside private subnets.
- SSH access is allowed only through the Bastion Host.
