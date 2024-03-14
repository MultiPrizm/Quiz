import mysql.connector, random, logging

logging.basicConfig(filename='errors.log', level=logging.ERROR)

Scripts = {
    
    "AddUser":'''
        INSERT INTO users(name, password, status)

                VALUES (%s, %s, %s);
    ''',

    "Select":'''
        SELECT * FROM users WHERE name = %s;
    ''',

    "AddAdmin":'''
        INSERT INTO users(name, password, status)

                VALUES (%s, %s, 'admin');
    ''',

    "AddQuiz":'''
        INSERT quiz(name, root, code)

                VALUES (%s, %s, %s);
    ''',

    "AddQuestion":'''
        INSERT INTO questions(name, quiz, questions)

                VALUES (%s, %s, %s);
    ''',

    "GetQuiz":'''
        SELECT name FROM quiz;
    ''',

    "GetUserQuiz":'''
        SELECT name FROM quiz WHERE root = %s;
    ''',

    "GetCode":'''
        SELECT code FROM quiz WHERE root = %s AND name = %s;
    ''',

    "GetQuizForCode":'''
        SELECT * FROM quiz WHERE code = %s;
    ''',

    "GetQuestion":'''
        SELECT questions FROM questions WHERE quiz = %s;
    '''
}


def AddUser(name, password):

    try:

        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="5170Ill$",
            database="mydatabase"
        )

        cursor = conn.cursor()

        cursor.execute(Scripts["Select"], (name,))

        check_name = cursor.fetchall()

        if check_name:
            return False
        
        cursor.execute(Scripts["AddUser"], (str(name), str(password), "user"))
        conn.commit()
        cursor.close()
        
        return True
    
    except BaseException as e:
        logging.exception(f"[ERROR]:{e}")
        return False

def CheckPassword(name, password):

    try:

        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="5170Ill$",
            database="mydatabase"
        )

        cursor = conn.cursor()

        cursor.execute(Scripts["Select"], (name,))
        check_user = cursor.fetchall()
        cursor.close()

        if not check_user:
            return False, False, False
        elif str(check_user[0][1]) == str(password):
            return True, True, check_user[0][2]
        else:
            return True, False, False
        
    except BaseException as e:
        logging.exception(f"[ERROR]:{e}")
        return False

def SetQuezConf(conf, user):

    try:

        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="5170Ill$",
            database="mydatabase"
        )

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
        
        for i in conf["new"]["questions"].keys():
            content = conf["new"]["questions"][i]["content"]
            answer1 = conf["new"]["questions"][i]["1"]
            answer2 = conf["new"]["questions"][i]["2"]
            answer3 = conf["new"]["questions"][i]["3"]
            answer4 = conf["new"]["questions"][i]["4"]

            cursor.execute(Scripts["AddQuestion"], (i, code, f"{content}|{answer1}|{answer2}|{answer3}|{answer4}"))
        cursor.close()
        conn.commit()
        return True
    
    except BaseException as e:
        logging.exception(f"[ERROR]:{e}")
        return False

def GetQuiz():
    try:

        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="5170Ill$",
            database="mydatabase"
        )

        cursor = conn.cursor()

        cursor.execute(Scripts["GetQuiz"])
        quezList = cursor.fetchall()
        cursor.close()

        response = []

        for i in quezList:
            response.append(i[0])

        return response
    
    except BaseException as e:
        logging.error(f"[ERROR]:{e}")
        return False

def GetCode(user, quiz):

    try:

        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="5170Ill$",
            database="mydatabase"
        )

        cursor = conn.cursor()

        cursor.execute(Scripts["GetCode"], (user, quiz))
        quezList = cursor.fetchall()
        cursor.close()

        return quezList
    
    except BaseException as e:
        logging.exception(f"[ERROR]:{e}")
        return False

def GetUserQuiz(user):
    try:

        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="5170Ill$",
            database="mydatabase"
        )

        cursor = conn.cursor()

        cursor.execute(Scripts["GetUserQuiz"], (user,))
        quezList = cursor.fetchall()
        cursor.close()

        response = []

        for i in quezList:
            response.append(i[0])

        return response
    except BaseException as e:
        logging.exception(f"[ERROR]:{e}")
        return False


def GetQuestion(quez):
    try:

        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="5170Ill$",
            database="mydatabase"
        )

        cursor = conn.cursor()

        cursor.execute(Scripts["GetQuestion"], (quez,))
        quezList = cursor.fetchall()
        cursor.close()

        if quezList:
            return quezList
        else:
            return False
        
    except BaseException as e:
        logging.exception(f"[ERROR]:{e}")
        return False

def random_code():
    
    prefab = "0a1b2c3d4e5f6g7h8i9jklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    code = ""

    for i in range(32):
        code += prefab[random.randint(0, len(prefab)-1)]

    return code

    