from flask import Flask, render_template, request, redirect, url_for, session, g
from Forms import CreateUserForm, CreateCustomerForm, SearchCustomerForm, UpdateUserForm, UpdateCustomerForm
from UserRequestForm import CreateRequestForm,UpdateRequestForm
from RForm import RewardForm, PackageFormA, PackageFormB, PackageFormC, PackageFormD,SearchReward
from FForm import SubmitFeedback, UpdateFeedback, SearchUser, SearchStatus
from SForms import CreateStockPaintForm, CreateStockLightingForm, CreateStockFanForm, CreateStockTileForm, CreateStockOtherForm, SearchStockFan, SearchStockLighting, SearchStockPaint, SearchStockTile, SearchStockOther

import shelve, User, Customer,Rewards, Packages, PackagesA, RequestForm, Feedback, StockPaint, StockLighting, StockFan, StockTile, StockOther

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
    update_user_form = UpdateUserForm(request.form)
    if request.method == 'POST' and update_user_form.validate():
        db = shelve.open('user.db', 'w')
        users_dict = db['Users']

        user = users_dict.get(id)
        user.set_username(update_user_form.username.data)
        user.set_email(update_user_form.email.data)
        user.set_gender(update_user_form.gender.data)
        user.set_password(update_user_form.password.data)

        db['Users'] = users_dict
        db.close()

        return redirect(url_for('retrieve_users'))
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
    update_customer_form = UpdateCustomerForm(request.form)
    if request.method == 'POST' and update_customer_form.validate():
        customers_dict = {}
        db = shelve.open('customer.db', 'w')
        customers_dict = db['Customers']

        customer = customers_dict.get(id)
        customer.set_username(update_customer_form.username.data)
        customer.set_email(update_customer_form.email.data)
        customer.set_gender(update_customer_form.gender.data)
        customer.set_address(update_customer_form.address.data)
        customer.set_membership(update_customer_form.membership.data)
        customer.set_password(update_customer_form.password.data)

        db['Customers'] = customers_dict
        db.close()

        return redirect(url_for('profile'))
    else:
        customers_dict = {}
        db = shelve.open('customer.db', 'r')
        customers_dict = db['Customers']
        db.close()

        customer = customers_dict.get(id)
        update_customer_form.username.data = customer.get_username()
        update_customer_form.email.data = customer.get_email()
        update_customer_form.gender.data = customer.get_gender()
        update_customer_form.address.data = customer.get_address()
        update_customer_form.membership.data = customer.get_membership()
        update_customer_form.password.data = customer.get_password()

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
    return render_template('searchCustomer.html')

@app.route('/Packages')
def packages():
    return render_template('Packages.html')

@app.route('/Reward')
def reward():
    return render_template('Reward.html')

@app.route('/Rewardform', methods=['GET', 'POST'])
def create_reward():
    create_reward_form = RewardForm(request.form)
    if request.method == 'POST' and create_reward_form.validate():
        rewards_dict = {}
        db = shelve.open('reward.db', 'c')

        try:
            rewards_dict = db['Rewards']
        except:
            print("Error in retrieving Customers Rewards from reward.db.")

        reward = Rewards.Reward(create_reward_form.first_name.data, create_reward_form.last_name.data, create_reward_form.phone_no.data, create_reward_form.email.data, create_reward_form.reward_type.data, create_reward_form.remarks.data)
        rewards_dict[reward.get_reward_id()] = reward
        db['Rewards'] = rewards_dict

        db.close()

        return redirect(url_for('home'))
    return render_template('Rewardform.html', form=create_reward_form)

@app.route('/retrieveReward')
def retrieve_reward():
    rewards_dict = {}
    db = shelve.open('reward.db', 'r')
    rewards_dict = db['Rewards']
    db.close()

    rewards_list = []
    for key in rewards_dict:
        reward = rewards_dict.get(key)
        rewards_list.append(reward)

    return render_template('retrieveReward.html', count=len(rewards_list), rewards_list=rewards_list)



@app.route('/deleteReward/<int:id>', methods=['POST'])
def delete_reward(id):
    rewards_dict = {}
    db = shelve.open('reward.db', 'w')
    rewards_dict = db['Rewards']

    rewards_dict.pop(id)

    db['Rewards'] = rewards_dict
    db.close()

    return redirect(url_for('retrieve_reward'))

@app.route('/updateReward/<int:id>/', methods=['GET', 'POST'])
def update_reward(id):
    update_reward_form = RewardForm(request.form)
    if request.method == 'POST' and update_reward_form.validate():
        rewards_dict = {}
        db = shelve.open('reward.db', 'w')
        rewards_dict = db['Rewards']

        reward = rewards_dict.get(id)
        reward.set_first_name(update_reward_form.first_name.data)
        reward.set_last_name(update_reward_form.last_name.data)
        reward.set_phone_no(update_reward_form.phone_no.data)
        reward.set_email(update_reward_form.email.data)
        reward.set_reward_type(update_reward_form.reward_type.data)
        reward.set_remarks(update_reward_form.remarks.data)

        db['Rewards'] = rewards_dict
        db.close()

        return redirect(url_for('retrieve_reward'))
    else:
        rewards_dict = {}
        db = shelve.open('reward.db', 'r')
        rewards_dict = db['Rewards']
        db.close()

        reward = rewards_dict.get(id)
        update_reward_form.first_name.data = reward.get_first_name()
        update_reward_form.last_name.data = reward.get_last_name()
        update_reward_form.phone_no.data = reward.get_phone_no()
        update_reward_form.email.data = reward.get_email()
        update_reward_form.reward_type.data = reward.get_reward_type()
        update_reward_form.remarks.data = reward.get_remarks()

        return render_template('updateReward.html', form=update_reward_form)

@app.route('/packageA', methods=['GET', 'POST'])
def create_packageA():
    create_packageA_form = PackageFormA(request.form)
    if request.method == 'POST' and create_packageA_form.validate():
        packageA_dict = {}
        db = shelve.open('packageA.db', 'c')

        try:
            packageA_dict = db['PackageA']
        except:
            print("Error in retrieving Packages from packageA.db.")

        package = PackagesA.PackageA(create_packageA_form.package_type.data, create_packageA_form.brand.data, create_packageA_form.installation.data,create_packageA_form.service.data, create_packageA_form.product1.data, create_packageA_form.product2.data, create_packageA_form.product3.data, create_packageA_form.design.data,create_packageA_form.cost.data)
        packageA_dict[Packages.Packages.get_order_id] = package
        db['PackageA'] = packageA_dict

        db.close()

        return redirect(url_for('home'))
    return render_template('packageA.html', form=create_packageA_form)


