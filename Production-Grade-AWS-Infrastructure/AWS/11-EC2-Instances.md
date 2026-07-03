# EC2 Instances

## Bastion Host

- Amazon Linux 2023
- Public Subnet
- Public IP Enabled
- Security Group: prod-bastion-sg

## Application Server 1

- Private Subnet A
- No Public IP
- Docker Installed
- IAM Role Attached

## Application Server 2

- Private Subnet B
- No Public IP
- Docker Installed
- IAM Role Attached

## Outcome

Deployed two private EC2 instances running Docker and one Bastion Host for secure administration.
