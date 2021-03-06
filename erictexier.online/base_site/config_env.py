# -*- coding: utf-8 -*-

import os
import sys


def get_config_files():
    """
        Envi is a python package to build environment
        variable base on package
    """

    main_dev = os.path.join(os.environ.get("DSKENV", "/"), 'python')
    if not os.path.exists(main_dev):
        return []
    sys.path.insert(0, main_dev)

    try:
        from dskenv.envi import Envi
    except Exception as e:
        print("Error No envi %s" % str(e))
        return list()
    cmd = os.environ.get("CMS_ESN", None)
    if cmd:
        Envi().execute(["from_flask", cmd], True)
        return list(filter(lambda x: x != '',
                           os.environ.get(
                               'ESN_CONF_FILE', "").split(os.pathsep)))
    return list()
