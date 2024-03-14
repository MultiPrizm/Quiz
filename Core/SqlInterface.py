import sqlite3, random



Scripts = {
    "Create":[
        '''
        CREATE TABLE IF NOT EXISTS users(
        
            name TEXT PRIMARY KEY NOT NULL,    
            password INT NOT NULL,
            status TEXT NOT NULL

        );
        ''',

        '''
        CREATE TABLE IF NOT EXISTS quiz(
        
            name TEXT NOT NULL,
            root TEXT NOT NULL,
            code TEXT NOT NULL    

        );
        ''',

        '''
        CREATE TABLE IF NOT EXISTS questions(
        
            name TEXT NOT NULL,
            quiz TEXT NOT NULL,    
            questions TEXT NOT NULL
        );
        '''
    ],

    "AddUser":'''
        INSERT INTO users(name, password, status)

                VALUES (?, ?, 'user');
    ''',

    "Select":'''
        SELECT * FROM users WHERE name = ?;
    ''',

    "AddAdmin":'''
        INSERT INTO users(name, password, status)

                VALUES (?, ?, 'admin');
    ''',

    "AddQuiz":'''
        INSERT OR IGNORE INTO quiz(name, root, code)

                VALUES (?, ?, ?);
    ''',

    "AddQuestion":'''
        INSERT INTO questions(name, quiz, questions)

                VALUES (?, ?, ?);
    ''',

    "GetQuiz":'''
        SELECT name FROM quiz;
    ''',

    "GetUserQuiz":'''
        SELECT name FROM quiz WHERE root = ?;
    ''',

    "GetCode":'''
        SELECT code FROM quiz WHERE root = ? AND name = ?;
    ''',

    "GetQuizForCode":'''
        SELECT * FROM quiz WHERE code = ?;
    ''',

    "GetQuestion":'''
        SELECT questions FROM questions WHERE quiz = ?;
    '''
}


def AddUser(name, password):
    conn = sqlite3.connect("app.db")

    cursor = conn.cursor()

    cursor.execute(Scripts["Select"], (name,))

    check_name = cursor.fetchall()

    cursor.execute("SELECT * FROM users")

    if check_name:
        return False
    
    cursor.execute(Scripts["AddUser"], (name, password))
    conn.commit()
    
    conn.close()
    return True

def CheckPassword(name, password):
    conn = sqlite3.connect("app.db")

    cursor = conn.cursor()

    cursor.execute(Scripts["Select"], (name,))
    check_user = cursor.fetchall()
    cursor.close()
    conn.close()

    if not check_user:
        return False, False, False
    elif str(check_user[0][1]) == str(password):
        return True, True, check_user[0][2]
    else:
        return True, False, False

def SetQuezConf(conf, user):
    conn = sqlite3.connect("app.db")

    cursor = conn.cursor()

    code = ""
    
    while True:

        code = random_code()

        cursor.execute(Scripts["GetQuizForCode"], (code,))

        buffer = cursor.fetchall()

        if buffer:
            pass
        else:
            break

    for i in conf["new"]["quizs"]:
        cursor.execute(Scripts["AddQuiz"], (str(i), user, code))
    
    print(conf)
    
    for i in conf["new"]["questions"].keys():
        content = conf["new"]["questions"][i]["content"]
        answer1 = conf["new"]["questions"][i]["1"]
        answer2 = conf["new"]["questions"][i]["2"]
        answer3 = conf["new"]["questions"][i]["3"]
        answer4 = conf["new"]["questions"][i]["4"]

        cursor.execute(Scripts["AddQuestion"], (i, code, f"{content}|{answer1}|{answer2}|{answer3}|{answer4}"))
    cursor.close()
    conn.commit()
    conn.close()
    return True

def GetQuiz():
    conn = sqlite3.connect("app.db")

    cursor = conn.cursor()

    cursor.execute(Scripts["GetQuiz"])
    quezList = cursor.fetchall()
    conn.close()

    response = []

    for i in quezList:
        response.append(i[0])

    return response

def GetCode(user, quiz):
    conn = sqlite3.connect("app.db")

    cursor = conn.cursor()

    cursor.execute(Scripts["GetCode"], (user, quiz))
    quezList = cursor.fetchall()
    conn.close()

    return quezList

def GetUserQuiz(user):
    conn = sqlite3.connect("app.db")

    cursor = conn.cursor()

    cursor.execute(Scripts["GetUserQuiz"], (user,))
    quezList = cursor.fetchall()
    conn.close()

    response = []

    for i in quezList:
        response.append(i[0])

    return response


def GetQuestion(quez):
    conn = sqlite3.connect("app.db")

    cursor = conn.cursor()
    print(quez)

    cursor.execute(Scripts["GetQuestion"], (quez,))
    quezList = cursor.fetchall()
    conn.close()

    if quezList:
        return quezList
    else:
        return False

def random_code():
    
    prefab = "0a1b2c3d4e5f6g7h8i9jklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    code = ""

    for i in range(32):
        code += prefab[random.randint(0, len(prefab)-1)]

    return code


if __name__ == "__main__":
    conn = sqlite3.connect("app.db")

    cursor = conn.cursor()
    for i in Scripts["Create"]:
        cursor.execute(i)
    
    #cursor.execute('''SELECT * FROM users''')

    cursor.execute('''SELECT * FROM quiz''')

    a = cursor.fetchall()
    
    for i in a:
        print(a)
    
    #cursor.execute(Scripts["AddAdmin"], ("admin", "admin"))
    #conn.commit()
    
    