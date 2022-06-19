FROM python:3.9.10

WORKDIR /app.py
COPY . /app.py
 
RUN pip install - r requirments.txt
 
ENTRYPOINT ["python"]
CMD ["-m", "app"]
