#! /bin/sh

python /edit-keycloak-redirect-uris.py \
    --keycloak-user "${INPUT_KEYCLOAK_USER}" \
    --keycloak-pass "${INPUT_KEYCLOAK_PASS}" \
    --client-id "${INPUT_CLIENT_ID}" \
    --action "${INPUT_ACTION}" \
    --redirect-uri "${INPUT_REDIRECT_URI}"
