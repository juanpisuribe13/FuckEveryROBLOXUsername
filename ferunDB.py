import sqlite3, sys

def AlreadyExists():
    db = sqlite3.connect('FERUN.db')
    dbc = db.cursor()
    try:
        dbc.execute('''CREATE TABLE FERUN
                        (fkdID qty, username text, userID qty)''')
        dbc.close()
        return False
    except sqlite3.OperationalError:
        dbc.close()
        return True

def createRow(username, userID):
    db = sqlite3.connect('FERUN.db')
    dbc = db.cursor()
    for row in dbc.execute('SELECT * FROM FERUN ORDER BY fkdID'):
        i = row[0]
    try:
        i += 1
    except NameError:
        i = 1
    newRow = [(i, username, userID)]
    dbc.executemany('INSERT INTO FERUN VALUES (?,?,?)', newRow)
    db.commit()
    dbc.close()

def isAlreadyTweeted(y):
    db = sqlite3.connect('FERUN.db')
    dbc = db.cursor()
    for x in dbc.execute('SELECT username FROM FERUN'):
        if x[0] == y:
            print("Found {}".format(y))
            dbc.close()
            return True
    dbc.close()
    return False

def getLastCount():
    db = sqlite3.connect('FERUN.db')
    dbc = db.cursor()
    for row in dbc.execute('SELECT fkdID FROM FERUN ORDER BY fkdID'):
        i = row[0]
    try:
        i += 1
    except NameError:
        i = 1
    return i
    dbc.close()

# if __name__ == '__main__':
#     print(getLastCount())
#     x = FindPamID('t2TlAVwDPpGKW2qB_lReMA')
#     print(x)
## Only use this to troubleshoot