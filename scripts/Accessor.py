import logging
import requests
import requests.exceptions


class Accessor:

    def __init__(self,url):
        self.url = url

    def get_json(self):

        try:

            r = requests.get(self.url)
            r.raise_for_status()  # Raises a HTTPError if the status is 4xx, 5xxx

        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
            logging.info("API server is down")
            # TODO: try connection again

        except requests.exceptions.HTTPError:
            logging.info("400, 500 error")
            # TODO: try connection again

        else:
            return r.json()

