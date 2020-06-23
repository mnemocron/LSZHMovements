# LSZHMovements
web API for ZRH/LSZH Zürich Airport Airport arrivals/departures Table

---

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![volkswagen status](https://auchenberg.github.io/volkswagen/volkswargen_ci.svg?v=1)](https://github.com/auchenberg/volkswagen)

This script downloads the `json` table from the new LSZH website: [flughafen-zuerich.ch](https://dxp-fds.flughafen-zuerich.ch/flights) and parses it into two `timetable.json` files.


### Usage

Use the `-o` parameter to specify the output directory.

```bash
python3 get-lszh.py -o zrh/
```

Outputs: `zrh/arrivals.timetable.json` and `zrh/departures.timetable.json` 

### Example Output

```json
{
  "data": [
    {
      "id": 776369,
      "flightType": "A",
      "SDT": "2020-06-23T00:00:00Z",
      "STA": "2020-06-23T13:50:00Z",
      "ETA": "2020-06-23T13:01:00Z",
      "TER": "2",
      "FLC": "LX",
      "airlineLogo": "https://www.flughafen-zuerich.ch/-/jssmedia/airport/portal/logos/airline/swiss.svg?vs=1",
      "FLN": "189",
      "REG": "HBJNH",
      "statusCode": 10,
      "statusTextDe": "Fracht",
      "statusTextEn": "Cargo",
      "airportName": "International Airport",
      "cityDe": "Shanghai",
      "cityEn": "Shanghai",
      "search": "LX189 LX 189 SWISS PVG  International Airport Shanghai Shanghai       ",
      "POR": "PVG",
      "ICT": "B77W",
      "TYP": "777",
      "TYS": "77W",
      "model": "777-300",
      "manufacturerName": "Boeing",
      "isCommercial": false,
      "airline": "SWISS"
    }
  ]
}
```


---

### Statement

> "Wir freuen uns, dass Sie unsere neue Webseite bereits ausprobiert haben und danken Ihnen für Ihre Anfrage für einen API-Zugang auf unsere Homepage.

> Bezüglich der detaillierten Informationen über den Flugzeugtyp und Registration der Flugzeuge möchten wir Ihnen mitteilen, dass wir diese Funktion für unsere Aviatikfans verbessert und erweitert haben. So werden beispielsweise neu auch Frachtflüge angezeigt. Sie können sich ein Profil erstellen und erhalten detaillierte, geräteübergreifende Informationen oder Sie stellen sich den Spottermodus zeitlich begrenzt ein. Diese sowie weiterführende Informationen für Spotter finden Sie unter dem folgenden Link: [www.flughafen-zuerich.ch/de/passagiere/erleben/erlebnisse/spotter-informationen](http://www.flughafen-zuerich.ch/de/passagiere/erleben/erlebnisse/spotter-informationen).

> Wir sind überzeugt, dass wir so für die Aviatikfans eine gute Möglichkeit gefunden haben, um Informationen abrufen zu können und hoffen, dass Ihnen die neue Webseite künftig von besserem Nutzen sein wird."


---

LICENSE

Apache License 2.0

(c) 2020 Simon Burkhardt





