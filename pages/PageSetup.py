
from commons.config import SetupClass
from commons.utils import Utils


class PageSetupClass():

    def __init__(self):
        setup_class = SetupClass()
        self.page_setup_driver = setup_class.get_driver()
        self.utils = Utils(self.page_setup_driver)


