# Auto Scaling Group

## Objective

Implement Auto Scaling to automatically maintain application availability by launching or terminating EC2 instances based on demand.

---

## Architecture

Application Load Balancer
        │
        ▼
Target Group
        │
        ▼
Auto Scaling Group
        │
 ┌──────────────┐
 │              │
EC2-1        EC2-2
