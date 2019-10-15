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
        'location': session.region_name
    }
    return render(request, 'listS3Documents/index.html', context)


def bucketContent(request, bucketname, path=None):
    client = boto3.client('s3')
    paginator = client.get_paginator('list_objects')
    subfolders = []
    
    if not path:
        result = paginator.paginate(Bucket=bucketname, Delimiter='/')
        for prefix in result.search('CommonPrefixes'):
            subfolders.append(prefix.get('Prefix'))

    objects = []
    if not subfolders:         
        resource = boto3.resource('s3')
        bucket = resource.Bucket(bucketname)
        for obj_sum in bucket.objects.all():
            obj = resource.Object(obj_sum.bucket_name, obj_sum.key)
            # print(obj.last_modified)
            objects.append(obj)
    
    content = {
        'bucket': bucketname,
        'subfolders': subfolders,
        'objects': objects
    }
    return render(request, 'listS3Documents/content.html', content)