from cs50 import SQL
from flask import Flask, render_template, request, session, redirect, url_for
import logging

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.secret_key = 'as'

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

db = SQL("sqlite:///shop.db")


@app.route("/")
def index():
    if 'username' in session:
        name = session['username']
        return render_template("index.html")
    return render_template("login.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/home")
def home():
    if 'username' in session:
        name = session['username']
        return render_template("index.html")
    return render_template("login.html")


@app.route("/login")
def login():
    name = request.args.get("username")
    password = request.args.get("password")
    rows = db.execute("select * from register where username = :name and password = :password",
                      name=name, password=password)
    logger.info(rows)
    logger.info(name)
    logger.info(password)

    if name == " " and password == " ":
        return render_template("login.html")
    elif rows is None:
        return render_template("failure.html")
    session['username'] = name
    logger.info(session)
    return render_template("index.html", rows=rows)

@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/registerSubmit")
def registerSubmit():
    logger.info(request.args)
    firstname = request.args.get("firstname")
    lastname = request.args.get("lastname")
    email = request.args.get("email")
    username = request.args.get("username")
    password = request.args.get("password")

    db.execute("INSERT INTO register" +
                         "(firstname, lastname, email, username, password)" +
                         "VALUES (:firstname, :lastname,:email, :username, :password)",
                         firstname=firstname, lastname=lastname, email=email, username=username, password=password)
    session['username'] = username
    return render_template("index.html")

@app.route("/category")
def category():
    product_info_category = request.args.get("product_info_category")
    rows = db.execute("select * from product_info where Category = :product_info_category", 
                                product_info_category = product_info_category)
    logger.info("product_info_category")
    logger.info(rows)
    return render_template("products.html", products_info=rows)


@app.route("/checkout")
def checkout():
    logger.info("product_info_name")
    product_info_name = request.args.get("product_info_name")
    product_info_id = request.args.get("product_info_id")
    product_info_price = request.args.get("product_info_price")
    product_info_category = request.args.get("product_info_category")
    product_info_image = request.args.get("product_info_image")
    logger.info(product_info_name)
    logger.info(product_info_price)
    logger.info(product_info_category)
    return render_template("checkout.html", productName=product_info_name, productID=product_info_id,
                                            productPrice=product_info_price, productCategory=product_info_category,
                                            productImage = product_info_image)


@app.route("/orderConfirmation")
def orderConfirmation():
    orderID = request.args.get("orderID")
    return render_template("confirmation.html", orderID=orderID)


@app.route("/confirm")
def confirm():
    logger.info(request.args)
    firstname = request.args.get("firstname")
    lastname = request.args.get("lastname")
    email = request.args.get("email")
    telephone = request.args.get("telephone")
    country = request.args.get("country")
    city = request.args.get("city")
    address = request.args.get("address")
    postcode = request.args.get("postcode")
    product_info_id = request.args.get("product_info_id")
    logger.info(product_info_id)
    orderID = db.execute("INSERT INTO checkout" +
                         "(firstname, lastname, email, telephone, country, city, address, postcode, product_id)" +
                         "VALUES (:firstname, :lastname,:email, :telephone, :country, :city, :address, :postcode, :product_id)",
                         firstname=firstname, lastname=lastname, email=email, telephone=telephone, country=country,
                         city=city, address=address, postcode=postcode, product_id = product_info_id)
    logger.info(orderID)
    return redirect(url_for('.orderConfirmation', orderID=orderID))


@app.route("/product_details")
def product_details():
    product_info_id = request.args.get("product_info_id")

    logger.info(product_info_id)
    logger.info("product retrieved")

    products = db.execute("select * from product_info where ID= :productID", productID=product_info_id)
    product_info = None
    if products is not None:
        product_info = products[0]
        logger.info(product_info)
    return render_template("product_details.html", product_info=product_info)
