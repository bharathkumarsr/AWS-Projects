# Elastic IP

## Objective

Allocate an Elastic IP (EIP) to provide a static public IP address for the NAT Gateway.

## Configuration

| Property | Value |
|----------|-------|
| Name | prod-nat-eip |
| Region | ap-south-1 |
| Purpose | NAT Gateway |

## Why Elastic IP?

A NAT Gateway requires a static public IP address to allow outbound internet access for resources in private subnets.
