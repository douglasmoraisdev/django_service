from apig_wsgi import make_lambda_handler
from .wsgi import application
from .asgi import application as app
import json
from mangum import Mangum


# Configure this as your entry point in AWS Lambda
apig_wsgi_handler = make_lambda_handler(application, binary_support=True)



handler = Mangum(app=app)

def lambda_handler(event, context):
    print(json.dumps(event, indent=2, sort_keys=True))
    response = apig_wsgi_handler(event, context)
    print(json.dumps(response, indent=2, sort_keys=True))
    return response