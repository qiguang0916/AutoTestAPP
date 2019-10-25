#!bin/usr/env python3
# -*-coding:utf-8-*-

from appium import webdriver


def getDriver():
    capabilities = {
        "platformName": "Android",
        "deviceName": "127.0.0.1:21503",
        "app": "E:\\apptestproject\\skymarketing-client-test-0813.apk"
        ###真机测试信息
        # "platformName": "Android",
        # "deviceName": "8BN0217A11000281",
        # "platfromVersion": "9.0",
        # "app": "E:\\apptestproject\\skymarketing-client-test-0813.apk"
    }
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
    return driver
    # print('这是1018分支')
    print('commit 1')
    print('commit 2')
    print('commit 3')

    print('提交version 1')
    print('提交version 2')
    print('提交version 5')
    print('提交version 6')

driver = getDriver()


# 获取当前屏幕
def getSize():
    size = driver.get_window_size()
    curWidth = size['width']
    curHeight = size['height']
    return curWidth, curHeight


# 向左滑动,滑动时间默认1秒
def swipeLeft(duration=1000):
    x1 = getSize()[0] / 10 * 9
    y1 = getSize()[1] / 2
    x2 = getSize()[0] / 10
    driver.swipe(x1, y1, x2, y1, duration)


# 向右滑动,滑动时间默认1秒
def swipeRight(duration=1000):
    x1 = getSize()[0] / 10
    y1 = getSize()[1] / 2
    x2 = getSize()[0] / 10 * 9
    driver.swipe(x1, y1, x2, y1, duration)


# 向上滑动,滑动时间默认1秒
def swipeUp(duration=1000):
    x1 = getSize()[0] / 2
    y1 = getSize()[1] / 10 * 9
    y2 = getSize()[1] / 10
    driver.swipe(x1, y1, x1, y2, duration)


# 向下滑动,滑动时间默认1秒
def swipeDown(duration=1000):
    x1 = getSize()[0] / 2
    y1 = getSize()[1] / 10
    y2 = getSize()[1] / 10 * 9
    driver.swipe(x1, y1, x1, y2, duration)


# 滑动页面
def swipeTo(direction='left', duration=1000):
    if direction == 'left':
        swipeLeft(duration)
    elif direction == 'right':
        swipeRight(duration)
    elif direction == 'up':
        swipeUp(duration)
    else:
        swipeDown(duration)


swipeTo('left')
