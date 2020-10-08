import xlrd
from ArAdjust import Reverser, Reshaper, isArabic
import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from pprint import pprint

# kivy.require('1.11.1')
# Window.size = 1200, 800

trials = [[Reshaper(Reverser(cell.value)) if any(isArabic(y) for y in cell.value) else str(cell.value) for cell in row]
          for row in xlrd.open_workbook('Test.xlsx').sheet_by_index(0).get_rows() if row]

pprint(trials)



#
# class ArInput(TextInput):
#     pass
#
#
# class OS(Screen):
#
#     def _success(self, selection):
#         self.manager.Screens[1].loadfile(selection)
#
#     def _cancel(self):
#         pass
#
#
# class TS(Screen):
#     def __init__(self):
#         super(self, TS).__init__(*args, **kwargs)
#         self.trials = []
#         self.headings = []
#
#
#     def loadfile(self, filename):
#         pass
#
#
#     def loadword(self):
#
#         pass
#
#
# class SS(Screen):
#     pass
#
#
# class SM(ScreenManager):
#     pass
#
#
# class FlashyApp(App):
#     def build(self):
#         return SM()
#
#
# if __name__ == '__main__':
#     FlashyApp().run()
