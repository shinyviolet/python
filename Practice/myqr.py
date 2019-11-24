from MyQR import myqr
import os
myqr.run(
    words = "https://finance.sina.com.cn/",
    version = 1,
    level = 'H',
    picture='sina.gif',
    colorized=True,
    save_name='testqr.gif',
    save_dir=os.getcwd()
)