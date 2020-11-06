# Set base image(host OS)
FROM python:3.8-alpine
# FROM python:3.8 is very large so -alpine prefered as it's small and contains pip

# Set base directory in the container
WORKDIR /twitty

# Copy files
COPY twitty/config.py /twitty/
COPY twitty/user.py /twitty/
COPY twitty/followback.py /twitty/
COPY twitty/retweeter.py /twitty/
COPY requirements.txt /tmp

# Install dependencies
RUN pip3 install -r /tmp/requirements.txt

# Command to run on container start
CMD ["python3", "followback.py"]