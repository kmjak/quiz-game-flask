from flask import render_template
from flask import request, redirect, url_for
import sqlite3
from contextlib import closing

class CreateQuiz:
  def create():
    status = request.args.get('status')
    return render_template('create_quiz.html', status=status)

  def createQuiz():
    question = request.form['question']
    answer = request.form['answer']

    if not question or not answer:
      return redirect(url_for("create", status="error"))

    try:
      with closing(sqlite3.connect('./db/sample.db')) as con:

        cur = con.cursor()
        cur.execute('''
                      create table if not exists quiz (
                      id integer primary key autoincrement,
                      question text,
                      answer text
                      )
                    ''')
        con.commit()

        cur.execute("insert into quiz (question, answer) values (:question, :answer)", {'question': question, 'answer': answer})
        con.commit()
        return redirect(url_for("create", status="success"))
    except sqlite3.Error as e:
        print(e)
        return redirect(url_for("create", status="error"))
