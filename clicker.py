from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)
click_count = 0  # Initialize click counter

@app.route('/')
def index():
    global click_count
    # HTML template with count displayed
    html_template = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Python Clicker</title>
    </head>
    <body>
        <h1>Click Count: {{ count }}</h1>
        <form action="/click" method="post">
            <button type="submit">Click Me!</button>
        </form>
    </body>
    </html>
    '''
    return render_template_string(html_template, count=click_count)

@app.route('/click', methods=['POST'])
def click():
    global click_count
    click_count += 1
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
