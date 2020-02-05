import logging
import random
from datetime import datetime
from threading import Lock, Thread
from time import sleep

import numpy as np

logger = logging.getLogger()


class DataService:
    def __init__(self):
        self.data = []
        self.lock = Lock()

    @staticmethod
    def generate_data():
        # TODO: replace this method with an actual API call
        n = random.randint(0, 5)
        current_date = datetime.now().time().replace(microsecond=0).isoformat()
        return [(current_date, np.random.normal() + 100) for _ in range(n)]

    def requests_producer(self):
        """ Fetch new data infinitely """
        while True:
            data = self.generate_data()

            self.lock.acquire()
            try:
                self.data.extend(data)
            finally:
                self.lock.release()
            sleep(1)

    def get_and_clear_data(self):
        """ Method returns latest values from the list and clears it """
        self.lock.acquire()
        try:
            current_buffer = self.data
            self.data = []
        finally:
            self.lock.release()
        return current_buffer

    def start(self):
        """ Start a thread """
        logger.info('Starting thread for DataService')
        for worker in [self.requests_producer]:
            t = Thread(target=worker)
            t.daemon = True
            t.start()
