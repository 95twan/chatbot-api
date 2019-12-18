from django.core.files.storage import FileSystemStorage
from rest_framework.views import APIView
from rest_framework.response import Response


class Image(APIView):
    def get(self, request):
        return Response({"desc": "ImageUpload"})

    def post(self, request):
        # 사진 파일인지 확인 필요한가?
        image = request.FILES.get('img')
        fs = FileSystemStorage()
        image_name = fs.save(image.name, image)
        image_url = fs.url(image_name)

        return Response({"image_url": image_url})
