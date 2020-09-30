import re

from locators.locator import Locators


class Parser:
    """
    A class to take in an item soup and find properties of an item.
    """

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'<Item {self.name} | ID: {self.serial} | {self.stock} | {self.material} | {self.diameter}>'

    @property
    def name(self):
        locator = Locators.NAME_LOCATOR
        item_name = re.sub(' +', ' ', self.parent.select_one(locator).string)
        return item_name

    @property
    def serial(self):
        locator = Locators.SERIAL_LOCATOR
        item_serial = self.parent.select(locator)[1].string
        return item_serial

    @property
    def stock(self):
        locator_green = Locators.STOCK_GREEN
        locator_yellow = Locators.STOCK_YELLOW
        if self.parent.select_one(locator_green):
            return "green"
        elif self.parent.select_one(locator_yellow):
            return "yellow"
        else:
            return "red"

    @property
    def material(self):
        locator = Locators.SPECIFICATION_LOCATOR
        item_material = self.parent.select(locator)[1].string
        return item_material

    @property
    def diameter(self):
        locator = Locators.SPECIFICATION_LOCATOR
        item_diameter = float(self.parent.select(locator)[3].string)
        return item_diameter

    @property
    def cutting_length(self):
        locator = Locators.SPECIFICATION_LOCATOR
        item_cutting_length = self.parent.select(locator)[7].string
        return item_cutting_length

    @property
    def total_length(self):
        locator = Locators.SPECIFICATION_LOCATOR
        item_total_length = self.parent.select(locator)[9].string
        return item_total_length
