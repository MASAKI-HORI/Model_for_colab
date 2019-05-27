from icrawler.builtin import GoogleImageCrawler
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
print(os.environ.get("APPLE_PIC"))
print(os.environ.get("APPLE"))
os.mkdir(os.environ.get("APPLE_PIC"))
crawler = GoogleImageCrawler(storage={"root_dir": str(os.environ.get("APPLE_PIC"))})
crawler.crawl(keyword="apple fluits", max_num=1000, filters={
  "type": "photo",
  "color": "red",
})

os.mkdir(os.environ.get("TOMATO_PIC"))
crawler = GoogleImageCrawler(storage={"root_dir": str(os.environ.get("TOMATO_PIC"))})
crawler.crawl(keyword="tomato vegetable", max_num=1000, filters={
  "type": "photo",
  "color": "red",
})