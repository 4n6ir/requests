import cdk_nag

from aws_cdk import (
    Aspects,
    RemovalPolicy,
    Stack,
    aws_lambda as _lambda,  
)

from constructs import Construct

class RequestsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        Aspects.of(self).add(
            cdk_nag.AwsSolutionsChecks()
        )

        Aspects.of(self).add(
            cdk_nag.HIPAASecurityChecks()    
        )

        Aspects.of(self).add(
            cdk_nag.NIST80053R5Checks()
        )

        Aspects.of(self).add(
            cdk_nag.PCIDSS321Checks()
        )

        layer = _lambda.LayerVersion(
            self, 'layer',
            code = _lambda.Code.from_asset('bundle/requests.zip'),
            compatible_architectures = [
                _lambda.Architecture.ARM_64,
                _lambda.Architecture.X86_64
            ],
            compatible_runtimes = [
                _lambda.Runtime.PYTHON_3_7,
                _lambda.Runtime.PYTHON_3_8,
                _lambda.Runtime.PYTHON_3_9,
                _lambda.Runtime.PYTHON_3_10,
                _lambda.Runtime.PYTHON_3_11,
                _lambda.Runtime.PYTHON_3_12
            ],
            description = 'requests 2.31.0 (https://github.com/psf/requests)',
            layer_version_name = 'requests',
            license = 'Apache-2.0 License',
            removal_policy = RemovalPolicy.DESTROY
        )

        layer.add_permission(
            id = 'permission',
            account_id = '*'
        )
