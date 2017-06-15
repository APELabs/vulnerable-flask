from flask import Blueprint, render_template, request

bruteforce = Blueprint('bruteforce', __name__, template_folder='templates')

accounts = {'admin': 'password'}


@bruteforce.route('/brute', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            if accounts[request.form['username']] == request.form['password']:
                return render_template('brute.html.j2', logged_in=True,
                                       username=request.form['username'])
            else:
                return render_template('brute.html.j2', logged_in=False,
                                       login_failed=True)               
        except:
            return render_template('brute.html.j2', logged_in=False,
                                   login_failed=True)
    else:
        return render_template('brute.html.j2', logged_in=False,
                               login_failed=False)
