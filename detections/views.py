from django.shortcuts import render
from django.http import StreamingHttpResponse
from .camera import Camera

# Create your views here.
def gen(cam):
    while True:
        f = cam.get_frame()
        yield (b"--frame\r\n"
               b"Content-Type: image/jpeg\r\n\r\n" + f + b"\r\n\r\n")
        
def video_feed(req):
    return StreamingHttpResponse(gen(Camera()), content_type="multipart/x-mixed-replace; boundary=frame")