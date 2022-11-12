#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 nu

import os
import pathlib
import sys

sys.path.append(str(pathlib.Path(__file__).parent.resolve()))

from constants import Conf
from web import app

#if not os.getenv("DONT_SETUP_FILTER"):
if True:
    Conf.logger.info(f"setting up filter via {Conf.filter_module}")
    initial_setup = Conf.get_filter_func("initial_setup")
    Conf.logger.info(f"get_filter: {type(initial_setup)}")
    initial_setup()

if __name__ == "__main__":
    app.run(debug=True,host=os.getenv("BIND_TO", "0.0.0.0"), port=int(os.getenv("PORT", 5000)))
else:
    application = app
