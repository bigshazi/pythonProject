#  连接设备，设备名可以通过adb命令拿到
cls.con = atx.connect('443993b8')
#  参数可以通过weditor拿到
cls.con.start_app('包名','MainActivity')
time.sleep(2)
#   截图操作
cls.con.screenshot(path)
