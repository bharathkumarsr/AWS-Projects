                        IAM
                         │
         ┌───────────────┼───────────────┐
         │                               │
      Users                          Roles
                                         │
                                         ▼
                                 EC2 (Docker)
                                         │
                              ┌──────────┴─────────┐
                              │                    │
                              ▼                    ▼
                             S3                 RDS
                              │                    │
                              └────────┬───────────┘
                                       ▼
                                CloudWatch
                                       │
                          ┌────────────┴───────────┐
                          ▼                        ▼
                     CloudTrail                 Alarms
                                                   │
                                                   ▼
                                                  SNS
                                                   │
                                                   ▼
                                                 Email
