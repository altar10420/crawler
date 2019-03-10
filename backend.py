import requests
from bs4 import BeautifulSoup
from send_mail import send_mail


def message_generator(data):
    with open('message.txt', 'r+') as file:
        file.truncate(0)  # erase file content (truncate to size of 0)
        for d in data:
            file.write("%s \n" % d)


def flat_spider(email, top_price, max_pages=1):
    page = 1
    while page <= max_pages:
        url = "https://www.anonse.com/lista/rejon/warszawski/kategoria/nieruchomosci/podkategoria/mieszkania/rt/sprzedam/" + str(page)
        r = requests.get(url)
        c = r.content

        soup = BeautifulSoup(c, "html.parser")

        all_properties = soup.find_all("a", {"class": "center2"})

        first_prop_name = all_properties[0].text.split()[0]
        first_prop_price = int(all_properties[0].find_all("span", {"style": "font-size:10px; "})[0].text.replace(" ", "").replace("zł", ""))
        print(first_prop_name)
        print(str(first_prop_price) + " PLN")
        print("=========================")

        cheap_pairs = []

        for prop in all_properties:
            price = prop.find_all("span", {"style": "font-size:10px; "})[0].text.replace(" ", "").replace("zł", "")
            city = prop.find_all("div", {"class": "atrybut_miasto"})[0].text.split()[0]
            prop_name = prop.text.split()[0]
            href = 'https://www.anonse.com' + prop.get('href')

            if city == "WARSZAWA":
                if 50000 < int(price) < int(top_price):
                    cheap_pairs.append([prop_name, str(price) + "zł", href])

        # print(cheap_pairs)
        message_generator(cheap_pairs)

        with open("message.txt", "r") as myfile:
            data = myfile.read().replace('\n', '<br><br>')
            if len(data) > 0:  # prevent from sending mail if results are 0
                send_mail(email, data)

        page += 1

# flat_spider(1)




