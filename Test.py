import os

print("this  a test")
import requests

import Document

class people:
     age = 0
     name = ''
     _weight = 0 #私有属性
     def __init__(self,n,a,w):
         self.age = a
         self.name = n
         self._weight = w
     def speak(seif):
         print("%s say me %d year old." %(seif.name,seif.age))
#继承
class studeent(people):
    grade = 0
    def __init__(self,n,a,w,g):
        people.__init__(self, n, a, w)
        self.grade = g
    def speak(seif):
        print("%s say me %d year old.and my Grade is %d" % (seif.name, seif.age, seif.grade))


p = studeent("jack", 28, 56, 10)
p.speak()
Document.documentOperation("1.txt")


# s = input("\n\n按下 enter 键后退出。")
# temp = requests.get("http://2021lqy.free.svipss.top/")
# print(temp.status_code)
# print(temp.text)
# input1 = input("\n\n按下 enter 键后退出。")
