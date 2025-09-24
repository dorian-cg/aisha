import random
import uuid


def generate_unique_id():
    og_seed = random.getstate()
    random.seed("*** super unique seed here ***")
    id = uuid.uuid4()
    random.setstate(og_seed)
    return id.hex
