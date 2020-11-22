import time

from PyQt5.QtCore import QRunnable, pyqtSlot, QObject, pyqtSignal, QThread
import traceback, sys
from all_models import get_drop, get_info, get_items
from checkout import add_to_cart, send_checkout_request, get_order_status
from get_params import get_size_style_ids, check_matching, get_stock



class Bot(QObject):
    def __init__(self, date):
        super(Bot, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.date = date
        self.signals = BotSignals()

    def run(self):
        print("in run")
        self.signals.result.emit("Bot starting...")
        try:
            items = get_items()
            profile_data = get_info()
            delay = get_drop()["timer"]
            while True:
                current_stock = get_stock()
                drop_date = current_stock["release_date"].split("/")
                drop_date = (int(drop_date[2]), int(drop_date[0]), int(drop_date[1]))

                if drop_date == self.date:
                    self.signals.result.emit("Items dropped")
                    time_1 = time.time() # Return the result of the processing
                    # Start of parsing)
                    session = 0
                    print("items=", items)
                    for item in items:
                        print("item=", item)
                        # items_in_category = current_stock["products_and_categories"][item[-1]]
                        items_in_category = current_stock["products_and_categories"][item["category"]]
                        for item_in_category in items_in_category:
                            # print("item_in_category", item_in_category)
                            print(item["name"], item_in_category["name"],
                                  check_matching(item["name"], item_in_category["name"]),
                                  item_in_category["id"])
                            if check_matching(item["name"], item_in_category["name"]):
                                # if check_matching(item[0], item_in_category["name"]):
                                # To console matching found
                                print("@@@matching found@@@")
                                self.signals.result.emit(f"{item} - matching found")
                                item_id = item_in_category["id"]
                                out = get_size_style_ids(item_id, item["size"], item["color"])
                                # out = get_size_style_ids(item_id, item[1], item[2])
                                if len(out) == 2:
                                    # adding item to cart
                                    if session:
                                        session = add_to_cart(item_id, out[0], out[1], session)

                                        print("item added 1")
                                    else:
                                        session = add_to_cart(item_id, out[0], out[1])

                                        print("item added 2")

                                    if session:
                                        # To console, item  added
                                        self.signals.result.emit(f"Added to cart ({item})")
                                        print("session ok")
                                        break
                                    else:
                                        # To console, item not added
                                        self.signals.result.emit(f"Not added to cart ({item})")
                                        print("session wrong")
                                        break
                                else:
                                    if out == "sold out":
                                        # To console item sold out
                                        self.signals.result.emit(f"Sold out ({item})")
                                        print("sold out")
                                        break
                                    else:
                                        # To console no style or size found
                                        self.signals.result.emit(f"Size or style not found ({item})")
                                        print("no style or size found")

                                        break
                    print("\n\nsession\n", session, "\n!!!!!!!!!!!!!!!!!!!!!!!\n")
                    if session:
                        print("ready for parser checkout")
                        if parser_checkout(session, delay, profile_data, time.time()):
                            print("checkout right")
                            self.signals.result.emit(f"Time: {time.time() - time_1}")
                            print("time:", time.time() - time_1)
                            # To console, checkout success, check email
                            break
                        print("checkout wrong")
                        print("time:", time.time() - time_1)
                        # To console, checkout not success
                        break

                    else:
                        print("no session")
                        break
                        # To console: something went wrong

                self.signals.result.emit(f"Waiting for drop, date = {'-'.join(map(str, drop_date))}")
                time.sleep(1)
        except Exception as ex:
            print("!!!!!!!!", ex.args)

        finally:

            self.signals.result.emit("done")  # Done
            print(222222222222)

    '''def stopping(self):
        self.run.stop()'''

"""except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  # Return the result of the processing"""


class BotSignals(QObject):
    finished = pyqtSignal()
    error = pyqtSignal()
    result = pyqtSignal(str)
    progress = pyqtSignal()


def parser_checkout(session, timer, profile_data, checkout_start_time):
    print("in checkout function")
    checkout_request = send_checkout_request(session, timer, profile_data, checkout_start_time)
    print("order_status=", get_order_status(session, checkout_request))
    if get_order_status(session, checkout_request):
        print("in get order status")
        # to console: paid
        return True
    # to console: failed
    return False
