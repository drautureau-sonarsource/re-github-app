from aws_cdk import Stack
from aws_cdk.aws_apigatewayv2_alpha import HttpApi, HttpMethod
from aws_cdk.aws_apigatewayv2_integrations_alpha import HttpLambdaIntegration
from constructs import Construct
from aws_cdk.aws_lambda_python_alpha import PythonFunction
from aws_cdk import aws_lambda


class EndpointStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        api = HttpApi(self, "EndpointHttpApi")
        function = PythonFunction(
            self, "EndpointFunction",
            entry="endpoint/lambda",
            index="index.py",
            handler="handler",
            runtime=aws_lambda.Runtime.PYTHON_3_9
        )
        integration = HttpLambdaIntegration("EndpointHttpLambdaIntegration", handler=function)
        api.add_routes(
            path="/webhooks",
            methods=[HttpMethod.POST],
            integration=integration
        )

