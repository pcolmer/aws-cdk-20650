This branch is the changes made to upgrade from CDK v1 to CDK v2.

Uninstall all AWS CDK modules ...

```
pip uninstall aws-cdk.assertions aws-cdk.assets aws-cdk.aws-applicationautoscaling aws-cdk.aws-autoscaling-common
pip uninstall aws-cdk.aws-cloudwatch aws-cdk.aws-codeguruprofiler aws-cdk.aws-codestarnotifications aws-cdk.aws-ec2 aws-cdk.aws-ecr aws-cdk.aws-ecr-assets aws-cdk.aws-efs aws-cdk.aws-events aws-cdk.aws-iam aws-cdk.aws-kms aws-cdk.aws-lambda aws-cdk.aws-logs
pip uninstall aws-cdk.aws-s3 aws-cdk.aws-s3-assets aws-cdk.aws-signer aws-cdk.aws-sns aws-cdk.aws-sqs aws-cdk.aws-ssm aws-cdk.cloud-assembly-schema aws-cdk.core aws-cdk.cx-api aws-cdk.region-info
```

Modify requirements.txt and install new modules ...
```
python -m pip install -r requirements.txt
```

Modify code to upgrade to v2 and run `diff` ...
```
cdk diff
```

Output includes:

```
Resources
[-] AWS::Lambda::Version pjctestheadersCurrentVersion6A41A3741e769839a4a4eca15363055ff023227a destroy
[+] AWS::Lambda::Version pjc-test-headers/CurrentVersion pjctestheadersCurrentVersion6A41A374f92b3f06e16da8e8e102c48b89c67cef
```
