# Auto Scaling Group

## Objective

Automatically maintain and scale EC2 application servers based on CPU utilization.

## Configuration

- Launch Template: prod-app-template
- VPC: prod-devops-vpc
- Private Subnets:
  - prod-private-app-a
  - prod-private-app-b

## Capacity

- Minimum: 2
- Desired: 2
- Maximum: 4

## Scaling Policy

- Metric: Average CPU Utilization
- Target: 60%

## Outcome

Application instances are automatically replaced if unhealthy and scale based on demand.
