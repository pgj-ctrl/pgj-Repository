class Role:
    def __init__(self, name, weapon):
        # 构造器方法，实例化时自动调用，注意，self不是关键字，可以是任何合法变量名
        # 绑定在实身上的属性，可以在类中任意位置使用
        self.name = name
        self.weapon = weapon
class weapon:
    def __init__(self,name,strength,type):
        self.name = name
        self.strength = strength
        self.type = type
if __name__ == '__main__':
    ji = weapon('方天画戟',100,'物理')
    print(ji.name,ji.strength,ji.type)
    lb = Role('吕布', ji)
    print(lb.weapon.name,lb.weapon.strength,lb.weapon.type)