
#创建人物的类，即战士和敌人。类的实例化操作会自动调用__init__()方法
class Person:
    def __init__(self, name):
        #姓名
        self.name = name
        #血量
        self.blood = 100

    #给弹夹安装子弹
    def installBullet(self, clip, bullet):
        clip.saveBullet(bullet)

    #安装弹夹
    def installCilp(self, gun, clip):
        gun.mountingClip(clip)

    #拿枪
    def takeGun(self, gun):
        self.gun = gun

    #开火
    def fire(self, enemy):
        self.gun.shoot(enemy)

    #显示
    def __str__(self):
        return self.name + "剩余血量：" + str(self.blood)

    #掉血
    def loseBlood(self, damage):
        self.blood -= damage


#创建弹夹Clip,并且创建子弹数量和弹夹容量的属性
class Clip:
    def __init__(self, capacity):
        self.capacity = capacity
        self.currentList = []

    #安装子弹
    def saveBullet(self, bullet):
        #判断子弹是否装满
        if len(self.currentList) < self.capacity:
            self.currentList.append(bullet)

    #显示弹夹信息
    def __str__(self):
        return "弹夹当前的数" + str(len(self.currentList)) + "/" + str(self.capacity)

    #射出子弹
    def shotBullet(self):
        #判断是否有子弹
        if len(self.currentList) > 0 :
            # 子弹减1
            self.currentList.pop()
            return bullet
        else:
            return None

#创建子弹的类Bullet
class Bullet:
    def __init__(self, damage):
        self.damage = damage

    #子弹伤害的方法
    def hurt(self,enemy):
        enemy.loseBlood(self.damage)

    pass

#创造枪的类Gun
class Gun:
    def __init__(self):
        self.clip = None

    def __str__(self):
        if self.clip:
            return '枪有弹夹'
        else:
            return '枪没有弹夹'

    #子弹连接弹夹
    def mountingClip(self, clip):
        if not self.clip:
            self.clip = clip

    #射击
    def shoot(self, enemy):
        bullet = self.clip.shotBullet()
        if bullet:
            bullet.hurt(enemy)
        else:
            print("没有子弹了，放了空枪。。。。。")


if __name__ == '__main__':
    soldier = Person("小明")
    clip = Clip(20)
    i = 0
    #装子弹
    while i < 4:
        bullet = Bullet(4)
        soldier.installBullet(clip, bullet)
        i +=1
    print(clip)  #弹夹当前数量
    gun = Gun()
    print(gun)   #弹夹情况
    soldier.installCilp(gun, clip)
    print(gun)  #弹夹情况
    enemy = Person("敌人")
    print(enemy) #敌人剩余血量
    soldier.takeGun(gun)
    soldier.fire(enemy)
    print(clip) #弹夹当前数量
    print(enemy)#敌人剩余数量
    soldier.fire(enemy)
    print(clip)#弹夹当前数量
    print(enemy) #敌人剩余血量


