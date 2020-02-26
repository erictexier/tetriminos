import os
import sys

# Envi().execute(["from_flask","-c init -p esn_api -p google_api"], True)
# environment=DSK_STUDIO_ROOT="/opt/esn",DSK_ENV_ROOT="/opt/esn/dev",DSKENV="/opt/esn/packages/dsk_envi",DSKENVPATH="/opt/esn/dev/dsk_configuration/envi",CMS_ESN="-c init -p esn_api -p google_api"
# main_dev = "/Users/etexier/workspace/mygit/dsk_envi/python"

def get_config_files():

    main_dev = os.path.join(os.environ.get("DSKENV","/"), 'python')
    if not os.path.exists(main_dev):
        return []
    sys.path.insert(0, main_dev)

    try:
        from dskenv.envi import Envi
    except Exception as e:
        print("Error No envi %s" % str(e))
        return list()
    cmd = os.environ.get("CMS_ESN",None)
    if cmd:
        Envi().execute(["from_flask",cmd], True)
        return list(filter(lambda x: x != '', os.environ.get('ESN_CONF_FILE',"").split(os.pathsep)))
    return list()