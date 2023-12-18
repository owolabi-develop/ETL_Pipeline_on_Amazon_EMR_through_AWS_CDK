import aws_cdk as core
import aws_cdk.assertions as assertions

from aws_batch_processing_with_py_spark_on_emr.aws_batch_processing_with_py_spark_on_emr_stack import AwsBatchProcessingWithPySparkOnEmrStack

# example tests. To run these tests, uncomment this file along with the example
# resource in aws_batch_processing_with_py_spark_on_emr/aws_batch_processing_with_py_spark_on_emr_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AwsBatchProcessingWithPySparkOnEmrStack(app, "aws-batch-processing-with-py-spark-on-emr")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
