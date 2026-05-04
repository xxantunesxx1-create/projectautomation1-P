import speech_recognition as sr
import wikipedia
import pyttsx3
import datetime
import pywhatkit
import os
import requests
import webbrowser
import random
from urllib.parse import quote

audio = sr.Recognizer()
maquina = pyttsx3.init()

voices = maquina.getProperty("voices")
for voice in voices:
    if "Brazil" in voice.name.lower():
        maquina.setProperty("voice", voice.id)

print("Ajustando o microfone para o ruído da sala")
with sr.Microphone() as source:
    audio.adjust_for_ambient_noise(source,duration=1)
def falar(texto):
    print(f"saphira: {texto}")
    maquina.say(texto)
    maquina.runAndWait()

def ouvirComando():
    comando = ""
    try:
        with sr.Microphone() as source:
           
            voz = audio.listen(source, phrase_time_limit=5)
            comando = audio.recognize_google(voz, language = "pt-BR")
            comando = comando.lower()

            if "saphira" in comando:
                comando = comando.replace("saphira", "").strip()

                respostas_ativacao = ["Sim?", "Pois não?", "Estou ouvindo.", "Oi!"]
                falar(random.choice(respostas_ativacao))
                return comando

    except sr.UnknownValueError:
       pass
    except Exception as e:
        print("Erro no microfone: {e}")

    return ""

def buscar_clima(cidade):
    cidade_codificada = quote(cidade)

    api_key = "ff0eef6e1c66219aea89ba4804f5e72c"

    link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade_codificada}&appid={api_key}&lang-pt_br&units-metric"
    try:
        requisicao = requests.get(link)
        dados = requisicao.json()
        if dados["cod"] == 200:
           temp = dados["main"]["temp"]
           desc = dados["weather"][0]["description"]
           return f"Em {cidade}, faz {temp:.1f} graus com {desc}."
    except:
        return "Não consegui checar o clima agora."
    return "Cidade não encontrada."



    if dados["cod"] == 200:
        temp = dados["main"]["temp"]
        descricao = dados["weather"][0]["descri"]

def executar_saphira():

    comando = ouvirComando()

    if comando == "":
        return
    
    print(f"Você disse: {comando}")

    if "horas" in comando:
        hora_atual = datetime.datetime.now().strftime("%H:%M")
        falar(f"São {hora_atual}")

    elif "pesquisar" in comando:
        procurar = comando.replace("pesquisar", "")
        falar(f"Buscando{procurar}")
        wikipedia.set_lang("pt")
        falar(wikipedia.summary(procurar, sentences = 1))
    elif "tempo em" in comando or "clima em" in comando:
        cidade = comando.replace("tempo em", "").replace("clima em", "")

        if cidade:
            info_clima = buscar_clima(cidade)
            falar(info_clima)
        else:
            falar("Qual cidade você gostaria de saber o clima?")

    elif "abrir github" in comando:
        falar("Abrindo seu Github, bons códigos!")
        webbrowser.open("https://github.com")

    elif "abrir youtube" in comando:
        falar("Abrindo Youtube, aproveite os vídeos!")
        webbrowser.open("https://youtube.com")

    elif "abrir noticias" in comando:
        falar("Abrindo as últimas notícias para você.")

    elif "anote" in comando or "anotar" in comando:
        nota = comando.replace("anote", "").replace("anotar", "").strip()
        with open("notas.txt", "a") as f:
            f.write(f"- {nota}\n")
        falar("Anotei no seu bloco de notas.")
    elif "desligar" in comando or "sair" in comando:
        falar("Desligando. Até mais!")
        exit()

falar("Saphira online e pronta!")
while True:
    executar_saphira()