# -*- coding: utf-8 -*-
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# 引用私密金鑰
cred = credentials.Certificate('chatbot-106318130-firebase-adminsdk-em6qj-75ef67d950.json')

# 初始化firebase，注意不能重複初始化
#firebase_admin.initialize_app(cred)

# 初始化firestore
db = firestore.client()

# 建立文件 必須給定 集合名稱 文件id
# 語法:doc_ref = db.collection("集合名稱").document("文件id")
doc = {}
doc['count'] = '10'

doc_ref = db.collection('test').document('檔名')
doc_ref.set(doc)


