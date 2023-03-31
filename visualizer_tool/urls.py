from django.urls import path
from visualizer_tool import views

urlpatterns = [
    path('', views.form_init, name='form_init'),
    path('submitted/', views.submit_form, name='submit_form')
]