# Introduction

It's an AWS S3-Bucket clone by using Python's [**boto3**](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html?id=docs_gateway).
This repo lists all your S3-Buckets and Files within the Bucket.

# What else is used?

It is written in Python via [Django](https://www.djangoproject.com/) and
using the [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)-library in order to connect AWS via Python.

# Prerequirements

Make sure that you put your credentials in `~/.aws`. 
You can configure them by using the [AWS-CLI](https://aws.amazon.com/cli/) and `aws configure`.
See if it works by using `aws s3 ls`. Below is a **sample** output by using the command.
```
2019-01-01 19:34:33 bucket1
2019-02-02 09:49:17 bucket2
2019-03-03 17:09:46 bucket3
```

# How to use

```
cd ListS3Bucket
python manage.py runserver
```
