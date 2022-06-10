# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core as cdk
from aws_cdk import aws_lambda as lambda_

CLOUDFRONT_ADD_SECURITY_HEADERS_NAME = "pjc-test-headers"

class AwsCdk20650Stack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        lambda_security_header = lambda_.Function(
            self,
            CLOUDFRONT_ADD_SECURITY_HEADERS_NAME,
            runtime=lambda_.Runtime.NODEJS_12_X,
            code=lambda_.Code.from_asset("lambda/add-security-headers"),
            handler="add-security-headers.handler",
            function_name=CLOUDFRONT_ADD_SECURITY_HEADERS_NAME
        )
        self.add_security_headers_arn = lambda_security_header.current_version.edge_arn
