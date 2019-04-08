from    django.urls import path

from .views import (
    about, contacts, main, registr
)


urlpatterns = [
    path('contacts/', contacts),
    path('about/', about),
    path('registr/', registr),
    path('', main),
]