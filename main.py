from watchdog.events import PatternMatchingEventHandler
from datetime import datetime
import csv
from os import path
from decouple import config
from pathlib import Path
from watchdog.observers import Observer
name = ""
date_file = ""


def get_date_file(filename):
    return filename[-12:-4]

# custom class for event handler


class custom_event_handler(PatternMatchingEventHandler):
    def __init__(self, source_path):
        # event handler only file .csv
        super(custom_event_handler, self).__init__(patterns=["*.csv"])
        self.source_path = source_path
        self.print_info = None

    def on_moved(event):
        global name
        p = Path(event.src_path).name
        # name = p

    def on_created(selft, event):
        global name
        p = Path(event.src_path)
        name = p

    def on_deleted(event):
        global name
        p = Path(event.src_path).name
        # name = p

    def on_modified(event):
        global name
        p = Path(event.src_path).name
        # name = p
        # print(p)

    def on_closed(event):
        global name
        p = Path(event.src_path).name
        # name = p

    def return_logs(self):
        return self.print_info


# main function
if __name__ == "__main__":
    path_susbrib = config("PATH_FOR_SUSCRIB")
    custom_handler = custom_event_handler(source_path=path_susbrib)
    my_observer = Observer()
    my_observer.schedule(custom_handler, path_susbrib, recursive=True)
    my_observer.start()
    try:
        while True:
            if (name != date_file) and (name != ""):
                date_file = name
                print(get_date_file(str(date_file)))
            name = ""
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()
