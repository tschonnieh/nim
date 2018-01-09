class Event(object):
    def __init__(self, *args):
        self.handlers = set()
        self.args = args

    def add(self, fn):
        self.handlers.add(fn)

    def remove(self, fn):
        self.handlers.remove(fn)

    def __call__(self, *args):
        '''fire the event -- uses __call__ so we can just invoke the object directly...'''
        runtime_args = self.args + args
        for each_handler in self.handlers:
            each_handler(*runtime_args)
