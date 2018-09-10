import example

class Callback(example.ICallback):
    def __init__(self, fnToCall):
        example.ICallback.__init__(self)
        self.fnToCall = fnToCall
    def Call(self):
        self.fnToCall()        

def TestFunction():
    print('Hello from a callback!')

callback = Callback(TestFunction)

example1 = example.Example()
print('Giving python callback class to C++...')
example1.GiveCallback(callback)
print('Calling python callback from python through C++..')
example1.CallCallback()