from django.http import HttpResponse
from django.shortcuts import render
import boto3
# Let's use Amazon S3
s3 = boto3.client('s3')

def index(request):
    documents = s3.list_buckets()
    context = {
        'buckets': documents['Buckets'],
    }
    return render(request, 'listS3Documents/index.html', context)