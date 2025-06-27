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

        if len(datas) == 0:
          return render_template('error.html', message="クイズが存在しません")

        selected_id = rd.randint(0, len(datas)-1)
        selected_quiz_id = datas[selected_id][0]
        selected_quiz = datas[selected_id][1]

        return render_template('quiz.html', currentMode="quiz", quiz_id=selected_quiz_id, quiz=selected_quiz, disabled=False)

    except sqlite3.Error as e:
      print(e)
      return render_template('error.html')

  def quizAnswer():
    quiz_id = request.form.get('id')
    answer = request.form.get('answer')

    if not quiz_id:
      return render_template('error.html',message="IDがありません")

    dbController = DBController()
    answer_data = dbController.getQuizData(quiz_id)

    if not answer_data:
      return render_template('error.html', message="クイズが存在しません")

    if answer_data[0][2] == answer:
      message = "正解です！"
    else:
      message = "不正解です。(正解: " + answer_data[0][2] + ")"
    return render_template('quiz.html', currentMode="quiz", quiz_id=answer_data[0][0], quiz=answer_data[0][1], message=message, disabled=True)
