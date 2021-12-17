from aws_cdk import App
from endpoint.endpoint_stack import EndpointStack
from release.checks.dependencies.check_dependencies_stack import CheckDependenciesStack
from release.checks.parent_pom.check_parent_pom_stack import CheckParentPomStack
from release.checks.quality_gate.check_quality_gate_stack import CheckQualityGateStack
from release.checks.whitesource.check_whitesource_stack import CheckWhiteSourceStack

app = App()

EndpointStack(app, 'EndpointStack')

# ReleaseStack(app, 'ReleaseStack')
CheckDependenciesStack(app, 'CheckDependenciesStack')
CheckParentPomStack(app, 'CheckParentPomStackStack')
CheckQualityGateStack(app, 'CheckQualityGateStack')
CheckWhiteSourceStack(app, 'CheckWhiteSourceStack')

app.synth()
