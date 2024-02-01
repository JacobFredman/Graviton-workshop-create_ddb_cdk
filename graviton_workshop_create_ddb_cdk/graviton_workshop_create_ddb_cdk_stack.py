
import aws_cdk as cdk
import aws_cdk.aws_dynamodb as dynamodb
from constructs import Construct
from aws_cdk import Stack
class GravitonWorkshopCreateDdbCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # create a dynamodb table
        urls_table = dynamodb.Table(
            self, "GravitonWorkshopDdbUrlsTable",
            partition_key=dynamodb.Attribute(
                name="short_url",
                type=dynamodb.AttributeType.STRING
            ),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
        )

        account = self.account
        print(f"This stack is being deployed to account: {account}")
       