import sqlite3
from contextlib import closing

class DBController:
  def getQuizData(self, quiz_id):
    try:
      with closing(sqlite3.connect('./db/sample.db')) as con:
        cur = con.cursor()
        cur.execute("select * from quiz where id=:id", {'id': quiz_id})
        target = cur.fetchall()
        return target
    except sqlite3.Error as e:
      print(e)
      return []

  def isExistsQuiz(self, quiz_id):
    target = self.getQuizData(quiz_id)
    if(len(target) == 0):
      return False
    return True
