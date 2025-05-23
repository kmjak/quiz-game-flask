from flask import render_template
from flask import request, redirect, url_for
import sqlite3
from contextlib import closing
from controller.DBController import DBController

class EditQuiz:
  def edit():
    status = request.args.get('status')
    id = request.args.get('id')
    message = request.args.get('message')
    target = []
    datas = []
    try:
      with closing(sqlite3.connect('./db/sample.db')) as con:
        cur = con.cursor()
        cur.execute("select * from quiz")
        datas = cur.fetchall()
        target = DBController().getQuizData(id)

    except sqlite3.Error as e:
      print(e)
    return render_template('edit_quiz.html', status=status, currentMode="edit", datas=datas, message=message, target=target)

  def editQuiz():
    id = request.form['id']
    question = request.form['question']
    answer = request.form['answer']
    mode = request.form['mode']

    if mode == "read":
      if not id:
        return redirect(url_for("edit", status="error"))
      if not DBController().isExistsQuiz(id):
        return redirect(url_for("edit", status="error", message="読み込み"))

      return redirect(url_for("edit", status="success", id=id, message="読み込み"))

    if mode == "edit":
      if not id or not question or not answer:
        return redirect(url_for("edit", status="error", message="修正"))

      try:
        if not DBController().isExistsQuiz(id):
          return redirect(url_for("edit", status="error", message="修正"))

        with closing(sqlite3.connect('./db/sample.db')) as con:
          cur = con.cursor()
          cur.execute("update quiz set question=:question, answer=:answer where id=:id", {'question': question, 'answer': answer, 'id': id})
          con.commit()
          return redirect(url_for("edit", status="success", message="修正"))
      except sqlite3.Error as e:
        print(e)
        return redirect(url_for("edit", status="error", message="修正"))

    if mode == "delete":
      if not id:
        return redirect(url_for("edit", status="error", message="削除"))

      if not DBController().isExistsQuiz(id):
        return redirect(url_for("edit", status="error", message="削除"))

      try:
        with closing(sqlite3.connect('./db/sample.db')) as con:
          cur = con.cursor()

          cur.execute("delete from quiz where id=:id", {'id': id})
          con.commit()
          return redirect(url_for("edit", status="success", message="問"+id+"の削除"))
      except sqlite3.Error as e:
        print(e)
        return redirect(url_for("edit", status="error", message="問"+id+"の削除"))
