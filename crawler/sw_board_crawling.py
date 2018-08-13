import requests
from bs4 import BeautifulSoup
import os

#파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

html = requests.get('http://sw.ssu.ac.kr/bbs/board.php?bo_table=sub6_1')
soup = BeautifulSoup(html.text, 'html.parser')
posts = soup.select('.board_list .subject')
latest = posts[0].text

with open(os.path.join(BASE_DIR, 'latest.txt'), 'r+') as f_read:
    before = f_read.readline()
    if before != latest:
        '''
        모든 구독자에게 새 글 알림을 보낸다.
        '''
        pass
    f_read.close()

with open(os.path.join(BASE_DIR, 'latest.txt'), 'w+') as f_write:
    f_write.write(latest)
    f_write.close()

'''
link = 'http://sw.ssu.ac.kr' + posts[0].find('a').get('href')[2:]
title = posts[0].text.strip()
post = {
    'link': link,
    'title': title,
}
'''