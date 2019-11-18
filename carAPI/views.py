from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .serializers import CarSerializer, CarDetailSerializer, MakerSerializer, ColorSerializer
from .models import Car, Maker, CarColor, Color


class CarList(APIView):
    def get(self, request):

        _cars = Car.objects.all().order_by('id')

        maker_id = request.GET.get('maker_id', None)

        if maker_id:
            cars = get_list_or_404(_cars, maker=maker_id)
        else:
            cars = _cars

        paginator = PageNumberPagination()
        paginator.page_size = 10
        result_page = paginator.paginate_queryset(cars, request)
        current_page = paginator.page.number
        end_page = paginator.page.paginator.num_pages

        serializer = CarSerializer(result_page, many=True)

        return Response({
            'page': current_page,
            'end_page': end_page,
            'datas': serializer.data
        })

    def post(self, request):
        serializer = CarDetailSerializer(data=request.data)
        if serializer.is_valid():
            print("is_valid")
            # serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    
class CarDetail(APIView):
    def get(self, request, pk):
        cars = Car.objects.all()
        car = get_object_or_404(cars, pk=pk)
        serializer = CarDetailSerializer(car)
        return Response(serializer.data)

    def put(self, request, pk):
        cars = Car.objects.all()
        car = get_object_or_404(cars, pk=pk)
        serializer = CarDetailSerializer(car, request.data)
        if serializer.is_valid():
            print("is_valid")
            # serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        cars = Car.objects.all()
        car = get_object_or_404(cars, pk=pk)
        # car.delete()
        print("delete")
        return Response(status=HTTP_204_NO_CONTENT)


class CarColorAPI(APIView):
    def get(self, request, pk):
        car_color = CarColor.objects.all()
        color_ids = get_list_or_404(car_color, car_id=pk)

        colors = Color.objects.all()

        data = []
        for id in color_ids:
            color = get_object_or_404(colors, pk=id.color_id)
            serializer = ColorSerializer(color)
            data.append(serializer.data)

        return Response(data)


class MakerList(APIView):
    def get(self, request):
        maker = Maker.objects.all().order_by('id')
        serializer = MakerSerializer(maker, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = MakerSerializer(data=request.data)
        if serializer.is_valid():
            print("is_valid")
            # serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class MakerDetail(APIView):
    def get(self, request, pk):
        makers = Maker.objects.all()
        maker = get_object_or_404(makers, pk=pk)
        serializer = MakerSerializer(maker)
        return Response(serializer.data)

    def put(self, request, pk):
        makers = Maker.objects.all()
        maker = get_object_or_404(makers, pk=pk)
        serializer = MakerSerializer(maker, request.data)
        if serializer.is_valid():
            print("is_valid")
            # serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        makers = Maker.objects.all()
        maker = get_object_or_404(makers, pk=pk)
        # maker.delete()
        print("delete")
        return Response(status=HTTP_204_NO_CONTENT)