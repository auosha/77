from django.urls import path

from serviceApp import views

urlpatterns = [
    path("", views.index, name="index"),
    path("AddCategory", views.add_category, name="add-category"),
    path('showCategory/<id>', views.show_category, name='show-category'),
    path('AddService/<id>', views.add_service, name='add-service'),
    path('ShowService/<id>', views.show_service, name='show-service')

]
