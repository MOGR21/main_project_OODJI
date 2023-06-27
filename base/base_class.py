import datetime


class Base():

    def __init__(self, driver):
        self.driver = driver

    """Metod get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current Url " + get_url)

    """Method assert word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good Value Word")

    """Method screenshot"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenhot' + now_date + ".png"
        self.driver.save_screenshot('C:\\Users\\MOGR\\PycharmProjects\\main_project_OODJI\\screen\\' + name_screenshot)
        print("Screenshot Is Done")

    """Method assert url"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good Value Url")