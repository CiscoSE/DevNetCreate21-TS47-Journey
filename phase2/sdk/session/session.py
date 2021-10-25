#!/usr/bin/env python3


import os
import sys
import requests
from urllib3.exceptions import InsecureRequestWarning


class session(requests.Session):
    """
    Manages the connections to the service, tracking credentials,
    token generation/renewal/expiration, and service versioning
    """
    def __init__(
        self, host: str, username: str, password: str,
        secure: bool = True, timeout: int = 30
    ):
        """
        Object instantiation will attempt to identify service version
        and authenticate against service to generate a valid token.

        host:     (required) service FQDN or IP
        username: (required) username for service
        password: (required) password for service
        secure:   (default) True = enforce TLS validation
                  False = ignore TLS validation
        timeout:  token lifetime in seconds (default 30s)
        """

        # Get service version
        self._version = self.version()

        # Authenticate to service
        self.authenticate()

    def version(self):
        """
        Identify the API version for this service.
        """
        # Make API version call and store version in this instance.
        pass

    def authenticate(self):
        """
        Use credentials to authenticate to service and get token (stored)
        """
        pass


def create_session():
    """
    The connection information is pulled from environment variables.
    """

    # If any of the 3 aren't defined, we must exit
    try:
        server_host = os.environ['SERVER_NAME']
        username = os.environ['SERVER_USER']
        password = os.environ['SERVER_PASS']
    except KeyError as key:
        print(f"Required environment variables missing: {key}")
        sys.exit(1)

    # Expect an authenticated session to be returned
    try:
        conn = session(server_host, username, password)
    except:
        # Fail gracefully
        sys.exit(1)
        pass

    return conn
