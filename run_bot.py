import time
from PyQt5.QtCore import QObject, pyqtSignal
from all_models import get_drop, get_info, get_items, get_token

from checkout import add_to_cart, send_checkout_request, get_order_status
from get_params import get_size_style_ids, check_matching, get_stock, get_drop_date
from search_items import SearchItem


class Bot(QObject):
    def __init__(self, date):
        super(Bot, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.date = date
        self.signals = BotSignals()
        self.is_running = True

    def run(self):
        try:
            captcha_token = get_token()
            self.signals.result.emit("Bot starting...\n")
            items = get_items()
            profile_data = get_info()
            delay = get_drop()["timer"]
            while self.is_running:
                current_stock = get_stock()
                drop_date = get_drop_date(current_stock)
                if drop_date == self.date:
                    self.signals.result.emit("Items dropped")
                    start_time = time.time()
                    session = None
                    for item in items:
                        search_item = SearchItem(current_stock, item, self.signals.result.emit)
                        item_vars = search_item.get_item_params()
                        session = search_item.to_cart(item_vars, session)
                    if session:
                        self.signals.result.emit("Checking out...")
                        if parser_checkout(session, delay, profile_data, start_time, self.signals.result.emit,
                                           captcha_token):
                            self.signals.result.emit(f"Time: {time.time() - start_time}")
                            break
                        break
                    else:
                        self.signals.result.emit("Request went wrong, try again!!!")
                        break
                self.signals.result.emit(f"Waiting for drop, date = {'-'.join(map(str, drop_date))}")
                time.sleep(0.5)
        except Exception as ex:
            self.signals.result.emit("Program finished accidentally, check \nInternet connection")
        finally:
            self.signals.result.emit("\nBot stopped")


class BotSignals(QObject):
    finished = pyqtSignal()
    error = pyqtSignal()
    result = pyqtSignal(str)
    progress = pyqtSignal()


def parser_checkout(session, timer, profile_data, checkout_start_time, sender, token):
    # Getting checkout response
    checkout_response, cookies = send_checkout_request(session, timer, profile_data, checkout_start_time, sender, token)
    if get_order_status(session, checkout_response, sender):
        # Checking order status
        return True
    return False
