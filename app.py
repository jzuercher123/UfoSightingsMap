from flask import Flask, render_template
import os

# Initialize Flask
app = Flask(__name__)


@app.route('/')
def index():
    """
    :return: The rendered HTML template for the index.html page.
    """
    return render_template('index.html')


@app.route('/js/<path:filename>')
def serve_js(filename):
    """
    Serve JavaScript File

    :param filename: The name of the JavaScript file to be served.
    :return: The JavaScript file.
    """
    return app.send_static_file('js/' + filename)


if __name__ == "__main__":
    # Deployment env networking settings
    port = int(os.environ.get('PORT', 5000))
    # start application on all hosts
    app.run(debug=True, host='0.0.0.0', port=port)