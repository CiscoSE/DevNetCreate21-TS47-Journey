#!/usr/bin/env python3

import sdk.session as session

def add_switch(fabric: str, role: str, name: str, serial: str = "", ip: str = ""):
    """
    Add a switch to the specified fabric, with the specified switch role
    and name.  Optionally identify the switch with serial number or mgmt0
    IP address.
        fabric, role, name are required.
        serial, ip are optional.
    """

    # Create connection to the service
    conn = session.create_session()

    # Check with the API to see if fabric is valid

    # Check with the API to see if role is valid

    # Make API call to add the switch with the specified name, serial, and IP

    # Create results data structure, return to UI for output processing
    pass
