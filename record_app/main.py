import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.input.recorder import Recorder

import sys
from time import sleep
import librosa
import numpy as np

import random
import os
import wave
import time
import threading
import tkinter as tk
import pyaudio
from record import VoiceRecorder

kivy.require('2.3.0')

class MyRoot(BoxLayout):

    def __init__(self):
        super(MyRoot, self).__init__()
        self.voice_recorder = VoiceRecorder(self.ids.random_label)
        self.recording = False
    
    def generate_number(self):
        if not self.recording:
            self.random_label.text = "recording"
            self.voice_recorder.start_recording()
            self.recording = True
        else:
            self.random_label.text = "-"
            self.voice_recorder.stop_recording()
            self.recording = False

class NeuralRandom(App):
    def build(self):
        return MyRoot()

if __name__ == "__main__":
    NeuralRandom().run()
