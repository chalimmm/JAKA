from seleniumbase import BaseCase

class DemoSiteTests(BaseCase):
    def test_demo_site(self):
        self.open("https://academic.ui.ac.id/main/Authentication/")
        self.sleep(10)
