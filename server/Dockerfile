from python:3.9
LABEL maintainer="t3zv1y@gmail.com"
workdir ./server
COPY . .
run pip install -r requirements.txt
CMD ["python", "./server/main.py"]