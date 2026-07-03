# VPC Creation

## Objective

Create a dedicated Virtual Private Cloud (VPC) to host a secure and highly available AWS infrastructure.

---

## Configuration

| Property | Value |
|----------|-------|
| Name | prod-devops-vpc |
| Region | ap-south-1 |
| CIDR Block | 10.0.0.0/16 |
| IPv6 | Disabled |
| Tenancy | Default |

---

## Why /16 CIDR?

A /16 CIDR provides 65,536 private IP addresses, allowing the VPC to be divided into multiple public and private subnets while leaving room for future expansion.

---

## Outcome

Successfully created a custom VPC that will host all networking, compute, security, and monitoring components for this project.
