FROM python:3.8-slim

COPY entrypoint.sh edit-keycloak-redirect-uris.py requirements.txt /
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r /requirements.txt

ENTRYPOINT [ "sh", "/entrypoint.sh" ]
