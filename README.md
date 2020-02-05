# pandas-analytics-server

pandas-analytics-server is an open source project that simplifies connecting
pandas to a realtime data feed, testing hypothesis and visualizing results in a web browser.

## Instalation

```
sudo yum install gcc
sudo yum install tmux
sudo yum install htop

sudo yum -y install python36-devel
sudo yum -y install python36

python3 -m venv env
source env/bin/activate

pip install -r requirements.txt
```

## Run

Run the server with: `python app.py` for development.

Use gunicorn in production: `gunicorn -b :5000 app:app`.
