import logging
import random
import time

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.edge.options import Options  # Use EdgeOptions
from selenium.webdriver.edge.service import Service  # Use EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager  # Edge driver manager

# Logging setup for professional tracking of activity
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# URL of the YouTube video
video_url = "https://youtu.be/Ia4YsHmFeRA?si=sCTLQLkaf-B11BMB"

# Setup Edge options
edge_options = Options()
# edge_options.add_argument("--headless")  # Headless mode, remove to see the browser
edge_options.add_argument("--no-sandbox")
edge_options.add_argument("--disable-dev-shm-usage")
edge_options.add_argument("--disable-infobars")
edge_options.add_argument("--disable-extensions")
edge_options.add_argument(
    "start-maximized"
)  # Ensures full-screen rendering of the page
edge_options.add_argument("--disable-gpu")  # Good for systems without a GPU


# Initialize the WebDriver (Edge)
def create_driver():
    try:
        logging.info("Setting up WebDriver.")
        return webdriver.Edge(
            service=Service(EdgeChromiumDriverManager().install()), options=edge_options
        )
    except WebDriverException as e:
        logging.error(f"Error initializing WebDriver: {e}")
        raise


# Function to simulate human-like pauses and interactions
def human_like_delay(min_time, max_time):
    delay = random.uniform(min_time, max_time)
    logging.info(f"Simulating human-like delay of {delay:.2f} seconds.")
    time.sleep(delay)


# Function to watch a video for a specific duration, stop, and repeat
def watch_video(driver, video_url, watch_duration, repeat_times):
    for i in range(repeat_times):
        try:
            logging.info(f"Watching the video, iteration: {i + 1}")

            # Open the YouTube video URL
            driver.get(video_url)
            human_like_delay(2, 5)  # Wait for the page to load

            # Scroll down slightly to simulate human interaction
            driver.execute_script("window.scrollBy(0, 500);")
            logging.info("Scrolled down to mimic user behavior.")

            # Wait for the video to "play" (simulate watch time)
            human_like_delay(watch_duration - 2, watch_duration + 2)

            logging.info(
                f"Finished watching for {watch_duration} seconds. Restarting..."
            )

            # Quit the driver to simulate user closing the browser or moving on
            driver.quit()
            driver = create_driver()  # Reinitialize driver for next iteration

            # Optional: Random pause between video views to simulate human behavior
            human_like_delay(5, 15)

        except WebDriverException as e:
            logging.error(f"Error occurred during video watching: {e}")
            driver.quit()
            break


def main():
    driver = create_driver()

    try:
        watch_duration = 10
        repeat_times = 5
        watch_video(driver, video_url, watch_duration, repeat_times)
    except Exception as e:
        logging.error(f"Unhandled error: {e}")
    finally:
        # Ensure the driver is properly closed
        if driver:
            driver.quit()
        logging.info("Driver closed, task completed.")


if __name__ == "__main__":
    main()
