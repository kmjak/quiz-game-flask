from flask import Flask, render_template
from controller.CreateQuiz import CreateQuiz
from controller.EditQuiz import EditQuiz
from controller.Quiz import Quiz

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('home.html', currentMode="index")

@app.route('/create', methods=['GET'])
def create():
  return CreateQuiz.create()

@app.route('/create_quiz', methods=['POST'])
def createQuiz():
  return CreateQuiz.createQuiz()

@app.route('/edit')
def edit():
  return EditQuiz.edit()

@app.route('/edit_quiz', methods=['POST'])
def editQuiz():
  return EditQuiz.editQuiz()

@app.route('/quiz')
def quiz():
  return Quiz.quiz()

@app.route('/quiz_answer', methods=['POST'])
def quizAnswer():
  return Quiz.quizAnswer()

if __name__ == '__main__':
  app.run(debug=True, port=5000)