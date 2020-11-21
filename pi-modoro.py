import datetime
from threading import Timer
from time import sleep
from gpiozero import PWMLED, Button, TonalBuzzer
from gpiozero.tones import Tone
from signal import pause

BUTTON_PIN = 8
BUZZER_PIN = 18
LIGHT_PIN = 7

class PomodoroTimer(object): 
	def __init__(self):
		self.timer = None
		self.led = PWMLED(LIGHT_PIN)
		self.buzzer = TonalBuzzer(BUZZER_PIN)

	def times_up(self):
		print("Time's up")
		self.fin()

	def start_pomodoro(self, channel):
		print("Start Pomodoro")
		self.led.blink(on_time=0.3, off_time=0.3, n=5, background=True)

		if (self.timer != None): 
			print("Pomodoro was re-started")
			self.timer.cancel()

		self.timer = Timer(5, self.times_up)
		self.timer.start()

	def play_note(self, note, duration=0.04):
		self.buzzer.play(Tone.from_note(note))
		sleep(duration)
		self.buzzer.stop();

	def ending_music(self):
		# Available Range
		# A3, B3, C4, D4, E4, F4, G4, A4, B4
		arpeggio = [
			"A#3", "C#4", "E#4",
			"A#3", "C#4", "E#4",
			"A#3", "C#4", "E#4",
			"A#3", "C#4", "E#4",

			"A3", "C4", "E4",
			"A3", "C4", "E4",
			"A3", "C4", "E4",
			"A3", "C4", "E4",

			"C4", "E4", "G4",
			"C4", "E4", "G4",
			"C4", "E4", "G4",
			"C4", "E4", "G4",

			"Cb4", "Eb4", "Gb4",
			"Cb4", "Eb4", "Gb4",
			"Cb4", "Eb4", "Gb4",
			"Cb4", "Eb4", "Gb4",

			"A#3", "C#4", "E#4",
			"A#3", "C#4", "E#4",
			"A#3", "C#4", "E#4",
			"A#3", "C#4", "E#4",

			"A3", "C4", "E4",
			"A3", "C4", "E4",
			"A3", "C4", "E4",
			"A3", "C4", "E4",
		]

		for note in arpeggio:
			self.play_note(note)

		self.play_note("A3", duration=0.2)

	def fin(self): 
		self.led.pulse()
		self.ending_music()
		self.led.off()

	def run(self):
		self.button = Button(BUTTON_PIN, pull_up=False)
		self.button.when_pressed = self.start_pomodoro

		pause()

if __name__ == '__main__':
	PomodoroTimer().run()

