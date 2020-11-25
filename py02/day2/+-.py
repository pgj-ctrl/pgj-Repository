import random
# b = random.randint(1,100)
# c = random.randint(1,100)
# print(b)
# print(c)
def example():
    '出题用户作答'
    nums = [random.randint(1,100)for i in range(2)]
    nums.sort(reverse=True)
    op = random.choice('+-')
    if op == '+':
        result = nums[0] + nums[1]
    else:
        result = nums[0] - nums[1]
    for i in range(1, 4):
        prompt = '%s %s %s =' % (nums[0],op,nums[1])
        answer = int(input(prompt))
        if answer == result:
            print("不错哟～")
            print("正确答案是：\n%s%s" % (prompt, result))
            break
        else:
            print("不对哟～")

        if i == 3:
            print("正确答案是：\n%s%s" % (prompt, result))
            break


def main():
    '主代码逻辑'
    while 1:
        example()
        yn = input('Continue(y/n)').strip()[0]
        if yn in 'nN':
            print("Bye-bye")
            break
if __name__ == '__main__':
    main()