from flask import render_template, request, url_for, redirect, flash
from flask_login import login_user, logout_user, login_required, current_user

from apps.auth import auth_app
from apps.auth.forms import LoginForm, RegisterForm
from apps.auth.models import User

from apps.main import db
from apps.main.email import send_email


@auth_app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('index'))

        flash("Invalid credentials", 'error')

    return render_template("login.html", form=form)


@auth_app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out")
    return redirect(url_for('index'))


@auth_app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()

        token = user.generate_confirmation_token()
        send_email(user.email, "Confir your account",
                   template="confirm",
                   token=token)

        flash('Confirmation token has been sent to your email.')
        return redirect(url_for('index'))
    return render_template("register.html", form=form)


@auth_app.route("/confirm/<token>")
@login_required
def confirm(token):
    if current_user.confirmed:
        flash("Confirmed already")
        return redirect(url_for('index'))

    if current_user.confirm(token):
        flash("You have confirmed your account")

    else:
        flash("The confirmation link is invalid or expired.")

    return redirect(url_for('index'))


@auth_app.route("/unconfirmed")
def unconfirmed():
    if current_user.is_anonymous or current_user.confirmed:
        return redirect(url_for('index'))

    return render_template("unconfirmed.html")


@auth_app.route("/confirm")
def resend_confirmation():
    token = current_user.generate_confirmation_token()
    send_email(current_user.email, "Confir your account",
               template="confirm",
               token=token)

    flash('Confirmation token has been sent to your email.')
    return redirect(url_for('index'))
