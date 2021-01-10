from django.urls import path
from hello import views

app_name = 'hello'
urlpatterns = [
    path('', views.session_counter, name="session_counter"),
]
