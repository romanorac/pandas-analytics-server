# pandas-analytics-server

pandas-analytics-server is an open source project that simplifies connecting
pandas to a realtime data feed, testing hypothesis and visualizing results in a web browser.

Read more about the project: [pandas analytics server](https://towardsdatascience.com/pandas-analytics-server-d64d20ef01be?sk=0292c30f7a54f42c037b0da6af9782e4).

You can try the Server, it is [live](http://ec2-18-203-115-238.eu-west-1.compute.amazonaws.com:5000/plot).

## Instalation

```
sudo yum install python3 -y
sudo yum install git -y

sudo yum -y install gcc
sudo yum -y install tmux
sudo yum -y install htop

git clone https://github.com/romanorac/pandas-analytics-server.git

cd pandas-analytics-server
python3 -m venv env
source env/bin/activate

pip install -r requirements.txt
```

## Run

Make sure you are in folder `/home/ec2-user/pandas-analytics-server/pandas-analytics-server`.

Run the server with: `python app.py` for development.

Use gunicorn in production: `gunicorn -b :5000 app:app`.
