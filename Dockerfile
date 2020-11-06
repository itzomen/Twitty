FROM python:3.7-alpine

COPY twitty/config.py /bots/
COPY twitty/user.py /bots/
COPY twitty/followback.py /bots/
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /bots
CMD ["python3", "followback.py"]