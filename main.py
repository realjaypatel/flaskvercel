from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Data passed to the template
    title = "Welcome to My Flask App"
    items = ['Item 1', 'Item 2', 'Item 3']
    return render_template('index.html', title=title, items=items)

if __name__ == '__main__':
    app.run(debug=True)