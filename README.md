The `main` branch is the CDK v1 project.

Deployment looked like this:

```
$ cdk1 deploy

✨  Synthesis time: 1.5s

This deployment will make potentially sensitive changes according to your current security approval level (--require-approval broadening).
Please confirm you intend to make the following modifications:

IAM Statement Changes
┌───┬─────────────────────────────────────┬────────┬────────────────┬──────────────────────────────┬───────────┐
│   │ Resource                            │ Effect │ Action         │ Principal                    │ Condition │
├───┼─────────────────────────────────────┼────────┼────────────────┼──────────────────────────────┼───────────┤
│ + │ ${pjc-test-headers/ServiceRole.Arn} │ Allow  │ sts:AssumeRole │ Service:lambda.amazonaws.com │           │
└───┴─────────────────────────────────────┴────────┴────────────────┴──────────────────────────────┴───────────┘
IAM Policy Changes
┌───┬─────────────────────────────────┬────────────────────────────────────────────────────────────────────────────────┐
│   │ Resource                        │ Managed Policy ARN                                                             │
├───┼─────────────────────────────────┼────────────────────────────────────────────────────────────────────────────────┤
│ + │ ${pjc-test-headers/ServiceRole} │ arn:${AWS::Partition}:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole │
└───┴─────────────────────────────────┴────────────────────────────────────────────────────────────────────────────────┘
(NOTE: There may be security-related changes not in this list. See https://github.com/aws/aws-cdk/issues/1299)

Do you wish to deploy these changes (y/n)? y
AwsCdk20650Stack: deploying...
[0%] start: Publishing 96db6d3d6f8bdf46b66225a2dbd32c04ed02cc00b827431ec356b680eb61e973:current
[100%] success: Published 96db6d3d6f8bdf46b66225a2dbd32c04ed02cc00b827431ec356b680eb61e973:current
AwsCdk20650Stack: creating CloudFormation changeset...

 ✅  AwsCdk20650Stack

✨  Deployment time: 53.13s

Stack ARN:
arn:aws:cloudformation:us-east-1:621503700583:stack/AwsCdk20650Stack/1bcc7790-e8a7-11ec-a0a7-0ee5e157a7d5

✨  Total time: 54.63s


NOTICES

19836   AWS CDK v1 entering maintenance mode soon

        Overview: AWS CDK v1 is entering maintenance mode on June 1, 2022.
                  Migrate to AWS CDK v2 to continue to get the latest features
                  and fixes!

        Affected versions: framework: 1.*, cli: 1.*

        More information at: https://github.com/aws/aws-cdk/issues/19836


If you don’t want to see a notice anymore, use "cdk acknowledge <id>". For example, "cdk acknowledge 19836".
```
