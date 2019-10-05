class InputHandler:
    def __init__(self):
        self.bindings = {}

    def bind(self, key, callback):
        self.bindings[key] = callback

    def unbind(self, key):
        del self.bindings[key]

    def handle(self, key):
        if key in self.bindings:
            self.bindings[key]()