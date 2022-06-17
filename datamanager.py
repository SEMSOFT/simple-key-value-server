class DataManager:
    def __init__(self):
        self.data = {}

    def append(self, key, value):
        lst = self.data.get(key)

        if lst is None:
            lst = []
        lst.append(value)

        self.data.update({key: lst})

    def get_last(self, key):
        lst = self.data.get(key)

        if lst is None:
            raise KeyError('%s not found' % key)

        return lst[-1]

    def get_history(self, key):
        lst = self.data.get(key)

        if lst is None:
            raise KeyError('%s not found' % key)

        return lst
