FROM python:3.8-slim-buster
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip3 install -r requirements.txt
# RUN source bin/activate
COPY . .
CMD ["python", "main.py"]