@app.route('/packageB', methods=['GET', 'POST'])
def create_packageB():
    create_packageB_form = PackageFormB(request.form)
    if request.method == 'POST' and create_packageB_form.validate():
        packageB_dict = {}
        db = shelve.open('packageB.db', 'c')

        try:
            packageB_dict = db['PackageB']
        except:
            print("Error in retrieving Packages from packageB.db.")

        package = PackagesA.PackageA(create_packageB_form.package_type.data, create_packageB_form.brand.data,create_packageB_form.installation.data,create_packageB_form.service.data, create_packageB_form.product1.data, create_packageB_form.product2.data, create_packageB_form.product3.data, create_packageB_form.design.data,create_packageB_form.cost.data)
        packageB_dict[Packages.Packages.get_order_id] = package
        db['Package'] = packageB_dict

        db.close()

        return redirect(url_for('home'))
    return render_template('packageB.html', form=create_packageB_form)

@app.route('/packageC', methods=['GET', 'POST'])
def create_packageC():
    create_packageC_form = PackageFormC(request.form)
    if request.method == 'POST' and create_packageC_form.validate():
        packageC_dict = {}
        db = shelve.open('packageC.db', 'c')

        try:
            packageC_dict = db['PackageC']
        except:
            print("Error in retrieving Packages from package.db.")

        package = PackagesA.PackageA(create_packageC_form.package_type.data, create_packageC_form.brand.data,create_packageC_form.installation.data,create_packageC_form.service.data, create_packageC_form.product1.data, create_packageC_form.product2.data, create_packageC_form.product3.data, create_packageC_form.design.data,create_packageC_form.cost.data)
        packageC_dict[Packages.Packages.get_order_id] = package
        db['PackageC'] = packageC_dict

        db.close()

        return redirect(url_for('home'))
    return render_template('packageC.html', form=create_packageC_form)

@app.route('/packageD', methods=['GET', 'POST'])
def create_packageD():
    create_packageD_form = PackageFormD(request.form)
    if request.method == 'POST' and create_packageD_form.validate():
        packageD_dict = {}
        db = shelve.open('packageD.db', 'c')

        try:
            packageD_dict = db['PackageD']
        except:
            print("Error in retrieving Packages from packageD.db.")

        package = PackagesA.PackageA(create_packageD_form.package_type.data, create_packageD_form.brand.data,create_packageD_form.installation.data,create_packageD_form.service.data, create_packageD_form.product1.data, create_packageD_form.product2.data, create_packageD_form.product3.data, create_packageD_form.design.data,create_packageD_form.cost.data)
        packageD_dict[Packages.Packages.get_order_id] = package
        db['PackageD'] = packageD_dict

        db.close()

        return redirect(url_for('home'))
    return render_template('packageD.html', form=create_packageD_form)

@app.route('/retrievePackageA')
def retrieve_packageA():

    packageA_dict = {}
    db = shelve.open('packageA.db', 'r')
    packageA_dict = db['PackageA']
    db.close()

    packages_list = []
    for key in packageA_dict :
        rqform = packageA_dict.get(key)
        packages_list.append(rqform)

    return render_template('retrievePackageA.html', count=len(packages_list), packages_list=packages_list)

@app.route('/retrievePackageB')
def retrieve_packageB():

    packageB_dict = {}
    db = shelve.open('packageB.db', 'r')
    packageB_dict = db['PackageB']
    db.close()

    packages_list = []
    for key in packageB_dict :
        rqform = packageB_dict.get(key)
        packages_list.append(rqform)

    return render_template('retrievePackageB.html', count=len(packages_list), packages_list=packages_list)

@app.route('/retrievePackageC')
def retrieve_packageC():

    packageC_dict = {}
    db = shelve.open('packageC.db', 'r')
    packageC_dict = db['PackageC']
    db.close()

    packages_list = []
    for key in packageC_dict :
        rqform = packageC_dict.get(key)
        packages_list.append(rqform)

    return render_template('retrievePackageC.html', count=len(packages_list), packages_list=packages_list)

@app.route('/retrievePackageD')
def retrieve_packageD():

    packageD_dict = {}
    db = shelve.open('packageD.db', 'r')
    packageD_dict = db['PackageD']
    db.close()

    packages_list = []
    for key in packageD_dict :
        rqform = packageD_dict.get(key)
        packages_list.append(rqform)

    return render_template('retrievePackageD.html', count=len(packages_list), packages_list=packages_list)


@app.route('/deletePackage/<int:id>', methods=['POST'])
def delete_package(id):
    package_dict = {}
    db = shelve.open('package.db', 'w')
    package_dict = db['Package']

    package_dict.pop(id)

    db['Package'] = package_dict
    db.close()

    return redirect(url_for('retrieve_packages'))

@app.route('/updatePackageA/<int:id>/', methods=['GET', 'POST'])
def update_packageA(id):
    update_packageA_form = PackageFormA(request.form)
    if request.method == 'POST' and update_packageA_form.validate():
        package_dict = {}
        db = shelve.open('package.db', 'w')
        package_dict = db['Package']

        package = package_dict.get(id)
        package.set_package_type(update_packageA_form.package_type.data)
        package.set_brand(update_packageA_form.brand.data)
        package.set_installation(update_packageA_form.installation.data)
        package.set_service(update_packageA_form.service.data)
        package.set_product1(update_packageA_form.product1.data)
        package.set_product2(update_packageA_form.product2.data)
        package.set_product3(update_packageA_form.product3.data)
        package.set_design(update_packageA_form.design.data)

        db['Package'] = package_dict
        db.close()

        return redirect(url_for('retrieve_packages'))
    else:
        package_dict = {}
        db = shelve.open('package.db', 'r')
        package_dict = db['Package']
        db.close()

        package = package_dict.get(id)
        update_packageA_form.package_type.data = package.get_package_type()
        update_packageA_form.brand.data = package.get_brand()
        update_packageA_form.installation.data = package.get_installation()
        update_packageA_form.service.data = package.get_service()
        update_packageA_form.product1.data = package.get_product1()
        update_packageA_form.product2.data = package.get_product2()
        update_packageA_form.product3.data = package.get_product3()
        update_packageA_form.design.data = package.get_design()

        return render_template('updatePackages.html', form=update_packageA_form)

@app.route('/searchReward', methods=['GET', 'POST'])
def search_reward():
    search_reward_form = SearchReward(request.form)
    if request.method == "POST" and search_reward_form.validate():
        search = search_reward_form.searchUser.data
        rewards_dict = {}
        db = shelve.open("reward.db", "r")
        rewards_dict = db['Rewards']
        db.close()

        rewards_list = []
        for key in rewards_dict:
            reward = rewards_dict.get(key)

            if reward.get_first_name() == search:
                rewards_list.append(reward)
            else:
                continue

        if len(rewards_list) != 0:
            return render_template("retrieveReward.html", count=len(rewards_list), feedback_list=rewards_list)
        else:
            return render_template("noResults.html")

    return render_template("searchReward.html", form=search_reward_form)

