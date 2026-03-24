import os
from core.loader import load_verses
from ui.app_window import AppWindow

verses = load_verses("data/verses.json")
AppWindow(verses)