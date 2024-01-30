import requests

def get():
    rec = requests.get("http://127.0.0.1/get/quizlist")
    #rec = requests.get("http://127.0.0.1/get/question/Україна")

    rec.encoding = 'utf-16'

    print(f"Code:{rec.status_code}\nContent:{rec.content}")

if __name__ == "__main__":
    get()