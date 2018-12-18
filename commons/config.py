from appium import webdriver

#config.py is to have the basic setup related to app configuration

#Setup related variables

AppiumHostedOn = 'http://127.0.0.1:4723/wd/hub'
PlatformName = 'Android'
PlatformVersion = '8.0'
DeviceName = 'Nexus_6'
AppName = '/Users/Docs/apps/appName.apk'
ActivityName = 'com.android.apps.ui.HomeActivity'
PackageName = 'com.android.packageName'
AppWaitActivity = 'com.*'


class SetupClass():

    def __init__(self):
        self.driver = None
        self.setup()

    def setup(self):
        desired_capabilities = {}
        desired_capabilities['platformName'] = PlatformName
        desired_capabilities['platformVersion'] = PlatformVersion
        desired_capabilities['deviceName'] = DeviceName
        desired_capabilities['app'] = AppName
        desired_capabilities['appPackage'] = PackageName
        desired_capabilities['appActivity'] = ActivityName
        desired_capabilities['appWaitActivity'] = AppWaitActivity

        self.driver = webdriver.Remote(AppiumHostedOn, desired_capabilities)
        self.driver.implicitly_wait(20)

    def get_driver(self):
        return self.driver


