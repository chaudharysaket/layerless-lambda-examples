from newrelic import agent
import newrelic.agent
from newrelic_lambda.lambda_handler import lambda_handler  # noqa

# In a python Lambda, the runtime loads the handler code as a module; so code in the top level
# of the module occurs once, during cold start.
print("Lambda Handler starting up")


newrelic.agent.initialize()

@lambda_handler()
def lambda_handler(event, context):
    # At this point, we're handling an invocation. Cold start is over; this code runs for each invocation.

    # This is an example of a custom event. `FROM MyPythonEvent SELECT *` in New Relic will find this event.
    agent.record_custom_event("MyPythonEvent", {
        "zip": "zap"
    })
    # This attribute gets added to the normal AwsLambdaInvocation event
    agent.add_custom_attribute('customAttribute', 'customAttributeValue')

    # As normal, anything you write to stdout ends up in CloudWatch
    print("Hello, world")

    return "Success!"
