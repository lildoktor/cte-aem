import os
from urllib.parse import urlparse
import redis

url = urlparse(os.environ.get("rediss://:p4fd8396dff901c7c43ad2341e8afa136b004a47214118360491ee4d38edd6966@ec2-34-255-23-118.eu-west-1.compute.amazonaws.com:24360"))
r = redis.Redis(host=url.hostname, port=url.port, username=url.username, password=url.password, ssl=True, ssl_cert_reqs=None)
r.ping()
