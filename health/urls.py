from django.urls import path
from health.views import health_view, add_glucos, add_bloodpressure

app_name = "health"
urlpatterns = [
    path('health', health_view, name="heath_view"),
    path('add_glucos', add_glucos, name="add_glucos"),
    path('add_bloodpressure', add_bloodpressure, name="add_bloodpressure"),
    path('', health_view, name="heath_view")
]
