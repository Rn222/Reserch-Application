from django.urls import path
from .import views

urlpatterns = [
        path('', views.PostList.as_view(), name='object_list'),
        #path('', views.post_list, name='post_list'),
]
