from django.contrib import admin
from django.urls import path
from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post', views.post),  
    path('get/<int:id>', views.get),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),       
]