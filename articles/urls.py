from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.article_list, name="list"),
    path('create/', views.article_create, name="create"),
    path('results/',views.article_search, name="search"),
    path('ascend/', views.article_list_ascend, name="list_ascend"),
    path('<user>/',views.article_list_user, name="list_user"),
    path('delete/<slug>/',views.article_delete, name="delete"),
    path('edit/<slug>/',views.article_edit, name="edit"),
    path('<slug>',views.article_detail, name="detail"),

]
