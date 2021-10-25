#!/usr/bin/env python3

import sdk.session as session

def list_switch(fabric: str, name: str = ""):
    """
    List all switches in the given fabric, if no name is given.
    List switch details if a switch name is provided.
        fabric is required.
        name is optional.
    """

    # Create connection to the service
    conn = session.create_session()

    # Check with the API to see if fabric is valid

    # If no name provided, make API call to get all switches

    # If name provided, make API call to get specific switch info

    # Create results data structure, return to UI for output processing
    pass

