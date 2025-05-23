from flask import render_template
from flask import request, redirect, url_for
import sqlite3
from contextlib import closing
from controller.DBController import DBController
import random as rd

class Quiz:
  def quiz():
    datas = []
    try:
      with closing(sqlite3.connect('./db/sample.db')) as con:
        cur = con.cursor()
        cur.execute("select * from quiz")
        datas = cur.fetchall()

        selected_id = rd.randint(0, len(datas)-1)
        selected_quiz_id = datas[selected_id][0]
        selected_quiz = datas[selected_id][1]

        return render_template('quiz.html', currentMode="quiz", quiz_id=selected_quiz_id, quiz=selected_quiz)

    except sqlite3.Error as e:
      print(e)
      return render_template('error.html')

  def quizAnswer():
    id = request.form.get('id')
    answer = request.form.get('answer')

    if not id:
      return render_template('error.html',message="IDがありません")

    answer_data = DBController.getQuizData(id)
