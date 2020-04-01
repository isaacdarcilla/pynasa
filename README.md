<p align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png" width="500"></p>

<p align="center">🚀 Python package that can track the location of ISS </p>

## ✨ Installation

* `git clone https://github.com/isaacdarcilla/pynasa.git` - clone the repository
* `cd pynasa` - change to project directory
* `python test.py` - run test

## ✨ Usage 

```python
# Print the location
print(nasa.location())

# Print the crew names
print(nasa.crews())

# Print the total crews
print(nasa.count())
```

## ✨ API

* `URL` - http://api.open-notify.org/iss-now.json
* `GET` - method 

```json
{
  "message": "success",
  "iss_position": {
    "longitude": "91.6876",
    "latitude": "-23.5057"
  },
  "timestamp": 1585715434
}
```

* `URL` - http://api.open-notify.org/astros.json
* `GET` - method 

```json
{
  "people": [
    {
      "craft": "ISS",
      "name": "Andrew Morgan"
    },
    ...
  ],
  "message": "success",
  "number": 3
}
```
## ✨ License

[Apache 2.0 License](https://github.com/isaacdarcilla/DesktopQuery/blob/master/LICENSE)

## 💻 Developer

Developed by Isaac [(facebook.com/isaacdarcilla)](https://web.facebook.com/isaacdarcilla)

## ✨ Support

Fork or star this repository for support.

## 🐞 Issues and Pull Requests

Not accepting any issues and pull requests. 

## 🚫 No Scammers
