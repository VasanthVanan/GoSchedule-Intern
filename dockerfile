FROM python:alpine
ADD index.py /
CMD [ "python", "./index.py" ]
RUN apk add --no-cache bash