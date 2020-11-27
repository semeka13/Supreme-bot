from selenium import webdriver

driver = webdriver.Chrome()
driver.header_overrides = {
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
# driver.add_cookie(cookies)
driver.get("https://www.supremenewyork.com/checkout")

elem = driver.find_element_by_name("q")
elem.send_keys("Hello WebDriver!")
elem.submit()
print(driver.title)