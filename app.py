from flask import Flask, request, render_template_string
from mymath import power

# Initialize the Flask application
app = Flask(__name__)

# Template for the home page
home_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Welcome to IS3313 App</title>
</head>
<body>
    <h1>Welcome to IS3313 Flask App!</h1>
    <p>This app demonstrates basic Flask functionality.</p>
    <form action="/calculate" method="post">
        <label for="base">Base:</label>
        <input type="number" id="base" name="base" required>
        <label for="exponent">Exponent:</label>
        <input type="number" id="exponent" name="exponent" required>
        <button type="submit">Calculate Power</button>
    </form>
</body>
</html>
"""

# Template for displaying results
result_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Calculation Result</title>
</head>
<body>
    <h1>Calculation Result</h1>
    <p>{{ base }} raised to the power of {{ exponent }} is: <strong>{{ result }}</strong></p>
    <a href="/">Go back</a>
</body>
</html>
"""

# Home route
@app.route('/')
def home():
    return render_template_string(home_template)

# Route to calculate power
@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        base = int(request.form['base'])
        exponent = int(request.form['exponent'])
        result = power(base, exponent)
        return render_template_string(result_template, base=base, exponent=exponent, result=result)
    except ValueError:
        return "<h2>Invalid input. Please enter valid numbers.</h2>", 400

# Error handling for 404 (Page Not Found)
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404 - Page Not Found</h1><p>Sorry, the page you are looking for doesn't exist.</p>", 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
