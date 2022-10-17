#!/usr/bin/env python3

from api import core
from api.rest.v12_0.core import api as rest

class v12_0(core):
    """
    API Methods for Service version 11.5.  The unique, version specific methods
    should be stored in here.  Anything supported and unchanged across the 
    supported versions should be placed in api.models.core
    """
    def __init__(self, session = None):
        """
        Reference to the service session is stored locally in order
        to make the direct API calls
        """

        if not session:
            raise Exception('Sample')

        self._api = rest(session)
    
    def get_record(self):
        """
        Example method of get_record in v12.0
        """

        print('v12_0: get_record')
        pass
