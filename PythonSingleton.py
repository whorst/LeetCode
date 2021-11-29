import threading
class Instance:
    instance = None
    lock = threading.Lock()
    def __init__(self):
        if self.instance != None:
            raise RuntimeError("An Instance Exists!")

    @staticmethod
    def getInstance():
        if Instance.instance == None:
            with Instance.lock:
                if Instance.instance == None:
                    Instance.instance = Instance()
                return Instance.instance
        # else:
        #     raise RuntimeError("An Instance Exists!")
        return Instance.instance

x = Instance()
print(x.getInstance())
print(x.getInstance())
print(x.getInstance())
# print(x.getInstance
# y = Instance()
# print(y)