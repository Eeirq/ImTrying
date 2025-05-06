import os
from django.http import HttpResponse

BASE_DIR = os.path.dirname(__file__)

def home(_request):
    html_path = os.path.join(BASE_DIR, 'home.html')
    with open(html_path, 'r') as f:
        html = f.read()
    return HttpResponse(html)

def serve_css(_request):
    css_path = os.path.join(BASE_DIR, 'style.css')
    with open(css_path, 'r') as f:
        css = f.read()
    return HttpResponse(css, content_type='text/css')
