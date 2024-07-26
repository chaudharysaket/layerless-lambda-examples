# layerless-lambda-examples
Layerless approach to instrument Python lambda
Refer newrelic docs for [monitoring-aws-lambda-layerles](https://docs.newrelic.com/docs/serverless-function-monitoring/aws-lambda-monitoring/instrument-lambda-function/enable-serverless-monitoring-aws-lambda-layerless/#python)

## Install instructions

```
cd python/original_handler/newrelic_example_python/ 
pip install -t . newrelic
./deploy.sh <NRAccountId> <aws-region<> <NRLicenseKey> <aws-s3-bucket-name>
```

Add newrelic_lambda files from the [PR](https://github.com/newrelic/newrelic-lambda-layers/pull/225/files#diff-8751b2dd2bff783f7ddea28427cbfbb87304457216ecf5da6cc1c4cbf0215814) which Adds python's newrelic_lambda package directly to layers
