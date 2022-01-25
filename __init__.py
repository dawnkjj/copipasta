from flask import Flask, render_template, request, redirect, url_for, session, g
from Forms import CreateUserForm, CreateCustomerForm, SearchCustomerForm
import shelve, User, Customer

app = Flask(__name__)
app.secret_key = 'iamgod'


@app.route('/')
def home():
    return render_template('home.html')


def index():
    if not session.get("s_customer"):
        return redirect("/login")
    return render_template('index.html')


@app.route('/createUser', methods=['GET', 'POST'])
def create_user():
    create_user_form = CreateUserForm(request.form)
    if request.method == 'POST' and create_user_form.validate():
        users_dict = {}
        db = shelve.open('user.db', 'c')

        try:
            users_dict = db['Users']
        except:
            print("Error in retrieving Users from user.db.")

        user = User.User(create_user_form.username.data, create_user_form.email.data, create_user_form.gender.data,
                         create_user_form.password.data)
        users_dict[user.get_user_id()] = user
        db['Users'] = users_dict

        db.close()

        return redirect(url_for('retrieve_users'))
    return render_template('createUser.html', form=create_user_form)


@app.route('/createCustomer', methods=['GET', 'POST'])
def create_customer():
    create_customer_form = CreateCustomerForm(request.form)
    if request.method == 'POST' and create_customer_form.validate():
        customers_dict = {}
        db = shelve.open('customer.db', 'c')

        try:
            customers_dict = db['Customers']
        except:
            print("Error in retrieving Customers from customer.db.")
        customer = Customer.Customer(create_customer_form.username.data, create_customer_form.email.data,
                                     create_customer_form.gender.data, create_customer_form.password.data,
                                     create_customer_form.membership.data, create_customer_form.address.data)
        customers_dict[customer.get_customer_id()] = customer
        db['Customers'] = customers_dict

        db.close()

        return redirect(url_for('home'))
    return render_template('createCustomer.html', form=create_customer_form)


@app.route('/retrieveUsers')
def retrieve_users():
    if "user" in session:
        user = session["user"]
        return retrieve_users

    users_dict = {}
    db = shelve.open('user.db', 'r')
    users_dict = db['Users']
    db.close()
    users_list = []

    for key in users_dict:
        user = users_dict.get(key)
        users_list.append(user)

    return render_template('retrieveUsers.html', count=len(users_list), users_list=users_list)


@app.route('/retrieveCustomers')
def retrieve_customers():
    customers_dict = {}
    db = shelve.open('customer.db', 'r')
    customers_dict = db['Customers']
    db.close()

    customers_list = []
    for key in customers_dict:
        customer = customers_dict.get(key)
        customers_list.append(customer)
    return render_template('retrieveCustomers.html', count=len(customers_list), customers_list=customers_list)


@app.route('/updateUser/<int:id>/', methods=['GET', 'POST'])
def update_user(id):
    update_user_form = CreateUserForm(request.form)
    if request.method == 'POST' and update_user_form.validate():
        db = shelve.open('user.db', 'w')
        users_dict = db['Users']

        user = users_dict.get(id)
        user.set_username(update_user_form.username.data)
        user.set_email(update_user_form.email.data)

        db['Users'] = users_dict
        db.close()

        return redirect(url_for('retrieveUsers.html'))
    else:
        users_dict = {}
        db = shelve.open('user.db', 'r')
        users_dict = db['Users']
        db.close()

        user = users_dict.get(id)
        update_user_form.username.data = user.get_username()
        update_user_form.password.data = user.get_password()
        update_user_form.gender.data = user.get_gender()

        return render_template('updateUser.html', form=update_user_form)


