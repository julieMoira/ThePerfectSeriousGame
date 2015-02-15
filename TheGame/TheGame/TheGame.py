#!/usr/bin/python
# -*- coding: utf-8 -*-

import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget

import os

from GameScreens.StartScreen import StartScreen
from GameScreens.MapScreen import MapScreen
from GameScreens.DeskScreen import DeskScreen
from GameScreens.BossScreen import BossScreen

from Managers.GameManager import GameManager

class GameApp(App):
    def build(self):
        from kivy.base import EventLoop
        EventLoop.ensure_window()
        self.window = EventLoop.window

        self.configure()
        self.root = GameWidget(app=self)

    def configure(self):
        self.window.size = (1200, 800)
        self.APPLICATION_PATH = os.path.dirname(os.path.abspath(__file__))
        self.APPLICATION_ENV = "DEBUG"


class GameWidget(Widget):
    app = ObjectProperty(None)
    gameScreen = ObjectProperty(None)
    gameManager = object

    def __init__(self, **kwargs):
        super(GameWidget, self).__init__(**kwargs)

        try:
            self.changeScreen("LoadingScreen")
            self.gameManager = GameManager(self.app.APPLICATION_PATH)
            self.changeScreen("StartScreen")
        except Exception as ex:
            self.gameScreen.showError(ex.message)

    def changeScreen(self, screen):
        if self.gameScreen is not None:
            self.gameScreen.hide()

            while self.gameScreen.visible:
                continue

        self.clear_widgets()
        if screen == "StartScreen":
            self.gameScreen = StartScreen(app=self, opacity=0)
        elif screen == "MapScreen":
            self.gameScreen = MapScreen(app=self, opacity=0)
        elif screen == "DeskScreen":
            self.gameScreen = DeskScreen(app=self, opacity=0)
        elif screen == "BossScreen":
            self.gameScreen = BossScreen(app=self, opacity=0)
        else:
            self.gameScreen = MapScreen(app=self, opacity=0)
        self.add_widget(self.gameScreen)

        self.gameScreen.show()

GameApp().run()