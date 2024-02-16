"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from config import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/',views.ProductListAPIView.as_view()),
    path('product/create/',views.ProductCreateAPIView.as_view()),
    path('product/<int:pk>/',views.ProductRetrieveAPIView.as_view()),
    path('product/<int:pk>/update/',views.ProductUpdateAPIView.as_view()),
    path('product/<int:pk>/delete/',views.ProductDestroyAPIView.as_view()),
    
    path('category/',views.CategoryListAPIView.as_view()),
    path('category/create/',views.CategoryCreateAPIView.as_view()),
    path('category/<int:pk>/',views.CategoryRetrieveAPIView.as_view()),
    path('category/<int:pk>/update/',views.CategoryUpdateAPIView.as_view()),
    path('category/<int:pk>/delete/',views.CategoryDestroyAPIView.as_view()),
    
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    

]
