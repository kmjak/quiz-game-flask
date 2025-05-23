from flask import Flask, render_template
from controller.createQuiz import CreateQuiz

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('home.html')

@app.route('/create', methods=['GET'])
def create():
  return CreateQuiz.create()

@app.route('/create_quiz', methods=['POST'])
def create_quiz():
  return CreateQuiz.createQuiz()

@app.route('/edit')
def edit():
  return render_template('home.html')

@app.route('/quiz')
def quiz():
  return render_template('home.html')

if __name__ == '__main__':
  app.run(debug=True, port=5000)