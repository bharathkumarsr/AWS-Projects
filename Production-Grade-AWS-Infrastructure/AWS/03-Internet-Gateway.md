# Internet Gateway

## Objective

Create and attach an Internet Gateway (IGW) to enable internet connectivity for public resources within the VPC.

## Configuration

| Property | Value |
|----------|-------|
| Name | prod-igw |
| Attached VPC | prod-devops-vpc |
| State | Attached |

## Why is an Internet Gateway Required?

An Internet Gateway enables communication between the VPC and the internet. It is required for internet-facing resources such as the Application Load Balancer (ALB) and NAT Gateway.

## Note

Attaching an Internet Gateway alone does not make a subnet public. A route to the Internet Gateway must also be configured in the route table.
