#/ijp python compiled

print("hello world")

# Functions are now !fun
def saygoodbye():
    print('say goodbye')

def inafun():
    print('root of inafun')

    def anotherfun():
        print('in another inafun')
        print("!fun")

    anotherfun()

class classes_suck():
    def __init__(self, arg):
        if arg == True:
            print('Success')
        else:
            print('Fail')

inafun()
saygoodbye()
