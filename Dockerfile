FROM python:3.9.10

WORKDIR /app
COPY . /app
 
RUN pip install - r requirments.txt
 
ENTRYPOINT ["python"]
CMD ["-m", "app"]