@app.route('/createRequestForm', methods=['GET', 'POST'])
def create_request_form():
    create_request_form = CreateRequestForm(request.form)
    if request.method == 'POST' and create_request_form.validate():
        userrequestform_dict = {}
        db = shelve.open('userrequestform.db', 'c')

        try:
            userrequestform_dict = db['UserRequestForm']
        except:
            print("Error in retrieving from userrequestform.db.")

        #customer_id = "cust001" #customer_id = session["loginid"]

        amount = 0
        if create_request_form.type_of_services.data == "Installation":
            amount = amount + 200
        elif create_request_form.type_of_services.data == "Painting":
            amount = amount + 400
        elif create_request_form.type_of_services.data == "Wall Hacking":
            amount = amount + 600
        elif create_request_form.type_of_services.data == "Carpentry":
            amount = amount + 800
        if create_request_form.type_of_installation.data == "Full":
            amount = amount + 2000
        elif create_request_form.type_of_installation.data == "Partial":
            amount = amount + 1000

        rqform = RequestForm.RequestForm(create_request_form.type_of_services.data, create_request_form.type_of_installation.data, create_request_form.type_of_items.data, create_request_form.type_of_brands.data, create_request_form.items_available.data)
# rqform.set_customer_id(customer_id) #-> need to know which customer paid for which amount.

        rqform.set_amount(amount)
        print("**",create_request_form.type_of_services.data,create_request_form.type_of_installation.data)
        print("*** amount",rqform.get_amount())
        userrequestform_dict[rqform.get_request_id()] = rqform
        db['UserRequestForm'] = userrequestform_dict

        return redirect(url_for('cartpage'))
    return render_template('createRequestForm.html', form=create_request_form)


@app.route('/updateUserRequestForm/<int:id>/', methods=['GET', 'POST'])
def update_userrequestforms(id):
    update_userrequest_form = CreateRequestForm(request.form)
    if request.method == 'POST' and update_userrequest_form.validate():
        userrequestform_dict = {}
        db = shelve.open('userrequestform.db', 'w')
        userrequestform_dict = db['UserRequestForm']

        rqform = userrequestform_dict.get(id)
        rqform.set_type_of_services(update_userrequest_form.type_of_services.data)
        rqform.set_type_of_installation(update_userrequest_form.type_of_installation.data)
        rqform.set_type_of_items(update_userrequest_form.type_of_items.data)
        rqform.set_type_of_brands(update_userrequest_form.type_of_brands.data)
        rqform.set_items_available(update_userrequest_form.items_available.data)

        amount = 0
        if update_userrequest_form.type_of_services.data == "Installation":
            amount = amount + 200
        elif update_userrequest_form.type_of_services.data == "Painting":
            amount = amount + 400
        elif update_userrequest_form.type_of_services.data == "Wall Hacking":
            amount = amount + 600
        elif update_userrequest_form.type_of_services.data == "Carpentry":
            amount = amount + 800
        if update_userrequest_form.type_of_installation.data == "Full":
            amount = amount + 2000
        elif update_userrequest_form.type_of_installation.data == "Partial":
            amount = amount + 1000

        rqform.set_amount(amount)
        print("*** amount",rqform.get_amount())
        db['UserRequestForm'] = userrequestform_dict
        db.close()

        return redirect(url_for('cartpage'))

    else:
        userrequestform_dict = {}
        db = shelve.open('userrequestform.db', 'r')
        userrequestform_dict = db['UserRequestForm']
        db.close()

        rqform = userrequestform_dict.get(id)
        update_userrequest_form.type_of_services.data = rqform.get_type_of_services()
        update_userrequest_form.type_of_installation.data = rqform.get_type_of_installation()
        update_userrequest_form.type_of_items.data = rqform.get_type_of_items()
        update_userrequest_form.type_of_brands.data = rqform.get_type_of_brands()
        update_userrequest_form.items_available.data = rqform.get_items_available()
        return render_template('updateUserRequestForm.html', form=update_userrequest_form)


@app.route('/deleteUserRequestForm/<int:id>', methods=['POST'])
def delete_userrequestform(id):

    userrequestform_dict = {}
    db = shelve.open('userrequestform.db', 'w')
    userrequestform_dict = db['UserRequestForm']

    userrequestform_dict.pop(id)
    print(userrequestform_dict.get(id))
    db['UserRequestForm'] = userrequestform_dict
    db.close()

    return redirect(url_for('cartpage'))


@app.route('/CartPage')
def cartpage():

    userrequestform_dict = {}
    db = shelve.open('userrequestform.db', 'r')
    userrequestform_dict = db['UserRequestForm']
    db.close()

    usersrequestform_list = []
    for key in userrequestform_dict:
        form = userrequestform_dict.get(key)
        usersrequestform_list.append(form)

    return render_template('CartPage.html', count=len(usersrequestform_list), usersrequestform_list=usersrequestform_list)
# request id overrun because it's a number, have to change to string and add a field for user to input to prevent overwrite.

@app.route('/retrieveUserRequestForm')
def retrieve_usersrequestforms():

    userrequestform_dict = {}
    db = shelve.open('userrequestform.db', 'r')
    userrequestform_dict = db['UserRequestForm']
    db.close()

    usersrequestform_list = []
    for key in userrequestform_dict:
        form = userrequestform_dict.get(key)
        usersrequestform_list.append(form)

    return render_template('retrieveUserRequestForm.html', count=len(usersrequestform_list), usersrequestform_list=usersrequestform_list)


@app.route('/updateAdminRequestForm/<int:id>/', methods=['GET', 'POST'])
def update_adminrequestforms(id):
    update_adminrequest_form = UpdateRequestForm(request.form)
    if request.method == 'POST' and update_adminrequest_form.validate():
        userrequestform_dict = {}
        db = shelve.open('userrequestform.db', 'w')
        userrequestform_dict = db['UserRequestForm']

        form = userrequestform_dict.get(id)

        form.set_startdate(update_adminrequest_form.startdate.data)
        form.set_enddate(update_adminrequest_form.enddate.data)
        form.set_workcompletion_status(update_adminrequest_form.workcompletion_status.data)
        form.set_remarks(update_adminrequest_form.remarks.data)
        db['UserRequestForm'] = userrequestform_dict
        db.close()

        return redirect(url_for('retrieve_usersrequestforms'))

    else:
        userrequestform_dict = {}
        db = shelve.open('userrequestform.db', 'r')
        userrequestform_dict = db['UserRequestForm']
        db.close()

        form = userrequestform_dict.get(id)

        update_adminrequest_form.startdate.data = form.get_startdate()
        update_adminrequest_form.enddate.data = form.get_enddate()
        update_adminrequest_form.workcompletion_status.data = form.get_workcompletion_status()
        update_adminrequest_form.remarks.data = form.get_remarks()
        return render_template('updateAdminRequestForm.html', form=update_adminrequest_form)


@app.route('/Showroom')
def showroom():
    return render_template('showroom.html')

