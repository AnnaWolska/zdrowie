from  django.urls import path
from health.views import health_view

app_name = "health"
urlpatterns = [
    path('health', health_view, name="heath_view")
]
