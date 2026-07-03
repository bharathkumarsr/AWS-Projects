# Route Tables

## Objective

Configure route tables to enable internet access for public subnets and outbound internet access for private subnets through the NAT Gateway.

## Public Route Table

| Destination | Target |
|-------------|--------|
| VPC CIDR | Local |
| 0.0.0.0/0 | Internet Gateway |

Associated Subnets

- prod-public-subnet-a
- prod-public-subnet-b

---

## Private Route Table

| Destination | Target |
|-------------|--------|
| VPC CIDR | Local |
| 0.0.0.0/0 | NAT Gateway |

Associated Subnets

- prod-private-app-a
- prod-private-app-b

## Outcome

Public resources can communicate directly with the internet through the Internet Gateway, while private resources use the NAT Gateway for secure outbound internet access.
