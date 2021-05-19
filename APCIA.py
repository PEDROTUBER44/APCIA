import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import logging
import os

logger = logging.getLogger()
logger.setLevel(logging.ERROR)
bot = ChatBot("Ana")

while True:
	def ouvir_microfone():
		while True:
			with sr.Microphone() as source:
				r = sr.Recognizer()
				r.adjust_for_ambient_noise(source)
				print('\n\033[1;33m###_MICROFONE_###\033[m\n')
				audio = r.listen(source)
				try:
					frase = r.recognize_google(audio, language='pt-BR')
					print('\033[1;34mHUMANO:\033[m',frase)
				except sr.UnknownValueError:
					print('\033[1;35mBOT:\033[m \033[mNÃO CONSEGUI TE OUVIR\033[m')
					continue
				except Exception as ex:
					print(ex)
				return frase

	def cria_audio(audio):
		if not os.path.exists("bot.mp3"):
			tts = gTTS(audio, lang="pt-BR")
			tts.save('bot.mp3')
			playsound("bot.mp3")

		else:
			os.remove("bot.mp3")
			tts = gTTS(audio, lang="pt-BR")
			tts.save('bot.mp3')
			playsound("bot.mp3")

	falas = [
		'oi',
		'olá',
		'tudo bem ?',
		'tudo bem e você ?',
		'eu estou bem',
		'que bom',
		'qual o melhor sistema ?',
		'o melhor sistema é linux',]

	trainer = ListTrainer(bot)
	trainer.train(falas)

	while True:
		quest = ouvir_microfone()
		resposta = bot.get_response(quest)
		cria_audio(str(resposta))
		print('Bot: ',resposta)