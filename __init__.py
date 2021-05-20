class Config(object):
	#menentukan lokasi mysql yang diambil 
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:''@localhost/pos'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
