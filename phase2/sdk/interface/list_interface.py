#!/usr/bin/env python3

import sdk.session as session

def list_interface(switch: str, interface: str = ""):
    """
    List all interfaces on a given switch, if no interface is given.
    List interface details if an interface name is provided.
    """

    # Create connection to the service API
    conn = session.create_session()

    # Check the service to see if the switch is a valid switch

    # If interface is not provided, call API service for list of interfaces

    # If interface is provided, call API service for interface details

    # Create results structure and return to the calling UI
    pass
