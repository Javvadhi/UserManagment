from django.contrib import admin
from django.urls import path
from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post', views.post),  
    path('get/<int:uid>', views.get),
    path('update/<int:uid>', views.update),
    path('delete/<int:uid>', views.destroy),       
]
