import os

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty, BooleanProperty, StringProperty
from kivy.factory import Factory
from kivy.uix.popup import Popup
import GUIdetect as recognition
import sys

import subprocess

Builder.load_file('layout.kv')

class LoadModelDialog(FloatLayout):
    load_model = ObjectProperty(None)
    cancel = ObjectProperty(None)

class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

class AppLayout(FloatLayout):
    loadfile = ObjectProperty(None)
    isShownVideoLoadMenu = BooleanProperty(False)
    isShownStreamUrlInput = BooleanProperty(True)
    sourceFilePath = StringProperty("")
    modelFilePath = StringProperty("")

    def dismiss_popup(self):
        self._popup.dismiss()

    def load(self, path, filename):
        filepath = str(filename[0])
        self.sourceFilePath = os.path.basename(filepath).split('/')[-1]
        self.ids.video_path_input.text = os.path.basename(filepath).split('/')[-1]
        self.dismiss_popup()

    def load_model(self, filepath):

        modelPath = str(filepath[0])
        self.modelFilePath = os.path.basename(modelPath).split('/')[-1]
        self.ids.model_path_input.text = os.path.basename(modelPath).split('/')[-1]
        self.dismiss_popup()

    def show_video_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def show_model_load(self):
        content = LoadModelDialog(load_model=self.load_model, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load model", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def process_input(self):
        self.sourceFilePath = self.ids.urlInput.text
        print(self.sourceFilePath)

    def run_recognition(self, isStream, modelPath, source):
        if (isStream):
            recognition.detect(source=source, weights=f'trainedModels/{modelPath}', conf_thresh=0.4, imgsz=640, view_img=True, trace=False)
        else:
            recognition.detect(source=f'videoClips/{source}', weights=f'trainedModels/{modelPath}', conf_thresh=0.4, imgsz=640, view_img=True, trace=False)


class BirdRecognitionApp(App):

    def build(self):
        return AppLayout()


Factory.register('AppLayout', cls=AppLayout)
Factory.register('LoadDialog', cls=LoadDialog)
Factory.register('LoadModelDialog', cls=LoadModelDialog)

if __name__ == '__main__':
    BirdRecognitionApp().run()
