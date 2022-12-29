class SingletonDecorator:

    def __init__(self, target_class):
        self._target_class = target_class
        self._instance = None

    def __call__(self, *args, **kwds):
        if self._instance is None:
            self._instance = self._target_class(*args, **kwds)
        return self._instance
