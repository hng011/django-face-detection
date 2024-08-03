from django.shortcuts import render,redirect
from django.http import StreamingHttpResponse, HttpResponseServerError
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
    try:       
        return StreamingHttpResponse(generator(Camera()), content_type="multipart/x-mixed-replace; boundary=frame")
    except Exception as e:
        return HttpResponseServerError(e)

def start_cam(req):
    req.session["cam_start"] = True
    return redirect("/")
    
def stop_cam(req):
    req.session.pop("cam_start")
    req.session.clear()
    req.session.flush()
    return redirect("/")