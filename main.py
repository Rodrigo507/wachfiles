from emailer import send_email
import re
from watchdog.events import PatternMatchingEventHandler, RegexMatchingEventHandler
from datetime import datetime
import time
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
    # class custom_event_handler(RegexMatchingEventHandler):
    def __init__(self, source_path):
        # event handler only file .csv
        # pattern = r'getTimeTable[0-9]{8}\.csv'
        # super(custom_event_handler, self).__init__(
        #     patterns=["*.csv"])
        # print(self.pattern)
        super(custom_event_handler, self).__init__(patterns=["*.csv"])
        self.source_path = source_path
        self.print_info = None

    def on_moved(selft, event):
        global name
        p = Path(event.src_path).name
        # name = p

    def on_created(selft, event):
        global name
        p = Path(event.src_path)
        # print(p.name)
        r1 = re.findall("getTimeTable[0-9]{8}\.csv", p.name)
        if r1:
            name = get_date_file(r1[0])
            send_email(r1[0])
            print(name)
            # print(f"{get_date_file(r1[0])}")

    def on_deleted(selft, event):
        global name
        p = Path(event.src_path).name
        # name = p

    def on_modified(selft, event):
        global name
        p = Path(event.src_path).name
        # name = p
        # print(p)

    def on_closed(selft, event):
        global name
        p = Path(event.src_path).name
        # name = p

    def return_logs(selft, event):
        return selft.print_info


# main function
if __name__ == "__main__":
    path_susbrib = config("PATH_FOR_SUSCRIB")
    custom_handler = custom_event_handler(source_path=path_susbrib)
    my_observer = Observer()
    my_observer.schedule(custom_handler, path_susbrib, recursive=True)
    my_observer.start()
    print("Iniciando script")
    try:
        while True:
            pass
            # if name != "":
            #     print(name)
            #     name = ""
            # else:
            #     name = ""
            # print(get_date_file(name))
            # if (name not in date_file) and (name != ""):
            #     date_file = name
            #     print(get_date_file(str(date_file)))
            # name = ""
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()
