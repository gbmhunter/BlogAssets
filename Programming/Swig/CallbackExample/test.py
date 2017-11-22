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
example1.GiveCallback(callback)
example1.CallCallback()