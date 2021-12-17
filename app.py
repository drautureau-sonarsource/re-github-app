from aws_cdk import App
from endpoint.endpoint_stack import EndpointStack

app = App()
EndpointStack(app, "EndpointStack")

app.synth()
