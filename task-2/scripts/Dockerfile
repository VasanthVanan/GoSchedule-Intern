FROM python:3-onbuild
EXPOSE 5000
WORKDIR /app
COPY requirements.txt /app
ADD init.sql /docker-entrypoint-initdb.d
RUN pip install -r requirements.txt
COPY app.py /app
CMD python app.py
