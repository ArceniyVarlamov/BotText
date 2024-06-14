from yandexgptlite import YandexGPTLite
import codecs


def bot_read(file):
    file = codecs.open( f"{file}", "r", "utf-8" )
    data = file.read()
    file.close()
    return data
def bot_character(file):
    file = codecs.open( f"{file}", "r", "utf-8" )
    data = file.read()
    file.close()
    return data
def bot_skills(file):
    file = codecs.open( f"{file}", "r", "utf-8" )
    data = file.read()
    file.close()
    return data
def bot_restrict(file):
    file = codecs.open( f"{file}", "r", "utf-8" )
    data = file.read()
    file.close()
    return data
account = YandexGPTLite('b1ghqjvoshov8q79s7f5', 'y0_AgAAAABnGlHCAATuwQAAAAEHgGuyAAD7npjmEllKNbG9uHGyh9At4qiK-g' )
zapros=input()
text = account.create_completion(f'Твой персонаж: {bot_character("характер.txt")}, твои навыки:{bot_skills("навыки.txt")}, ограничения, которых ты должен придерживаться: {bot_restrict("ограничения.txt")}, твоя задача очеловечить данный текст f{zapros}', '1', system_prompt = 'отвечай на русском')
print(text.replace('*',''))