@app.route('/submitFeedback', methods=['GET', 'POST'])
def submit_feedback():
    submit_feedback_form = SubmitFeedback(request.form)
    if request.method == 'POST' and submit_feedback_form.validate():
        feedback_dict = {}
        db = shelve.open('feedback.db', 'c')

        try:
            feedback_dict = db['Feedbacks']
        except:
            print("Error in retrieving Feedbacks from feedback.db")

        feedback = Feedback.Feedback(submit_feedback_form.first_name.data, submit_feedback_form.last_name.data, submit_feedback_form.email.data, submit_feedback_form.service_rating.data, submit_feedback_form.web_rating.data, submit_feedback_form.feedback.data)
        feedback.set_status('pending')
        feedback_dict[feedback.get_user_id()] = feedback
        db['Feedbacks'] = feedback_dict
        #TEst codes
        feedback_dict = db['Feedbacks']
        feedback = feedback_dict[feedback.get_user_id()]
        print("***  status ***", feedback.get_status())


        db.close()

        return redirect(url_for('view_feedback'))
    return render_template('submitFeedback.html', form=submit_feedback_form)


@app.route('/viewFeedback')
def view_feedback():
    feedback_dict = {}
    db = shelve.open('feedback.db', 'r')
    feedback_dict = db['Feedbacks']
    db.close()

    feedback_list = []
    for key in feedback_dict:
        feedback = feedback_dict.get(key)
        feedback_list.append(feedback)

    return render_template('viewFeedback.html', count=len(feedback_list), feedback_list=feedback_list)


@app.route('/retrieveFeedback')
def retrieve_feedback():
    feedback_dict = {}
    db = shelve.open('feedback.db', 'r')
    feedback_dict = db['Feedbacks']
    db.close()

    feedback_list = []
    for key in feedback_dict:
        feedback = feedback_dict.get(key)
        feedback_list.append(feedback)

    return render_template('retrieveFeedback.html', count=len(feedback_list), feedback_list=feedback_list)


@app.route('/deleteFeedback/<int:id>', methods=['POST'])
def delete_feedback(id):
    feedback_dict = {}
    db = shelve.open('feedback.db', 'w')
    feedback_dict = db['Feedbacks']

    feedback_dict.pop(id)

    db['Feedbacks'] = feedback_dict
    db.close()

    return redirect(url_for('retrieve_feedback'))


@app.route('/updateFeedback/<int:id>/', methods=['GET', 'POST'])
def update_feedback(id):
    update_feedback_form = UpdateFeedback(request.form)
    if request.method == 'POST' and update_feedback_form.validate():
        feedback_dict = {}
        db = shelve.open('feedback.db', 'w')
        feedback_dict = db['Feedbacks']

        feedback = feedback_dict.get(id)
        feedback.set_first_name(update_feedback_form.first_name.data)
        feedback.set_last_name(update_feedback_form.last_name.data)
        feedback.set_email(update_feedback_form.email.data)
        feedback.set_service_rating(update_feedback_form.service_rating.data)
        feedback.set_web_rating(update_feedback_form.web_rating.data)
        feedback.set_feedback(update_feedback_form.feedback.data)
        feedback.set_status(update_feedback_form.status.data)

        db['Feedbacks'] = feedback_dict
        db.close()

        return redirect(url_for('retrieve_feedback'))
    else:
        feedback_dict = {}
        db = shelve.open('feedback.db', 'r')
        feedback_dict = db['Feedbacks']
        db.close()

        feedback = feedback_dict.get(id)
        update_feedback_form.first_name.data = feedback.get_first_name()
        update_feedback_form.last_name.data = feedback.get_last_name()
        update_feedback_form.email.data = feedback.get_email()
        update_feedback_form.service_rating.data = feedback.get_service_rating()
        update_feedback_form.web_rating.data = feedback.get_web_rating()
        update_feedback_form.feedback.data = feedback.get_feedback()
        update_feedback_form.status.data = feedback.get_status()

        return render_template('updateFeedback.html', form=update_feedback_form)


@app.route('/searchUser', methods=['GET', 'POST'])
def search_user():
    search_user_form = SearchUser(request.form)
    if request.method == "POST" and search_user_form.validate():
        search = search_user_form.searchUser.data
        feedback_dict = {}
        db = shelve.open("feedback.db", "r")
        feedback_dict = db['Feedbacks']
        db.close()

        feedback_list = []
        for key in feedback_dict:
            feedback = feedback_dict.get(key)

            if feedback.get_first_name() == search:
                feedback_list.append(feedback)
            else:
                continue

        if len(feedback_list) != 0:
            return render_template("retrieveFeedback.html", count=len(feedback_list), feedback_list=feedback_list)
        else:
            return render_template("noResults.html")

    return render_template("searchUser.html", form=search_user_form)


@app.route('/searchStatus', methods=['GET', 'POST'])
def search_status():
    search_status_form = SearchStatus(request.form)
    if request.method == "POST" and search_status_form.validate():
        search2 = search_status_form.searchStatus.data
        feedback_dict = {}
        db = shelve.open("feedback.db", "r")
        feedback_dict = db['Feedbacks']
        db.close()

        feedback_list = []
        for key in feedback_dict:
            feedback = feedback_dict.get(key)

            if feedback.get_status() == search2:
                feedback_list.append(feedback)
            else:
                continue

        if len(feedback_list) != 0:
            return render_template("retrieveFeedback.html", count=len(feedback_list), feedback_list=feedback_list)
        else:
            return render_template('noResults.html')

    return render_template("searchStatus.html", form=search_status_form)

@app.route('/searchFan')
def searchFan():
    return render_template('searchFan.html')

@app.route('/searchLighting')
def searchLighting():
    return render_template('searchLighting.html')

@app.route('/searchOther')
def searchOther():
    return render_template('searchOther.html')

@app.route('/searchPaint')
def searchPaint():
    return render_template('searchPaint.html')

@app.route('/searchTile')
def searchTile():
    return render_template('searchTile.html')

@app.route('/brands')
def brands():
    return render_template('brands.html')

@app.route('/brands2')
def brands2():
    return render_template('brands2.html')

@app.route('/brandsAccount')
def brandsAccount():
    return render_template('brandsAccount.html')

@app.route('/createStockPaint', methods=['GET', 'POST'])
def create_stockPaint():
    create_stockPaint_form = CreateStockPaintForm(request.form)
    if request.method == 'POST' and create_stockPaint_form.validate():
        stockPaints_dict = {}
        db = shelve.open('stockPaint.db', 'c')

        try:
            stockPaints_dict = db['StockPaints']
        except:
            print("Error in retrieving StockPaints from stockPaint.db.")

        stockPaint = StockPaint.StockPaint(create_stockPaint_form.stock_name.data,
                                                    create_stockPaint_form.stock_count.data,
                                                    create_stockPaint_form.colour.data,
                                                    create_stockPaint_form.price.data,
                                                    create_stockPaint_form.date_created.data,
                                                    create_stockPaint_form.remarks.data)
        stockPaints_dict[stockPaint.get_stock_id()] = stockPaint
        db['StockPaints'] = stockPaints_dict

        db.close()

        return redirect(url_for('retrieve_stockPaints'))

    return render_template('createStockPaint.html', form=create_stockPaint_form)


