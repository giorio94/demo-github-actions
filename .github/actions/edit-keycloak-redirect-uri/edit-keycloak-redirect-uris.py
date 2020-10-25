import argparse
import os
import sys
import keycloak as kc

if __name__ == "__main__":
    # Parse the command line arguments
    parser = argparse.ArgumentParser(description="Update the redirect URIs in keycloak")
    parser.add_argument("--keycloak-user", help="The admin username for the OIDC server", required=True)
    parser.add_argument("--keycloak-pass", help="The admin password for the OIDC server", required=True)
    parser.add_argument("--client-id", help="The ID of the Keycloak client to be edited", required=True)
    parser.add_argument("--action", choices=['add','remove'], help="The action to be performed (add/remove)")
    parser.add_argument("--redirect-uri", help="The redirect URI to be added/removed", required=True)


    args = parser.parse_args()

    server_url="https://auth.crownlabs.polito.it/auth/"
    print(f"Establishing connection to: {server_url}")

    keycloak_admin = kc.KeycloakAdmin(
        server_url=server_url,
        username=args.keycloak_user,
        password=args.keycloak_pass,
        user_realm_name="master",
        realm_name="crownlabs",
        verify=True)

    # Get the client information
    print(f"Retrieving client information...")
    client_info = keycloak_admin.get_client(args.client_id)
    redirect_uris = set(client_info['redirectUris'])

    if args.action == 'add':
        print(f"Adding redirect URI: {args.redirect_uri}")
        redirect_uris.add(args.redirect_uri)

    if args.action == 'remove':
        print(f"Removing redirect URI: {args.redirect_uri}")
        redirect_uris.discard(args.redirect_uri)

    print(f"Updating client information...")
    client_info['redirectUris'] = list(redirect_uris)
    client_info = keycloak_admin.update_client(args.client_id, client_info)
    print(f"Update completed correctly")
