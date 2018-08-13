from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def get_cafeteria():
    cafeteria_url = 'http://www.soongguri.com/main.php?mkey=2&w=3&l=2'
    try:
        html = urlopen(cafeteria_url)
    except:
        raise HTTPError('사이트 접속에 실패했습니다.')
    else:
        source = html.read()
    finally:
        html.close()
    soup = BeautifulSoup(source.decode('utf-8'), 'html.parser')
    
    menu_lists = []
    for menu_list_t1 in soup.select('.menu-list-t1'):
        menu_list = []
        menu_lists.append(menu_list)
        for menu in menu_list_t1.select('font'):
            menu_list.append(menu.text)
    
    cafe_list = [cafe.text for cafe in soup.select('td div[style^="float:left;padding"]')[:-1]]
    
    return dict(zip(cafe_list, menu_lists))