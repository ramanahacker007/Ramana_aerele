from flask import Flask, render_template, request, redirect, flash, session, url_for
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash



app = Flask(__name__)
app.config['SECRET_KEY'] = "mykey"
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "aerele"

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('layout.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT id, username, password FROM users WHERE username = %s', (username,))
        user = cursor.fetchone()
        cursor.close()

        if user and check_password_hash(user[2], password):
            session['user_id'] = user[0]
            session['username'] = user[1]
            return redirect(url_for('home'))
        else:
            flash('Login failed. Please check your credentials.', 'danger')

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'], method='sha256')
        deposit = float(request.form['deposit']) if 'deposit' in request.form else 0.0 
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO users (username, password, cash_balance) VALUES (%s, %s, %s)',(username, password, deposit))
        mysql.connection.commit()
        cursor.close()
        
        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/home')
def home():
    if 'user_id' not in session:
        flash('Please log in to access this page.', 'info')
        return redirect(url_for('login'))

    cursor = mysql.connection.cursor()
    cursor.execute('SELECT id, item_name, price FROM items')
    items = cursor.fetchall()
    cursor.close()

    return render_template('home.html', username=session['username'], items=items)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/add_item', methods=['GET', 'POST'])
def add_item():
    if 'user_id' not in session:
        flash('Please log in to access this page.', 'info')
        return redirect(url_for('login'))

    if request.method == 'POST':
        item_name = request.form['item_name']
        price = float(request.form['price'])
        seller_id = session['user_id']  # Get the logged-in user's ID as the seller
        qty = int(request.form['qty'])

        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO items (item_name, price, seller_id, qty) VALUES (%s, %s, %s ,%s)', (item_name, price, seller_id, qty))
        mysql.connection.commit()
        cursor.close()

        flash('Item added successfully!', 'success')
        return redirect(url_for('home'))

    return render_template('add_item.html')


@app.route('/purchase', methods=['POST'])
def purchase():
    if 'user_id' not in session:
        flash('Please log in to access this page.', 'info')
        return redirect(url_for('login'))
    
    item_id = int(request.form['item_id'])
    quantity = int(request.form['quantity'])

    cursor = mysql.connection.cursor()
    cursor.execute('SELECT item_name, price, seller_id FROM items WHERE id = %s', (item_id,))
    item = cursor.fetchone()

    if not item:
        flash('Item not found.', 'danger')
        return redirect(url_for('home'))

    total_amount = item[1] * quantity
    seller_id = item[2]

    cursor.execute('SELECT cash_balance FROM users WHERE id = %s', (session['user_id'],))
    buyer_balance = cursor.fetchone()[0]

    if buyer_balance >= total_amount:
        # Update buyer's balance
        cursor.execute('UPDATE users SET cash_balance = cash_balance - %s WHERE id = %s', (total_amount, session['user_id']))
        #cursor.execute('UPDATE items SET qty = qty + %s WHERE id = %s', (quantity, item_id))

        # Update seller's balance
        cursor.execute('UPDATE users SET cash_balance = cash_balance + %s WHERE id = %s', (total_amount, seller_id))
        cursor.execute('UPDATE items SET qty = qty - %s WHERE id = %s', (quantity, item_id))

        # Insert purchase record
        cursor.execute('INSERT INTO purchases (buyer_id, seller_id, item_id, quantity, rate, amount) VALUES (%s, %s, %s, %s, %s, %s)',
                       (session['user_id'], seller_id, item_id, quantity, item[1], total_amount))

        # Insert sales record
        cursor.execute('INSERT INTO sales (buyer_id, seller_id, item_id, quantity, rate, amount) VALUES (%s, %s, %s, %s, %s, %s)',
                       (session['user_id'], seller_id, item_id, quantity, item[1], total_amount))

        mysql.connection.commit()
        cursor.close()

        flash('Purchase successful!', 'success')
    else:
        flash('Insufficient funds for the purchase.', 'danger')

    return redirect(url_for('home'))


@app.route('/view_sales')
def view_sales():
    if 'user_id' not in session:
        flash('Please log in to access this page.', 'info')
        return redirect(url_for('login'))

    cursor = mysql.connection.cursor()
    cursor.execute('SELECT sales.timestamp, items.item_name, sales.quantity, sales.rate, sales.amount FROM sales JOIN items ON sales.item_id = items.id WHERE sales.seller_id = %s',
                   (session['user_id'],))
    sales_records = cursor.fetchall()
    cursor.close()

    return render_template('view_sales.html', sales_records=sales_records)

@app.route('/view_purchases')
def view_purchases():
    if 'user_id' not in session:
        flash('Please log in to access this page.', 'info')
        return redirect(url_for('login'))

    cursor = mysql.connection.cursor()
    cursor.execute('SELECT purchases.timestamp, items.item_name, purchases.quantity, purchases.rate, purchases.amount FROM purchases JOIN items ON purchases.item_id = items.id WHERE purchases.buyer_id = %s',
                   (session['user_id'],))
    purchase_records = cursor.fetchall()
    cursor.close()

    return render_template('view_purchases.html', purchase_records=purchase_records)


@app.route('/view_added_item')
def view_added_item():
    if 'user_id' not in session:
        flash('Please log in to access this page.', 'info')
        return redirect(url_for('login'))

    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM items WHERE seller_id = %s', (session['user_id'],))
    added_items = cursor.fetchall()
    cursor.close()

    return render_template('view_added_item.html', added_items=added_items)


@app.route('/report')
def report():
    if 'user_id' not in session:
        flash('Please log in to access this page.', 'info')
        return redirect(url_for('login'))

    cursor = mysql.connection.cursor()
    cursor.execute('SELECT cash_balance FROM users WHERE id = %s', (session['user_id'],))
    current_balance = cursor.fetchone()[0]
    cursor.close()

    return render_template('report.html', current_balance=current_balance)


if __name__ == '__main__':
    app.run(debug=True)
