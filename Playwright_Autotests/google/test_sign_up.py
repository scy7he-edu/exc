import os
from dotenv import load_dotenv
from playwright.sync_api import Page

class EnvInfo:
    def __init__(self):
        load_dotenv()
        self.email = os.getenv('EMAIL')
        self.password = os.getenv('PASSWORD')
        self.first_name = os.getenv('FIRST_NAME')
        self.last_name = os.getenv('LAST_NAME')
        self.day_of_birth = os.getenv('DAY_OF_BIRTH')
        self.year_of_birth = os.getenv('YEAR_OF_BIRTH')

user = EnvInfo()

class InitSignUp:
    def __init__(self, page: Page):
        page.goto('https://workspace.google.com/gmail/', wait_until = 'commit')
        self.dropdown = page.locator('.dropdown-gws-button.variant-primary').nth(1)
        self.dd_button = page.get_by_role('menuitem').nth(0)

    def init_sign_up(self):
        self.dropdown.click()
        self.dd_button.click()

class UserName:
    def __init__(self, page: Page):
        self.name_field = page.locator('#firstName')
        self.surname_field = page.locator('#lastName')
        self.next_step_button = page.locator('button')

    def fill_info(self):
        self.name_field.fill(user.first_name)
        self.surname_field.fill(user.last_name)

    def next_step(self):
        self.next_step_button.click()


class PersonalInformation:
    def __init__(self, page: Page):
        self.day_of_birth = page.locator('#day')
        self.month_dropdown = page.locator('#month')
        self.month_of_birth = page.get_by_role('option').nth(2)
        self.year_of_birth = page.locator('#year')
        self.gender_dropdown = page.locator('#gender')
        self.gender = page.get_by_role('option').nth(1)
        self.next_step_button = page.locator('#birthdaygenderNext')

    def fill_info(self):
        self.day_of_birth.fill(user.day_of_birth)
        self.month_dropdown.click()
        self.month_of_birth.click()
        self.year_of_birth.fill(user.year_of_birth)
        self.gender_dropdown.click()
        self.gender.click()

    def next_step(self):
        self.next_step_button.click()

class ChooseEmail:
    def __init__(self, page: Page):
        self.custom_email_variant = page.locator('[data-value="custom"]')
        self.custom_email_type = page.get_by_role('textbox')
        self.next_step_button = page.locator('#next')

    def fill_info(self):
        self.custom_email_variant.click()
        self.custom_email_type.fill(user.email)

    def next_step(self):
        self.next_step_button.click()

class SetPassword:
    def __init__(self, page: Page):
        self.password_field = page.locator('input[name="Passwd"]')
        self.password_again = page.locator('input[name="PasswdAgain"]')
        self.next_step_button = page.locator('#createpasswordNext')

    def fill_info(self):
        self.password_field.fill(user.password)
        self.password_again.fill(user.password)

    def next_step(self):
        self.next_step_button.click()

class TestSignUp:
    def test_init_sign_up(self, page: Page):
        # Initiating sign up procedure
        init_page = InitSignUp(page)
        init_page.init_sign_up()
        # Filling First and Second name on the next page
        name_page = UserName(page)
        name_page.fill_info()
        name_page.next_step()
        # Filling Gender and Birth data
        personal_data_page = PersonalInformation(page)
        personal_data_page.fill_info()
        personal_data_page.next_step()
        # Choosing custom e-mail address and filling it in
        email_page = ChooseEmail(page)
        email_page.fill_info()
        email_page.next_step()
        # Setting up password
        password_page = SetPassword(page)
        password_page.fill_info()
        password_page.next_step()