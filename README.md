se adjunta el resultado de las consultas para las nuevas url
# http://localhost:8000/measurements/

[{"model": "measurements.measurement", "pk": 1, "fields": {"variable": 1, "value": 25.0, "unit": "C", "place": "place 1", "dateTime": "2022-02-13T19:13:56.298Z"}}, {"model": "measurements.measurement", "pk": 2, "fields": {"variable": 1, "value": 2.0, "unit": "C", "place": "place 2", "dateTime": "2022-02-13T19:14:04.547Z"}}, {"model": "measurements.measurement", "pk": 3, "fields": {"variable": 2, "value": 10.0, "unit": "C", "place": "place 1", "dateTime": "2022-02-13T19:14:16.236Z"}}]

# http://localhost:8000/measurements/3

[ {"model": "measurements.measurement", "pk": 3, "fields": {"variable": 2, "value": 10.0, "unit": "C", "place": "place 1", "dateTime": "2022-02-13T19:14:16.236Z"}}]
