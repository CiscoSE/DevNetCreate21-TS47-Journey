#!/usr/bin/env python3

import api
from api.rest.all.core import api as rest

class core(object):
    """
    API Methods for Service common to all versions. The unique, version
    specific methods should be stored in their respective api.modes.VERSION
    file/class.
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
        Example method of get_record in versions before v12.0
        """

        print('all: get_record')
        pass
