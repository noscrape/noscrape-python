import os
import platform


def load_noscrape_lib():
    os_name = platform.system().lower()
    arch = platform.machine().lower()
    filename = os.path.join(os.path.dirname(__file__), f"bin/noscrape_{os_name}_{arch}")

    if os_name == "windows":
        filename += ".exe"

    if not os.path.isfile(filename) or not os.access(filename, os.R_OK):
        raise Exception(f"os/arch not supported: %s" % filename)

    return filename
