from flask import request, current_app, flash, redirect, url_for
from flask_login import current_user


def before_app_req():
    current_app.logger.debug("Request to: [{}]".format(request.endpoint))

    if current_user.is_authenticated:
        if not current_user.confirmed and\
                "auth" not in request.endpoint:
            flash("Need to confirm account")
            return redirect(url_for('auth.unconfirmed'))
