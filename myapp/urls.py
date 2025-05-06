from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('style.css', views.serve_css),  # this serves your CSS manually
]
# This is a simple Django URL configuration that maps the root URL to the `home` view and the `/style.css` URL to the `serve_css` view.
# The `home` view serves an HTML file, while the `serve_css` view serves a CSS file.