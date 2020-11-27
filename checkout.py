import time
import requests


def add_to_cart(item_id, size_id, style_id, session=0):
    """
    Add an item to cart with a specific item_id, size_id, and style_id.
    Only return session object if item added to cart properly.
    """
    if not session:
        s = requests.Session()
    else:
        s = session
    atc_url = f"https://www.supremenewyork.com/shop/{item_id}/add.json"
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 '
                      '(KHTML, like Gecko) CriOS/80.0.3987.95 Mobile/15E148 Safari/604.1',
        'Accept': 'application/json',
        'Accept-Language': 'en-US,en;q=0.5',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://www.supremenewyork.com',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Referer': 'https://www.supremenewyork.com/mobile/',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'TE': 'Trailers',
    }

    data = {
        "size": size_id,
        "style": style_id,
        "qty": "1"
    }
    add_to_cart_request = s.post(atc_url, headers=headers, data=data)
    if add_to_cart_request.json():
        if add_to_cart_request.json()[-1]["in_stock"]:
            print("add_to_cart_request=", add_to_cart_request, add_to_cart_request.json())
            return s


def make_checkout_parameters(s, profile_data, token):
    """
    returns checkout parameters.
    """
    print("in make_checkout_parameters")
    cookie_sub = s.cookies.get_dict()["pure_cart"]
    print("cookies=", s.cookies.get_dict())
    print("cookie_sub", cookie_sub)
    if token:
        checkout_params = {"order[billing_name]": profile_data["name"],
                           "order[email]": profile_data["email"],
                           "order[tel]": profile_data["tel"],
                           "order[billing_address]": profile_data["address_1"],
                           "order[billing_address_2]": profile_data["address_2"],
                           "order[billing_city]": profile_data["city"],
                           "order[billing_zip]": profile_data["zip"],
                           "order[billing_country]": profile_data["country"],
                           "same_as_billing_address": 1,
                           "credit_card[type]": profile_data["card_type"],
                           "credit_card[cnb]": profile_data["card_number"],
                           "credit_card[month]": profile_data["exp_month"],
                           "credit_card[year]": profile_data["exp_year"],
                           "credit_card[ovv]": profile_data["cvv"],
                           "order[terms]": 1,
                           "g-recaptcha-response": token
                           }

    else:
        checkout_params = {"order[billing_name]": profile_data["name"],
                           "order[email]": profile_data["email"],
                           "order[tel]": profile_data["tel"],
                           "order[billing_address]": profile_data["address_1"],
                           "order[billing_address_2]": profile_data["address_2"],
                           "order[billing_city]": profile_data["city"],
                           "order[billing_zip]": profile_data["zip"],
                           "order[billing_country]": profile_data["country"],
                           "same_as_billing_address": 1,
                           "credit_card[type]": profile_data["card_type"],
                           "credit_card[cnb]": profile_data["card_number"],
                           "credit_card[month]": profile_data["exp_month"],
                           "credit_card[year]": profile_data["exp_year"],
                           "credit_card[ovv]": profile_data["cvv"],
                           "order[terms]": 1,
                           }
    print(checkout_params)
    return checkout_params, cookie_sub


def send_checkout_request(s, delay, profile_data, start_checkout_time, sender, token):
    print("in send_checkout_request")
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/80.0.3987.95 Mobile/15E148 Safari/604.1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'TE': 'Trailers',
    }

    checkout_params, cookies = make_checkout_parameters(s, profile_data, token)
    print("checkout_params", checkout_params)
    sender(f"Sleeping for {delay}s")
    time.sleep(delay)
    checkout_request = s.post("https://www.supremenewyork.com/checkout.json", headers=headers, data=checkout_params)
    print("checkout_request=", checkout_request)
    sender("Checkout request was sent")
    sender(f"Time: {round(time.time() - start_checkout_time, 2)}s")
    return checkout_request, cookies


def get_order_id_status(s, order_id):
    """
    Sends a request and gets order_id status
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/80.0.3987.95 Mobile/15E148 Safari/604.1',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
        'Referer': 'https://www.supremenewyork.com/mobile/',
        'TE': 'Trailers'
    }
    status_url = f"https://www.supremenewyork.com/checkout/{order_id}/status.json"
    order_id_content = s.get(status_url, headers=headers).json()
    print("order_id_content=", order_id_content)
    order_status = order_id_content["status"]
    return order_status


def display_order_id_status(s, checkout_response):
    """
    This function displays the content returned from the slug url
    until the 'status' is something other than 'queued'.
    """

    order_id = checkout_response["slug"]
    while True:
        slug_status = get_order_id_status(s, order_id)
        if slug_status == "queued":
            return "queued"
        elif slug_status == "paid":
            return "paid"
        elif slug_status == "failed":
            return "failed"
        time.sleep(5)


def get_order_status(s, checkout_request, sender):
    checkout_response = checkout_request.json()
    print("checkout_response=", checkout_response)
    if checkout_response["status"] == "queued":
        status = display_order_id_status(s, checkout_response)
        while status == "queued":
            status = display_order_id_status(s, checkout_response)
            time.sleep(3)
            sender(f"Waiting for status: status ({status})")
        if status == "failed":
            sender("Checkout failed")
            return False
        else:
            sender("Checkout Successful")
            sender("Check your email")
            return True
    elif checkout_response["status"] == "paid":
        sender("Checkout Successful")
        sender("Check your email")
    else:
        sender("Checkout failed")
        return False
