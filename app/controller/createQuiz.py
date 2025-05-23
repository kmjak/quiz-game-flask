from flask import render_template
from flask import request, redirect, url_for
import sqlite3
from contextlib import closing

class CreateQuiz:
  def create():
    status = request.args.get('status')
    return render_template('create_quiz.html', status=status, currentMode="create")

  def createQuiz():
    question = request.form.get('question')
    answer = request.form.get('answer')

    if not question or not answer:
      return redirect(url_for("create", status="error"))

    try:
      with closing(sqlite3.connect('./db/sample.db')) as con:

        cur = con.cursor()
        cur.execute('''
                    CREATE TABLE IF NOT EXISTS quiz (
                    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    question VARCHAR(256) NOT NULL,
                    answer VARCHAR(256) NOT NULL
            )
        ''')
        con.commit()

        cur.execute("insert into quiz (question, answer) values (:question, :answer)", {'question': question, 'answer': answer})
        con.commit()
        return redirect(url_for("create", status="success"))
    except sqlite3.Error as e:
      print(e)
      return redirect(url_for("create", status="error"))
