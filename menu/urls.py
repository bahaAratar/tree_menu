from django.urls import path
from .views import *

urlpatterns = [
    path('category/', home, name='home'),
    path('category/<int:cat_id>/', show_category, name='category')
]