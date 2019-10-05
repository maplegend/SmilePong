class Scene:
    def __init__(self, bounds, screen):
        self.bounds = bounds
        self.screen = screen
        self.sprites = []
        self.handlers = []

    def add_sprite(self, sprite):
        self.add_handler(sprite)
        self.sprites.append(sprite)

    def get_sprites(self):
        return self.sprites

    def delete_sprite(self, sprite):
        self.handlers.remove(sprite)
        self.sprites.remove(sprite)

    def add_handler(self, handler):
        handler.scene = self
        self.handlers.append(handler)

    def get_handlers(self):
        return self.handlers

    def delete_handler(self, handler):
        self.handlers.remove(handler)