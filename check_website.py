import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def check_website(url):
    try:
        response_head = requests.head(url, timeout=5, allow_redirects=False)
        if response_head.status_code == 200:
            logging.info("Server is alive")
        elif response_head.status_code == 403:
            logging.warning("Access forbidden (403)")
        elif response_head.status_code == 404:
            logging.warning("Resource not found (404)")
        elif response_head.status_code == 500:
            logging.error("Internal server error (500)")
        else:
            logging.warning(f"Server returned status code: {response_head.status_code}")

        response_get = requests.get(url, timeout=5)
        server_header = response_get.headers.get('Server')
        if server_header:
            logging.info(f"Server technology: {server_header}")
        else:
            logging.warning("Server header not found")

        response_options = requests.options(url, timeout=10)
        allow_header = response_options.headers.get('Allow')
        if allow_header:
            logging.info(f"Allowed HTTP methods: {allow_header}")
        else:
            logging.warning("Allow header not found")

    except requests.exceptions.Timeout:
        logging.error("Request timed out")
    except requests.exceptions.ConnectionError:
        logging.error("Failed to connect to the server")
    except requests.exceptions.RequestException as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    url = input("url to check : ")  
    check_website(url) 