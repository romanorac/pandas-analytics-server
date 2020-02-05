import logging
from datetime import datetime
from threading import Lock, Thread
from time import sleep

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

logger = logging.getLogger()


class StrategyService:
    def __init__(self, data_service):
        self.data_service = data_service
        self.max_df_len = 100  # max size of DataFrame
        self.n_reduce_to = 50  # when max size is reached, reduce to this size
        self.df = pd.DataFrame()
        self.lock = Lock()

    def apply(self):
        """ apply the strategy """
        # TODO: replace the code with your strategy. Currently code just append rows
        while True:
            data = self.data_service.get_and_clear_data()
            if data:
                df_current = pd.DataFrame(data, columns=['timestamp', 'price'])
                df_current.set_index('timestamp', inplace=True)

                self.lock.acquire()
                try:
                    self.df = self.df.append(df_current)
                    if len(self.df) > self.max_df_len:
                        self.df = self.df[-self.n_reduce_to:]
                finally:
                    self.lock.release()
            sleep(1)

    def plot(self, n_entries):
        self.lock.acquire()
        try:
            if len(self.df) < 10:
                return None
            current_datetime = datetime.now().replace(microsecond=0).isoformat().replace('T', ' ')
            fig, ax = plt.subplots(2, 2, figsize=(20, 10))
            fig.suptitle('Plots with last %d entries at %s' % (n_entries, current_datetime),
                         fontsize=16)

            ax[0, 0].set_title('price line plot')
            self.df[-n_entries:].price.plot(ax=ax[0, 0], color='navy')

            ax[0, 1].set_title('log price line plot')
            self.df[-n_entries:].price.apply(np.log).plot(ax=ax[0, 1], color='darkgreen')

            ax[1, 0].set_title('histogram plot')
            self.df[-n_entries:].price.hist(ax=ax[1, 0], bins=30, color='deepskyblue')

            ax[1, 1].set_title('log histogram plot')
            self.df[-n_entries:].price.apply(np.log).hist(ax=ax[1, 1], bins=30, color='darkcyan')
        finally:
            self.lock.release()
        return fig

    def start(self):
        logger.info('Starting threads for StrategyService')
        for worker in [self.apply]:
            t = Thread(target=worker)
            t.daemon = True
            t.start()
