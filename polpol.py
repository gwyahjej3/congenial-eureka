from seleniumbase import SB
import time
import requests
import sys
import requests
import os
import random
import subprocess
from dataclasses import dataclass
from typing import List, Optional

import requests
geo_data = requests.get("http://ip-api.com/json/").json()

latitude = geo_data["lat"]
longitude = geo_data["lon"]
timezone_id = geo_data["timezone"]
language_code = geo_data["countryCode"].lower()  # e.g., 'us' -> 'en-US'
with SB(uc=True, test=True,locale=f"{language_code.upper()}") as yeyed:
    yeyed.execute_cdp_cmd(
        "Emulation.setGeolocationOverride",
        {
            "latitude": latitude,
            "longitude": longitude,
            "accuracy": 100
        }
    )
    yeyed.execute_cdp_cmd(
        "Emulation.setTimezoneOverride",
        {"timezoneId": timezone_id}
    )
    url = "https://www.twitch.tv/brutalles"
    yeyed.uc_open_with_reconnect(url, 5)
    yeyed.sleep(14)
    if yeyed.is_element_present("#live-channel-stream-information"):

        if yeyed.is_element_present('button:contains("Accept")'):
            yeyed.uc_click('button:contains("Accept")', reconnect_time=4)
        if True:
            yeyed.uc_open_with_reconnect(url, 5)
            yeyed2 = yeyed.get_new_driver(undetectable=True)
            yeyed2.uc_open_with_reconnect(url, 5)
            yeyed.sleep(10)
            if yeyed2.is_element_present('button:contains("Accept")'):
                yeyed2.uc_click('button:contains("Accept")', reconnect_time=4)
            while yeyed2.is_element_present("#live-channel-stream-information"):
                yeyed2.sleep(1)
            yeyed.quit_extra_driver()
    yeyed.sleep(1)
