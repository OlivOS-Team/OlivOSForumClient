import os
import importlib
import webview

url = 'https://forum.olivos.run/'
title = 'OlivOS论坛'

if __name__ == '__main__':
    if '_PYIBoot_SPLASH' in os.environ and importlib.util.find_spec("pyi_splash"):
        import pyi_splash
        pyi_splash.close()
    webview.create_window(
        title=title,
        url=url,
        background_color='#00A0EA'
    )
    webview.start(
        private_mode=False
    )
