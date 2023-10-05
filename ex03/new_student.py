
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
	active: bool = field(default=False)
	login: str = field(init=False)
	id: str = field(default_factory=generate_id, init=False)
	
	def __post_init__(self):
		'''Post init'''
		self.login = self.name[0] + self.surname

		

