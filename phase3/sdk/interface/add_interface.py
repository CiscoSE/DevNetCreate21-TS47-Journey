#!/usr/bin/env python3

import sdk.session as session

def add_interface(switch: str, interface: str = None):
    """
    Add the specified logical interface (loopback, SVI, VPC, Portchannel, etc)
    to the specified switch.
    """

    # Create connection to the service API
    conn = session.create_session()

    # Check the service to see if the switch is a valid switch

    # In a more feature rich example, there would be interface attributes
    # to build into the right data structure to submit to the API.

    # Call the correct version dependent API to create the correct interface
    # type

    # Create results structure and return to the calling UI
    pass
