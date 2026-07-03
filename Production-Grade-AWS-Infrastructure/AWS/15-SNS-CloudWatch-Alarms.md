# CloudWatch Alarms and SNS Notifications

## Objective

Implement proactive monitoring by sending email alerts when EC2 CPU utilization exceeds a defined threshold.

## Services Used

- Amazon CloudWatch
- Amazon SNS
- Amazon EC2

## Alarm Configuration

- Metric: CPUUtilization
- Threshold: > 70%
- Notification: Email
- SNS Topic: prod-devops-alerts

## Benefits

- Real-time alerting
- Faster incident response
- Production monitoring
- Operational visibility
