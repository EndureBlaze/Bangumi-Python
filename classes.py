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
				"name": "看过"
			},
			"3": {
				"type": "do",
				"name": "在看"
			},
			"4": {
				"type": "onhold",
				"name": "搁置"
			},
			"5": {
				"type": "dropped",
				"name": "抛弃"
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
				"name": "看过"
			},
			"1": {
				"type": "queue",
				"name": "想看"
			},
			"3": {
				"type": "drop",
				"name": "抛弃"
			},
			"?": {
				"type": "remove",
				"name": "撤销"
			}
		}
		self.id = 0
		self.type = chart[str(self.id)]['type']
		self.name = chart[str(self.id)]['name']
class MonoBase:
	"""
	Character (Base Model)
	:attribute id: Integer, Character ID
	:attribute url: String, Character link url
	:attribute name: String, Character name
	:attribute images: Dict, 4 String keys (large, medium, small, grid), each with 1 String value (pic url)
	"""
	def __init__(self):
		self.id = 0
		self.url = ''
		self.name = ''
		self.images = {}
class Alias:
	"""
	:attribute jp: String, Japanese name
	:attribute kana: String, Japanese kana name
	:attribute nick: String, Nickname
	:attribute romaji: String, Roman script
	:attribute zh: String, Another Chinese name
	"""
	def __init__(self):
		self.jp = ''
		self.kana = ''
		self.nick = ''
		self.romaji = ''
		self.zh = ''
		self.other = ''
class Mono(MonoBase):
	"""
	Character (Inherited from MonoBase)
	:attribute name_cn: String, Character's Chinese name
	:attribute comment: Integer, Number of replies
	:attribute collects: Integer, Favourites
	"""
	def __init__(self):
		super().__init__()
		self.name_cn = ''
		self.comment = 0
		self.collects = 0
class MonoInfo(Mono):
	"""
	Character Info (Inherited from Mono)
	:attribute birth: String, Birthday
	:attribute height: String, Height
	:attribute gender: String, Gender
	:attribute alias: Alias, Alias
	:attribute source: Dict, Cite sources
	:attribute cv: String, Dubbing actor
	"""
	def __init__(self):
		super().__init__()
		self.birth = ''
		self.height = ''
		self.gender = ''
		self.alias = Alias()
		self.source = {}
		self.cv = ''
class Person:
	"""
	Real person
	:attribute id: Integer, Person's ID
	:attribute url: String, Person's URL
	:attribute name: String, Person's name
	:attribute images: Dict, Images' URLs
	:attribute name_cn: String, Person's Chinese name
	:attribute comment: Integer, Numbers of replies
	:attribute collects: Integer, Favourites
	:attribute info: MonoInfo, Person's infomation
	"""
	def __init__(self):
		self.id = 0
		self.url = ''
		self.name = ''
		self.images = {}
		self.name_cn = ''
		self.comment = 0
		self.collects = 0
		self.info = MonoInfo()
class Character:
	"""
	Virtual character
	:attribute id: Integer, Character's ID
	:attribute url: String, Character's URL
	:attribute name: String, Character's name
	:attribute images: Dict, Images' URLs
	:attribute name_cn: String, Character's Chinese name
	:attribute comment: Integer, Numbers of replies
	:attribute collects: Integer, Favourites
	:attribute info: MonoInfo, Character's infomation
	:attribute actors: List[MonoBase], List of dubbing actors
	"""
	def __init__(self):
		self.id = 0
		self.url = ''
		self.name = ''
		self.images = {}
		self.name_cn = ''
		self.comment = 0
		self.collects = 0
		self.info = MonoInfo()
		self.actors = []
class Episode:
	"""
	Episode infomation
	:attribute id: Integer, Episode ID
	:attribute url: String, Episode's URL
	:attribute type: Integer, Episode type
	:attribute sort: Integer, Number of episode
	:attribute name: String, Title
	:attribute name_cn: String, Title in Simplified Chinese
	:attribute duration: String, Duration of episode
	:attribute airdat: String, Air date
	:attribute comment: Integer, Number of replies
	:attribute desc: String, A brief introduction
	:attribute status: String, 3 possibility
	"""
	def __init__(self):
		type_chart = {
			"0": "本篇",
			"1": "特别篇",
			"2": "OP",
			"3": "ED",
			"4": "预告/宣传/广告",
			"5": "MAD",
			"6": "其他"
		}
		status_chart = {
			"Air": "已放送",
			"Today": "正在放送",
			"NA": "未放送"
		}
		self.id = 0
		self.url = ''
		self.type = 0
		self.sort = 0
		self.name = ''
		self.name_cn = ''
		self.duration = ''
		self.airdate = ''
		self.comment = 0
		self.desc = ''
		self.status = ''













