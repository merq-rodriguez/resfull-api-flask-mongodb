from pathlib import Path
from dotenv import load_dotenv
from yaml import FullLoader, load
import os

class Setting(object):
  __instance = None

  def __init__(self, path=".development.yml"):
    self.__path = path
    self.config = None
    self.on_init()
  
  def __str__(self):
    return Setting.__str__

  def __new__(cls):
    if Setting.__instance is None:
      Setting.__instance = object.__new__(cls)
    return Setting.__instance

  def on_init(self):
      self.get_environments_yml()
  
  def get_environments_yml(self):
    absolute_path = os.getcwd().split("/")[:]
    env_path = "/".join(absolute_path)+"/"+self.__path
    with open(env_path) as file:
      env = load(file, Loader=FullLoader)
      self.config = env

