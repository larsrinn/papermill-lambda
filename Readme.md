The purpose of this repository is to test how [papermill](https://github.com/nteract/papermill) can be used to run parametrized notebooks on AWS Lambda.

### Docker Lambda
To run the lambda function locally in an environment that's as close to AWS Lambda, [docker-lambda](https://hub.docker.com/r/lambci/lambda/) is used.  
Also, we use docker-lambda to bundle the function code along with the dependencies and deploy this to AWS Lambda (via upload to S3).
For this repository, building via docker is probably not required as no installed dependencies need a specific build process.
However, as this is only a demo repository, we want to setup the pipeline to also work for a lambda function having compiled dependencies.

#### Build and run locally
When the dependencies have changed, you need to rebuild the docker image using the first command.
To run the lambda function, use the second command.
It mounts the current working directory to the docker container and executes the method `lambda_handler` inside `lambda_function.py`.
```
docker build -t papermill-lambda-test .
docker run -v "$PWD":/var/task papermill-lambda-test
```

#### Build and deploy to S3
The first step creates a folder containing the function code along with all dependencies installed via `pip`.
That way, our python code can import them on lambda as if they were installed globally/to the active virtual environment.

The second command zips the folder and uploads the zipped file to a S3 bucket.
From the S3 bucket, it is deployed to AWS Lambda.
For this to work, you need to pass on along AWS credentials.
The credentials must have access to a S3 bucket called `papermill-lambda` and a lambda function with the same name.
Also it needs to have permissions to upload to that bucket and to deploy to the lambda function.
```
docker build -t papermill-lambda-test-deploy -f Dockerfile-deploy .
docker run -e AWS_ACCESS_KEY_ID='xxx' -e AWS_SECRET_ACCESS_KEY='xxx' papermill-lambda-test-deploy
```

#### Running on AWS Lambda
For testing purpose, it is possible to use the default `hello world` test event proposed by AWS Lambda.
The function currently doesn't take any parameters as input.
