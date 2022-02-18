FROM python:3.10
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY pandas-analytics-server .

CMD [ "python", "./app.py" ]

