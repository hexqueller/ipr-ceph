FROM python:3.12-slim

WORKDIR /app

RUN pip install boto3

COPY check_ceph_bucket.py /app/check_ceph_bucket.py

CMD ["python", "check_ceph_bucket.py"]
