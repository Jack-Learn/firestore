# 引用必要套件
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os
import collections


def time_sort(time):
    print('ok')
    i=0
    for x in time:
        i=i+1

    for j in range(i):
        k=j
        for k in range(i-1):
            time1 = time[k]
            time2 = time[k+1]
            sum1= int(time1[0:2])*3600 + int(time1[3:5])*60 + int(time1[6:time1.find('秒')])
            sum2= int(time2[0:2])*3600 + int(time2[3:5])*60 + int(time2[6:time2.find('秒')])
            print('(',sum1,sum2,')\n')
            if sum2 < sum1:
                temp = time[k]
                time[k] = time[k+1]
                time[k+1] = temp

    return time
                    
#firestore
# 引用私密金鑰
cred = credentials.Certificate('chatbot-106318130-firebase-adminsdk-em6qj-75ef67d950.json')

# 初始化firebase，注意不能重複初始化
try:
    firebase_admin.initialize_app(cred)
except:
    print("重複初始化")
    
# 初始化firestore
db = firestore.client()

#從資料夾中讀取txt檔
foldPath = './data'
allFileList = os.listdir(foldPath)

#i計算讀了幾筆資料

for filename in allFileList:
    filepath = os.path.join(foldPath,filename)
    file = open(filepath,encoding="utf-8",mode='r')

    #將txt逐行存入test中
    text = []
    for line in file:
        text.append(line)    

    file.close()

    #將標籤和數值存入doc中
    doc={}
    for data in text:
        pos = data.find(':')
        label =data[:pos]
        value = data[pos+1:]
        doc[label]=value
        #print(label,':',value)   
    # 建立文件 必須給定 集合名稱 文件id
    # 語法:doc_ref = db.collection("集合名稱").document("文件id")
    doc_mame = filename[:-4]
    #print(doc_mame)
    doc_ref = db.collection("data").document(doc_mame)
    doc_ref.set(doc)
    

#查詢資料
data = ''
docs = collections.OrderedDict()
doc_ref = db.collection("data").document("2020-10-22")
docs = doc_ref.get()
docs = docs.to_dict()
time=[]
for key, value in docs.items():
    #print(key)
    data = data  + '\n' + key + ':' + value[:-1]
    time.append(key)
print(data)
time_sort(time)



    

