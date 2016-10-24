#!/usr/bin/env python

from flask_script import Manager, Shell

from apps.main import create_app
from apps.main.config import confs
from apps.main.cmd import (CmdTest, make_shell_context,
                           CmdAdmin)
import os
import sys


if __name__ == "__main__":
    try:
        app = create_app(confs[os.environ['FLASK_CONFIG']])
    except KeyError:
        print("( FLASK_CONFIG ) didn'set")
        sys.exit(0)

    manager = Manager(app)
    manager.add_command("test", CmdTest())
    manager.add_command("shell", Shell(make_context=make_shell_context))
    manager.add_command("admin", CmdAdmin())
    manager.run()
else:
    print("Hi gunicorn")
    app = create_app(confs[os.environ['FLASK_CONFIG']])
