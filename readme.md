
##  Using Docker 

#####  1. Build Dockerfile
```bash
docker build -t django_face_detection -f Dockerfile .
```

##### 2. Run Docker Container
```bash
docker run --rm -it -device=/dev/video0 -p 8888:8888 django_face_detection
```