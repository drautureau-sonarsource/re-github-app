from aws_cdk import Stack
from constructs import Construct
from aws_cdk.aws_lambda_python_alpha import PythonFunction
from aws_cdk import aws_lambda


class CheckQualityGateStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        function = PythonFunction(
            self, "CheckQualityGateFunction",
            entry="release/checks/quality_gate/lambda",
            index="index.py",
            handler="handler",
            runtime=aws_lambda.Runtime.PYTHON_3_9
        )
