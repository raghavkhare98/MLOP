from django.http import HttpResponse
from rest_framework import viewsets
from .models import Product, Customer, Order
from .serializers import ProductSerializer, CustomerSerializer, OrderSerializer

import matplotlib.pyplot as plt
import pandas as pd

import io
# Create your views here.

class ProductViewset(viewsets.ModelViewSet):
    # queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        product_id=self.request.query_params.get('id')
        if product_id:
            return Product.objects.filter(id=product_id)
    
        return Product.objects.all()

class CustomerViewset(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class OrderViewset(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


def product_count_by_category(request):
    
    #here we want to fetch from mysql and then convert it to csv, then use that csv

    products = Product.objects.all()
    df = pd.DataFrame(products)
    print(type(df))
    products_by_category = df['product_category'].value_counts()

    plt.figure(figsize=(8,6))
    products_by_category.plot(kind='bar')
    plt.title('Product count by category')
    plt.xlabel('Category')
    plt.ylabel('Counts')

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')    
    plt.close()
    buffer.seek(0)

    return HttpResponse(buffer, content_type='image/png')

def visualization_router(request):

    chart_type = request.GET.get('type')

    if chart_type == 'category_count':
        return product_count_by_category(request)

    else:
        return HttpResponse('Invalid chart type', status=400)