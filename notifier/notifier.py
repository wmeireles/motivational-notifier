from plyer import notification
import requests
import time

API_URL = "http://localhost:8000/messages/random"

def fetch_and_notify():
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            data = response.json()
            notification.notify(
                title="⚡ Dica Motivacional do Dia ⚡",
                message=f"💬 {data['text']}",
                timeout=15,
                app_name="Motivator",
            #   app_icon="notifier/assets/rocket.ico"  # precisa ser .ico no Windows!
            )
        else:
            print("Erro ao buscar mensagem:", response.status_code)
    except Exception as e:
        print("Erro:", e)

if __name__ == "__main__":
    while True:
        fetch_and_notify()
        time.sleep(3600)  # 1 hora
