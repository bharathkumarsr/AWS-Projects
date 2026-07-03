# Public and Private Subnets

## Objective

Create highly available public and private subnets across two Availability Zones.

## Subnets Created

| Name | AZ | CIDR | Type |
|------|----|------|------|
| prod-public-subnet-a | ap-south-1a | 10.0.1.0/24 | Public |
| prod-public-subnet-b | ap-south-1b | 10.0.2.0/24 | Public |
| prod-private-app-a | ap-south-1a | 10.0.11.0/24 | Private |
| prod-private-app-b | ap-south-1b | 10.0.12.0/24 | Private |

## Why Two Availability Zones?

Using two Availability Zones improves application availability and fault tolerance. If one AZ experiences an outage, resources in the other AZ can continue serving traffic.

## Outcome

Successfully created four subnets to separate public-facing infrastructure from application resources.
