import requests


def get_stock():
    """
    Make a request to Supreme website and returns current stock
{'unique_image_url_prefixes': [], 'products_and_categories': {'Skate': [{'name': 'Supreme®/Spitfire® Classic Wheels (Set of 4)', 'id': 305244, 'image_url': '//d17ol771963kd3.cloudfront.net/196323/ca/Arkfk-mjwbk.jpg', 'image_url_hi': '//assets.supremenewyork.com/196323/rc/Arkfk-mjwbk.jpg', 'price': 3000, 'sale_price': 0, 'new_item': False, 'position': 50, 'category_name': 'Skate', 'price_euro': 4500, 'sale_price_euro': 0}, {'name': 'Supreme®/Independent® Truck', 'id': 305241, 'image_url': '//d17ol771963kd3.cloudfront.net/196331/ca/_RFtLT9T4NA.jpg', 'image_url_hi': '//assets.supremenewyork.com/196331/rc/_RFtLT9T4NA.jpg', 'price': 6400, 'sale_price': 0, 'new_item': False, 'position': 51, 'category_name': 'Skate', 'price_euro': 8000, 'sale_price_euro': 0}], 'Accessories': [{'name': 'Camo iPhone Case', 'id': 305531, 'image_url': '//d17ol771963kd3.cloudfront.net/198613/ca/uVenA7yXMrI.jpg', 'image_url_hi': '//assets.supremenewyork.com/198613/rc/uVenA7yXMrI.jpg', 'price': 3200, 'sale_price': 0, 'new_item': True, 'position': 43, 'category_name': 'Accessories', 'price_euro': 3600, 'sale_price_euro': 0}, {'name': 'Supreme®/Hohner® Keychain', 'id': 305529, 'image_url': '//d17ol771963kd3.cloudfront.net/196012/ca/HGguzYlx9nc.jpg', 'image_url_hi': '//assets.supremenewyork.com/196012/rc/HGguzYlx9nc.jpg', 'price': 3000, 'sale_price': 0, 'new_item': True, 'position': 44, 'category_name': 'Accessories', 'price_euro': 3200, 'sale_price_euro': 0}, {'name': 'Supreme®/Anker Nebula Capsule II Projector', 'id': 305291, 'image_url': '//d17ol771963kd3.cloudfront.net/195780/ca/motvJeWx7XM.jpg', 'image_url_hi': '//assets.supremenewyork.com/195780/rc/motvJeWx7XM.jpg', 'price': 55800, 'sale_price': 0, 'new_item': False, 'position': 45, 'category_name': 'Accessories', 'price_euro': 62800, 'sale_price_euro': 0}, {'name': 'Name Badge Stickers (Pack of 100)', 'id': 305279, 'image_url': '//d17ol771963kd3.cloudfront.net/195895/ca/9nwy8TBNVvA.jpg', 'image_url_hi': '//assets.supremenewyork.com/195895/rc/9nwy8TBNVvA.jpg', 'price': 1200, 'sale_price': 0, 'new_item': False, 'position': 46, 'category_name': 'Accessories', 'price_euro': 1400, 'sale_price_euro': 0}, {'name': 'Supreme®/Hanes® Tagless Tees (3 Pack)', 'id': 305322, 'image_url': '//d17ol771963kd3.cloudfront.net/343542/ca/BpsW5dyl3Qo.jpg', 'image_url_hi': '//assets.supremenewyork.com/343542/rc/BpsW5dyl3Qo.jpg', 'price': 2500, 'sale_price': 0, 'new_item': False, 'position': 47, 'category_name': 'Accessories', 'price_euro': 2800, 'sale_price_euro': 0}, {'name': 'Supreme®/Hanes® Boxer Briefs (4 Pack)', 'id': 305321, 'image_url': '//d17ol771963kd3.cloudfront.net/343539/ca/JWJq1LqdADI.jpg', 'image_url_hi': '//assets.supremenewyork.com/343539/rc/JWJq1LqdADI.jpg', 'price': 3200, 'sale_price': 0, 'new_item': False, 'position': 48, 'category_name': 'Accessories', 'price_euro': 3600, 'sale_price_euro': 0}, {'name': 'Supreme®/Hanes® Crew Socks (4 Pack)', 'id': 305243, 'image_url': '//d17ol771963kd3.cloudfront.net/196316/ca/kYTpmeDf3jM.jpg', 'image_url_hi': '//assets.supremenewyork.com/196316/rc/kYTpmeDf3jM.jpg', 'price': 1800, 'sale_price': 0, 'new_item': False, 'position': 49, 'category_name': 'Accessories', 'price_euro': 2000, 'sale_price_euro': 0}], 'Bags': [{'name': 'Canvas Backpack', 'id': 305415, 'image_url': '//d17ol771963kd3.cloudfront.net/195627/ca/eQapnOLLW_E.jpg', 'image_url_hi': '//assets.supremenewyork.com/195627/rc/eQapnOLLW_E.jpg', 'price': 9800, 'sale_price': 0, 'new_item': False, 'position': 38, 'category_name': 'Bags', 'price_euro': 11000, 'sale_price_euro': 0}, {'name': 'Canvas Tote', 'id': 305405, 'image_url': '//d17ol771963kd3.cloudfront.net/195425/ca/FrE3aUUDnYU.jpg', 'image_url_hi': '//assets.supremenewyork.com/195425/rc/FrE3aUUDnYU.jpg', 'price': 6800, 'sale_price': 0, 'new_item': False, 'position': 39, 'category_name': 'Bags', 'price_euro': 7800, 'sale_price_euro': 0}, {'name': 'Backpack', 'id': 305277, 'image_url': '//d17ol771963kd3.cloudfront.net/195565/ca/-B0ydah-R2Q.jpg', 'image_url_hi': '//assets.supremenewyork.com/195565/rc/-B0ydah-R2Q.jpg', 'price': 12800, 'sale_price': 0, 'new_item': False, 'position': 40, 'category_name': 'Bags', 'price_euro': 14800, 'sale_price_euro': 0}, {'name': 'Zip Tote', 'id': 305248, 'image_url': '//d17ol771963kd3.cloudfront.net/195579/ca/0srRDFGpYPQ.jpg', 'image_url_hi': '//assets.supremenewyork.com/195579/rc/0srRDFGpYPQ.jpg', 'price': 9800, 'sale_price': 0, 'new_item': False, 'position': 41, 'category_name': 'Bags', 'price_euro': 11000, 'sale_price_euro': 0}, {'name': 'Neck Pouch', 'id': 305299, 'image_url': '//d17ol771963kd3.cloudfront.net/196433/ca/4lvMUwqZVvo.jpg', 'image_url_hi': '//assets.supremenewyork.com/196433/rc/4lvMUwqZVvo.jpg', 'price': 3400, 'sale_price': 0, 'new_item': False, 'position': 42, 'category_name': 'Bags', 'price_euro': 3800, 'sale_price_euro': 0}], 'Pants': [{'name': 'Toshio Saeki/Supreme Work Pant', 'id': 305533, 'image_url': '//d17ol771963kd3.cloudfront.net/194207/ca/sXulVbz8bPM.jpg', 'image_url_hi': '//assets.supremenewyork.com/194207/rc/sXulVbz8bPM.jpg', 'price': 22800, 'sale_price': 0, 'new_item': True, 'position': 23, 'category_name': 'Pants', 'price_euro': 25800, 'sale_price_euro': 0}, {'name': '2-Tone Cinch Pant', 'id': 305522, 'image_url': '//d17ol771963kd3.cloudfront.net/194529/ca/KV9yABv4pZo.jpg', 'image_url_hi': '//assets.supremenewyork.com/194529/rc/KV9yABv4pZo.jpg', 'price': 11000, 'sale_price': 0, 'new_item': True, 'position': 24, 'category_name': 'Pants', 'price_euro': 12800, 'sale_price_euro': 0}, {'name': 'Cargo Pant', 'id': 305467, 'image_url': '//d17ol771963kd3.cloudfront.net/194249/ca/toytbv916e4.jpg', 'image_url_hi': '//assets.supremenewyork.com/194249/rc/toytbv916e4.jpg', 'price': 13800, 'sale_price': 0, 'new_item': False, 'position': 25, 'category_name': 'Pants', 'price_euro': 15800, 'sale_price_euro': 0}, {'name': 'Pin Up Chino Pant', 'id': 305515, 'image_url': '//d17ol771963kd3.cloudfront.net/194263/ca/bblh7atuHmk.jpg', 'image_url_hi': '//assets.supremenewyork.com/194263/rc/bblh7atuHmk.jpg', 'price': 12800, 'sale_price': 0, 'new_item': False, 'position': 26, 'category_name': 'Pants', 'price_euro': 14800, 'sale_price_euro': 0}, {'name': 'Studded Work Pant', 'id': 305278, 'image_url': '//d17ol771963kd3.cloudfront.net/194367/ca/zG4HSs6NmtA.jpg', 'image_url_hi': '//assets.supremenewyork.com/194367/rc/zG4HSs6NmtA.jpg', 'price': 12800, 'sale_price': 0, 'new_item': False, 'position': 27, 'category_name': 'Pants', 'price_euro': 14800, 'sale_price_euro': 0}, {'name': 'Work Pant', 'id': 305290, 'image_url': '//d17ol771963kd3.cloudfront.net/194193/ca/xLm96lFZSt8.jpg', 'image_url_hi': '//assets.supremenewyork.com/194193/rc/-KJSo14zwn8.jpg', 'price': 11000, 'sale_price': 0, 'new_item': False, 'position': 28, 'category_name': 'Pants', 'price_euro': 11800, 'sale_price_euro': 0}, {'name': 'Big Stitch Sweatpant', 'id': 305497, 'image_url': '//d17ol771963kd3.cloudfront.net/198220/ca/ZQH5L0MRpk4.jpg', 'image_url_hi': '//assets.supremenewyork.com/198220/rc/ZQH5L0MRpk4.jpg', 'price': 12800, 'sale_price': 0, 'new_item': False, 'position': 29, 'category_name': 'Pants', 'price_euro': 14800, 'sale_price_euro': 0}], 'Jackets': [{'name': 'Hooded Down Jacket ', 'id': 305527, 'image_url': '//d17ol771963kd3.cloudfront.net/198626/ca/CBS2FNm4Qko.jpg', 'image_url_hi': '//assets.supremenewyork.com/198626/rc/CBS2FNm4Qko.jpg', 'price': 33800, 'sale_price': 0, 'new_item': True, 'position': 1, 'category_name': 'Jackets', 'price_euro': 35800, 'sale_price_euro': 0}, {'name': 'Toshio Saeki/Supreme Work Jacket', 'id': 305526, 'image_url': '//d17ol771963kd3.cloudfront.net/198648/ca/EbtrrfdHRcw.jpg', 'image_url_hi': '//assets.supremenewyork.com/198648/rc/EbtrrfdHRcw.jpg', 'price': 32800, 'sale_price': 0, 'new_item': True, 'position': 4, 'category_name': 'Jackets', 'price_euro': 35800, 'sale_price_euro': 0}, {'name': 'Supreme®/Vanson Leathers® Worn Leather Jacket', 'id': 305293, 'image_url': '//d17ol771963kd3.cloudfront.net/193535/ca/pF50u7V6-fE.jpg', 'image_url_hi': '//assets.supremenewyork.com/193535/rc/pF50u7V6-fE.jpg', 'price': 76800, 'sale_price': 0, 'new_item': False, 'position': 2, 'category_name': 'Jackets', 'price_euro': 84800, 'sale_price_euro': 0}, {'name': 'King Hooded Varsity Jacket', 'id': 305490, 'image_url': '//d17ol771963kd3.cloudfront.net/193815/ca/FNLseAwAu38.jpg', 'image_url_hi': '//assets.supremenewyork.com/193815/rc/FNLseAwAu38.jpg', 'price': 39800, 'sale_price': 0, 'new_item': False, 'position': 3, 'category_name': 'Jackets', 'price_euro': 44800, 'sale_price_euro': 0}], 'Sweatshirts': [{'name': 'Toshio Saeki/Supreme Hooded Sweatshirt', 'id': 305525, 'image_url': '//d17ol771963kd3.cloudfront.net/198634/ca/lMNe5BOQqU8.jpg', 'image_url_hi': '//assets.supremenewyork.com/198634/rc/lMNe5BOQqU8.jpg', 'price': 21800, 'sale_price': 0, 'new_item': True, 'position': 10, 'category_name': 'Sweatshirts', 'price_euro': 24800, 'sale_price_euro': 0}, {'name': 'Side Logo Crewneck', 'id': 305538, 'image_url': '//d17ol771963kd3.cloudfront.net/198644/ca/F3CkJl9Y8Fk.jpg', 'image_url_hi': '//assets.supremenewyork.com/198644/rc/F3CkJl9Y8Fk.jpg', 'price': 13800, 'sale_price': 0, 'new_item': True, 'position': 11, 'category_name': 'Sweatshirts', 'price_euro': 15800, 'sale_price_euro': 0}, {'name': 'Hockey Hooded Sweatshirt', 'id': 305508, 'image_url': '//d17ol771963kd3.cloudfront.net/195103/ca/ZIC2b7lyrtg.jpg', 'image_url_hi': '//assets.supremenewyork.com/195103/rc/ZIC2b7lyrtg.jpg', 'price': 14800, 'sale_price': 0, 'new_item': False, 'position': 12, 'category_name': 'Sweatshirts', 'price_euro': 16800, 'sale_price_euro': 0}, {'name': 'Zip Up Sweat Vest', 'id': 305311, 'image_url': '//d17ol771963kd3.cloudfront.net/194707/ca/Pw-rXjad5tY.jpg', 'image_url_hi': '//assets.supremenewyork.com/194707/rc/Pw-rXjad5tY.jpg', 'price': 9800, 'sale_price': 0, 'new_item': False, 'position': 13, 'category_name': 'Sweatshirts', 'price_euro': 11000, 'sale_price_euro': 0}], 'Shirts': [{'name': 'Classic Logo Denim Shirt', 'id': 305539, 'image_url': '//d17ol771963kd3.cloudfront.net/194054/ca/SuPniivuSPs.jpg', 'image_url_hi': '//assets.supremenewyork.com/194054/rc/SuPniivuSPs.jpg', 'price': 11000, 'sale_price': 0, 'new_item': True, 'position': 6, 'category_name': 'Shirts', 'price_euro': 12800, 'sale_price_euro': 0}, {'name': 'Logo Taping Work Shirt', 'id': 305462, 'image_url': '//d17ol771963kd3.cloudfront.net/194081/ca/JtcHLwyzZJI.jpg', 'image_url_hi': '//assets.supremenewyork.com/194081/rc/JtcHLwyzZJI.jpg', 'price': 11800, 'sale_price': 0, 'new_item': False, 'position': 7, 'category_name': 'Shirts', 'price_euro': 13800, 'sale_price_euro': 0}, {'name': 'Chains Rayon S/S Shirt', 'id': 305494, 'image_url': '//assets.supremenewyork.com/194174/ca/pyj-9HeUX44.jpg', 'image_url_hi': '//assets.supremenewyork.com/194174/rc/pyj-9HeUX44.jpg', 'price': 11800, 'sale_price': 0, 'new_item': False, 'position': 8, 'category_name': 'Shirts', 'price_euro': 13800, 'sale_price_euro': 0}, {'name': 'Jacquard Stripe Twill Shirt', 'id': 305430, 'image_url': '//assets.supremenewyork.com/193997/ca/nlIYTm_coRY.jpg', 'image_url_hi': '//assets.supremenewyork.com/193997/rc/nlIYTm_coRY.jpg', 'price': 11000, 'sale_price': 0, 'new_item': False, 'position': 9, 'category_name': 'Shirts', 'price_euro': 12800, 'sale_price_euro': 0}], 'Tops/Sweaters': [{'name': 'Brushed Plaid Sweater', 'id': 305534, 'image_url': '//d17ol771963kd3.cloudfront.net/193970/ca/_0tE1RVj52Q.jpg', 'image_url_hi': '//assets.supremenewyork.com/193970/rc/_0tE1RVj52Q.jpg', 'price': 12800, 'sale_price': 0, 'new_item': True, 'position': 5, 'category_name': 'Tops/Sweaters', 'price_euro': 14800, 'sale_price_euro': 0}, {'name': 'Stati Uniti Stripe S/S Top', 'id': 305537, 'image_url': '//d17ol771963kd3.cloudfront.net/195237/ca/RMr-WVmuTZQ.jpg', 'image_url_hi': '//assets.supremenewyork.com/195237/rc/RMr-WVmuTZQ.jpg', 'price': 7800, 'sale_price': 0, 'new_item': True, 'position': 14, 'category_name': 'Tops/Sweaters', 'price_euro': 8800, 'sale_price_euro': 0}, {'name': 'Woven Label L/S Top', 'id': 305540, 'image_url': '//d17ol771963kd3.cloudfront.net/195188/ca/c7KFjswRsiU.jpg', 'image_url_hi': '//assets.supremenewyork.com/195188/rc/c7KFjswRsiU.jpg', 'price': 5800, 'sale_price': 0, 'new_item': True, 'position': 15, 'category_name': 'Tops/Sweaters', 'price_euro': 6800, 'sale_price_euro': 0}, {'name': 'Small Box L/S Tee', 'id': 305523, 'image_url': '//d17ol771963kd3.cloudfront.net/194898/ca/_bhZ7-LkGmM.jpg', 'image_url_hi': '//assets.supremenewyork.com/194898/rc/_bhZ7-LkGmM.jpg', 'price': 5800, 'sale_price': 0, 'new_item': True, 'position': 16, 'category_name': 'Tops/Sweaters', 'price_euro': 6800, 'sale_price_euro': 0}, {'name': 'Bobsled L/S Top', 'id': 305495, 'image_url': '//assets.supremenewyork.com/195295/ca/ucF2uT6BYM8.jpg', 'image_url_hi': '//assets.supremenewyork.com/195295/rc/ucF2uT6BYM8.jpg', 'price': 8800, 'sale_price': 0, 'new_item': False, 'position': 17, 'category_name': 'Tops/Sweaters', 'price_euro': 9800, 'sale_price_euro': 0}, {'name': 'Cutout Logo S/S Top', 'id': 305507, 'image_url': '//assets.supremenewyork.com/194922/ca/f0Ve66A2Zbs.jpg', 'image_url_hi': '//assets.supremenewyork.com/194922/rc/f0Ve66A2Zbs.jpg', 'price': 6800, 'sale_price': 0, 'new_item': False, 'position': 18, 'category_name': 'Tops/Sweaters', 'price_euro': 7800, 'sale_price_euro': 0}, {'name': 'World Class L/S Top', 'id': 305471, 'image_url': '//assets.supremenewyork.com/195248/ca/BA8S7cdqaI4.jpg', 'image_url_hi': '//assets.supremenewyork.com/195248/rc/BA8S7cdqaI4.jpg', 'price': 7800, 'sale_price': 0, 'new_item': False, 'position': 19, 'category_name': 'Tops/Sweaters', 'price_euro': 8800, 'sale_price_euro': 0}, {'name': 'Interstate Waffle Thermal ', 'id': 305520, 'image_url': '//assets.supremenewyork.com/195263/ca/3_QjND7E6ys.jpg', 'image_url_hi': '//assets.supremenewyork.com/195263/rc/3_QjND7E6ys.jpg', 'price': 8800, 'sale_price': 0, 'new_item': False, 'position': 20, 'category_name': 'Tops/Sweaters', 'price_euro': 9800, 'sale_price_euro': 0}, {'name': 'Shoulder Arc S/S Top', 'id': 305484, 'image_url': '//d17ol771963kd3.cloudfront.net/195123/ca/PJpmBhG-xQk.jpg', 'image_url_hi': '//assets.supremenewyork.com/195123/rc/PJpmBhG-xQk.jpg', 'price': 5800, 'sale_price': 0, 'new_item': False, 'position': 21, 'category_name': 'Tops/Sweaters', 'price_euro': 6800, 'sale_price_euro': 0}, {'name': 'Oval S/S Top', 'id': 305486, 'image_url': '//assets.supremenewyork.com/195272/ca/OXNUoFij-9A.jpg', 'image_url_hi': '//assets.supremenewyork.com/195272/rc/OXNUoFij-9A.jpg', 'price': 4800, 'sale_price': 0, 'new_item': False, 'position': 22, 'category_name': 'Tops/Sweaters', 'price_euro': 5800, 'sale_price_euro': 0}], 'Hats': [{'name': 'Supreme®/Nike® Air Max Plus Running Hat', 'id': 305530, 'image_url': '//d17ol771963kd3.cloudfront.net/198824/ca/DGYfbkjYNCk.jpg', 'image_url_hi': '//assets.supremenewyork.com/198824/rc/DGYfbkjYNCk.jpg', 'price': 3800, 'sale_price': 0, 'new_item': True, 'position': 31, 'category_name': 'Hats', 'price_euro': 4500, 'sale_price_euro': 0}, {'name': 'Inset Logo Camp Cap', 'id': 305532, 'image_url': '//d17ol771963kd3.cloudfront.net/195114/ca/tb8IRFF4_QM.jpg', 'image_url_hi': '//assets.supremenewyork.com/195114/rc/tb8IRFF4_QM.jpg', 'price': 5000, 'sale_price': 0, 'new_item': True, 'position': 32, 'category_name': 'Hats', 'price_euro': 5600, 'sale_price_euro': 0}, {'name': 'WINDSTOPPER® Small Box Earflap 6-Panel', 'id': 305528, 'image_url': '//d17ol771963kd3.cloudfront.net/198739/ca/Ypcd2ZBpRiI.jpg', 'image_url_hi': '//assets.supremenewyork.com/198739/rc/Ypcd2ZBpRiI.jpg', 'price': 5400, 'sale_price': 0, 'new_item': True, 'position': 33, 'category_name': 'Hats', 'price_euro': 6000, 'sale_price_euro': 0}, {'name': 'Snakeskin Corduroy Bell Hat', 'id': 305524, 'image_url': '//d17ol771963kd3.cloudfront.net/195347/ca/TlqU_O67sYo.jpg', 'image_url_hi': '//assets.supremenewyork.com/195347/rc/TlqU_O67sYo.jpg', 'price': 5000, 'sale_price': 0, 'new_item': True, 'position': 34, 'category_name': 'Hats', 'price_euro': 5600, 'sale_price_euro': 0}, {'name': 'Alpine Beanie', 'id': 305541, 'image_url': '//d17ol771963kd3.cloudfront.net/195516/ca/bz9D8uOSlgk.jpg', 'image_url_hi': '//assets.supremenewyork.com/195516/rc/bz9D8uOSlgk.jpg', 'price': 3200, 'sale_price': 0, 'new_item': True, 'position': 35, 'category_name': 'Hats', 'price_euro': 3600, 'sale_price_euro': 0}, {'name': 'Woven Label Beanie', 'id': 305536, 'image_url': '//d17ol771963kd3.cloudfront.net/198747/ca/aNT_CCLisBY.jpg', 'image_url_hi': '//assets.supremenewyork.com/198747/rc/aNT_CCLisBY.jpg', 'price': 3000, 'sale_price': 0, 'new_item': True, 'position': 36, 'category_name': 'Hats', 'price_euro': 3400, 'sale_price_euro': 0}, {'name': 'New Era® Sequin Beanie', 'id': 305510, 'image_url': '//d17ol771963kd3.cloudfront.net/195605/ca/7n-d3SXk5uM.jpg', 'image_url_hi': '//assets.supremenewyork.com/195605/rc/7n-d3SXk5uM.jpg', 'price': 3400, 'sale_price': 0, 'new_item': False, 'position': 37, 'category_name': 'Hats', 'price_euro': 3800, 'sale_price_euro': 0}], 'Shorts': [{'name': 'Spray Sweatshort', 'id': 305516, 'image_url': '//d17ol771963kd3.cloudfront.net/194433/ca/rSpDoVbzkgg.jpg', 'image_url_hi': '//assets.supremenewyork.com/194433/rc/rSpDoVbzkgg.jpg', 'price': 9800, 'sale_price': 0, 'new_item': False, 'position': 30, 'category_name': 'Shorts', 'price_euro': 11800, 'sale_price_euro': 0}], 'Shoes': [{'name': 'Supreme®/Nike® Air Max Plus', 'id': 305535, 'image_url': '//d17ol771963kd3.cloudfront.net/198820/ca/Gr1pWt4E4VI.jpg', 'image_url_hi': '//assets.supremenewyork.com/198820/rc/Gr1pWt4E4VI.jpg', 'price': 16000, 'sale_price': 0, 'new_item': True, 'position': 0, 'category_name': 'Shoes', 'price_euro': 18000, 'sale_price_euro': 0}], 'new': [{'name': 'Toshio Saeki/Supreme Work Jacket', 'id': 305526, 'image_url': '//d17ol771963kd3.cloudfront.net/198648/ca/EbtrrfdHRcw.jpg', 'image_url_hi': '//assets.supremenewyork.com/198648/rc/EbtrrfdHRcw.jpg', 'price': 32800, 'sale_price': 0, 'new_item': True, 'position': 4, 'category_name': 'Jackets', 'price_euro': 35800, 'sale_price_euro': 0}, {'name': 'Hooded Down Jacket ', 'id': 305527, 'image_url': '//d17ol771963kd3.cloudfront.net/198626/ca/CBS2FNm4Qko.jpg', 'image_url_hi': '//assets.supremenewyork.com/198626/rc/CBS2FNm4Qko.jpg', 'price': 33800, 'sale_price': 0, 'new_item': True, 'position': 1, 'category_name': 'Jackets', 'price_euro': 35800, 'sale_price_euro': 0}, {'name': 'Classic Logo Denim Shirt', 'id': 305539, 'image_url': '//d17ol771963kd3.cloudfront.net/194054/ca/SuPniivuSPs.jpg', 'image_url_hi': '//assets.supremenewyork.com/194054/rc/SuPniivuSPs.jpg', 'price': 11000, 'sale_price': 0, 'new_item': True, 'position': 6, 'category_name': 'Shirts', 'price_euro': 12800, 'sale_price_euro': 0}, {'name': 'Small Box L/S Tee', 'id': 305523, 'image_url': '//d17ol771963kd3.cloudfront.net/194898/ca/_bhZ7-LkGmM.jpg', 'image_url_hi': '//assets.supremenewyork.com/194898/rc/_bhZ7-LkGmM.jpg', 'price': 5800, 'sale_price': 0, 'new_item': True, 'position': 16, 'category_name': 'Tops/Sweaters', 'price_euro': 6800, 'sale_price_euro': 0}, {'name': 'Brushed Plaid Sweater', 'id': 305534, 'image_url': '//d17ol771963kd3.cloudfront.net/193970/ca/_0tE1RVj52Q.jpg', 'image_url_hi': '//assets.supremenewyork.com/193970/rc/_0tE1RVj52Q.jpg', 'price': 12800, 'sale_price': 0, 'new_item': True, 'position': 5, 'category_name': 'Tops/Sweaters', 'price_euro': 14800, 'sale_price_euro': 0}, {'name': 'Stati Uniti Stripe S/S Top', 'id': 305537, 'image_url': '//d17ol771963kd3.cloudfront.net/195237/ca/RMr-WVmuTZQ.jpg', 'image_url_hi': '//assets.supremenewyork.com/195237/rc/RMr-WVmuTZQ.jpg', 'price': 7800, 'sale_price': 0, 'new_item': True, 'position': 14, 'category_name': 'Tops/Sweaters', 'price_euro': 8800, 'sale_price_euro': 0}, {'name': 'Woven Label L/S Top', 'id': 305540, 'image_url': '//d17ol771963kd3.cloudfront.net/195188/ca/c7KFjswRsiU.jpg', 'image_url_hi': '//assets.supremenewyork.com/195188/rc/c7KFjswRsiU.jpg', 'price': 5800, 'sale_price': 0, 'new_item': True, 'position': 15, 'category_name': 'Tops/Sweaters', 'price_euro': 6800, 'sale_price_euro': 0}, {'name': 'Toshio Saeki/Supreme Hooded Sweatshirt', 'id': 305525, 'image_url': '//d17ol771963kd3.cloudfront.net/198634/ca/lMNe5BOQqU8.jpg', 'image_url_hi': '//assets.supremenewyork.com/198634/rc/lMNe5BOQqU8.jpg', 'price': 21800, 'sale_price': 0, 'new_item': True, 'position': 10, 'category_name': 'Sweatshirts', 'price_euro': 24800, 'sale_price_euro': 0}, {'name': 'Side Logo Crewneck', 'id': 305538, 'image_url': '//d17ol771963kd3.cloudfront.net/198644/ca/F3CkJl9Y8Fk.jpg', 'image_url_hi': '//assets.supremenewyork.com/198644/rc/F3CkJl9Y8Fk.jpg', 'price': 13800, 'sale_price': 0, 'new_item': True, 'position': 11, 'category_name': 'Sweatshirts', 'price_euro': 15800, 'sale_price_euro': 0}, {'name': '2-Tone Cinch Pant', 'id': 305522, 'image_url': '//d17ol771963kd3.cloudfront.net/194529/ca/KV9yABv4pZo.jpg', 'image_url_hi': '//assets.supremenewyork.com/194529/rc/KV9yABv4pZo.jpg', 'price': 11000, 'sale_price': 0, 'new_item': True, 'position': 24, 'category_name': 'Pants', 'price_euro': 12800, 'sale_price_euro': 0}, {'name': 'Toshio Saeki/Supreme Work Pant', 'id': 305533, 'image_url': '//d17ol771963kd3.cloudfront.net/194207/ca/sXulVbz8bPM.jpg', 'image_url_hi': '//assets.supremenewyork.com/194207/rc/sXulVbz8bPM.jpg', 'price': 22800, 'sale_price': 0, 'new_item': True, 'position': 23, 'category_name': 'Pants', 'price_euro': 25800, 'sale_price_euro': 0}, {'name': 'Snakeskin Corduroy Bell Hat', 'id': 305524, 'image_url': '//d17ol771963kd3.cloudfront.net/195347/ca/TlqU_O67sYo.jpg', 'image_url_hi': '//assets.supremenewyork.com/195347/rc/TlqU_O67sYo.jpg', 'price': 5000, 'sale_price': 0, 'new_item': True, 'position': 34, 'category_name': 'Hats', 'price_euro': 5600, 'sale_price_euro': 0}, {'name': 'WINDSTOPPER® Small Box Earflap 6-Panel', 'id': 305528, 'image_url': '//d17ol771963kd3.cloudfront.net/198739/ca/Ypcd2ZBpRiI.jpg', 'image_url_hi': '//assets.supremenewyork.com/198739/rc/Ypcd2ZBpRiI.jpg', 'price': 5400, 'sale_price': 0, 'new_item': True, 'position': 33, 'category_name': 'Hats', 'price_euro': 6000, 'sale_price_euro': 0}, {'name': 'Supreme®/Nike® Air Max Plus Running Hat', 'id': 305530, 'image_url': '//d17ol771963kd3.cloudfront.net/198824/ca/DGYfbkjYNCk.jpg', 'image_url_hi': '//assets.supremenewyork.com/198824/rc/DGYfbkjYNCk.jpg', 'price': 3800, 'sale_price': 0, 'new_item': True, 'position': 31, 'category_name': 'Hats', 'price_euro': 4500, 'sale_price_euro': 0}, {'name': 'Inset Logo Camp Cap', 'id': 305532, 'image_url': '//d17ol771963kd3.cloudfront.net/195114/ca/tb8IRFF4_QM.jpg', 'image_url_hi': '//assets.supremenewyork.com/195114/rc/tb8IRFF4_QM.jpg', 'price': 5000, 'sale_price': 0, 'new_item': True, 'position': 32, 'category_name': 'Hats', 'price_euro': 5600, 'sale_price_euro': 0}, {'name': 'Woven Label Beanie', 'id': 305536, 'image_url': '//d17ol771963kd3.cloudfront.net/198747/ca/aNT_CCLisBY.jpg', 'image_url_hi': '//assets.supremenewyork.com/198747/rc/aNT_CCLisBY.jpg', 'price': 3000, 'sale_price': 0, 'new_item': True, 'position': 36, 'category_name': 'Hats', 'price_euro': 3400, 'sale_price_euro': 0}, {'name': 'Alpine Beanie', 'id': 305541, 'image_url': '//d17ol771963kd3.cloudfront.net/195516/ca/bz9D8uOSlgk.jpg', 'image_url_hi': '//assets.supremenewyork.com/195516/rc/bz9D8uOSlgk.jpg', 'price': 3200, 'sale_price': 0, 'new_item': True, 'position': 35, 'category_name': 'Hats', 'price_euro': 3600, 'sale_price_euro': 0}, {'name': 'Supreme®/Hohner® Keychain', 'id': 305529, 'image_url': '//d17ol771963kd3.cloudfront.net/196012/ca/HGguzYlx9nc.jpg', 'image_url_hi': '//assets.supremenewyork.com/196012/rc/HGguzYlx9nc.jpg', 'price': 3000, 'sale_price': 0, 'new_item': True, 'position': 44, 'category_name': 'Accessories', 'price_euro': 3200, 'sale_price_euro': 0}, {'name': 'Camo iPhone Case', 'id': 305531, 'image_url': '//d17ol771963kd3.cloudfront.net/198613/ca/uVenA7yXMrI.jpg', 'image_url_hi': '//assets.supremenewyork.com/198613/rc/uVenA7yXMrI.jpg', 'price': 3200, 'sale_price': 0, 'new_item': True, 'position': 43, 'category_name': 'Accessories', 'price_euro': 3600, 'sale_price_euro': 0}, {'name': 'Supreme®/Nike® Air Max Plus', 'id': 305535, 'image_url': '//d17ol771963kd3.cloudfront.net/198820/ca/Gr1pWt4E4VI.jpg', 'image_url_hi': '//assets.supremenewyork.com/198820/rc/Gr1pWt4E4VI.jpg', 'price': 16000, 'sale_price': 0, 'new_item': True, 'position': 0, 'category_name': 'Shoes', 'price_euro': 18000, 'sale_price_euro': 0}]}, 'release_date': '11/05/2020', 'release_week': '12FW20'}
    """

    url = "https://www.supremenewyork.com/mobile_stock.json"
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/80.0.3987.95 Mobile/15E148 Safari/604.1",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "DNT": "1",
        "Connection": "close",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "TE": "Trailers"
    }
    stock = requests.get(url, headers=headers).json()
    return stock


