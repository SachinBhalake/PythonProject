# import statements
from selenium.common.exceptions import *
from selenium import webdriver
import time
import random
from selenium.webdriver.support.ui import Select
import pytest
from datetime import datetime
from read_csv import getCSVData
from setup import setup
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



# class definition using fixture setup
@pytest.mark.usefixtures("setup")
class Test_project:



    # test case-1 : registering new user
    @pytest.mark.registerpositive
    def test_case1_register_new_user(self):

        try:

            # implicit wait
            self.driver.implicitly_wait(30)

            # registration details: use new email every time for successful registration
            usernumber = random.randint(0,9999)
            user_email = f"tester{usernumber}@gmail.com"

            # opening url
            self.driver.get("http://localhost/Avactis/")

            # click on my account
            self.driver.find_element_by_xpath("//a[@href='sign-in.php']").click()

            # click on register
            self.driver.find_element_by_xpath("//button[@class='btn btn-default']").click()

            # filling registration form
            self.driver.find_element_by_xpath("//input[@name='customer_info[Customer][Email]']").send_keys(user_email)
            self.driver.find_element_by_xpath("//input[@name='customer_info[Customer][Password]']").send_keys('tester12345')
            self.driver.find_element_by_xpath("//input[@name='customer_info[Customer][RePassword]']").send_keys('tester12345')
            self.driver.find_element_by_xpath("//input[@name='customer_info[Customer][FirstName]']").send_keys('test')
            self.driver.find_element_by_xpath("//input[@name='customer_info[Customer][LastName]']").send_keys('tester')

            # dropdown selection using select: country and state
            Country = Select(self.driver.find_element_by_xpath("//select[@name='customer_info[Customer][Country]']"))
            Country.select_by_visible_text("Canada")
            state = Select(self.driver.find_element_by_xpath("//select[@name='customer_info[Customer][State]']"))
            state.select_by_visible_text("Quebec")

            # continue registration form
            self.driver.find_element_by_xpath("//input[@name='customer_info[Customer][ZipCode]']").send_keys('12345')
            self.driver.find_element_by_xpath("//input[@name='customer_info[Customer][City]']").send_keys('test_city')
            self.driver.find_element_by_xpath("//input[@name='customer_info[Customer][Streetline1]']").send_keys('address line 1')
            self.driver.find_element_by_xpath("//input[@name='customer_info[Customer][Streetline2]']").send_keys('address line 2')
            self.driver.find_element_by_xpath("//input[@name='customer_info[Customer][Phone]']").send_keys('9876543210')
            self.driver.find_element_by_xpath("//input[@type='submit']").submit()

            # hard-coded wait
            time.sleep(10)

            # checking if registration is successful
            if (self.driver.current_url != 'http://localhost/Avactis/register.php'):
                registered = self.driver.find_element_by_xpath("(//div[@class='note note-success'])[1]").text
                assert(registered == 'Account created successfully. You are now registered.')
            else:
                assert(self.driver.current_url != 'http://localhost/Avactis/register.php')

        except Exception:
            assert False

            # end of the test case-1 : registering new user



    # test case-2 : registering existing user
    @pytest.mark.registerduplicate
    def test_case2_register_existing_user(self):

        try:

            # implicit wait
            self.driver.implicitly_wait(30)

            # registration details: use existing user email
            user_email = "tester@gmail.com"

            # opening url
            self.driver.get("http://localhost/Avactis/")

            # click on my account
            self.driver.find_element_by_xpath("//a[@href='sign-in.php']").click()

            # click on register
            self.driver.find_element_by_xpath("//button[@class='btn btn-default']").click()

            # filling registration form
            self.driver.find_element_by_xpath("//input[@name='customer_info[Customer][Email]']").send_keys(user_email)
            self.driver.find_element_by_xpath("//input[@name='customer_info[Customer][Password]']").send_keys('tester12345')
            self.driver.find_element_by_xpath("//input[@name='customer_info[Customer][RePassword]']").send_keys('tester12345')
            self.driver.find_element_by_xpath("//input[@name='customer_info[Customer][FirstName]']").send_keys('test')
            self.driver.find_element_by_xpath("//input[@name='customer_info[Customer][LastName]']").send_keys('tester')

            # dropdown selection using select: country and state
            Country = Select(self.driver.find_element_by_xpath("//select[@name='customer_info[Customer][Country]']"))
            Country.select_by_visible_text("Canada")
            state = Select(self.driver.find_element_by_xpath("//select[@name='customer_info[Customer][State]']"))
            state.select_by_visible_text("Quebec")

            # continue registration form
            self.driver.find_element_by_xpath("//input[@name='customer_info[Customer][ZipCode]']").send_keys('12345')
            self.driver.find_element_by_xpath("//input[@name='customer_info[Customer][City]']").send_keys('test_city')
            self.driver.find_element_by_xpath("//input[@name='customer_info[Customer][Streetline1]']").send_keys('address line 1')
            self.driver.find_element_by_xpath("//input[@name='customer_info[Customer][Streetline2]']").send_keys('address line 2')
            self.driver.find_element_by_xpath("//input[@name='customer_info[Customer][Phone]']").send_keys('9876543210')
            self.driver.find_element_by_xpath("//input[@type='submit']").submit()

            # hard-coded wait
            time.sleep(10)

            # checking if registration is duplicate
            if (self.driver.current_url == 'http://localhost/Avactis/register.php'):
                duplicate = self.driver.find_element_by_xpath("//div[@class='note note-danger']").text
                assert(duplicate == 'This account name is already taken. Please choose a different account name.')
            else:
                assert(self.driver.current_url == 'http://localhost/Avactis/register.php')

        except Exception:
            assert False

            # end of the test case-2 : registering existing user



    # test case-3 : login positive
    @pytest.mark.loginpositive
    def test_case3_login_success(self):

        try:

            # implicit wait
            self.driver.implicitly_wait(30)

            # login details : use existing user details
            username="tester@gmail.com"
            password="tester12345"

            # opening url
            self.driver.get("http://localhost/Avactis/")

            # click on my account
            self.driver.find_element_by_xpath("//a[@href='sign-in.php']").click()

            # filling login form
            self.driver.find_element_by_xpath("//input[@id='account_sign_in_form_email_id']").send_keys(username)
            self.driver.find_element_by_xpath("//input[@id='account_sign_in_form_passwd_id']").send_keys(password)
            self.driver.find_element_by_xpath("//input[@value='Sign In']").submit()

            # hard-coded wait
            time.sleep(10)

            # checking if login is successful
            if (self.driver.current_url != 'http://localhost/Avactis/sign-in.php'):
                assert(self.driver.find_element_by_xpath("(//a[text()='Sign Out'])[1]").text == "Sign Out")
                self.driver.find_element_by_xpath("(//a[text()='Sign Out'])[1]").click()
            else:
                assert (self.driver.current_url != 'http://localhost/Avactis/sign-in.php')

        except Exception:
            assert False

            # end of the test case-3 : login positive



    # test case-4 : login negative
    @pytest.mark.loginnegative
    def test_case4_login_failed(self):

        try:

            # implicit wait
            self.driver.implicitly_wait(30)

            # login details : use invalid user details
            username="abc@gmail.com"
            password="abc"

            # opening url
            self.driver.get("http://localhost/Avactis/")

            # click on my account
            self.driver.find_element_by_xpath("//a[@href='sign-in.php']").click()

            # filling login form
            self.driver.find_element_by_xpath("//input[@id='account_sign_in_form_email_id']").send_keys(username)
            self.driver.find_element_by_xpath("//input[@id='account_sign_in_form_passwd_id']").send_keys(password)
            self.driver.find_element_by_xpath("//input[@value='Sign In']").submit()

            # hard-coded wait
            time.sleep(10)

            # checking if login is failed
            if ('http://localhost/Avactis/sign-in.php' in self.driver.current_url):
                loginfailed = self.driver.find_element_by_xpath("//div[@class='note note-danger']").text
                assert(loginfailed == 'Account and password could not be identified. Try again or create an account.')
            else:
                assert ('http://localhost/Avactis/sign-in.php' not in self.driver.current_url)

        except Exception:
            assert False

            # end of the test case-4 : login negative



    # test case-5 : guest checkout
    @pytest.mark.guestcheckout
    def test_case5_guest_checkout(self):

        try:

            # implicit wait
            self.driver.implicitly_wait(30)

            # opening url
            self.driver.get("http://localhost/Avactis/")

            # going to cart to check if its empty
            self.driver.find_element_by_xpath("//a[text()='My cart']").click()

            # clearing cart content
            while (self.driver.find_element_by_xpath("//a[@class='top-cart-info-count']").text != '0 items'):
                self.driver.find_element_by_xpath("//a[@class='del-goods']").click

            # getting csv data
            csv_data = getCSVData("DataForTesting/product_selection.csv")

            # setting price
            all_product_price = 0.00

            # adding products from csv file
            for cat_prod_qua in csv_data:
                self.driver.find_element_by_xpath(f"(//a[text()='{cat_prod_qua[0]}'])[1]").click()
                self.driver.find_element_by_xpath(f"//h3[text()='{cat_prod_qua[1]}']").click()
                quantity = Select(self.driver.find_element_by_xpath("//select[@name='quantity_in_cart']"))
                quantity.select_by_value(cat_prod_qua[2])

                # calculating product price
                product_price = self.driver.find_element_by_xpath("//strong[@class='product_sale_price']").text
                product_price = product_price.replace('$', '')
                product_price = float(product_price)
                product_quantity = cat_prod_qua[2]
                product_quantity = float(product_quantity)
                total_price = product_price * product_quantity

                # getting product price total
                all_product_price = all_product_price + total_price

                # adding product to cart
                self.driver.find_element_by_xpath("//input[@value='Add To Cart']").click()

                # hard-coded wait
                time.sleep(10)

            # going to cart
            self.driver.find_element_by_xpath("//a[text()='My cart']").click()

            # hard-coded wait
            time.sleep(10)

            # verifying the products added
            if (self.driver.find_element_by_xpath(f"(//a[text()='{cat_prod_qua[1]}'])[2]").text == cat_prod_qua[1]):
                self.driver.find_element_by_xpath("(//a[@class='btn btn-primary'])[2]").click()

                # hard-coded wait
                time.sleep(10)

                # checkout process
                # billing and shipping address
                self.driver.find_element_by_xpath("//input[@name='billingInfo[Firstname]']").send_keys('test')
                self.driver.find_element_by_xpath("//input[@name='billingInfo[Lastname]']").send_keys('tester')
                self.driver.find_element_by_xpath("//input[@name='billingInfo[Email]']").send_keys('tester@gmail.com')
                country = Select(self.driver.find_element_by_xpath("//select[@name='billingInfo[Country]']"))
                country.select_by_value("39")
                self.driver.find_element_by_xpath("//input[@name='billingInfo[Postcode]']").send_keys('12345')
                state = Select(self.driver.find_element_by_xpath("//select[@name='billingInfo[Statemenu]']"))
                state.select_by_value("39")
                self.driver.find_element_by_xpath("//input[@name='billingInfo[City]']").send_keys('test_city')
                self.driver.find_element_by_xpath("//input[@name='billingInfo[Streetline1]']").send_keys('address line 1')
                self.driver.find_element_by_xpath("//input[@name='billingInfo[Streetline2]']").send_keys('address line 2')
                self.driver.find_element_by_xpath("//input[@name='billingInfo[Phone]']").send_keys('9876543210')

                # same shipping address : selecting checkbox
                if (not self.driver.find_element_by_xpath("//input[@type='checkbox']").is_selected()):
                    self.driver.find_element_by_xpath("//input[@type='checkbox']").click()
                self.driver.find_element_by_xpath("(//input[@value='Continue Checkout'])[1]").submit()

                # hard-coded wait
                time.sleep(10)

                # shipping methods
                # verifying address line 1 and 2
                add1 = self.driver.find_element_by_xpath("(//label[@class='control-label col-lg-10'])[2]").text
                add2 = self.driver.find_element_by_xpath("(//label[@class='control-label col-lg-10'])[3]").text
                if (add1 == "address line 1" and add2 == "address line 2"):
                    if (not self.driver.find_element_by_xpath("(//input[@type='radio'])[3]").is_selected()):
                        self.driver.find_element_by_xpath("(//input[@type='radio'])[3]").click()
                    shipping_charges = self.driver.find_element_by_xpath("(//div[@class='shipping_method_cost'])[2]").text
                    self.driver.find_element_by_xpath("(//input[@value='Continue Checkout'])[2]").submit()

                    # hard-coded wait
                    time.sleep(10)

                    # review and place order
                    # verifying price
                    shipping_charges = shipping_charges.replace('$', '')
                    shipping_charges = float(shipping_charges)
                    subtotal = all_product_price + shipping_charges
                    order_total = self.driver.find_element_by_xpath("(//strong[@class='price'])[3]").text
                    order_total = order_total.replace('$', '')
                    order_total = round(float(order_total), 2)
                    subtotal = round(subtotal, 2)

                    if (subtotal == order_total):
                        self.driver.find_element_by_xpath("//input[@value='Place Order']").click()

                        # hard-coded wait
                        time.sleep(10)

                        # taking screenshot
                        now = datetime.now()
                        now = now.strftime("%d-%m-%Y_%H-%M-%S")
                        SS = f'Screenshots/OrderGuest_{now}.png'
                        self.driver.save_screenshot(SS)

                        # getting order number
                        order_number = self.driver.find_element_by_xpath("//div[@class='note note-success note-bordered']").text
                        order_number = order_number.replace('Your order is placed. Order ID: #', '')
                        order_number = order_number.replace('\nOrder details have been sent to your e-mail address.','')

                        # login into avactis admin account
                        self.driver.get("http://localhost/avactis/avactis-system/admin/signin.php")
                        self.driver.find_element_by_xpath("(//input[@name='AdminEmail'])[1]").send_keys('sachinbhalake@gmail.com')
                        self.driver.find_element_by_xpath("(//input[@name='Password'])[1]").send_keys('s9975607009')
                        self.driver.find_element_by_xpath("//button[@type='submit']").click()

                        # hard-coded wait
                        time.sleep(10)

                        # clicking on orders button
                        self.driver.find_element_by_xpath("(//a[@href='orders.php'])[1]").click()

                        # hard-coded wait
                        time.sleep(30)

                        # getting order number
                        admin_order_number = self.driver.find_element_by_xpath("(//a[@title='Order Info'])[1]").text

                        # verifying order number
                        if (order_number == admin_order_number):
                            assert (order_number == admin_order_number)
                        else:
                            assert (order_number == admin_order_number)

        except Exception:
            assert False

            # end of the test case-5 : guest checkout



    # test case-6 : login checkout
    @pytest.mark.logincheckout
    def test_case6_login_checkout(self):

        try:

            # implicit wait
            self.driver.implicitly_wait(30)

            # login details : use existing user details
            username = "tester@gmail.com"
            password = "tester12345"

            # opening url
            self.driver.get("http://localhost/Avactis/")

            # user login checkout
            # click on my account
            self.driver.find_element_by_xpath("//a[@href='sign-in.php']").click()

            # filling login form
            self.driver.find_element_by_xpath("//input[@id='account_sign_in_form_email_id']").send_keys(username)
            self.driver.find_element_by_xpath("//input[@id='account_sign_in_form_passwd_id']").send_keys(password)
            self.driver.find_element_by_xpath("//input[@value='Sign In']").submit()

            # going to cart to check if its empty
            self.driver.find_element_by_xpath("//a[text()='My cart']").click()

            # clearing cart content
            while (self.driver.find_element_by_xpath("//a[@class='top-cart-info-count']").text != '0 items'):
                self.driver.find_element_by_xpath("//a[@class='del-goods']").click()

            # getting csv data
            csv_data = getCSVData("DataForTesting/product_selection.csv")

            # setting price
            all_product_price = 0.00

            # adding products from csv file
            for cat_prod_qua in csv_data:
                self.driver.find_element_by_xpath(f"(//a[text()='{cat_prod_qua[0]}'])[1]").click()
                self.driver.find_element_by_xpath(f"//h3[text()='{cat_prod_qua[1]}']").click()
                quantity = Select(self.driver.find_element_by_xpath("//select[@name='quantity_in_cart']"))
                quantity.select_by_value(cat_prod_qua[2])

                # calculating product price
                product_price = self.driver.find_element_by_xpath("//strong[@class='product_sale_price']").text
                product_price = product_price.replace('$', '')
                product_price = float(product_price)
                product_quantity = cat_prod_qua[2]
                product_quantity = float(product_quantity)
                total_price = product_price * product_quantity

                # getting product price total
                all_product_price = all_product_price + total_price

                # adding product to cart
                self.driver.find_element_by_xpath("//input[@value='Add To Cart']").click()

                # hard-coded wait
                time.sleep(10)

            # going to cart
            self.driver.find_element_by_xpath("//a[text()='My cart']").click()

            # verifying the products added
            if (self.driver.find_element_by_xpath(f"(//a[text()='{cat_prod_qua[1]}'])[2]").text == cat_prod_qua[1]):
                self.driver.find_element_by_xpath("(//a[@class='btn btn-primary'])[2]").click()

                # hard-coded wait
                time.sleep(10)

                # checkout process
                # same shipping address : selecting checkbox
                if (not self.driver.find_element_by_xpath("//input[@type='checkbox']").is_selected()):
                    self.driver.find_element_by_xpath("//input[@type='checkbox']").click()
                self.driver.find_element_by_xpath("(//input[@value='Continue Checkout'])[1]").submit()

                # hard-coded wait
                time.sleep(10)

                # shipping methods
                # verifying address line 1 and 2
                add1 = self.driver.find_element_by_xpath("(//label[@class='control-label col-lg-10'])[2]").text
                add2 = self.driver.find_element_by_xpath("(//label[@class='control-label col-lg-10'])[3]").text
                if (add1 == "address line 1" and add2 == "address line 2"):
                    if (not self.driver.find_element_by_xpath("(//input[@type='radio'])[3]").is_selected()):
                        self.driver.find_element_by_xpath("(//input[@type='radio'])[3]").click()
                    shipping_charges = self.driver.find_element_by_xpath("(//div[@class='shipping_method_cost'])[2]").text
                    self.driver.find_element_by_xpath("(//input[@value='Continue Checkout'])[2]").submit()

                    # hard-coded wait
                    time.sleep(10)

                    # review and place order
                    # verifying price
                    shipping_charges = shipping_charges.replace('$', '')
                    shipping_charges = float(shipping_charges)
                    subtotal = all_product_price + shipping_charges
                    order_total = self.driver.find_element_by_xpath("(//strong[@class='price'])[3]").text
                    order_total = order_total.replace('$', '')
                    order_total = float(order_total)
                    subtotal = round(subtotal, 2)
                    order_total = round(order_total, 2)

                    if (subtotal == order_total):
                        self.driver.find_element_by_xpath("//input[@value='Place Order']").click()

                        # hard-coded wait
                        time.sleep(10)

                        # taking screenshot
                        now = datetime.now()
                        now = now.strftime("%d-%m-%Y_%H-%M-%S")
                        SS = f'Screenshots/OrderLogin_{now}.png'
                        self.driver.save_screenshot(SS)

                        # getting order number
                        order_number = self.driver.find_element_by_xpath("//div[@class='note note-success note-bordered']").text
                        order_number = order_number.replace('Your order is placed. Order ID: #', '')
                        order_number = order_number.replace('\nOrder details have been sent to your e-mail address.','')

                        # login into avactis admin account
                        self.driver.get("http://localhost/avactis/avactis-system/admin/signin.php")
                        self.driver.find_element_by_xpath("(//input[@name='AdminEmail'])[1]").send_keys('sachinbhalake@gmail.com')
                        self.driver.find_element_by_xpath("(//input[@name='Password'])[1]").send_keys('s9975607009')
                        self.driver.find_element_by_xpath("//button[@type='submit']").click()

                        # hard-coded wait
                        time.sleep(10)

                        # clicking on orders button
                        self.driver.find_element_by_xpath("(//a[@href='orders.php'])[1]").click()

                        # hard-coded wait
                        time.sleep(30)

                        # getting order number
                        admin_order_number = self.driver.find_element_by_xpath("(//a[@title='Order Info'])[1]").text

                        if (order_number == admin_order_number):
                            assert (order_number == admin_order_number)
                        else:
                            assert (order_number == admin_order_number)

        except Exception:
            assert False

            # end of the test case-6 : login checkout



# end of the project