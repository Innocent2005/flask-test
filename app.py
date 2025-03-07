from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for tutorial videos
@app.route('/tutorials')
def tutorials():
    return "Tutorials page - Embed video lectures here."

# Route to download past questions
@app.route('/past-questions')
def past_questions():
    return "Past Questions page - List and download previous exam/test questions."

# Route to access PDF handouts
@app.route('/handouts')
def handouts():
    handouts_folder = os.path.join(os.getcwd(), 'static/handouts')
    files = os.listdir(handouts_folder)
    return render_template('handouts.html', files=files)

# Route to serve PDF files
@app.route('/handouts/<filename>')
def download_handout(filename):
    return send_from_directory('static/handouts', filename)

if __name__ == '__main__':
 app.run(host="0.0.0.0", port=5002, debug=True)