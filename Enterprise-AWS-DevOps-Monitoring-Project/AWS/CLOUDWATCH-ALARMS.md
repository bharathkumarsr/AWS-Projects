# CloudWatch Alarms

## Objective

Automatically detect failures and notify administrators.

---

## Alarm Created

```text
EC2-StatusCheckFailed
```

---

## Configuration

Metric:

```text
StatusCheckFailed
```

Condition:

```text
Greater than 0
```

Action:

```text
Send notification to SNS
```

Topic:

```text
enterprise-devops-alerts
```

---

## Why Alarms?

- Automated monitoring
- Incident detection
- Alerting
- Operational visibility

---

## Key Learning

CloudWatch Alarms provide proactive monitoring capabilities.
