import os
import re
from os.path import join, dirname
from dotenv import load_dotenv

apples = os.listdir(os.environ.get("APPLE"))
tomatos = os.listdir(os.environ.get("TOMATO"))

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

i = 0
for apple in apples:
  i += 1
  png = re.search('.png', apple)
  jpeg = re.search('.jpeg', apple)
  gif = re.search('.gif', apple)
  JPEG = re.search('.JPG', apple)
  jpg = re.search('.jpg', apple)
  if png or jpeg or gif or JPEG or jpg:
    base = os.path.splitext(apple)[0]
    os.rename(os.environ.get("APPLE") + apple, os.environ.get("APPLE") + '.' + str(i) + ".jpg")

i = 0
for tomato in tomatos:
  i += 1
  png = re.search('.png', tomato)
  jpeg = re.search('.jpeg', tomato)
  gif = re.search('.gif', tomato)
  JPEG = re.search('.JPG', tomato)
  jpg = re.search('.jpg', apple)
  if png or jpeg or gif or JPEG or jpg:
    base = os.path.splitext(tomato)[0]
    os.rename(apple, os.environ.get("TOMATO") + tomato, os.environ.get("TOMATO") + '.' + str(i) + ".jpg")
