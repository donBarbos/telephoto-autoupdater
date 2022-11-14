FROM python:3-slim

WORKDIR /usr/src/app
COPY . .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/cache/apt

ENTRYPOINT ["python", "-m", "bot"]
