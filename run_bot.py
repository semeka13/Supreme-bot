import time

from PyQt5.QtCore import QObject, pyqtSignal
from all_models import get_drop, get_info, get_items, get_token
from checkout import add_to_cart, send_checkout_request, get_order_status
from get_params import get_size_style_ids, check_matching, get_stock


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
                drop_date = current_stock["release_date"].split("/")
                drop_date = (int(drop_date[2]), int(drop_date[0]), int(drop_date[1]))

                if drop_date == self.date:
                    self.signals.result.emit("Items dropped")
                    time_1 = time.time()
                    session = 0
                    print("items=", items)
                    for item in items:
                        print("item=", item)
                        items_in_category = current_stock["products_and_categories"][item["category"]]
                        for item_in_category in items_in_category:
                            if check_matching(item["name"], item_in_category["name"]):
                                self.signals.result.emit(f"Matching found ({item_in_category['name']})")
                                item_id = item_in_category["id"]
                                out = get_size_style_ids(item_id, item["size"], item["color"])
                                if len(out) == 2:
                                    # adding item to cart
                                    if session:
                                        session = add_to_cart(item_id, out[0], out[1], session)
                                    else:
                                        session = add_to_cart(item_id, out[0], out[1])

                                    if session:
                                        # To console, item  added
                                        self.signals.result.emit(f"Added to cart ({item_in_category['name']})")
                                        print("session ok")
                                        break
                                    else:
                                        self.signals.result.emit(f"Not added to cart ({item_in_category['name']})")
                                        break
                                else:
                                    if out == "sold out":
                                        self.signals.result.emit(f"Sold out ({item_in_category['name']})")
                                        break
                                    else:
                                        self.signals.result.emit(
                                            f"Size or color not found ({item_in_category['name']})")
                                        break
                    if session:
                        self.signals.result.emit("Checking out...")
                        if parser_checkout(session, delay, profile_data, time_1, self.signals.result.emit, captcha_token):
                            self.signals.result.emit(f"Time: {time.time() - time_1}")
                            print("time:", time.time() - time_1)
                            break
                        print("checkout wrong")
                        break

                    else:
                        self.signals.result.emit("Request went wrong, try again!!!")
                        break

                self.signals.result.emit(f"Waiting for drop, date = {'-'.join(map(str, drop_date))}")
                time.sleep(1)
        except Exception as ex:
            self.signals.result.emit("Program finished accidentally, check \nInternet connection")
            print("!!!!!!!!", ex.args)

        finally:
            self.signals.result.emit("\nBot stopped")


class BotSignals(QObject):
    finished = pyqtSignal()
    error = pyqtSignal()
    result = pyqtSignal(str)
    progress = pyqtSignal()


def parser_checkout(session, timer, profile_data, checkout_start_time, sender, token):
    # Getting checkout response
    checkout_response = send_checkout_request(session, timer, profile_data, checkout_start_time, sender, token)
    if get_order_status(session, checkout_response, sender):
        # Checking order status
        return True
    return False
