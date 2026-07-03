# Application Load Balancer

## Objective

Deploy an internet-facing Application Load Balancer to distribute traffic across application servers in private subnets.

## Configuration

- Internet-facing
- IPv4
- Public Subnet A
- Public Subnet B
- Security Group: prod-alb-sg

## Target Group

- prod-app-tg
- HTTP
- Port 80
- Registered Targets:
  - prod-app-server-1
  - prod-app-server-2

## Outcome

Traffic is distributed across two private EC2 instances using an Application Load Balancer.
