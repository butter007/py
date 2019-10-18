from urllib.request import urlretrieve
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import win32api,win32con,win32gui

from PIL import Image


#利用PhantomJS加载网页
browser = webdriver.PhantomJS()
# 设置最大等待时间为30s
browser.set_page_load_timeout(30)
url = 'https://cn.bing.com/'
try:
    browser.get(url)
except TimeoutException:
# 当加载时间超过30秒后，自动停止加载该页面
    browser.execute_script('window.stop()')
# 从id为bgDiv的标签中获取背景图片的信息

t = browser.find_element_by_id('bgLink')
bg = t.get_attribute('href')
print (bg)
# 从字符串中提取背景图片的下载网址
#start_index = bg.index('"')
#end_index = bg.index('"')
img_url = bg
# 下载该图片到本地


img_path = 'E://Bing//Bing.jpg'
urlretrieve(img_url, img_path)

# convert jpg to bmp设置壁纸时需要将图片格式改为BMP
def setWallPaper(imagePath):
    bmpImage = Image.open(imagePath)
    newPath = imagePath.replace('.jpg', '.bmp')
    bmpImage.save(newPath, "BMP")
    return newPath

img_path = setWallPaper(img_path)

# 将下载后的图片设置为Windows系统的桌面
#  打开指定注册表路径
reg_key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
# 最后的参数:2拉伸,0居中,6适应,10填充,0平铺
win32api.RegSetValueEx(reg_key, "WallpaperStyle", 0, win32con.REG_SZ, "2")
# 最后的参数:1表示平铺,拉伸居中等都是0
win32api.RegSetValueEx(reg_key, "TileWallpaper", 0, win32con.REG_SZ, "0")
# 刷新桌面
win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, img_path, win32con.SPIF_SENDWININICHANGE)
