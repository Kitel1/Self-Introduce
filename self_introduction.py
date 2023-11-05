import datetime
currentdate = datetime.datetime.now()

#クラス定義
class Person:
	#国籍
	NATIONALITY= None
	#コンストラクタ
	def __init__(self, firstname, lastname, age, gender):
		self.firstname = firstname
		self.lastname = lastname
		self.age = age
		self.gender = gender
	#変数name操作
	def setName(self, firstname, lastname):
		self.firstname = firstname
		self.lastname = lastname
	def getName(self):
		fullname = "{0} {1}".format(self.firstname, self.lastname)
		return fullname
	#変数age操作
	def setAge(self, age):
		self.age=age
	def getAge(self):
		return self.age
	def addAge(self):
		self.age += 1
	#変数gender操作
	def setGender(self, gender):
		self.gender=gender
	def getGender(self):
		return self.gender
	#成人判定（多くの国では１８歳以上を成人として扱う
	def isAdult(self):
		return True if self.age >= 18 else False
	#選挙権判定（多くの国では１８歳で選挙権を得る）
	def isVote(self):
		return True if self.age >= 18 else False
	#自己紹介
	def saySelfIntroduction(self):
		str1 = "My name is {0}.".format(self.getName())
		str2 = "I am {0} years old.".format(self.getAge())
		#国籍有無判定
		if self.NATIONALITY is None:
			str3 = "I dont't know my nationality."
		else:
			str3 = "My nationality is {0}.".format(self.NATIONALITY)
		#成人判定
		if self.isAdult():
			str4 = "I'm a grown person"
		else: 
			str4 = "I'm not a grown person"
		#選挙権判定
		if self.isVote():
			str5 = "I have the voting right"
		else: 
			str5 = "I dont't have the voting right"
		
		print(str1, str2, str3, str4, str5, sep='\n')

#
class Vietnamese(Person):
	NATIONALITY= "Vietnamese"
	#成人判定（21歳以上を成人として扱う)
	def isAdult(self):
		return True if self.age >= 18 else False
	#選挙権判定（21で選挙権を得る）
	def isVote(self):
		return True if self.age >= 18 else False
	def getName(self):
		fullname = "{0} {1}".format( self.lastname, self.firstname)
		return fullname
#
class American(Person):
	NATIONALITY="American"
	STATE="General"
	def __init__(self, firstname, middlename, lastname, age, gender):
		super().__init__(firstname, lastname, age, gender)
		#middlename
		self.middlename = middlename
	def setName(self, firstname, middlename, lastname):
		self.fistname=firstname
		self.middlename=middlename
		self.lastname=lastname
	def getName(self):
		fullname = "{0} {1} {2}".format( self.firstname, self.middlename, self.lastname)
		return fullname	

#
class Japanese(Person):
	NATIONALITY="日本"
	def getName(self):
		fullname = "{0} {1}".format( self.lastname, self.firstname)
		return fullname

	def isAdult(self):
		date1=datetime.datetime(2022, 4, 1)
		if currentdate >= date1:
			return	True if self.age >= 18 else False
		
		elif currentdate < date1:
			return True if self.age >= 20 else False

	def saySelfIntroduction(self):
		str1 = "私の名前は {0}。".format(self.getName())
		str2 = "私は{0}才です。".format(self.getAge())
		str3 = "私の国籍は{0}です。".format(self.NATIONALITY)
		if self.isAdult():
			str4 = "私は成人です。"
		else: 
			str4 = "私は成人ではありません。"
		if self.isVote():
			str5 = "私は選挙権があります。"
		else: 
			str5 = "私は選挙権がありません。"
		
		print(str1, str2, str4, str5, str3, sep='\n')
	
#############################################


bao=Vietnamese("Bao", "Nguyen Duong Gia", 25, "M")
bao.saySelfIntroduction()
print("---")

bao=American("Bao", "D.G", "Nguyen", 25, "M")
bao.saySelfIntroduction()	
print("---")


bao=Japanese("ズオン ギア バオ", "グエン", 25,"M")
bao.saySelfIntroduction()
print("---")
