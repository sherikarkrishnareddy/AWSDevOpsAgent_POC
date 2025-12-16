from aws_cdk import (
    Stack,
    Duration,
    aws_lambda as _lambda,
    aws_apigatewayv2 as apigw,
    aws_apigatewayv2_integrations as integrations,
    aws_dynamodb as dynamodb,
    aws_cloudwatch as cloudwatch,
)
from constructs import Construct
import os

class DevOpsAgentPOCStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        # DynamoDB table
        table = dynamodb.Table(
            self, "POCTable",
            partition_key={"name": "pk", "type": dynamodb.AttributeType.STRING},
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST
        )

        # Lambda function
        lambda_fn = _lambda.Function(
            self, "POCLambda",
            runtime=_lambda.Runtime.PYTHON_3_12,
            handler="lambda_app.handler",
            code=_lambda.Code.from_asset("devops_agent_poc"),
            timeout=Duration.seconds(30),
            memory_size=256,
            environment={"TABLE_NAME": table.table_name}
        )

        table.grant_read_write_data(lambda_fn)

        # API Gateway HTTP API
        api = apigw.HttpApi(
            self, "POCApi",
            default_integration=integrations.HttpLambdaIntegration(
                "LambdaIntegration", lambda_fn
            )
        )

        # CloudWatch Alarm: Lambda Errors
        cloudwatch.Alarm(
            self, "LambdaErrorAlarm",
            metric=lambda_fn.metric_errors(),
            threshold=1,
            evaluation_periods=1,
            alarm_description="Triggers when Lambda errors occur"
        )

        # Output API URL
        self.api_url = api.api_endpoint
