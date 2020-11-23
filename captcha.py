import logging
from threading import Thread

from PyQt5.QtCore import QObject, pyqtSignal
from harvester.server import Harvester

from all_models import add_token


class Captcha(QObject):
    def __init__(self):
        super(Captcha, self).__init__()
        self.signals = CaptchaSignals()

    def run(self):
        try:
            logging.getLogger('harvester').setLevel(logging.CRITICAL)

            harvester = Harvester()

            tokens = harvester.intercept_recaptcha_v2(
                domain='www.supremenewyork.com',
                sitekey='6LeWwRkUAAAAAOBsau7KpuC9AV-6J8mhw4AjC3Xz')
            server_thread = Thread(target=harvester.serve, daemon=True)
            server_thread.start()
            harvester.launch_browser()

            token = tokens.get()
            print(token)
            if token:
                add_token(token)
                print(token)
                self.signals.result.emit('Captcha token generated')
            else:
                self.signals.result.emit('Captcha token not generated, \n'
                                               'try again.')
            server_thread.join()
        except Exception:
            self.signals.result.emit('Captcha token not generated, \n'
                                           'try again.')


class CaptchaSignals(QObject):
    result = pyqtSignal(str)

