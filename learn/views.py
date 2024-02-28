from django.shortcuts import render
from rest_framework import viewsets
from .models import Product, Lesson, Group, User
from .serializers import ProductSerializer, LessonSerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class LessonViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = LessonSerializer

    def get_queryset(self):
        user = self.request.user
        product_id = self.kwargs['product_id']
        return Lesson.objects.filter(product_id=product_id, product__accesses__user=user)


def home(request):
    return render(request, 'learn/home.html')


def product_list(request):
    products = Product.objects.all()
    return render(request, 'learn/product_list.html', {'products': products})


def group_list(request):
    groups = Group.objects.prefetch_related('users').all()
    for group in groups:
        # Исключаем администраторов из списка пользователей каждой группы
        group.student_users = group.users.filter(is_superuser=False)
    return render(request, 'learn/group_list.html', {'groups': groups})


def student_list(request):
    students = User.objects.filter(is_staff=False)  # или ваш фильтр для определения студентов
    return render(request, 'learn/student_list.html', {'students': students})
