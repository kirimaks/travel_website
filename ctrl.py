#!/usr/bin/env python

import os
from flask_script import Manager, Shell

from apps.main import create_app
from apps.main.config import confs
from apps.main.cmd import (CmdTest, make_shell_context,
                           CmdAdmin)


if __name__ == "__main__":
    app = create_app(confs[os.environ.get('FLASK_CONFIG')])
    manager = Manager(app)
    manager.add_command("test", CmdTest())
    manager.add_command("shell", Shell(make_context=make_shell_context))
    manager.add_command("admin", CmdAdmin())
    manager.run()
else:
    # Create app for gunicorn or uwsgi.
    pass
