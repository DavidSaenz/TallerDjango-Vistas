from ..models import Measurement

#todas las medidas
def get_measurements():
    measurements = Measurement.objects.all()
    return measurements

#medida por id
def get_measurement(var_pk):
    measurement = Measurement.objects.get(pk=var_pk)
    return measurement

def update_measurement(var_pk, new_var,new_value,new_unit,new_place):
    measurement = get_measurement(var_pk)
    measurement.variable = new_var["variable"]
    measurement.unit = new_unit["unit"]
    measurement.value = new_value["value"]
    measurement.place = new_place["place"]
    measurement.save()
    return variable

def create_measurement(mes):
    measurement = Measurement(variable=mes["variable"],unit=mes["unit"],value=mes["value"],place=mes["place"])
    measurement.save()
    return measurement