# -*- coding: utf-8 -*-
# @Time     :   2020/3/18 21:55
# @Author   :   Payne
# @File     :   3-18-mongo.py
# @Software :   PyCharm

import pymongo

'''
MongoDB 是由C++语言编写的非关系型数据库。基于分布式文件存储的开源数据库系统，
内容以 ‘ 类字典’的JSON对象
它的字段值阔以包含其他文档，数据及文档数组
'''
# 连接
client = pymongo.MongoClient(host='localhost', port=27017)
# client = pymongo.MongoClient('mongodb://localhost:27017/')
# 指定数据库 test  库名 student 表名 没有则自动创建
db = client.test
# db = client['test']

collection = db.students

student = {
    'id': '201890782',
    'name': 'Payne',
    'age': 20,
    'gender': 'male'
}

# 插入单个数据
'''
result = collection.insert_one(student)
print(result)
print(result.inserted_id)
'''

# 插入多个数据 以列表形式传递
'''
student1 = {
    'id' : '201890722',
    'name' : 'one',
    'age' : 22,
    'gender' : 'male'
}
student2 = {
    'id' : '201890724',
    'name' : 'Two',
    'age' : 23,
    'gender' : 'male'
}
result = collection.insert_many([student1,student2])
print(result)
print(result.inserted_ids)
'''

# 数据库操作 find返回的为生成器对象
'''查找'''
'''
result = collection.find_one({'name':'one'})
print(result)
print(type(result))

from bson.objectid import ObjectId
result = collection.find_one({'_id': ObjectId('5e722ee37b314673187b34a5')})
print(result)
print(type(result))
'''

'''多条件查找'''
'''
results = collection.find({'age':{'$gt':20}})
for result in results:
    print(result)
    print(type(result))
'''

'''计数'''
'''
count = collection.find(条件).count()
print(count)
'''

'''排序 与 偏移(skip)'''
'''
results = collection.find().sort('name', pymongo.ASCENDING)
results = collection.find().sort('name', pymongo.DESCENDING)
# print([result['name'] for result in results])
'''

'''
results = collection.find().sort('name', pymongo.ASCENDING).skip(1).limit(1)
# results = collection.find().sort('name', pymongo.DESCENDING)
print([result['name'] for result in results])
'''
'''更新(改)update'''
'''单一条件'''
'''
data = {'name' : 'one'}
students = collection.find_one(data)
print(students)
students['age'] = 27
# result = collection.update(data,students)
result = collection.update_one(data,{'$set': students})
print(result)
'''

'''
data = {'name' : 'one'}
students = collection.find_one(data)
print(students)
students['age'] = 27
# result = collection.update(data,students)
result = collection.update_one(data,{'$set': students})
print(result.matched_count,result.modified_count)
'''

'''
cond = {'age' : {'$inc': 20}}
result = collection.update_many(cond, {'$inc': {'age': 1}})
print(result)
print(result.matched_count,result.modified_count)
'''

'删除'
# result = collection.remove_one({'name':'one'})
# print(result)

'''批量删除'''
result = collection.delete_one({'name': 'Payne'})
print(result)