@app.route('/retrieveStockPaints')
def retrieve_stockPaints():
    stockPaints_dict = {}
    db = shelve.open('stockPaint.db', 'r')
    stockPaints_dict = db['StockPaints']
    db.close()

    stockPaints_list = []
    for key in stockPaints_dict:
        stockPaint = stockPaints_dict.get(key)
        stockPaints_list.append(stockPaint)

    return render_template('retrieveStockPaints.html', count=len(stockPaints_list), stockPaints_list=stockPaints_list)


@app.route('/updateStockPaints/<int:id>/', methods=['GET', 'POST'])
def update_stockPaint(id):
    update_stockPaint_form = CreateStockPaintForm(request.form)
    if request.method == 'POST' and update_stockPaint_form.validate():
        stockPaints_dict = {}
        db = shelve.open('stockPaint.db', 'w')
        stockPaints_dict = db['StockPaints']

        stockPaint = stockPaints_dict.get(id)
        stockPaint.set_stock_name(update_stockPaint_form.stock_name.data)
        stockPaint.set_stock_count(update_stockPaint_form.stock_count.data)
        stockPaint.set_colour(update_stockPaint_form.colour.data)
        stockPaint.set_price(update_stockPaint_form.price.data)
        stockPaint.set_date_created(update_stockPaint_form.date_created.data)
        stockPaint.set_remarks(update_stockPaint_form.remarks.data)

        db['StockPaints'] = stockPaints_dict
        db.close()

        return redirect(url_for('retrieve_stockPaints'))
    else:
        stockPaints_dict = {}
        db = shelve.open('stockPaint.db', 'r')
        stockPaints_dict = db['StockPaints']
        db.close()

        stockPaint = stockPaints_dict.get(id)
        update_stockPaint_form.stock_name.data = stockPaint.get_stock_name()
        update_stockPaint_form.stock_count.data = stockPaint.get_stock_count()
        update_stockPaint_form.colour.data = stockPaint.get_colour()
        update_stockPaint_form.price.data = stockPaint.get_price()
        update_stockPaint_form.date_created.data = stockPaint.get_date_created()
        update_stockPaint_form.remarks.data = stockPaint.get_remarks()

        return render_template('updateStockPaints.html', form=update_stockPaint_form)


@app.route('/deleteStockPaint/<int:id>', methods=['POST'])
def delete_stockPaint(id):
    stockPaints_dict = {}
    db = shelve.open('stockPaint.db', 'w')
    stockPaints_dict = db['StockPaints']

    stockPaints_dict.pop(id)

    db['StockPaints'] = stockPaints_dict
    db.close()

    return redirect(url_for('retrieve_stockPaints'))


@app.route('/createStockLighting', methods=['GET', 'POST'])
def create_stockLighting():
    create_stockLighting_form = CreateStockLightingForm(request.form)
    if request.method == 'POST' and create_stockLighting_form.validate():
        stockLightings_dict = {}
        db = shelve.open('stockLighting.db', 'c')

        try:
            stockLightings_dict = db['StockLightings']
        except:
            print("Error in retrieving StockLightings from stockLighting.db.")

        stockLighting = StockLighting.StockLighting(create_stockLighting_form.stock_name.data,
                                                    create_stockLighting_form.stock_count.data,
                                                    create_stockLighting_form.colour.data,
                                                    create_stockLighting_form.price.data,
                                                    create_stockLighting_form.date_created.data,
                                                    create_stockLighting_form.remarks.data)
        stockLightings_dict[stockLighting.get_stock_id()] = stockLighting
        db['StockLightings'] = stockLightings_dict

        db.close()

        return redirect(url_for('retrieve_stockLightings'))

    return render_template('createStockLighting.html', form=create_stockLighting_form)


@app.route('/retrieveStockLightings')
def retrieve_stockLightings():
    stockLightings_dict = {}
    db = shelve.open('stockLighting.db', 'r')
    stockLightings_dict = db['StockLightings']
    db.close()

    stockLightings_list = []
    for key in stockLightings_dict:
        stockLighting = stockLightings_dict.get(key)
        stockLightings_list.append(stockLighting)

    return render_template('retrieveStockLightings.html', count=len(stockLightings_list),
                           stockLightings_list=stockLightings_list)


@app.route('/updateStockLightings/<int:id>/', methods=['GET', 'POST'])
def update_stockLighting(id):
    update_stockLighting_form = CreateStockLightingForm(request.form)
    if request.method == 'POST' and update_stockLighting_form.validate():
        stockLightings_dict = {}
        db = shelve.open('stockLighting.db', 'w')
        stockLightings_dict = db['StockLightings']

        stockLighting = stockLightings_dict.get(id)
        stockLighting.set_stock_name(update_stockLighting_form.stock_name.data)
        stockLighting.set_stock_count(update_stockLighting_form.stock_count.data)
        stockLighting.set_colour(update_stockLighting_form.colour.data)
        stockLighting.set_price(update_stockLighting_form.price.data)
        stockLighting.set_date_created(update_stockLighting_form.date_created.data)
        stockLighting.set_remarks(update_stockLighting_form.remarks.data)

        db['StockLightings'] = stockLightings_dict
        db.close()

        return redirect(url_for('retrieve_stockLightings'))
    else:
        stockLightings_dict = {}
        db = shelve.open('stockLighting.db', 'r')
        stockLightings_dict = db['StockLightings']
        db.close()

        stockLighting = stockLightings_dict.get(id)
        update_stockLighting_form.stock_name.data = stockLighting.get_stock_name()
        update_stockLighting_form.stock_count.data = stockLighting.get_stock_count()
        update_stockLighting_form.colour.data = stockLighting.get_colour()
        update_stockLighting_form.price.data = stockLighting.get_price()
        update_stockLighting_form.date_created.data = stockLighting.get_date_created()
        update_stockLighting_form.remarks.data = stockLighting.get_remarks()

        return render_template('updateStockLightings.html', form=update_stockLighting_form)


@app.route('/deleteStockLighting/<int:id>', methods=['POST'])
def delete_stockLighting(id):
    stockLightings_dict = {}
    db = shelve.open('stockLighting.db', 'w')
    stockLightings_dict = db['StockLightings']

    stockLightings_dict.pop(id)

    db['StockLightings'] = stockLightings_dict
    db.close()

    return redirect(url_for('retrieve_stockLightings'))


@app.route('/createStockFan', methods=['GET', 'POST'])
def create_stockFan():
    create_stockFan_form = CreateStockFanForm(request.form)
    if request.method == 'POST' and create_stockFan_form.validate():
        stockFans_dict = {}
        db = shelve.open('stockFan.db', 'c')

        try:
            stockFans_dict = db['StockFans']
        except:
            print("Error in retrieving StockFans from stockFan.db.")

        stockFan = StockFan.StockFan(create_stockFan_form.stock_name.data, create_stockFan_form.stock_count.data,
                                     create_stockFan_form.colour.data, create_stockFan_form.price.data,
                                     create_stockFan_form.date_created.data,
                                     create_stockFan_form.remarks.data)
        stockFans_dict[stockFan.get_stock_id()] = stockFan
        db['StockFans'] = stockFans_dict

        db.close()

        return redirect(url_for('retrieve_stockFans'))

    return render_template('createStockFan.html', form=create_stockFan_form)


