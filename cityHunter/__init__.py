# -*- coding: utf-8 -*-


from flask import Flask


# instance_relative_config enable this file finding ../instance/config.py
app = Flask(__name__, instance_relative_config=True)

# load the default config
app.config.from_object("config.default")

# load the instance config
app.config.from_pyfile("config.py")

# load the file specified by the environment variable
# later config will override the previous configuration
app.config.from_envvar("CityHunter_CONFIG_FILE")
