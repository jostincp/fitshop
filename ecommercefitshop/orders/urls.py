from django.urls import path
from orders.views import UserListView

urlpatterns = [
    path("listView/", UserListView.as_view(), name="listView"),

]   
