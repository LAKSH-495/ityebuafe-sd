import sys
import time 
import random 
import os 
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

source_folder = "C:\\Users\\Admin\\Desktop\\time pass folder source"
destination_folder = "C:\\Users\\Admin\\Desktop\\time pass folder destination"

class FileEventHandler(FileSystemEventHandler):
    def on_created(self,event):
        print(f"hey,{event.src_path} has been created")
    def on_deleted(self,event):
        print(f"Oops!,{event.src_path} has been delted")   

eventhandler = FileEventHandler()
observer = Observer()
observer.schedule(eventhandler,source_folder,recursive=True)
observer.start()
try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped")
    observer.stop()