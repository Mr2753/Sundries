import sys
import os
import pyppeteer.chromium_downloader


def current_platform() -> str:
    """Get current platform name by short string."""
    if sys.platform.startswith('linux'):
        return 'linux'
    elif sys.platform.startswith('darwin'):
        return 'mac'
    elif (sys.platform.startswith('win') or
          sys.platform.startswith('msys') or
          sys.platform.startswith('cyg')):
        if sys.maxsize > 2 ** 31 - 1:
            return 'win64'
        return 'win32'
    raise OSError('Unsupported platform: ' + sys.platform)


platform = current_platform()
print('默认版本是：{}'.format(pyppeteer.__chromium_revision__))
print('平台下载链接为：{}'.format(pyppeteer.chromium_downloader.downloadURLs.get(platform)))
print('解压目录：{}'.format(
    os.path.dirname(os.path.dirname(pyppeteer.chromium_downloader.chromiumExecutable.get(platform)))
))
