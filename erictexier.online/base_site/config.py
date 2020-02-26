import os
import json
from base_site import config_env


CONF_FILES = config_env.get_config_files()

data = dict()
for ff in CONF_FILES:
    if os.path.exists(ff):
        with open(ff, "r") as config_file:
            localdict = json.load(config_file)
            if 'SECRET_KEY' in localdict:
                data['Flask'] = localdict
            if 'api' in localdict:
                data[localdict['api']] = localdict

if len(data) == 0:
    data['Flask'] = {
        "file" : "",
        "SECRET_KEY" : "db1f5dd00c812fd540d72835d77743a2",
        "SQLALCHEMY_DATABASE_URI" : "sqlite:///site.db",
        "MAIL_USER" : "erictexier@gmail.com",
        "MAIL_PASS" : "",
        "MAIL_SERVER" : "smtp.gmail.com",
        "MAIL_USE_SSL" : True,
        "MAIL_USE_TLS": False,
        "MAIL_PORT" : 587
        }

class Config(object):
    
    if 'Flask' in data:
        # setting for remote
        confdata = data.pop("Flask")

        SQLALCHEMY_TRACK_MODIFICATIONS = False
        SECRET_KEY = confdata.get("SECRET_KEY")
        SQLALCHEMY_DATABASE_URI = confdata.get("SQLALCHEMY_DATABASE_URI")
        MAIL_USERNAME = confdata.get("MAIL_USER","no_user")
        MAIL_PASSWORD = confdata.get("MAIL_PASS","no_pass")
        MAIL_SERVER = confdata.get('MAIL_SERVER', None)
        MAIL_USE_TLS = confdata.get('MAIL_USE_TLS', False)
        MAIL_USE_SSL = confdata.get('MAIL_USE_SSL', False)
        MAIL_PORT = confdata.get('MAIL_PORT')
        if "POSTGRES_USER" in confdata:
            SQLALCHEMY_DATABASE_URI = 'postgresql://{user}:{pw}@{url}:{pt}/{db}'.format(
                                user = confdata.get("POSTGRES_USER", "devopsuser"),
                                pw = confdata.get("POSTGRES_PW", "devops"),
                                url = confdata.get("POSTGRES_URL", "localhost"),
                                pt = confdata.get("POSTGRES_PORT", 5432),
                                db = confdata.get("POSTGRES_DB", "flaskprofiledb"))
        del confdata
for i in data:
    if i != 'Flask':
        for k in data[i]:
            if k != 'api':
                exec("Config.%s = %r" % (k, data[i][k]),locals())
