from django.http import JsonResponse
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import  *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from django.core.cache import cache
from django.views.decorators.http import *

# Create your views here.

def hello_world(request):
    return HttpResponse("Hello, World!")

def customer_list(request):
    customers = Customer.objects.all()  # Get all customer records
    customers_data = serialize('json', customers)  # Serialize the data to JSON
    return JsonResponse(customers_data, safe=False)

class CustomerAPIView(APIView):
    renderer_classes = [JSONRenderer]
    def get(self, request):
        
        customers = Customer.objects.all()  # Fetch all Customers
        serializer = CustomerSerializer(customers, many=True)  # Serialize the data
        return Response(serializer.data)  # Return the serialized data

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)  # Deserialize incoming data
        if serializer.is_valid():  # Validate the data
            serializer.save()  # Save to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomerAPIViewCache(APIView):
    renderer_classes = [JSONRenderer]
    def get(self, request):
        
        cached_data = cache.get('customer_data')
        
        if cached_data:
            return Response(cached_data)
        
        customers = Customer.objects.all()  # Fetch all Customers
        serializer = CustomerSerializer(customers, many=True)  # Serialize the data
        
        cache.set('customer_data', serializer.data, timeout=10)
        
        return Response(serializer.data)  # Return the serialized data

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)  # Deserialize incoming data
        if serializer.is_valid():  # Validate the data
            serializer.save()  # Save to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@require_GET
def customer_by_first_name(request):
    # Get the first name from the request headers
    first_name = request.headers.get('first-name')

    if not first_name:
        return JsonResponse({'error': 'First name header is required'}, status=400)

    # Query the database for people with the given first name
    user_all = Customer.objects.filter(first_name__iexact=first_name)

    # Check if any people were found
    if not user_all:
        return JsonResponse({'message': 'No people found with that first name'}, status=404)

    # Serialize the data
    people_data = [{
        'first_name': customer.first_name,
        'last_name': customer.last_name,
        'email': customer.email,
    } for customer in user_all]

    return JsonResponse(people_data, safe=False, status=200)
