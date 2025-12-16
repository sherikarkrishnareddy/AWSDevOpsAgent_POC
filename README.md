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

🧪 Deploy the POC
bash
pip install -r requirements.txt
cdk bootstrap
cdk deploy
You’ll get an output like:

Code
ApiUrl = https://xxxxxx.execute-api.ap-south-1.amazonaws.com
Test it:

Code
curl "$ApiUrl?mode=normal"
curl "$ApiUrl?mode=error"
curl "$ApiUrl?mode=db_down"
curl "$ApiUrl?mode=cpu_stress"
CloudWatch alarms will fire → AWS DevOps Agent will investigate.

🧹 Rollback (zero billing)
bash
cdk destroy
Everything is removed cleanly.
