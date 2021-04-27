from aws_cdk import core
from data_platform.data_lake.stack import DataLakeStack
from data_platform.common_stack import CommonStack

app = core.App()
data_lake = DataLakeStack(app)
common_stack = CommonStack(app)
app.synth()