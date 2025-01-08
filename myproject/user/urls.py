from django.urls import path
from . import views

urlpatterns = [
    path('/hello',views.hello_world, name="hello world"),
    path('/get_all',views.customer_list,name="customer_list"),
    path('/get_all_ser',views.CustomerAPIView.as_view(),name='customer_list_ser'),
    path('/get_all_cache',views.CustomerAPIViewCache.as_view(),name='customer_list_cache'),
    path('/fiter_first_name',views.customer_by_first_name,name='customer_by_first_name')
    
]
