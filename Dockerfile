FROM python:3.7
WORKDIR /app
COPY . /app
EXPOSE 5000
RUN pip install -r requirements.txt
ENTRYPOint ["python"]
CMD ["server.py"]