import json
import urllib.request


class Api:
    @staticmethod
    def api_data(url):
        """Get the JSON data from the specified NASA Api"""
        url = url
        response = urllib.request.urlopen(url)
        string = response.read().decode("UTF-8")
        result = json.loads(string)

        if result['message']:
            return result
        else:
            return "Not reachable."
