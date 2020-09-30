from locators.locator import Locators
from parsers.parser import Parser
from bs4 import BeautifulSoup


class Links:
    """
    This class will take HTML url and find item links
    """
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    def __repr__(self):
        return f'<Link {self.page_links}>'

    @property
    def page_links(self):
        return [e.attrs['href'] for e in self.soup.select(Locators.LINK_LOCATOR)]

    @property
    def page_count(self):
        content = [number.string for number in self.soup.select(Locators.PAGES)][-1]
        pages = int(content)
        return pages


class Page:

    """
    A class to take in an item HTML url and find item properties.
    """

    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def page_items(self):
        return [Parser(e) for e in self.soup.select(Locators.ITEM)]
