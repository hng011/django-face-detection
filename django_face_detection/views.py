from django.http import HttpResponse
from django.template.loader import render_to_string

def index(req):

    context = {"cam_start": req.session.get("cam_start")}
    content = render_to_string("index.html", context)
    
    return HttpResponse(content)