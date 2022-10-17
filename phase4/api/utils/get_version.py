#!/usr/bin/env python3
"""
This method is one of the few that fall into the "chicken and egg"
problem of - how get I make an API call to get a version if the
API calls are versioned?

In short, we handle all the version dependencies here.
"""

def get_version(session = None) -> str:
    """
    With the given server session, attempt REST connections to it
    in order to determine its version.
    """

    # REST API Call for v11.x
    # session.get(url_11x)

    # REST API Call for v12.x
    # session.get(url_12x)

    return 'version'
