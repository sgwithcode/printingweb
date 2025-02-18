from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/order', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        details = request.form['details']
        return f"Đã nhận đơn hàng từ {name}, Email: {email}, Chi tiết: {details}"
    return render_template("order.html")

if __name__ == '__main__':
    app.run(debug=True)
