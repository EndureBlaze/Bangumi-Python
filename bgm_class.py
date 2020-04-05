class CollectionStatus:
	"""
	收藏状态
	"""
	def __init__(self):
		chart = {
			"1": {
				"type": "wish",
				"name": "想看"
			},
			"2": {
				"type": "collect",
				"name": "想看"
			},
			"3": {
				"type": "do",
				"name": "想看"
			},
			"4": {
				"type": "onhold",
				"name": "想看"
			},
			"5": {
				"type": "dropped",
				"name": "想看"
			}
		}
		self.id = 0
		self.type = chart[str(self.id)]['type']
		self.name = chart[str(self.id)]['name']
class EpStatus:

	def __init__(self):
		chart = {
			"2": {
				"type": "watched",
				"name": "想看"
			},
			"1": {
				"type": "queue",
				"name": "想看"
			},
			"3": {
				"type": "drop",
				"name": "想看"
			},
			"?": {
				"type": "remove",
				"name": "想看"
			}
		}
		self.id = 0
		self.type = chart[str(self.id)]['type']
		self.name = chart[str(self.id)]['name']
class MonoBase:
	def __init__(self):
		self.id = 0
		self.url = ''
		self.name = ''
		self.images = {}

class Mono(MonoBase):
	def __init__(self):
		super().__init__()

		