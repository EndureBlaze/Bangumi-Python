import requests
import json

API_URL = "https://api.bgm.tv"
headers = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15'
}

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

class Collection:
	"""
	用户收藏的动画/书籍
	"""
	def __init__(self):
		is_book = False
		self.name = ''
		self.subject_id = 0
		self.ep_status = 0
		self.vol_status = 0
		self.lasttouch = 0
		self.subject = SubjectSmall()

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

class Topic:
	"""
	Discussion
	"""
	def __init__(self):
		self.id = 0
		self.url = ''
		self.title = ''
		self.main_id = 0
		self.timestamp = 0
		self.lastpost = 0
		self.replies = 0
		self.user = User()

class Blog:
	"""
	
	"""
	def __init__(self):
		self.id = 0
		self.url = ''
		self.title = ''
		self.summary = ''
		self.image = ''
		self.replies = 0
		self.timestamp = 0
		self.dateline = ''
		self.user = User()

class SubjectCollection:
	"""
	Number of collection status
	"""
	def __init__(self):
		self.wish = -1
		self.collect = -1
		self.doing = -1
		self.on_hold = -1
		self.dropped = -1

	def set(self, collection):
		if 'wish' in collection.keys(): self.wish = collection['wish']
		if 'collect' in collection.keys(): self.collect = collection['collect']
		if 'doing' in collection.keys(): self.doing = collection['doing']
		if 'on_hold' in collection.keys(): self.on_hold = collection['on_hold']
		if 'dropped' in collection.keys(): self.dropped = collection['dropped']

class Subject:
	"""

	"""
	def __init__(self):
		self.id = 0
		self.url = ''
		self.type = 0
		self.name = ''

class SubjectBase:
	"""

	"""
	def __init__(self):
		self.id = 0
		self.url = ''
		self.type = 0
		self.name = ''
		self.name_cn = ''
		self.summary = ''
		self.air_date = ''
		self.air_weekday = 0
		self.images = Images()

class SubjectSmall(SubjectBase):
	"""

	"""
	def __init__(self):
		super().__init__()
		self.eps = 0
		self.eps_count = 0
		self.rating = {}
		self.rank = 0
		self.collection = {}

class SubjectMedium(SubjectSmall):
	"""

	"""
	def __init__(self):
		super().__init__()
		self.crt = []
		self.staff = []

class SubjectLarge(SubjectBase):
	""" """
	def __init__(self):
		super().__init__()

class User:
	""" """
	def __init__(self, **kwargs):
		self.id = 0
		self.url = ''
		self.username = ''
		self.nickname = ''
		self.avatar = Avatar()
		self.sign = ''
		self.usergroup = UserGroup()
		self.collections = []

	def __check_username(self, username=''):
		if username != '':
			return username
		elif self.username != '':
			return self.username
		elif self.id != 0:
			return self.id

	def get_user(self, username=''):
		"""
		返回用户基础信息
		:param username: 用户名，也可使用 UID
		"""
		username = self.__check_username(username)
		r = requests.get(API_URL + '/user/%s' % username, headers=headers)
		loaded = json.loads(r.text)
		self.id = loaded['id']
		self.url = loaded['url']
		self.username = loaded['username']
		self.nickname = loaded['nickname']
		self.avatar.large = loaded['avatar']['large']
		self.avatar.medium = loaded['avatar']['medium']
		self.avatar.small = loaded['avatar']['small']
		self.sign = loaded['sign']
		self.usergroup.type_id = loaded['usergroup']
		self.usergroup.get_type(self.usergroup.type_id)
		return r.text

	def get_user_collection(self, cat='watching', ids='', response_group='medium'):
		username = self.__check_username()
		params = {
			'cat': cat,
			'ids': ids,
			'responseGroup': response_group
		}
		r = requests.get(API_URL + '/user/%s/collection' % username, headers=headers, params=params)
		loaded = json.loads(r.text)

		for collection in loaded:
			new_collection = Collection()
			new_collection.name = collection['name']
			new_collection.subject_id = collection['subject_id']
			if 'ep_status' in collection.keys():
				new_collection.ep_status = collection['ep_status']
			if 'vol_status' in collection.keys():
				new_collection.is_book = True
				new_collection.vol_status = collection['vol_status']
			new_collection.lasttouch = collection['lasttouch']
			new_collection.subject.id = collection['subject']['id']
			new_collection.subject.url = collection['subject']['url']
			new_collection.subject.type = collection['subject']['type']
			new_collection.subject.name = collection['subject']['name']
			new_collection.subject.name_cn = collection['subject']['name_cn']
			new_collection.subject.summary = collection['subject']['summary']
			new_collection.subject.eps = collection['subject']['eps']
			new_collection.subject.eps_count = collection['subject']['eps_count']
			new_collection.subject.air_date = collection['subject']['air_date']
			new_collection.subject.air_weekday = collection['subject']['air_weekday']
			new_collection.subject.images.large = collection['subject']['images']['large']
			new_collection.subject.images.common = collection['subject']['images']['common']
			new_collection.subject.images.medium = collection['subject']['images']['medium']
			new_collection.subject.images.small = collection['subject']['images']['small']
			new_collection.subject.images.grid = collection['subject']['images']['grid']
			new_collection.subject.collection = collection['subject']['collection']
			self.collections.append(new_collection)
			print(collection['name'])

class UserGroup:
	""" """
	def __init__(self):
		self.type_id = 0
		self.type = self.get_type(self.type_id)

	def get_type(self, type_id):
		chart = ['','管理员','Bangumi 管理猿','天窗管理猿','禁言用户','禁止访问用户','','','人物管理猿','维基条目管理猿','用户','维基人']
		self.type = chart[type_id]		

class StatusCode:
	"""
	Response Status, HTTP codes are all 200
	"""
	def __init__(self):
		self.request = ''
		self.code = 0
		self.error = ''

class Avatar:
	"""头像"""
	def __init__(self):
		self.large = ''
		self.medium = ''
		self.small = ''

class Images:
	"""
	番剧图片
	"""
	def __init__(self):
		self.large = ''
		self.common = ''
		self.medium = ''
		self.small = ''
		self.grid = ''






