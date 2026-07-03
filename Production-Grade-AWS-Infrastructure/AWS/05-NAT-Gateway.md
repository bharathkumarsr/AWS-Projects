# NAT Gateway

## Objective

Create a NAT Gateway to provide outbound internet access for resources in private subnets.

## Configuration

| Property | Value |
|----------|-------|
| Name | prod-nat-gateway |
| Type | Public |
| Subnet | prod-public-subnet-a |
| Elastic IP | 13.203.142.89 |

## Why NAT Gateway?

A NAT Gateway enables instances in private subnets to access the internet for software updates, package installations, and AWS service communication without allowing inbound internet connections.

## Outcome

Successfully created a Public NAT Gateway associated with an Elastic IP in the public subnet.
