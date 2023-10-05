
import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
	'''Generate ID'''
	return "".join(random.choices(string.ascii_lowercase, k = 15))


@dataclass
class Student:
	'''Student class'''
	name: str
	surname: str
	active: bool
	


