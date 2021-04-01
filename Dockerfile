FROM amazon/aws-lambda-python:3.7

# service args to variables
# env
ARG STAGE
ARG CLUSTER_URL

# database
ARG DATABASE_URL

# version
ARG BUILD_ID

ENV STAGE=$STAGE
ENV CLUSTER_URL=$CLUSTER_URL
ENV DATABASE_URL=$DATABASE_URL
ENV BUILD_ID=$BUILD_ID

# default
ENV DEBUG='0'

COPY ./app ${LAMBDA_TASK_ROOT}/app

RUN pip install -r ${LAMBDA_TASK_ROOT}/app/requirements.txt

ENV PYTHONPATH=${LAMBDA_TASK_ROOT}/app

CMD [ "app.lambda.handler" ]
