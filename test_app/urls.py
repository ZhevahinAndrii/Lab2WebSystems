from django.urls import path
from . import views

app_name = 'test_app'


urlpatterns = [
    path('products/<int:product_id>', views.product_detail, name='product_detail')
]