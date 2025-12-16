# AWSDevOpsAgent_POC
POC for AWSDevopsAgent(preview)

High‑Level Architecture (CDK Version)

1. Three‑tier application
API Gateway (HTTP API) → public entry point

Lambda function → business logic + fault injection

DynamoDB table → data tier (simple, serverless, no maintenance)

2. CloudWatch alarms
Lambda Errors ≥ 1

Lambda Duration ≥ threshold (optional)

3. AWS DevOps Agent (Preview)
You manually configure the agent in the console

It listens to the CloudWatch alarms created by CDK

When alarms fire, the agent investigates and proposes mitigation

4. Rollback
cdk destroy removes all resources

Zero leftover billing
