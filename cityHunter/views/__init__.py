# -*- coding: utf-8 -*-


from flask import render_template
from flask_login import login_required
from .. import app
from .util import check_expired


@app.route("/use_app")
@login_required
@check_expired
def use_app():
    """
    Using the app
    """
    return render_template("use_app.html")


@app.route("/account/billing")
@login_required
def account_billing():
    """
    update your billing info.
    """
    return render_template("account/billing.html")
