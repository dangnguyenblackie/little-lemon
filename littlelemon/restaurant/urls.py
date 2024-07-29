from . import views
from django.urls import path

urlpatterns = [
    path('',                    views.index),
    path('items/',               views.MenuItemsView.as_view()),
    path('items/<int:pk>/',      views.SingleMenuItemView.as_view()),
]
