import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import mainthread

import speech_recognition as sr
import pyttsx3
import wikipedia

class AssistantLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(AssistantLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        self.label = Label(text="Press 'Listen' and speak", font_size=20)
        self.add_widget(self.label)
        
        self.button = Button(text="Listen", size_hint=(1, 0.2))
        self.button.bind(on_press=self.listen_command)
        self.add_widget(self.button)
        
        # Initialize TTS engine
        self.engine = pyttsx3.init()

    @mainthread
    def update_label(self, text):
        self.label.text = text

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def listen_command(self, instance):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            self.update_label("Listening...")
            audio = recognizer.listen(source)
            try:
                query = recognizer.recognize_google(audio)
                self.update_label("You said: " + query)
                self.handle_query(query)
            except sr.UnknownValueError:
                self.update_label("Sorry, I didn't catch that.")
                self.speak("Sorry, I didn't catch that.")
            except sr.RequestError:
                self.update_label("API unavailable.")
                self.speak("API unavailable.")

    def handle_query(self, query):
        query = query.lower()
        if "time" in query:
            from datetime import datetime
            time_str = datetime.now().strftime("%H:%M")
            self.update_label(f"The time is {time_str}")
            self.speak(f"The time is {time_str}")
        elif "what is" in query or "who is" in query:
            try:
                result = wikipedia.summary(query, sentences=2)
                self.update_label(result)
                self.speak(result)
            except Exception:
                self.update_label("I could not find information.")
                self.speak("I could not find information.")
        else:
            self.update_label("Command not recognized.")
            self.speak("I did not understand the command.")

class JusuAIApp(App):
    def build(self):
        return AssistantLayout()

if __name__ == "__main__":
    JusuAIApp().run()
