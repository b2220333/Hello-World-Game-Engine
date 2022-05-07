# 建立世界
class World:
  name = ''
world = World()
world.name = 'World'

# 建立人物
class Person:
  #人物有名字（1/2）
  name=''
  #人物會說話（1/2）
  message = ''
  ######人物在世界中有位置資訊（1/2）######
  x = None
  y = None
  z = None
  position = (x, y, z)
  ######人物在世界中有位置資訊（1/2）######

sam = Person()
#人物有名字（2/2）
sam.name = 'sam lin'

######人物在世界中有位置資訊（2/2）######
# 假設sam在世界正中央
sam.position = (0, 0, 0)
print(sam.position)
######人物在世界中有位置資訊（2/2）######

#人物會說話（2/2）
# sam說：Hello World
sam.message = sam.name + ':' + 'Hello ' + world.name