@app.route('/retrieveStockFans')
def retrieve_stockFans():
    stockFans_dict = {}
    db = shelve.open('stockFan.db', 'r')
    stockFans_dict = db['StockFans']
    db.close()

    stockFans_list = []
    for key in stockFans_dict:
        stockFan = stockFans_dict.get(key)
        stockFans_list.append(stockFan)

    return render_template('retrieveStockFans.html', count=len(stockFans_list), stockFans_list=stockFans_list)


@app.route('/updateStockFans/<int:id>/', methods=['GET', 'POST'])
def update_stockFan(id):
    update_stockFan_form = CreateStockFanForm(request.form)
    if request.method == 'POST' and update_stockFan_form.validate():
        stockFans_dict = {}
        db = shelve.open('stockFan.db', 'w')
        stockFans_dict = db['StockFans']

        stockFan = stockFans_dict.get(id)
        stockFan.set_stock_name(update_stockFan_form.stock_name.data)
        stockFan.set_stock_count(update_stockFan_form.stock_count.data)
        stockFan.set_colour(update_stockFan_form.colour.data)
        stockFan.set_price(update_stockFan_form.price.data)
        stockFan.set_price(update_stockFan_form.date_created.data)
        stockFan.set_remarks(update_stockFan_form.remarks.data)

        db['StockFans'] = stockFans_dict
        db.close()

        return redirect(url_for('retrieve_stockFans'))
    else:
        stockFans_dict = {}
        db = shelve.open('stockFan.db', 'r')
        stockFans_dict = db['StockFans']
        db.close()

        stockFan = stockFans_dict.get(id)
        update_stockFan_form.stock_name.data = stockFan.get_stock_name()
        update_stockFan_form.stock_count.data = stockFan.get_stock_count()
        update_stockFan_form.colour.data = stockFan.get_colour()
        update_stockFan_form.price.data = stockFan.get_price()
        update_stockFan_form.date_created.data = stockFan.get_date_created()
        update_stockFan_form.remarks.data = stockFan.get_remarks()

        return render_template('updateStockFans.html', form=update_stockFan_form)


@app.route('/deleteStockFan/<int:id>', methods=['POST'])
def delete_stockFan(id):
    stockFans_dict = {}
    db = shelve.open('stockFan.db', 'w')
    stockFans_dict = db['StockFans']

    stockFans_dict.pop(id)

    db['StockFans'] = stockFans_dict
    db.close()

    return redirect(url_for('retrieve_stockFans'))

@app.route('/createStockTile', methods=['GET', 'POST'])
def create_stockTile():
    create_stockTile_form = CreateStockTileForm(request.form)
    if request.method == 'POST' and create_stockTile_form.validate():
        stockTiles_dict = {}
        db = shelve.open('stockTile.db', 'c')

        try:
            stockTiles_dict = db['StockTiles']
        except:
            print("Error in retrieving StockTiles from stockTile.db.")

        stockTile = StockTile.StockTile(create_stockTile_form.stock_name.data,
                                           create_stockTile_form.stock_count.data,
                                           create_stockTile_form.colour.data,
                                           create_stockTile_form.price.data,
                                           create_stockTile_form.date_created.data,
                                           create_stockTile_form.remarks.data)
        stockTiles_dict[stockTile.get_stock_id()] = stockTile
        db['StockTiles'] = stockTiles_dict

        db.close()

        return redirect(url_for('retrieve_stockTiles'))

    return render_template('createStockTile.html', form=create_stockTile_form)


@app.route('/retrieveStockTiles')
def retrieve_stockTiles():
    stockTiles_dict = {}
    db = shelve.open('stockTile.db', 'r')
    stockTiles_dict = db['StockTiles']
    db.close()

    stockTiles_list = []
    for key in stockTiles_dict:
        stockTile = stockTiles_dict.get(key)
        stockTiles_list.append(stockTile)

    return render_template('retrieveStockTiles.html', count=len(stockTiles_list), stockTiles_list=stockTiles_list)


@app.route('/updateStockTiles/<int:id>/', methods=['GET', 'POST'])
def update_stockTile(id):
    update_stockTile_form = CreateStockTileForm(request.form)
    if request.method == 'POST' and update_stockTile_form.validate():
        stockTiles_dict = {}
        db = shelve.open('stockTile.db', 'w')
        stockTiles_dict = db['StockTiles']

        stockTile = stockTiles_dict.get(id)
        stockTile.set_stock_name(update_stockTile_form.stock_name.data)
        stockTile.set_stock_count(update_stockTile_form.stock_count.data)
        stockTile.set_colour(update_stockTile_form.colour.data)
        stockTile.set_price(update_stockTile_form.price.data)
        stockTile.set_date_created(update_stockTile_form.date_created.data)
        stockTile.set_remarks(update_stockTile_form.remarks.data)

        db['StockTiles'] = stockTiles_dict
        db.close()

        return redirect(url_for('retrieve_stockTiles'))
    else:
        stockTiles_dict = {}
        db = shelve.open('stockTile.db', 'r')
        stockTiles_dict = db['StockTiles']
        db.close()

        stockTile = stockTiles_dict.get(id)
        update_stockTile_form.stock_name.data = stockTile.get_stock_name()
        update_stockTile_form.stock_count.data = stockTile.get_stock_count()
        update_stockTile_form.colour.data = stockTile.get_colour()
        update_stockTile_form.price.data = stockTile.get_price()
        update_stockTile_form.date_created.data = stockTile.get_date_created()
        update_stockTile_form.remarks.data = stockTile.get_remarks()

        return render_template('updateStockTiles.html', form=update_stockTile_form)


@app.route('/deleteStockTile/<int:id>', methods=['POST'])
def delete_stockTile(id):
    stockTiles_dict = {}
    db = shelve.open('stockTile.db', 'w')
    stockTiles_dict = db['StockTiles']

    stockTiles_dict.pop(id)

    db['StockTiles'] = stockTiles_dict
    db.close()

    return redirect(url_for('retrieve_stockTiles'))

@app.route('/createStockOther', methods=['GET', 'POST'])
def create_stockOther():
    create_stockOther_form = CreateStockOtherForm(request.form)
    if request.method == 'POST' and create_stockOther_form.validate():
        stockOthers_dict = {}
        db = shelve.open('stockOther.db', 'c')

        try:
            stockOthers_dict = db['StockOthers']
        except:
            print("Error in retrieving StockOthers from stockOther.db.")

        stockOther = StockOther.StockOther(create_stockOther_form.stock_name.data,
                                           create_stockOther_form.stock_count.data,
                                           create_stockOther_form.colour.data,
                                           create_stockOther_form.price.data,
                                           create_stockOther_form.date_created.data,
                                           create_stockOther_form.remarks.data)
        stockOthers_dict[stockOther.get_stock_id()] = stockOther
        db['StockOthers'] = stockOthers_dict

        db.close()

        return redirect(url_for('retrieve_stockOthers'))

    return render_template('createStockOther.html', form=create_stockOther_form)