@app.route('/updateCustomer/<int:id>/', methods=['GET', 'POST'])
def update_customer(id):
    print(id)
    update_customer_form = CreateCustomerForm(request.form)
    if request.method == 'POST' and update_customer_form.validate():
        customers_dict = {}
        db = shelve.open('customer.db', 'w')
        customers_dict = db['Customers']

        customer = customers_dict.get(id)
        customer.set_username(update_customer_form.username.data)
        customer.set_gender(update_customer_form.gender.data)
        customer.set_address(update_customer_form.address.data)
        customer.set_membership(update_customer_form.email.data)

        db['Customers'] = customers_dict
        db.close()

        return redirect(url_for('retrieveCustomer.html'))
    else:
        customers_dict = {}
        db = shelve.open('customer.db', 'r')
        customers_dict = db['Customers']
        db.close()

        customer = customers_dict.get(id)
        update_customer_form.username.data = customer.get_username()
        update_customer_form.gender.data = customer.get_gender()
        update_customer_form.address.data = customer.get_address()
        update_customer_form.membership.data = customer.get_membership()

        return render_template('updateCustomer.html', form=update_customer_form)


@app.route('/deleteUser/<int:id>', methods=['POST'])
def delete_user(id):
    users_dict = {}
    db = shelve.open('user.db', 'w')
    users_dict = db['Users']

    users_dict.pop(id)

    db['Users'] = users_dict
    db.close()

    return redirect(url_for('retrieve_users'))


@app.route('/deleteCustomer/<int:id>', methods=['POST'])
def delete_customer(id):
    customers_dict = {}
    db = shelve.open('customer.db', 'w')
    customers_dict = db['Customers']

    customers_dict.pop(id)

    db['Customers'] = customers_dict
    db.close()

    return redirect(url_for('retrieve_customers'))

    pass


users_list = []


@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = [x for x in users_list if x.id == session['user_id']][0]
        g.user = user


@app.route('/Login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('s_user', None)
        session.pop('s_customer', None)

        username = request.form['username']
        password = request.form['password']
        users_dict = {}
        db = shelve.open('user.db', 'r')
        users_dict = db['Users']
        db.close()
        users_list = []
        for key in users_dict:
            user = users_dict.get(key)
            users_list.append(user)

            # user = [x for x in users_list if x.username == username][0]
            if username == user.get_username() and password == user.get_password():
                # if username == "abc" and password == "abc":
                session['s_user'] = username
                return redirect(url_for('retrieve_users'))
            # return redirect(url_for('retrieve_customers'))
        customers_dict = {}
        db = shelve.open('customer.db', 'r')
        customers_dict = db['Customers']
        db.close()
        customers_list = []
        for key in customers_dict:
            customer = customers_dict.get(key)
            customers_list.append(customer)
            if username == customer.get_username() and password == customer.get_password():
                session['s_customer'] = username
                return redirect(url_for('profile'))
        # return redirect(url_for('retrieve_customers'))
        # return redirect(url_for('login'))

    return render_template('Login.html')


@app.route("/CustomerProfile", methods=['GET', 'POST'])
def profile():
    customers_dict = {}
    db = shelve.open('customer.db', 'r')
    customers_dict = db['Customers']
    db.close()

    customers_list = []
    for key in customers_dict:
        customer = customers_dict.get(key)
        if session['s_customer'] == customer.get_username():
            customers_list.append(customer)
    return render_template('CustomerProfile.html', count=1, customers_list=customers_list)


@app.route("/logout")
def logout():
    session.pop('s_user', None)
    session.pop('s_customer', None)
    return redirect("/")


@app.route('/searchCustomer', methods=['GET', 'POST'])
def search_Customer():
    if request.method == 'POST':
        #username = 'koo'
        username = request.form['searchCustomer']
        customers_dict = {}
        db = shelve.open('customer.db', 'r')
        customers_dict = db['Customers']
        db.close()

        customers_list = []

        for key in customers_dict:
            customer = customers_dict.get(key)
    # user = [x for x in users_list if x.username == username][0]
            if username == customer.get_username():
                customers_list.append(customer)
                return render_template('CustomerProfile.html', count=1, customers_list=customers_list)
    return render_template  ('searchCustomer.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('error404.html'), 404


if __name__ == '__main__':
    app.run()
