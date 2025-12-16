#!/usr/bin/env python3
import aws_cdk as cdk
from devops_agent_poc.devops_agent_poc_stack import DevOpsAgentPOCStack
env = cdk.Environment(
    account="453971898162",
    region="us-east-1"
)
app = cdk.App()
stack = DevOpsAgentPOCStack(app, "DevOpsAgentPOC",env=env)


app.synth()
