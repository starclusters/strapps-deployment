from django.urls import path
from . import views

app_name = 'biditem'

urlpatterns = [

    path('search', views.search, name="biditem_search"),
    path('search/result', views.searchresult, name="biditem_searchresult"),

]
