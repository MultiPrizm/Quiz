import sqlite3



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
        
            name TEXT PRIMARY KEY NOT NULL    

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
        INSERT OR IGNORE INTO quiz(name)

                VALUES (?);
    ''',

    "AddQuestion":'''
        INSERT INTO questions(name, quiz, questions)

                VALUES (?, ?, ?);
    ''',

    "GetQuiz":'''
        SELECT name FROM quiz;
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
    conn.close()

    if not check_user:
        return False, False, False
    elif str(check_user[0][1]) == str(password):
        return True, True, check_user[0][2]
    else:
        return True, False, False

def SetQuezConf(conf):
    conn = sqlite3.connect("app.db")

    cursor = conn.cursor()

    for i in conf["new"]["quizs"]:
        cursor.execute(Scripts["AddQuiz"], (str(i),))
    
    for i in conf["new"]["questions"].keys():
        content = conf["new"]["questions"][i]["content"]
        answer1 = conf["new"]["questions"][i]["1"]
        answer2 = conf["new"]["questions"][i]["2"]
        answer3 = conf["new"]["questions"][i]["3"]
        answer4 = conf["new"]["questions"][i]["4"]

        cursor.execute(Scripts["AddQuestion"], (i, conf["new"]["questions"][i]["quiz"], f"{content}|{answer1}|{answer2}|{answer3}|{answer4}"))

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


if __name__ == "__main__":
    conn = sqlite3.connect("app.db")

    cursor = conn.cursor()
    for i in Scripts["Create"]:
        cursor.execute(i)
    
    #cursor.execute('''SELECT * FROM users''')

    cursor.execute('''SELECT * FROM questions''')

    a = cursor.fetchall()
    
    for i in a:
        print(a)
    
    #cursor.execute(Scripts["AddAdmin"], ("admin", "admin"))
    #conn.commit()
    
    