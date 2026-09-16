"""
Medium.com session keeper - Senior Developer Architecture.
"""
from pages.medium_page import MediumPage
from utils.driver_factory import (
    launch_native_chrome,
    close_chrome_process,
    random_sleep,
)


def main() -> None:
    page = MediumPage()

    # Check if already signed in from saved profile
    if page.is_signed_in():
        print("\n[+] SUCCESS: Already signed in! Session loaded from profiles/chrome_profile.")
        print("[+] Opening Chrome browser with your active session...")
        proc = launch_native_chrome("https://medium.com")
        print("[+] Your session is active and verified.")
        print("[+] Closing browser in 3 seconds...")
        random_sleep(2.5, 3.5)
        close_chrome_process(proc)
        return

    # If not signed in, launch clean native Chrome and wait for sign in / up
    print("[+] Launching clean native Chrome instance...")
    proc = launch_native_chrome("https://medium.com")
    try:
        if page.wait_for_human_signup(proc):
            print("\n[+] SUCCESS: Sign in / Sign up complete!")
            print("[+] Session saved permanently to profiles/chrome_profile.")
            print("[+] Closing browser in 2 seconds...")
            random_sleep(1.5, 2.5)
            close_chrome_process(proc)
        else:
            print("\n[-] Sign in not detected within timeout. Run again to finish sign in.")
            close_chrome_process(proc)
    except KeyboardInterrupt:
        print("\n[!] Stopped by user (Ctrl+C).")
        close_chrome_process(proc)


if __name__ == "__main__":
    main()