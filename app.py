import requests
import time

from page_content.page import Page, Links


main_page = 'https://www.kjv.dk/katalog/spantagning/fraesning/fraeser_hss-hsse-pm-hm/endefraeser/'
print(f'Loading page {main_page}')
page_content = requests.get(main_page).content

page = Links(page_content)

# get link to every item
_all_item_links = []
start = time.time()
print(f'Going through {page.page_count} pages and scrapping items...')
for page_num in range(page.page_count):
    page_start = time.time()
    url = f'{main_page}/?page={page_num + 1}'
    page_content = requests.get(url).content
    page = Links(page_content)
    print(f'{url} took {time.time() - page_start}')
    _all_item_links.extend(page.page_links)
print(f'Total took {time.time() - start}')
all_item_links = _all_item_links

# get properties for every item
_all_items = []
start = time.time()
print(f'Going through individual pages and scrapping items...')
for link in all_item_links:
    page_start = time.time()
    url = f'https://www.kjv.dk{link}'
    page_content = requests.get(url).content
    page = Page(page_content)
    print(f'{url} took {time.time() - page_start}')
    _all_items.extend(page.page_items)
print(f'Total took {time.time() - start}')

all_items = _all_items
