from requests import post, get

server = f"http://127.0.0.1:5000/"
address = "api/cards"

url = server + address

with open("1.txt", 'r', encoding='utf-8') as f:
    s = f.read()
    cards = s.split('*****')
    for card in cards:
        data = {'api_key': 'dimka'}
        lst = card.split('*')
        data['id'] = int(lst[0])
        data['name'] = lst[1].strip()
        data['field'] = lst[2].strip()
        els = list(map(int, lst[3].split(', ')))
        if any(els):
            data['elements'] = els
        else:
            data['elements'] = list()
        data['about'] = lst[4]
        response = post(url, json=data)
        if not response:
            print('ERROR')
        print(response, response.json())