@app.route('/retrieveStockOthers')
def retrieve_stockOthers():
    stockOthers_dict = {}
    db = shelve.open('stockOther.db', 'r')
    stockOthers_dict = db['StockOthers']
    db.close()

    stockOthers_list = []
    for key in stockOthers_dict:
        stockOther = stockOthers_dict.get(key)
        stockOthers_list.append(stockOther)

    return render_template('retrieveStockOthers.html', count=len(stockOthers_list), stockOthers_list=stockOthers_list)


@app.route('/updateStockOthers/<int:id>/', methods=['GET', 'POST'])
def update_stockOther(id):
    update_stockOther_form = CreateStockOtherForm(request.form)
    if request.method == 'POST' and update_stockOther_form.validate():
        stockOthers_dict = {}
        db = shelve.open('stockOther.db', 'w')
        stockOthers_dict = db['StockOthers']

        stockOther = stockOthers_dict.get(id)
        stockOther.set_stock_name(update_stockOther_form.stock_name.data)
        stockOther.set_stock_count(update_stockOther_form.stock_count.data)
        stockOther.set_colour(update_stockOther_form.colour.data)
        stockOther.set_price(update_stockOther_form.price.data)
        stockOther.set_date_created(update_stockOther_form.date_created.data)
        stockOther.set_remarks(update_stockOther_form.remarks.data)

        db['StockOthers'] = stockOthers_dict
        db.close()

        return redirect(url_for('retrieve_stockOthers'))
    else:
        stockOthers_dict = {}
        db = shelve.open('stockOther.db', 'r')
        stockOthers_dict = db['StockOthers']
        db.close()

        stockOther = stockOthers_dict.get(id)
        update_stockOther_form.stock_name.data = stockOther.get_stock_name()
        update_stockOther_form.stock_count.data = stockOther.get_stock_count()
        update_stockOther_form.colour.data = stockOther.get_colour()
        update_stockOther_form.price.data = stockOther.get_price()
        update_stockOther_form.date_created.data = stockOther.get_date_created()
        update_stockOther_form.remarks.data = stockOther.get_remarks()

        return render_template('updateStockOthers.html', form=update_stockOther_form)


@app.route('/deleteStockOther/<int:id>', methods=['POST'])
def delete_stockOther(id):
    stockOthers_dict = {}
    db = shelve.open('stockOther.db', 'w')
    stockOthers_dict = db['StockOthers']

    stockOthers_dict.pop(id)

    db['StockOthers'] = stockOthers_dict
    db.close()

    return redirect(url_for('retrieve_stockOthers'))


@app.route('/searchStockFan', methods=['GET', 'POST'])
def search_stockFan():
    search_stockFan_form = SearchStockFan(request.form)
    if request.method == "POST" and search_stockFan_form.validate():
        search = search_stockFan_form.searchStockFan.data
        stockFan_dict = {}
        db = shelve.open("stockFan.db", "r")
        stockFan_dict = db['StockFans']
        db.close()

        stockFans_list = []
        for key in stockFan_dict:
            stockFan = stockFan_dict.get(key)

            if stockFan.get_stock_name() == search:
                stockFans_list.append(stockFan)
            else:
                continue

        if len(stockFans_list) != 0:
            return render_template("showStockFan.html", count=len(stockFans_list), stockFans_list=stockFans_list)
        else:
            return render_template("noResults.html")

    return render_template("searchStockFan.html", form=search_stockFan_form)

@app.route('/searchStockFanPrice', methods=['GET', 'POST'])
def search_stockFanPrice():
    search_stockFanPrice_form = SearchStockFan(request.form)
    if request.method == "POST" and search_stockFanPrice_form.validate():
        search = search_stockFanPrice_form.searchStockFan.data
        stockFan_dict = {}
        db = shelve.open("stockFan.db", "r")
        stockFan_dict = db['StockFans']
        db.close()

        stockFans_list = []
        for key in stockFan_dict:
            stockFan = stockFan_dict.get(key)

            if stockFan.get_price() < search:
                stockFans_list.append(stockFan)
            else:
                continue

        if len(stockFans_list) != 0:
            return render_template("showStockFan.html", count=len(stockFans_list), stockFans_list=stockFans_list)
        else:
            return render_template("noResults.html")

    return render_template("searchStockFan.html", form=search_stockFanPrice_form)

@app.route('/searchStockLighting', methods=['GET', 'POST'])
def search_stockLighting():
    search_stockLighting_form = SearchStockLighting(request.form)
    if request.method == "POST" and search_stockLighting_form.validate():
        search = search_stockLighting_form.searchStockLighting.data
        stockLighting_dict = {}
        db = shelve.open("stockLighting.db", "r")
        stockLighting_dict = db['StockLightings']
        db.close()

        stockLighting_list = []
        for key in stockLighting_dict:
            stockLighting = stockLighting_dict.get(key)

            if stockLighting.get_stock_name() == search:
                stockLighting_list.append(stockLighting)
            else:
                continue

        if len(stockLighting_list) != 0:
            return render_template("showStockLighting.html", count=len(stockLighting_list), stockLightings_list=stockLighting_list)
        else:
            return render_template("noResults.html")

    return render_template("searchStockLighting.html", form=search_stockLighting_form)

@app.route('/searchStockLightingPrice', methods=['GET', 'POST'])
def search_stockLightingPrice():
    search_stockLightingPrice_form = SearchStockLighting(request.form)
    if request.method == "POST" and search_stockLightingPrice_form.validate():
        search = search_stockLightingPrice_form.searchStockLighting.data
        stockLighting_dict = {}
        db = shelve.open("stockLighting.db", "r")
        stockLighting_dict = db['StockLightings']
        db.close()

        stockLighting_list = []
        for key in stockLighting_dict:
            stockLighting = stockLighting_dict.get(key)

            if stockLighting.get_price() < search:
                stockLighting_list.append(stockLighting)
            else:
                continue

        if len(stockLighting_list) != 0:
            return render_template("showStockLighting.html", count=len(stockLighting_list), stockLightings_list=stockLighting_list)
        else:
            return render_template("noResults.html")

    return render_template("searchStockLighting.html", form=search_stockLightingPrice_form)

@app.route('/searchStockPaint', methods=['GET', 'POST'])
def search_stockPaint():
    search_stockPaint_form = SearchStockPaint(request.form)
    if request.method == "POST" and search_stockPaint_form.validate():
        search = search_stockPaint_form.searchStockPaint.data
        stockPaint_dict = {}
        db = shelve.open("stockPaint.db", "r")
        stockPaint_dict = db['StockPaints']
        db.close()

        stockPaint_list = []
        for key in stockPaint_dict:
            stockPaint = stockPaint_dict.get(key)

            if stockPaint.get_stock_name() == search:
                stockPaint_list.append(stockPaint)
            else:
                continue

        if len(stockPaint_list) != 0:
            return render_template("showStockPaint.html", count=len(stockPaint_list), stockPaints_list=stockPaint_list)
        else:
            return render_template("noResults.html")

    return render_template("searchStockPaint.html", form=search_stockPaint_form)

