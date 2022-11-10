FROM python:3.8
COPY python/lib.txt /lib.txt
RUN pip install --user --upgrade pip
RUN pip install --no-cache-dir --user -r /lib.txt
