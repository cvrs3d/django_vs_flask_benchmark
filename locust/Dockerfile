FROM locustio/locust

# Working directory in the container!
WORKDIR /mnt/locust

# We copy all necessary files into wordir
COPY locustfile.py /mnt/locust/
COPY order_urls.txt /mnt/locust/


CMD ["-f", "/mnt/locust/locustfile.py"]