@app.route('/searchStockPaintPrice', methods=['GET', 'POST'])
def search_stockPaintPrice():
    search_stockPaintPrice_form = SearchStockPaint(request.form)
    if request.method == "POST" and search_stockPaintPrice_form.validate():
        search = search_stockPaintPrice_form.searchStockPaint.data
        stockPaint_dict = {}
        db = shelve.open("stockPaint.db", "r")
        stockPaint_dict = db['StockPaints']
        db.close()

        stockPaint_list = []
        for key in stockPaint_dict:
            stockPaint = stockPaint_dict.get(key)

            if stockPaint.get_price() < search:
                stockPaint_list.append(stockPaint)
            else:
                continue

        if len(stockPaint_list) != 0:
            return render_template("showStockPaint.html", count=len(stockPaint_list), stockPaints_list=stockPaint_list)
        else:
            return render_template("noResults.html")

    return render_template("searchStockPaint.html", form=search_stockPaintPrice_form)

@app.route('/searchStockTile', methods=['GET', 'POST'])
def search_stockTile():
    search_stockTile_form = SearchStockTile(request.form)
    if request.method == "POST" and search_stockTile_form.validate():
        search = search_stockTile_form.searchStockTile.data
        stockTile_dict = {}
        db = shelve.open("stockTile.db", "r")
        stockTile_dict = db['StockTiles']
        db.close()

        stockTile_list = []
        for key in stockTile_dict:
            stockTile = stockTile_dict.get(key)

            if stockTile.get_stock_name() == search:
                stockTile_list.append(stockTile)
            else:
                continue

        if len(stockTile_list) != 0:
            return render_template("showStockTile.html", count=len(stockTile_list), stockTiles_list=stockTile_list)
        else:
            return render_template("noResults.html")

    return render_template("searchStockTile.html", form=search_stockTile_form)

@app.route('/searchStockTilePrice', methods=['GET', 'POST'])
def search_stockTilePrice():
    search_stockTilePrice_form = SearchStockTile(request.form)
    if request.method == "POST" and search_stockTilePrice_form.validate():
        search = search_stockTilePrice_form.searchStockTile.data
        stockTile_dict = {}
        db = shelve.open("stockTile.db", "r")
        stockTile_dict = db['StockTiles']
        db.close()

        stockTile_list = []
        for key in stockTile_dict:
            stockTile = stockTile_dict.get(key)

            if stockTile.get_price() < search:
                stockTile_list.append(stockTile)
            else:
                continue

        if len(stockTile_list) != 0:
            return render_template("showStockTile.html", count=len(stockTile_list), stockTiles_list=stockTile_list)
        else:
            return render_template("noResults.html")

    return render_template("searchStockTile.html", form=search_stockTilePrice_form)

@app.route('/searchStockOther', methods=['GET', 'POST'])
def search_stockOther():
    search_stockOther_form = SearchStockOther(request.form)
    if request.method == "POST" and search_stockOther_form.validate():
        search = search_stockOther_form.searchStockOther.data
        stockOther_dict = {}
        db = shelve.open("stockOther.db", "r")
        stockOther_dict = db['StockOthers']
        db.close()

        stockOther_list = []
        for key in stockOther_dict:
            stockOther = stockOther_dict.get(key)

            if stockOther.get_stock_name() == search:
                stockOther_list.append(stockOther)
            else:
                continue

        if len(stockOther_list) != 0:
            return render_template("showStockOther.html", count=len(stockOther_list), stockOthers_list=stockOther_list)
        else:
            return render_template("noResults.html")

    return render_template("searchStockOther.html", form=search_stockOther_form)

@app.route('/searchStockOtherPrice', methods=['GET', 'POST'])
def search_stockOtherPrice():
    search_stockOtherPrice_form = SearchStockOther(request.form)
    if request.method == "POST" and search_stockOtherPrice_form.validate():
        search = search_stockOtherPrice_form.searchStockOther.data
        stockOther_dict = {}
        db = shelve.open("stockOther.db", "r")
        stockOther_dict = db['StockOthers']
        db.close()

        stockOther_list = []
        for key in stockOther_dict:
            stockOther = stockOther_dict.get(key)

            if stockOther.get_price() < search:
                stockOther_list.append(stockOther)
            else:
                continue

        if len(stockOther_list) != 0:
            return render_template("showStockOther.html", count=len(stockOther_list), stockOthers_list=stockOther_list)
        else:
            return render_template("noResults.html")

    return render_template("searchStockOther.html", form=search_stockOtherPrice_form)

@app.route('/viewStockFans')
def view_stockFans():
    stockFans_dict = {}
    db = shelve.open('stockFan.db', 'r')
    stockFans_dict = db['StockFans']
    db.close()

    stockFans_list = []
    for key in stockFans_dict:
        stockFan = stockFans_dict.get(key)
        stockFans_list.append(stockFan)

    return render_template('viewStockFans.html', count=len(stockFans_list), stockFans_list=stockFans_list)

@app.route('/viewStockLightings')
def view_stockLightings():
    stockLightings_dict = {}
    db = shelve.open('stockLighting.db', 'r')
    stockLightings_dict = db['StockLightings']
    db.close()

    stockLightings_list = []
    for key in stockLightings_dict:
        stockLighting = stockLightings_dict.get(key)
        stockLightings_list.append(stockLighting)

    return render_template('viewStockLightings.html', count=len(stockLightings_list),
                           stockLightings_list=stockLightings_list)

@app.route('/viewStockOthers')
def view_stockOthers():
    stockOthers_dict = {}
    db = shelve.open('stockOther.db', 'r')
    stockOthers_dict = db['StockOthers']
    db.close()

    stockOthers_list = []
    for key in stockOthers_dict:
        stockOther = stockOthers_dict.get(key)
        stockOthers_list.append(stockOther)

    return render_template('viewStockOthers.html', count=len(stockOthers_list), stockOthers_list=stockOthers_list)

@app.route('/viewStockPaints')
def view_stockPaints():
    stockPaints_dict = {}
    db = shelve.open('stockPaint.db', 'r')
    stockPaints_dict = db['StockPaints']
    db.close()

    stockPaints_list = []
    for key in stockPaints_dict:
        stockPaint = stockPaints_dict.get(key)
        stockPaints_list.append(stockPaint)

    return render_template('viewStockPaints.html', count=len(stockPaints_list), stockPaints_list=stockPaints_list)

@app.route('/viewStockTiles')
def view_stockTiles():
    stockTiles_dict = {}
    db = shelve.open('stockTile.db', 'r')
    stockTiles_dict = db['StockTiles']
    db.close()

    stockTiles_list = []
    for key in stockTiles_dict:
        stockTile = stockTiles_dict.get(key)
        stockTiles_list.append(stockTile)

    return render_template('viewStockTiles.html', count=len(stockTiles_list), stockTiles_list=stockTiles_list)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('error404.html'), 404


if __name__ == '__main__':
    app.run()
