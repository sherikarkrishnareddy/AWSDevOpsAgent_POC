#!/usr/bin/env python3
import aws_cdk as cdk
from devops_agent_poc.devops_agent_poc_stack import DevOpsAgentPOCStack

app = cdk.App()
stack = DevOpsAgentPOCStack(app, "DevOpsAgentPOC")
cdk.CfnOutput(app, "ApiUrl", value=stack.api_url)

app.synth()
