import requests, time, json, base64, urllib.parse
PRODUCT_NAME = "black cat tee"
COLOR = 'magenta'
SIZE = 'large'
ADDRESS = '1345'


t0 = time.time()
r = requests.get(url = "https://www.supremenewyork.com/mobile_stock.json")
stock = r.json()
products_and_categories = stock['products_and_categories']
for categories in products_and_categories:
    for product in products_and_categories[categories]:
        if product['name'].lower() == PRODUCT_NAME.lower():
            product_id = str(product['id'])

r = requests.get(url = "https://www.supremenewyork.com/shop/"+product_id+".json")
styles = r.json()['styles']
for style in styles:
    if style['name'].lower() == COLOR:  
        size_id = str(style['id'])
        sizes = style['sizes']
        for size in sizes:
            if size['name'].lower() == SIZE:
                style_id = str(size['id'])

request_body = "s="+style_id+"&st="+size_id+"&qty=1"
print(request_body)
headers = {'content-type': 'application/x-www-form-urlencoded'}
r = requests.post(url = "https://www.supremenewyork.com/shop/"+ product_id +"/add.json",data=request_body, headers = headers)

buyer_name = urllib.parse.quote_plus("order[bn]") + "=" + urllib.parse.quote_plus("")
buyer_email = urllib.parse.quote_plus("order[email]") + "=" + urllib.parse.quote_plus("") 
buyer_tel = urllib.parse.quote_plus("order[tel]") + "=" + urllib.parse.quote_plus("")
buyer_address = urllib.parse.quote_plus("order[billing_address]") + "=" + urllib.parse.quote_plus("")
buyer_zipcode = urllib.parse.quote_plus("order[billing_zip]") + "=" + urllib.parse.quote_plus("")
buyer_city = urllib.parse.quote_plus("order[billing_city]") + "=" + urllib.parse.quote_plus("")
buyer_state = urllib.parse.quote_plus("order[billing_state]") + "=" + urllib.parse.quote_plus("")
buyer_country = urllib.parse.quote_plus("order[billing_country]") + "=" + urllib.parse.quote_plus("USA")
credit_num = urllib.parse.quote_plus("riearmxa") + "=" + urllib.parse.quote_plus("")
credit_month = urllib.parse.quote_plus("credit_card[month]") + "=" + urllib.parse.quote_plus("")
credit_year = urllib.parse.quote_plus("credit_card[year]") + "=" + urllib.parse.quote_plus("")
credit_pin = urllib.parse.quote_plus("credit_card[meknk]") + "=" + urllib.parse.quote_plus("")
json_dump = "{\""+style_id+"\":1}"
cookie_sub = urllib.parse.quote(urllib.parse.quote(json_dump))
print(cookie_sub)

request_body = "store_credit_id=&from_mobile=1&cookie-sub="+cookie_sub+"&same_as_billing_address=1&scerkhaj=CKCRSUJHXH&order%5Bbilling_name%5D=&"+buyer_name+"&"+buyer_email+"&"+buyer_tel+"&"+buyer_address+"&order%5Bbilling_address_2%5D=&"+buyer_zipcode+"&"+buyer_city+"&"+buyer_state+"&"+buyer_country+"&"+credit_num+"&"+credit_month+"&"+credit_year+"&rand=&"+credit_pin+"&order%5Bterms%5D=0&order%5Bterms%5D=1&is_from_android=1"
# r = requests.post(url = "https://www.supremenewyork.com/checkout.json",data=request_body, headers = headers)
print(request_body)

s2 = request_body
# Took 0.5804688930511475 seconds
print(s1 == s2)
# print(len(sample_body))
for idx, val in enumerate(s1):
    if s1[idx] != s2[idx]:
        print(s1[idx])

t1 = time.time()
print('Took', t1 - t0, 'seconds')