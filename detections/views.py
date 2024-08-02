from django.shortcuts import render
from django.http import StreamingHttpResponse
from .camera import Camera

# Create your views here.
def generator(cam):
    """_summary_
    Continuously fetch frames from a cam object 
    """
    while True:
        f = cam.get_frame()
        yield (b"--frame\r\n"
               b"Content-Type: image/jpeg\r\n\r\n" + f + b"\r\n\r\n")
        
def video_feed(req):
    return StreamingHttpResponse(generator(Camera()), content_type="multipart/x-mixed-replace; boundary=frame")