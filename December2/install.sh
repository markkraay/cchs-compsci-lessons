#If you want to follow the actual documentation:
#https://www.selenium.dev/selenium/docs/api/py/index.html

# Otherwise running this script should do the trick
# NOTE: This file might be unrunnable because your user account has improper
# permissions
# FIX: chmod 755 install.sh

# Downloads
pip3 install --user selenium
pip3 install --user webdriver_manager
curl https://chromedriver.storage.googleapis.com/97.0.4692.20/chromedriver_mac64.zip -o chromedriver.zip
unzip chromedriver.zip
rm chromedriver.zip


