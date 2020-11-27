from checkout import add_to_cart
from get_params import get_size_style_ids


class SearchItem:
    def __init__(self, stock, item, sender):
        self.stock = stock
        self.item = item
        self.sender = sender

    def get_items_in_category(self):
        return self.stock["products_and_categories"][self.item["category"]]

    def get_item_params(self):
        items_in_category = self.get_items_in_category()
        for item_in_category in items_in_category:
            if self.check_matching(self.item["name"], item_in_category["name"]):
                self.item_in_category = item_in_category
                self.item_id = item_in_category["id"]
                self.sender(f"Matching found ({item_in_category['name']})")
                return get_size_style_ids(self.item_id, self.item["size"], self.item["color"])

    def to_cart(self, data, session):
        if len(data) == 2:
            if session:
                session = add_to_cart(self.item_id, data[0], data[1], session)
            else:
                session = add_to_cart(self.item_id, data[0], data[1])

            if session:
                self.sender(f"Added to cart ({self.item_in_category['name']})")
                return session
            else:
                self.sender(f"Not added to cart ({self.item_in_category['name']})")
                return session
        else:
            if data == "sold out":
                self.sender(f"Sold out ({self.item_in_category['name']})")
                return
            else:
                self.sender(f"Size or color not found ({self.item_in_category['name']})")
                return

    def check_matching(self, sp_1, sp_2):
        if sp_1.lower() in sp_2.lower():
            return True
        return False
