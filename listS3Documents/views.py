from django.http import HttpResponse
from django.shortcuts import render
import boto3
# Let's use Amazon S3
s3 = boto3.client('s3')
session = boto3.Session()
def index(request):
    documents = s3.list_buckets()
    context = {
        'buckets': documents['Buckets'],
        'location' : session.region_name
    }
    print(session.region_name)
    return render(request, 'listS3Documents/index.html', context)