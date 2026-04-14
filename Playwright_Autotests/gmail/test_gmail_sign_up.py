from playwright.sync_api import Page, expect

class TestSignUp:

     def test_ok_sign_up(self, page: Page):

         page.goto('https://workspace.google.com/gmail/', wait_until = 'commit')
         page.locator('.dropdown-gws-button.variant-primary').nth(1).click()
         page.get_by_role('menuitem').nth(0).click()
         page.locator('#firstName').fill('Arteme')
         page.locator('#lastName').fill('Test')
         page.locator('button').click()

         page.locator('#day').fill('17')
         page.locator('#month').click()
         page.get_by_role('option').nth(2).click() # choosing 3rd month, March by 2nd element in order
         page.locator('#year').fill('1995')
         page.locator('#gender').click()
         page.get_by_role('option').nth(1).click() # choosing gender "Male" by 1st element in order
         page.locator('#birthdaygenderNext').click()

         page.locator('[data-value="custom"]').click()
         page.get_by_role('textbox').fill('aredupytest')
         page.locator('#next').click()

         page.locator('input[name="Passwd"]').fill('testpassword12345')
         page.locator('input[name="PasswdAgain"]').fill('testpassword12345')
         page.locator('#createpasswordNext').click()

     def test_wrong_sign_up(self, page: Page):
        pass

     def test_border_sign_up(self, page: Page):
        pass

class TestSignIn:

     def test_ok_sign_in(self, page: Page):
        
         page.goto('https://mail.google.com/', wait_until = 'commit')
         page.locator('input[name="identifier"]').fill('aredupytest')
         page.locator('#identifierNext').click()
         expect(page, '[aria-label="aredupytest"]')
         page.locator('input[name="Passwd"]').fill('testpassword12345')
         page.locator('#passwordNext').click()



     def test_wrong_sign_in(self, page: Page):
        pass
     
class TestSendMail:

    def test_send_mail(self, page: Page):

        pass