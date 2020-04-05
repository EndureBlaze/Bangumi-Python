import requests
import json

API_URL = "https://api.bgm.tv"
headers = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15'
}

class Subject:
	def __init__(self):
		self.id = 0
		self.url = ''
		self.type = 0
		self.name = ''
		self.name_cn = ''
		self.summury = ''
		self.air_date = ''
		self.air_weekday = 0
		self.image = {}
		self.ep_status = 0
		self.vol_status = 0
		self.lasttouch = 

	def get_subject(self):
		"""
		todo
		"""

class UserCollection:
	def __init__(self):
		collections = []
		"""
		:params books: Show books, default is False
		"""

	def get_user_collections(self, username):
		params = {
			'cat': 'all_watching'
		}
		r = requests.get(API_URL + '/user/' + username + '/collection', headers=headers, params=params)
		loaded = json.loads(r.text)
		for subject in loaded:
			sub = Subject()
			sub.name = subject['name']
			sub.id = subject['subject_id']
			sub.
		print(r.text)



class User:
	def __init__(self, **kwargs):
		if 'user_id' in kwargs:
			self.user_id = kwargs['user_id']
			get_user_info(self.user_id)
		if 'url' in kwargs:
			self.url = kwargs['url']
		if 'username' in kwargs:
			self.username = kwargs['username']
			get_user_info(self.username)
		if 'nickname' in kwargs:
			self.nickname = kwargs['nickname']
		self.avatar = {
			"small": "",
			"large": "",
			"medium": ""
		}
		if 'sign' in kwargs:
			self.sign = kwargs['sign']
		if 'usergroup' in kwargs:
			self.usergroup = kwargs['usergroup']
		self.user_collections = UserCollection()
		# self.user_collections.get_user_collections(self.username)

	def get_user_info(self, username):
		"""
		Get user info
		:params username: required, can be username or user id.
		:return: raw json string
		"""
		r = requests.get(API_URL + '/user/' + str(username), headers=headers)
		loaded = json.loads(r.text)
		self.user_id = loaded['id']
		self.url = loaded['url']
		self.username = loaded['username']
		self.nickname = loaded['nickname']
		self.avatar = loaded['avatar']
		self.sign = loaded['sign']
		self.usergroup = loaded['usergroup']

		self.user_collections.get_user_collections(str(self.user_id))
		return r.text

	def print_user_info(self):
		"""
		Print all user info
		"""
		print('User ID:\t', self.user_id)
		print('URL:\t', self.url)
		print('Username:\t', self.username)
		print('Nickname:\t', self.nickname)
		print('Avatars:\t', self.avatar)
		print('Sign:\t', self.sign)
		print('Usergroup\t', self.usergroup)

def main():
	user1 = User()
	user1.get_user_info(485506)
	# user1.print_user_info()
	# user1.user_collections.get_user_collections()

if __name__ == '__main__':
	main()

