"""
Medium.com session keeper - Day 1 task.

Sequence:
  1. Launch Chrome with a PERSISTENT profile (profiles/chrome_profile)
  2. Open medium.com
  3. If already signed in (cookie 'sid' present) -> done, exit
  4. Otherwise: wait while the human manually signs up in that same window
  5. Once the 'sid' cookie appears -> signed in, session is saved to disk
  6. Every future run of this script reuses that profile -> stays signed in

Run this from the project ROOT (the mindcob folder that contains
pages/, utils/, profiles/) - not from inside a subfolder - because the
imports below are relative to this file's own location.
"""

from pages.medium_page import MediumPage
from utils.driver_factory import create_driver


def main() -> None:
    driver = create_driver()
    try:
        page = MediumPage(driver)
        page.open_home()

        if page.is_signed_in():
            print("[+] Already signed in - session loaded from profiles/chrome_profile")
            return

        if page.wait_for_human_signup():
            print("[+] SUCCESS - you are signed in to medium.com.")
            print("[+] Session saved to profiles/chrome_profile.")
            print("[+] Run this script again anytime - you will stay signed in.")
        else:
            print("[-] Timed out (15 min). Run again and finish the signup a bit faster.")
    except KeyboardInterrupt:
        print("\n[!] Stopped by you (Ctrl+C). Run again to continue.")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()