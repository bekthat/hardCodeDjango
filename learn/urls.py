from django.urls import path
from .views import home, product_list, group_list, student_list


urlpatterns = [
    path('', home, name='home'),
    path('products/', product_list, name='product_list'),
    path('groups/', group_list, name='group_list'),
    path('students/', student_list, name='student_list'),
]
