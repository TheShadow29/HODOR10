image_resources = "Images\sprites"

class sprites(pygame.sprite.Sprite):
	"""docstring for sprites"pygame.sprite.Spritef __init__(self, arg):
		super(sprites,pygame.sprite.Sprite.__init__()"""
	def __init__(self,x1,y1,name1):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(name1)
		self.rect = self.image.get_rect()
		self.rect.left = x1
		self.rect.bottom = y1

