image_resources = "Images\sprites"

class sprites(pygame.sprite.Sprite):
	"""docstring for sprites"pygame.sprite.Spritef __init__(self, arg):
		super(sprites,pygame.sprite.Sprite.__init__()"""
	def __init__(self,name1):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(name1)
		self.rect = self.image.get_rect()

