# layerless-lambda-examples
Layerless approach to instrument Python lambda
Refer newrelic docs for [monitoring-aws-lambda-layerles](https://docs.newrelic.com/docs/serverless-function-monitoring/aws-lambda-monitoring/instrument-lambda-function/enable-serverless-monitoring-aws-lambda-layerless/#node)

## Install instructions

```
cd node/newrelic-example-node
npm install newrelic --save
./deploy.sh <NRAccountId> <aws-region<> <NRLicenseKey> <aws-s3-bucket-name>
```