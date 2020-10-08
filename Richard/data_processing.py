import sqlite3
from flask import g

from hashlib import pbkdf2_hmac

salt = b'\x15\xdc\xe7\r7\x18\xcfF\xba\xbf\xbe5\xf2A;!\xe7c\x1cRQ\xf8C\x8f:\x86BqO\x9d\xb9)'

DATABASE = 'login.db'

def establishConnection(func):
    #saves code repetition so i don't have to write conn = ... cur = ... everytime
    def connection(*args, **kwargs):
        conn = sqlite3.connect(DATABASE)
        try:
            cur = conn.cursor()
            val = func(cur, *args, **kwargs)
        except Exception as e:
            conn.rollback() #undoes the recent changes to database
            raise e
        else:
            if val == None: #if you don't return anything i.e. not a SELECT keyword
                conn.commit()
        finally:
            conn.close()

        if val != None: #if there is an actual value that has been passed
            return val
    return connection




def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def getHash(password):
    return pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)


@establishConnection
def createTable(cur):
    cur.execute('''CREATE TABLE user
                (id INTEGER not null primary key autoincrement,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                phone TEXT NOT NULL UNIQUE)''')
    #id INTEGER not null primary key autoincrement
    #could just be id INTEGER primary key - as integer primary keys default autoincrement
    #when null value is passed in autoincrement, id value is one larger then
    #previous largest value to exist in that column

@establishConnection
def getData(cur, userId):
    cur.execute("SELECT * FROM user WHERE id=?", (userId,))
    return cur.fetchall()

@establishConnection
def addUser(cur, username, password, email, phone):
    password = getHash(password)
    cur.execute("INSERT INTO user (username, password, email, phone) VALUES (?, ?, ?, ?)",
                (username, password, email, phone))

@establishConnection
def deleteUser(cur, userId):
    cur.execute("DELETE FROM user WHERE id =?", (userId,))


@establishConnection
def updatePassword(cur, userId, newPassword):
    password = getHash(newPassword)
    cur.execute("UPDATE user SET password=? WHERE id=?", (password, userId))

@establishConnection
def getUsername(cur, userId):
    cur.execute("SELECT username FROM user WHERE id=?", (userId,))
    return cur.fetchone()[0]

@establishConnection
def getUserId(cur, username):
    cur.execute("SELECT id FROM user WHERE username=?", (username,))
    val = cur.fetchone()
    return val[0] if val else None

@establishConnection
def checkPassword(cur, username, password):
    try:
        cur.execute("SELECT password FROM user WHERE username=?", (username,))
        if getHash(password)== cur.fetchone()[0]:
            return True
        else:
            return False
    except:
        return False

@establishConnection
def changeDefault(cur, settingDict, username):
    cur.execute('''UPDATE user
                SET colourTheme=?
                WHERE username=?''',
                 (settingDict['colourTheme'], username))


def getDefault(username):
    userId = getUserId(username)
    userData = getData(userId)
    defaults = userData[0][5:]
    return defaults