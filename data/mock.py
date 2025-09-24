from dataclasses import dataclass, field

from util.id import generate_unique_id

from models.room import Room
from models.device import Device
from models.light import Light
from models.lock import Lock
from models.thermo import Thermo


@dataclass
class MockData:
    rooms: list[Room] = field(default_factory=list)
    devices: list[Device] = field(default_factory=list)
    lights: list[Light] = field(default_factory=list)
    locks: list[Lock] = field(default_factory=list)
    thermos: list[Thermo] = field(default_factory=list)


mock_db = MockData()


def build_mock_data():
    create_mock_bedroom()
    create_mock_bathroom()
    create_mock_office()
    create_mock_living()
    create_mock_kitchen()
    create_mock_garage()


def create_mock_bedroom():
    bedroom = Room(id=generate_unique_id(), name="bedroom")
    mock_db.rooms.append(bedroom)

    bedroom_light_device = Device(
        id=generate_unique_id(),
        room_id=bedroom.id,
        name="bedroom light",
        kind=Light.__name__,
    )
    mock_db.devices.append(bedroom_light_device)

    bedroom_light = Light(id=generate_unique_id(), device_id=bedroom_light_device.id)
    mock_db.lights.append(bedroom_light)

    bedroom_thermo_device = Device(
        id=generate_unique_id(),
        room_id=bedroom.id,
        name="Bedroom Thermo",
        kind=Thermo.__name__,
    )
    mock_db.devices.append(bedroom_thermo_device)

    bedroom_thermo = Thermo(id=generate_unique_id(), device_id=bedroom_thermo_device.id)
    mock_db.thermos.append(bedroom_thermo)


def create_mock_bathroom():
    bathroom = Room(id=generate_unique_id(), name="bathroom")
    mock_db.rooms.append(bathroom)

    bathroom_light_device = Device(
        id=generate_unique_id(),
        room_id=bathroom.id,
        name="bathroom light",
        kind=Light.__name__,
    )
    mock_db.devices.append(bathroom_light_device)

    bathroom_light = Light(id=generate_unique_id(), device_id=bathroom_light_device.id)
    mock_db.lights.append(bathroom_light)

    bathroom_thermo_device = Device(
        id=generate_unique_id(),
        room_id=bathroom.id,
        name="bathroom thermo",
        kind=Thermo.__name__,
    )
    mock_db.devices.append(bathroom_thermo_device)

    bathroom_thermo = Thermo(
        id=generate_unique_id(), device_id=bathroom_thermo_device.id
    )
    mock_db.thermos.append(bathroom_thermo)


def create_mock_office():
    office = Room(id=generate_unique_id(), name="office")
    mock_db.rooms.append(office)

    office_light_device = Device(
        id=generate_unique_id(),
        room_id=office.id,
        name="office light",
        kind=Light.__name__,
    )
    mock_db.devices.append(office_light_device)

    office_light = Light(id=generate_unique_id(), device_id=office_light_device.id)
    mock_db.lights.append(office_light)

    office_thermo_device = Device(
        id=generate_unique_id(),
        room_id=office.id,
        name="office thermo",
        kind=Thermo.__name__,
    )
    mock_db.devices.append(office_thermo_device)

    office_thermo = Thermo(id=generate_unique_id(), device_id=office_thermo_device.id)
    mock_db.thermos.append(office_thermo)


def create_mock_living():
    living = Room(id=generate_unique_id(), name="living")
    mock_db.rooms.append(living)

    living_light_device = Device(
        id=generate_unique_id(),
        room_id=living.id,
        name="living light",
        kind=Light.__name__,
    )
    mock_db.devices.append(living_light_device)

    living_light = Light(id=generate_unique_id(), device_id=living_light_device.id)
    mock_db.lights.append(living_light)

    living_thermo_device = Device(
        id=generate_unique_id(),
        room_id=living.id,
        name="Living Thermo",
        kind=Thermo.__name__,
    )
    mock_db.devices.append(living_thermo_device)

    living_thermo = Thermo(id=generate_unique_id(), device_id=living_thermo_device.id)
    mock_db.thermos.append(living_thermo)

    living_lock_device = Device(
        id=generate_unique_id(),
        room_id=living.id,
        name="living lock",
        kind=Lock.__name__,
    )
    mock_db.devices.append(living_lock_device)

    living_lock = Lock(id=generate_unique_id(), device_id=living_lock_device.id)
    mock_db.locks.append(living_lock)


def create_mock_kitchen():
    kitchen = Room(id=generate_unique_id(), name="kitchen")
    mock_db.rooms.append(kitchen)

    kitchen_light_device = Device(
        id=generate_unique_id(),
        room_id=kitchen.id,
        name="kitchen light",
        kind=Light.__name__,
    )
    mock_db.devices.append(kitchen_light_device)

    kitchen_light = Light(id=generate_unique_id(), device_id=kitchen_light_device.id)
    mock_db.lights.append(kitchen_light)

    kitchen_thermo_device = Device(
        id=generate_unique_id(),
        room_id=kitchen.id,
        name="kitchen thermo",
        kind=Thermo.__name__,
    )
    mock_db.devices.append(kitchen_thermo_device)

    kitchen_thermo = Thermo(id=generate_unique_id(), device_id=kitchen_thermo_device.id)
    mock_db.thermos.append(kitchen_thermo)


def create_mock_garage():
    garage = Room(id=generate_unique_id(), name="garage")
    mock_db.rooms.append(garage)

    garage_light_device = Device(
        id=generate_unique_id(),
        room_id=garage.id,
        name="garage light",
        kind=Light.__name__,
    )
    mock_db.devices.append(garage_light_device)

    garage_light = Light(id=generate_unique_id(), device_id=garage_light_device.id)
    mock_db.lights.append(garage_light)

    garage_lock_device = Device(
        id=generate_unique_id(),
        room_id=garage.id,
        name="garage lock",
        kind=Lock.__name__,
    )
    mock_db.devices.append(garage_lock_device)

    garage_lock = Lock(id=generate_unique_id(), device_id=garage_lock_device.id)
    mock_db.locks.append(garage_lock)
