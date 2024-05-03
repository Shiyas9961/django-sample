from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_movies, name="movies"),
    path('pic', views.movie_pic_page, name="movies_pic"),
    path('create', views.create_page, name="create"),
    path('create_c', views.custome_create, name="custome"),
    path('edit/<pk>', views.edit_movie, name="edit"),
    path('delete/<pk>', views.delete_movie, name="delete"),
    path('upload', views.upload_movie_pic, name="upload")
]