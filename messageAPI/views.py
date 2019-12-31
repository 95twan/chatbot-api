from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
import boto3


class Image(APIView):
    s3_client = boto3.client(
        's3',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
    )

    def get(self, request):
        return Response({"desc": "ImageUploadAPI"})

    def post(self, request):

        file = request.FILES.get('img')

        self.s3_client.upload_fileobj(
                file,
                settings.AWS_STORAGE_BUCKET_NAME,
                f"media/photo/{file.name}"
            )

        file_urls = [f"https://{settings.AWS_STORAGE_BUCKET_NAME}.s3.ap-northeast-2.amazonaws.com/media/photo{file.name}"]

        return Response({'files': file_urls})
