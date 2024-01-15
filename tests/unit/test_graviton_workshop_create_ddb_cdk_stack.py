import aws_cdk as core
import aws_cdk.assertions as assertions

from graviton_workshop_create_ddb_cdk.graviton_workshop_create_ddb_cdk_stack import GravitonWorkshopCreateDdbCdkStack

# example tests. To run these tests, uncomment this file along with the example
# resource in graviton_workshop_create_ddb_cdk/graviton_workshop_create_ddb_cdk_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = GravitonWorkshopCreateDdbCdkStack(app, "graviton-workshop-create-ddb-cdk")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
