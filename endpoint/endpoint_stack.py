from aws_cdk import Stack, aws_iam
from aws_cdk.aws_apigatewayv2_alpha import HttpApi, HttpMethod
from aws_cdk.aws_apigatewayv2_integrations_alpha import HttpLambdaIntegration
from constructs import Construct
from aws_cdk.aws_lambda_python_alpha import PythonFunction
from aws_cdk import aws_lambda
from aws_cdk.aws_sns import Topic


class EndpointStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        release_request_topic = Topic(self, 'ReleaseTriggerTopic')
        backend_topic = Topic(self, 'BackendTopic')

        topics_policy = aws_iam.PolicyStatement(
            actions=["sns:Publish"],
            resources=[release_request_topic.topic_arn, backend_topic.topic_arn]
        )
        function = PythonFunction(
            self, "EndpointFunction",
            entry="endpoint/lambda",
            index="index.py",
            handler="handler",
            runtime=aws_lambda.Runtime.PYTHON_3_9,
            environment={
                'RELEASE_REQUEST_TOPIC_ARN': release_request_topic.topic_arn,
                'BACKEND_TOPIC_ARN': backend_topic.topic_arn
            },
            initial_policy=[topics_policy]
        )

        integration = HttpLambdaIntegration("EndpointHttpLambdaIntegration", handler=function)
        api = HttpApi(self, "EndpointHttpApi")
        api.add_routes(
            path="/webhooks",
            methods=[HttpMethod.POST],
            integration=integration
        )
