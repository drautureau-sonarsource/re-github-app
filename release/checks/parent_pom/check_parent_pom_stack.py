from aws_cdk import Stack
from constructs import Construct
from aws_cdk.aws_lambda_python_alpha import PythonFunction
from aws_cdk import aws_lambda


class CheckParentPomStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        function = PythonFunction(
            self, "CheckParentPomFunction",
            entry="release/checks/parent_pom/lambda",
            index="index.py",
            handler="handler",
            runtime=aws_lambda.Runtime.PYTHON_3_9
        )
