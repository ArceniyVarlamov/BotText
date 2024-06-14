import requests
import codecs


def bot_read(file):
    file = codecs.open( f"{file}", "r", "utf-8" )
    data = file.read()
    file.close()
    return data
zapros=input()
prompt = {
    "modelUri": "gpt://b1ghqjvoshov8q79s7f5/yandexgpt-lite",
    "completionOptions": {
        "stream": False,
        "temperature": 0.6,
        "maxTokens": "2000"
    },
    "messages": [
        {
            "role": "system",
            "text": f"{bot_read("требования.txt")}"
        },
        {
            "role": "user",
            "text": f"Здравствуй, уважаемый эксперт! Мне нужна твоя помощь. Необходимо очеловечить следующий текст: {zapros}"
        }
    ]
}


url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Api-Key AQVNxabsTLqkjvah_pgcXArGXxGAK0NZ71JsiH9C"
}

response = requests.post(url, headers=headers, json=prompt)
result = response.text
print(result) #нужно настроить вывод