def get_item_variants(item_id):
    """
    Makes a request to item's page and returns it's info
    {'styles': [{'id': 30062, 'name': 'Black Houndstooth', 'tag': None, 'currency': 'GBP', 'description': 'Cotton blend houndstooth with woven logo pattern. Slanted front pockets, zip fly, single coin pocket and snap closure on back pocket.', 'image_url': '//assets.supremenewyork.com/194193/sm/-KJSo14zwn8.jpg', 'image_url_hi': '//assets.supremenewyork.com/194193/rs/-KJSo14zwn8.jpg', 'swatch_url': '//d17ol771963kd3.cloudfront.net/194193/ca/xLm96lFZSt8.jpg', 'swatch_url_hi': '//assets.supremenewyork.com/194193/rc/-KJSo14zwn8.jpg', 'mobile_zoomed_url': '//assets.supremenewyork.com/194193/mo/-KJSo14zwn8.jpg', 'mobile_zoomed_url_hi': '//assets.supremenewyork.com/194193/rm/-KJSo14zwn8.jpg', 'bigger_zoomed_url': '//assets.supremenewyork.com/194193/zo/-KJSo14zwn8.jpg', 'sizes': [{'name': '30 ', 'id': 68943, 'stock_level': 0}, {'name': '32 ', 'id': 68944, 'stock_level': 0}, {'name': '34 ', 'id': 68945, 'stock_level': 1}, {'name': '36 ', 'id': 68946, 'stock_level': 1}], 'additional': [{'swatch_url': '//assets.supremenewyork.com/194194/ca/e9TsSIi6YBw.jpg', 'swatch_url_hi': '//assets.supremenewyork.com/194194/rc/e9TsSIi6YBw.jpg', 'image_url': '//assets.supremenewyork.com/194194/sm/e9TsSIi6YBw.jpg', 'image_url_hi': '//assets.supremenewyork.com/194194/rs/e9TsSIi6YBw.jpg', 'zoomed_url': '//assets.supremenewyork.com/194194/mo/e9TsSIi6YBw.jpg', 'zoomed_url_hi': '//assets.supremenewyork.com/194194/rm/e9TsSIi6YBw.jpg', 'bigger_zoomed_url': '//assets.supremenewyork.com/194194/zo/e9TsSIi6YBw.jpg'}]}, {'id': 30063, 'name': 'Brown Houndstooth', 'tag': None, 'currency': 'GBP', 'description': 'Cotton blend houndstooth with woven logo pattern. Slanted front pockets, zip fly, single coin pocket and snap closure on back pocket.', 'image_url': '//assets.supremenewyork.com/194200/sm/H3fd4pVe3Xc.jpg', 'image_url_hi': '//assets.supremenewyork.com/194200/rs/H3fd4pVe3Xc.jpg', 'swatch_url': '//d17ol771963kd3.cloudfront.net/194200/ca/H3fd4pVe3Xc.jpg', 'swatch_url_hi': '//assets.supremenewyork.com/194200/rc/H3fd4pVe3Xc.jpg', 'mobile_zoomed_url': '//assets.supremenewyork.com/194200/mo/H3fd4pVe3Xc.jpg', 'mobile_zoomed_url_hi': '//assets.supremenewyork.com/194200/rm/H3fd4pVe3Xc.jpg', 'bigger_zoomed_url': '//assets.supremenewyork.com/194200/zo/H3fd4pVe3Xc.jpg', 'sizes': [{'name': '30 ', 'id': 68947, 'stock_level': 1}, {'name': '32 ', 'id': 68948, 'stock_level': 0}, {'name': '34 ', 'id': 68949, 'stock_level': 1}, {'name': '36 ', 'id': 68950, 'stock_level': 1}], 'additional': []}, {'id': 30064, 'name': 'Bright Pink', 'tag': None, 'currency': 'GBP', 'description': 'Heavy cotton blend twill with enzyme wash. Slanted front pockets, zip fly, single coin pocket and snap closure on back pocket.', 'image_url': '//assets.supremenewyork.com/194201/sm/D8SLE1xFbfg.jpg', 'image_url_hi': '//assets.supremenewyork.com/194201/rs/D8SLE1xFbfg.jpg', 'swatch_url': '//d17ol771963kd3.cloudfront.net/194201/ca/D8SLE1xFbfg.jpg', 'swatch_url_hi': '//assets.supremenewyork.com/194201/rc/D8SLE1xFbfg.jpg', 'mobile_zoomed_url': '//assets.supremenewyork.com/194201/mo/D8SLE1xFbfg.jpg', 'mobile_zoomed_url_hi': '//assets.supremenewyork.com/194201/rm/D8SLE1xFbfg.jpg', 'bigger_zoomed_url': '//assets.supremenewyork.com/194201/zo/D8SLE1xFbfg.jpg', 'sizes': [{'name': '30 ', 'id': 68939, 'stock_level': 1}, {'name': '32 ', 'id': 68940, 'stock_level': 1}, {'name': '34 ', 'id': 68941, 'stock_level': 0}, {'name': '36 ', 'id': 68942, 'stock_level': 0}], 'additional': []}, {'id': 30067, 'name': 'Light Navy', 'tag': None, 'currency': 'GBP', 'description': 'Heavy cotton blend twill with enzyme wash. Slanted front pockets, zip fly, single coin pocket and snap closure on back pocket.', 'image_url': '//assets.supremenewyork.com/194191/sm/D0mER6MARwM.jpg', 'image_url_hi': '//assets.supremenewyork.com/194191/rs/D0mER6MARwM.jpg', 'swatch_url': '//d17ol771963kd3.cloudfront.net/194191/ca/D0mER6MARwM.jpg', 'swatch_url_hi': '//assets.supremenewyork.com/194191/rc/D0mER6MARwM.jpg', 'mobile_zoomed_url': '//assets.supremenewyork.com/194191/mo/D0mER6MARwM.jpg', 'mobile_zoomed_url_hi': '//assets.supremenewyork.com/194191/rm/D0mER6MARwM.jpg', 'bigger_zoomed_url': '//assets.supremenewyork.com/194191/zo/D0mER6MARwM.jpg', 'sizes': [{'name': '30 ', 'id': 68935, 'stock_level': 0}, {'name': '32 ', 'id': 68936, 'stock_level': 0}, {'name': '34 ', 'id': 68937, 'stock_level': 1}, {'name': '36 ', 'id': 68938, 'stock_level': 1}], 'additional': [{'swatch_url': '//assets.supremenewyork.com/194192/ca/TwddR-ALmp4.jpg', 'swatch_url_hi': '//assets.supremenewyork.com/194192/rc/TwddR-ALmp4.jpg', 'image_url': '//assets.supremenewyork.com/194192/sm/TwddR-ALmp4.jpg', 'image_url_hi': '//assets.supremenewyork.com/194192/rs/TwddR-ALmp4.jpg', 'zoomed_url': '//assets.supremenewyork.com/194192/mo/TwddR-ALmp4.jpg', 'zoomed_url_hi': '//assets.supremenewyork.com/194192/rm/TwddR-ALmp4.jpg', 'bigger_zoomed_url': '//assets.supremenewyork.com/194192/zo/TwddR-ALmp4.jpg'}]}, {'id': 30068, 'name': 'Dusty Teal', 'tag': None, 'currency': 'GBP', 'description': 'Heavy cotton blend twill with enzyme wash. Slanted front pockets, zip fly, single coin pocket and snap closure on back pocket.', 'image_url': '//assets.supremenewyork.com/194198/sm/j-MUOuh2Xzg.jpg', 'image_url_hi': '//assets.supremenewyork.com/194198/rs/j-MUOuh2Xzg.jpg', 'swatch_url': '//d17ol771963kd3.cloudfront.net/194198/ca/j-MUOuh2Xzg.jpg', 'swatch_url_hi': '//assets.supremenewyork.com/194198/rc/j-MUOuh2Xzg.jpg', 'mobile_zoomed_url': '//assets.supremenewyork.com/194198/mo/j-MUOuh2Xzg.jpg', 'mobile_zoomed_url_hi': '//assets.supremenewyork.com/194198/rm/j-MUOuh2Xzg.jpg', 'bigger_zoomed_url': '//assets.supremenewyork.com/194198/zo/j-MUOuh2Xzg.jpg', 'sizes': [{'name': '30 ', 'id': 68951, 'stock_level': 0}, {'name': '32 ', 'id': 68952, 'stock_level': 1}, {'name': '34 ', 'id': 68953, 'stock_level': 1}, {'name': '36 ', 'id': 68954, 'stock_level': 0}], 'additional': [{'swatch_url': '//assets.supremenewyork.com/194199/ca/KeENdJd0HPQ.jpg', 'swatch_url_hi': '//assets.supremenewyork.com/194199/rc/KeENdJd0HPQ.jpg', 'image_url': '//assets.supremenewyork.com/194199/sm/KeENdJd0HPQ.jpg', 'image_url_hi': '//assets.supremenewyork.com/194199/rs/KeENdJd0HPQ.jpg', 'zoomed_url': '//assets.supremenewyork.com/194199/mo/KeENdJd0HPQ.jpg', 'zoomed_url_hi': '//assets.supremenewyork.com/194199/rm/KeENdJd0HPQ.jpg', 'bigger_zoomed_url': '//assets.supremenewyork.com/194199/zo/KeENdJd0HPQ.jpg'}]}, {'id': 30065, 'name': 'Black', 'tag': None, 'currency': 'GBP', 'description': 'Heavy cotton blend twill with enzyme wash. Slanted front pockets, zip fly, single coin pocket and snap closure on back pocket.', 'image_url': '//assets.supremenewyork.com/194195/sm/YGKG-cKPGm0.jpg', 'image_url_hi': '//assets.supremenewyork.com/194195/rs/YGKG-cKPGm0.jpg', 'swatch_url': '//d17ol771963kd3.cloudfront.net/194195/ca/YGKG-cKPGm0.jpg', 'swatch_url_hi': '//assets.supremenewyork.com/194195/rc/YGKG-cKPGm0.jpg', 'mobile_zoomed_url': '//assets.supremenewyork.com/194195/mo/YGKG-cKPGm0.jpg', 'mobile_zoomed_url_hi': '//assets.supremenewyork.com/194195/rm/YGKG-cKPGm0.jpg', 'bigger_zoomed_url': '//assets.supremenewyork.com/194195/zo/YGKG-cKPGm0.jpg', 'sizes': [{'name': '30 ', 'id': 68927, 'stock_level': 0}, {'name': '32 ', 'id': 68928, 'stock_level': 1}, {'name': '34 ', 'id': 68929, 'stock_level': 1}, {'name': '36 ', 'id': 68930, 'stock_level': 1}], 'additional': []}, {'id': 30066, 'name': 'Khaki', 'tag': None, 'currency': 'GBP', 'description': 'Heavy cotton blend twill with enzyme wash. Slanted front pockets, zip fly, single coin pocket and snap closure on back pocket.', 'image_url': '//assets.supremenewyork.com/194196/sm/Hl6-3M-6PbQ.jpg', 'image_url_hi': '//assets.supremenewyork.com/194196/rs/Hl6-3M-6PbQ.jpg', 'swatch_url': '//d17ol771963kd3.cloudfront.net/194196/ca/Hl6-3M-6PbQ.jpg', 'swatch_url_hi': '//assets.supremenewyork.com/194196/rc/Hl6-3M-6PbQ.jpg', 'mobile_zoomed_url': '//assets.supremenewyork.com/194196/mo/Hl6-3M-6PbQ.jpg', 'mobile_zoomed_url_hi': '//assets.supremenewyork.com/194196/rm/Hl6-3M-6PbQ.jpg', 'bigger_zoomed_url': '//assets.supremenewyork.com/194196/zo/Hl6-3M-6PbQ.jpg', 'sizes': [{'name': '30 ', 'id': 68931, 'stock_level': 0}, {'name': '32 ', 'id': 68932, 'stock_level': 1}, {'name': '34 ', 'id': 68933, 'stock_level': 1}, {'name': '36 ', 'id': 68934, 'stock_level': 1}], 'additional': [{'swatch_url': '//assets.supremenewyork.com/194197/ca/nHrHQf_-DtY.jpg', 'swatch_url_hi': '//assets.supremenewyork.com/194197/rc/nHrHQf_-DtY.jpg', 'image_url': '//assets.supremenewyork.com/194197/sm/nHrHQf_-DtY.jpg', 'image_url_hi': '//assets.supremenewyork.com/194197/rs/nHrHQf_-DtY.jpg', 'zoomed_url': '//assets.supremenewyork.com/194197/mo/nHrHQf_-DtY.jpg', 'zoomed_url_hi': '//assets.supremenewyork.com/194197/rm/nHrHQf_-DtY.jpg', 'bigger_zoomed_url': '//assets.supremenewyork.com/194197/zo/nHrHQf_-DtY.jpg'}]}], 'description': 'Heavy cotton blend twill with enzyme wash. Slanted front pockets, zip fly, single coin pocket and snap closure on back pocket.', 'can_add_styles': True, 'can_buy_multiple': False, 'ino': 'FW20P14', 'cod_blocked': False, 'canada_blocked': False, 'purchasable_qty': 1, 'special_purchasable_qty': [], 'new_item': False, 'apparel': True, 'handling': 0, 'no_free_shipping': False, 'can_buy_multiple_with_limit': 0, 'tag': None, 'non_eu_blocked': False, 'russia_blocked': False}
    """

    item_url = f"https://www.supremenewyork.com/shop/{item_id}.json"
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/80.0.3987.95 Mobile/15E148 Safari/604.1",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "DNT": "1",
        "Connection": "close",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "TE": "Trailers"
    }
    item_variants = requests.get(item_url, headers=headers).json()
    return item_variants


def get_size_style_ids(item_id, size, style):
    """
   Searches if there is matching style and size for specific item
   Otherwise stops a program
    """

    item_variants = get_item_variants(item_id)
    print("item_variants=", item_variants)
    for style_name in item_variants["styles"]:
        if style_name["name"].lower().strip() == style.lower().strip():
            for item_size in style_name["sizes"]:
                if item_size["name"].lower().strip() == size.lower().strip():
                    if item_size["stock_level"] != 0:
                        return item_size["id"], style_name["id"]
                    else:
                        return "sold out"
    return "could not find style or size"



def check_matching(sp_1, sp_2):
    if sp_1.lower() in sp_2.lower():
        return True
    return False