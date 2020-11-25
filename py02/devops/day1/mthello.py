import threading

def hello(word):
    print('Hello %s!'% word)

if __name__ == '__main__':
    for w in ['world','China','Tedu']:
        t = threading.Thread(target=hello,args=(w,))
        t.start()