from django.urls import path

from .views import (
    product_detail,products_list
)



urlpatterns = [
    path('detail/', product_detail),
    path('', products_list),

]