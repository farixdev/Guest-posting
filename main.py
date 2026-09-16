from utils.driver_factory import get_driver
from pages.medium_page import MediumPage

driver = get_driver()

medium = MediumPage(driver)

medium.open_medium()

input(
    "\nPress ENTER if already logged in..."
)

try:

    medium.click_get_started()

    medium.click_google_signup()

    print(
        "\nLogin manually with Google."
    )

    input(
        "\nAfter login press ENTER..."
    )

except Exception as e:
    print(e)

print(
    "\nProfile saved successfully."
)

input(
    "\nPress ENTER to close browser..."
)

driver.quit()