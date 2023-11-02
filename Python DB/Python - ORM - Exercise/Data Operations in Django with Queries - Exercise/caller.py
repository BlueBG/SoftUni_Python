import os
from typing import List

import django
from django.db.models import QuerySet

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom


def create_pet(name: str, species: str) -> str:
    pet = Pet.objects.create(
        name=name,
        species=species,
    )
    return f"{name} is a very cute {species}!"


# print(create_pet('Buddy', 'Dog'))
# print(create_pet('Whiskers', 'Cat'))
# print(create_pet('Rocky', 'Hamster'))


def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool) -> str:
    artifact = Artifact.objects.create(
        name=name,
        origin=origin,
        age=age,
        description=description,
        is_magical=is_magical,
    )

    return f"The artifact {name} is {age} years old!"


def delete_all_artifacts():
    Artifact.objects.all().delete()


# print(create_artifact('Ancient Sword', 'Lost Kingdom', 500, 'A legendary sword with a rich history', True))


def show_all_locations() -> str:
    locations = Location.objects.all().order_by('-id')

    return '\n'.join(f"{l.name} has a population of {l.population}!" for l in locations)


def new_capital() -> None:
    first_location = Location.objects.first()
    first_location.is_capital = True

    first_location.save()


def get_capitals() -> QuerySet:
    return Location.objects.filter(is_capital=True).values('name')


def delete_first_location() -> None:
    Location.objects.first().delete()


# print(show_all_locations())
# print(new_capital())
# print(get_capitals())

def apply_discount() -> None:
    cars = Car.objects.all()

    for car in cars:
        percent_off = sum(int(c) for c in str(car.year)) / 100
        discount = float(car.price) * percent_off
        car.price_with_discount = float(car.price) - discount

        car.save()


def get_recent_cars() -> QuerySet:
    return Car.objects.filter(year__gte=2020).values('model', 'price_with_discount')


def delete_last_car() -> None:
    Car.objects.last().delete()


# apply_discount()
# print(get_recent_cars())


def show_unfinished_tasks() -> List:
    all_unfinished_tasks = Task.objects.filter(is_finished=False)

    return [f"Task - {t.title} needs to be done until {t.due_date}!" for t in all_unfinished_tasks]


def complete_odd_tasks():
    tasks = Task.objects.all()

    for task in tasks:
        if task.id % 2 != 0:
            task.is_finished = True
            task.save()


def encode_and_replace(text: str, task_title: str):
    encoded_text = "".join([chr(ord(s) - 3) for s in text])

    Task.objects.filter(title=task_title).update(description=encoded_text)


# encode_and_replace("Zdvk#wkh#glvkhv$", "Simple Task")
# print(Task.objects.get(title='Simple Task').description)


def get_deluxe_rooms() -> str:
    deluxe_room = HotelRoom.objects.filter(room_type='Deluxe')

    even_deluxe_rooms = []

    for room in deluxe_room:
        if room.id % 2 == 0:
            even_deluxe_rooms.append(str(room))

    return '\n'.join(even_deluxe_rooms)


def increase_room_capacity() -> None:
    all_rooms = HotelRoom.objects.all().order_by('id')

    previous_room_capacity = None

    for room in all_rooms:

        if not room.is_reserved:
            continue

        if previous_room_capacity:
            room.capacity += previous_room_capacity

        else:
            room.capacity += room.id

        previous_room_capacity = room.capacity

        room.save()


def reserve_first_room():
    first_room = HotelRoom.objects.first()
    first_room.is_reserved = True
    first_room.save()


def delete_last_room():
    last_room = HotelRoom.objects.last()

    if last_room.is_reserved:
        last_room.delete()


# print(get_deluxe_rooms())
# reserve_first_room()
# print(HotelRoom.objects.get(room_number=101).is_reserved)
