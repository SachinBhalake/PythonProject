wait = WebDriverWait(self.driver, 30)
wait.until(expected_conditions.url_changes(self.driver.current_url))
