import config
from peewee import *

database = MySQLDatabase(
    database=config.database,
    host=config.host,
    port=config.port,
    user=config.user,
    password=config.password
)


class BaseModel(Model):
    class Meta:
        database = database


class Car(BaseModel):
    id = PrimaryKeyField(null=False)
    engine = CharField(max_length=10, null=False)

    def __str__(self):
        return f'id={self.id}: engine={self.engine}'

    class Meta:
        db_table = "car"


try:
    database.connection()
    Car.create_table()
    print("ok")
except Exception:
    print("eror")

# car1 = Car(engine=1.6)
# car2 = Car(engine=2.0)
# car1.save()
# car2.save()

list_cars = Car.select()
for car in list_cars:
    print(car)

# car_4 = Car.get(Car.id == 2)
# print(car_4)

# car_5=Car.get_by_id(1)
# car_5.engine=3.0
# car_5.save()

Car.delete_by_id(2)