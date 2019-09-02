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
    return render(request, 'listS3Documents/index.html', context)

def bucketContent(request, bucketname):
    objects = s3.list_objects_v2(Bucket=bucketname,EncodingType='url')
    content = {
        'bucket': bucketname,
        'objects': objects['Contents']
    }
    return render(request, 'listS3Documents/content.html', content)