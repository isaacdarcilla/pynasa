import api.api as api
import api.url as url


class Nasa:
    """Developed by Isaac D. Arcilla (github.com/isaacdarcilla).
    🚀 Python package that can track the location of ISS.\n"""
    @staticmethod
    def crews():
        """Print the list of crews boarding the ISS"""
        message = ""
        data = api.Api()
        crew = data.api_data(url.astronauts())
        passengers = [astronaut['name'] + "\n" for astronaut in crew['people']]
        for person in passengers:
            message += person

        return message

    @staticmethod
    def count():
        """Print the total number of crews boarding the ISS"""
        data = api.Api()
        crew = data.api_data(url.astronauts())

        return crew["number"]

    @staticmethod
    def location():
        """Return latitude and longitude location from NASA Api."""
        data = api.Api()
        location = data.api_data(url.locations())
        location = location["iss_position"]
        latitude = location["latitude"]
        longitude = location["longitude"]

        return float(latitude), float(longitude)