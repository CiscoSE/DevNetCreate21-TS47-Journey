#!/usr/bin/env python3

import api

def get_api(session = None):
    if not session:
        raise Exception("Sample")

    if session.version() == 'version':
        return api.v11_5(session)
