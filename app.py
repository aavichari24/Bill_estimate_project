from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    try:
        return render_template("index.html")
    except Exception as e:
        return f"Error: {str(e)}", 500  # Show error message

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
