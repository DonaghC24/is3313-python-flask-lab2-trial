from flask import Flask
from mymath import power

# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def hello_world():
    # Calculate 3 raised to the power of 8
    result = power(3, 8)
    return (
        f"<h1>Hello IS3313!</h1>"
        f"<p>This was edited in GitHub. The answer is: <strong>{result}</strong></p>"
    )

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
