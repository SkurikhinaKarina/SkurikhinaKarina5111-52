class Engine:
    power: int
    torque: int
    fuel_rate: float
    name: str


class Vehicle:
    name: str
    release: int
    engine: Engine


the_first = Engine()
the_first.power = "50"
the_first.torque = "100"
the_first.fuel_rate = "40"
the_first.name = "Ваз 1101"

the_second = Engine()
the_second.power = "60"
the_second.torque = "120"
the_second.fuel_rate = "60"
the_second.name = "Нива 2002"

vaz = Vehicle()
vaz.name = "Ваз"
vaz.release = "01.01.1970"
vaz.engine = the_first

niva = Vehicle()
niva.name = "Нива"
niva.release = "05.05.1990"
niva.engine = the_second


print(niva.engine.name, vaz.engine.name, sep='\n')