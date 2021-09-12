import pygame
import random

#add collision detection
#add typing to delete weapons (or just reopen issue later and revisit later)
#reset variables on death
#change variables, stop invading namespaces? (stop using globals)

class Player(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    walk_1 = pygame.transform.scale(pygame.image.load('assets/art/emiyasprite.png').convert_alpha(), (30, 45))
    walk_2 = pygame.transform.scale(pygame.image.load('assets/art/emiyasprite.png').convert_alpha(), (30, 45))
    self.slide_l = pygame.transform.scale(pygame.image.load('assets/art/emiyasprite.png').convert_alpha(), (30, 45))
    self.slide_r  = pygame.transform.scale(pygame.image.load('assets/art/emiyasprite.png').convert_alpha(), (30, 45))
    self.walk = [walk_1, walk_2]
    self.index = 0
    
    self.image = self.walk[self.index]
    self.rect = self.image.get_rect(center = (width/2, height-100))
    self.pull = 0
    self.doublejump = False

    self.blades = 0
    self.currency = 0
    self.score = 0

  def reset(self):
    self.rect = self.image.get_rect(center = (width/2, height-100))
    self.pull = 0
    self.doublejump = False

    self.blades = 0
    self.currency = 0
    self.score = 0

  def left(self):
    if self.rect.centerx == width/2:
      self.pull = -25
    elif not self.doublejump:
      jumpamount = -20-self.pull
      if jumpamount > -5:
        jumpamount = -5
      elif jumpamount < -25:
        if self.rect.centerx > width/2:
          jumpamount -= self.pull
        elif self.pull > 0 and self.pull/3 > -25:
          jumpamount -= int(self.pull/3)
        else:
          jumpamount = -20
      self.pull += jumpamount
      self.doublejump = True

  def right(self):
    if self.rect.centerx == width/2:
      self.pull = 25
    elif not self.doublejump:
      jumpamount = 20-self.pull
      if jumpamount < 5:
        jumpamount = 5
      elif jumpamount > 25:
        if self.rect.centerx < width/2 :
          jumpamount -= self.pull
        elif self.pull < 0 and self.pull/3 < 25:
          jumpamount -= int(self.pull/3)
        else:
          jumpamount = 20
      self.pull += jumpamount
      self.doublejump = True

  def apply_move(self):
    if self.rect.centerx > width/2 and self.pull > -30: self.pull -= 1
    elif self.rect.centerx < width/2 and self.pull < 30: self.pull += 1

    self.rect.centerx += self.pull
    if self.rect.centerx <= (width/2+abs(self.pull)-1) and self.rect.centerx >= (width/2-abs(self.pull)+1):
      self.pull = 0
      self.rect.centerx = width/2
      self.doublejump = False

  def player_animation(self):
    if self.pull > 0:
      self.image = self.slide_r
    elif self.pull < 0:
      self.image = self.slide_l
    else:
      self.index += 0.1
      if self.index >= len(self.walk): self.index = 0
      self.image = self.walk[int(self.index)]

  def update(self):
    self.apply_move()
    self.player_animation()

#pause on spawn
#separate class for corresponding character? or just add to list like normal and then draw/blit those
class Obstacle(pygame.sprite.Sprite):
  def __init__(self, type):
    super().__init__()

    if type == 'axe':
      axe_1 = pygame.transform.scale(pygame.image.load('assets/art/weapons/axe.png'), (50, 50)).convert_alpha()
      axe_2 = pygame.transform.scale(pygame.image.load('assets/art/weapons/axe.png'), (50, 50)).convert_alpha()
      self.frames = [axe_1, axe_2]

    self.animation_index = 0
    self.image = self.frames[self.animation_index]
    self.rect = self.image.get_rect(midtop = (random.randint(0, width), 0))
    self.shifted = False
    
    """alphabet_keys = [pygame.key.key_code(letter) for letter in "abcdefghijklmnopqrstuvwxyz"]
    self.character = chr(random.choice(alphabet_keys)).upper()
    self.character_img = test_font.render(self.character, False, (64, 64, 64))
    self.character_rect = self.character_img.get_rect(bottomright = (self.rect.x, self.rect.y))"""

  def animation_state(self):
    self.animation_index += 0.1
    if self.animation_index >= len(self.frames): self.animation_index = 0
    self.image = self.frames[int(self.animation_index)]
  
  def movement(self, player):
    self.rect.y += 3 + int(level/2)
    if self.rect.y < height-100:
      if not self.shifted:
        if (player.sprite.rect.centerx-2-(level/2)) > self.rect.centerx:
          self.rect.x += 2
          self.rect.x += int(level/2)
        elif (player.sprite.rect.centerx+2+(level/2)) < self.rect.centerx:
          self.rect.x -= 2
          self.rect.x -= int(level/2)
    else:
      self.rect.y += 2
      if self.rect.y >= height:
        increment()
        self.kill()
        
    """screen.blit(self.character_img, self.character_rect)
    pygame.draw.rect(screen, "#c0e8ec", self.character_rect)
    pygame.draw.rect(screen, "#c0e8ec", self.character_rect, 7)
    self.shifted = not self.shifted"""

  def update(self):
    self.animation_state()
    self.movement(player)

#display level + score
def display_stats():
  global level, counted, timed

  timed = int(pygame.time.get_ticks()/1000) - start_time
  if timed % 15 == 0 and timed != counted:
    level += 1
    counted = timed
  
  time_surf = test_font.render(f"Time in Seconds: {timed}", False, (64, 64, 64))
  time_rect = time_surf.get_rect(bottomleft = (0, height))
  score_surf = test_font.render(f"Score: {player.sprite.score}", False, (64, 64, 64))
  score_rect = score_surf.get_rect(bottomleft = (0, height-50))
  level_surf = test_font.render(f"Level: {level+1}", False, (64, 64, 64))
  level_rect = level_surf.get_rect(bottomleft = (0, height-100))

  pygame.draw.rect(screen, "#c0e8ec", time_rect)
  pygame.draw.rect(screen, "#c0e8ec", time_rect, 10)
  pygame.draw.rect(screen, "#c0e8ec", score_rect)
  pygame.draw.rect(screen, "#c0e8ec", score_rect, 10)
  pygame.draw.rect(screen, "#c0e8ec", level_rect)
  pygame.draw.rect(screen, "#c0e8ec", level_rect, 10)
  screen.blit(time_surf, time_rect)
  screen.blit(score_surf, score_rect)
  screen.blit(level_surf, level_rect)

def collision_sprite():
  if pygame.sprite.spritecollide(player.sprite, obstacles, False):
    obstacles.empty()
    return False
  return True
def increment():
  global player
  player.sprite.blades += 1
  player.sprite.score += 1 + level
  player.sprite.currency += 1 + level

pygame.init()

screen = pygame.display.set_mode() #100 px off all? toggle size?
width, height = pygame.display.get_surface().get_size()
pygame.display.set_caption("Fate Game")

clock = pygame.time.Clock()
test_font = pygame.font.Font('assets/LEMONMILK-Regular.otf', 30)

game_active = False
start_time = 0
start_ms = 0
timed = 0
level = 0
counted = 0
lastspawn = 0

background = pygame.image.load('assets/art/ubw_background_sprite.jpg').convert()
background = pygame.transform.scale(background, (width, height))

game_name = test_font.render('UBW RUN', False, (64, 64, 64))
game_rect = game_name.get_rect(center = (width/2, height/4))
game_message = test_font.render('Press space to start!', False, (64, 64, 64))
game_message_rect = game_message.get_rect(center = (width/2, 3*height/4))
player_stand = pygame.image.load('assets/art/emiyasprite.png').convert_alpha()
player_stand_rect = player_stand.get_rect(center=(width/2, height/2))

weapon_surf = pygame.transform.scale(pygame.image.load('assets/art/weapons/axe.png'), (50, 50)).convert_alpha()
weapon_list = []
obstacle_rect_list = []
obstacle_chr_list = []

player = pygame.sprite.GroupSingle()
player.add(Player())

obstacles = pygame.sprite.Group()

soundcontrol = 0.25
bgm = pygame.mixer.Sound('assets/audio/ubw_bgm.wav')
bgm.set_volume(soundcontrol)
#bgm.play(loops=-1)

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()

    if game_active:
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT or event.key == pygame.K_LSHIFT:
          player.sprite.left()
        elif event.key == pygame.K_RIGHT or event.key == pygame.K_RSHIFT:
          player.sprite.right()

        elif event.key in obstacle_chr_list:
          index = obstacle_chr_list.index(event.key)
          obstacle_chr_list.remove(event.key)
          obstacle_rect_list.remove(obstacle_rect_list[index])

    else:
      #reset variables
      if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not game_active:
        game_active = True
        #player_rect.centerx = width/2
        
        #reset variables
        
        start_time = int(pygame.time.get_ticks() / 1000)
        start_ms = pygame.time.get_ticks()
        player.sprite.reset()

        counted = 0
        lastspawn = 0
        obstacle_rect_list.clear()
        obstacle_chr_list.clear()
  
  if game_active:
    ms_timed = pygame.time.get_ticks() - start_ms
    if ms_timed - random.randint(800, 1000) + (level*20) >= lastspawn:
      obstacles.add(Obstacle('axe'))
      lastspawn = ms_timed
      #obstacle_chr_list.append(random.choice(alphabet_keys))

    screen.blit(background, (0, 0))
    
    display_stats()

    player.draw(screen)
    player.update()
    obstacles.draw(screen)
    obstacles.update()
    game_active = collision_sprite()
  else:
    #check if game is in menu or ended
    screen.blit(background, (0, 0))
    screen.blit(player_stand, player_stand_rect)
    
    score_message = test_font.render(f"You survived for {timed} seconds, dodged {player.sprite.blades} blades, and had a final score of {player.sprite.score}!", False, (64, 64, 64))
    score_message_rect = score_message.get_rect(center = (width/2, 3*height/4))
    screen.blit(game_name, game_rect)
    
    if timed == 0:
      screen.blit(game_message, game_message_rect)
    else:
      screen.blit(score_message, score_message_rect)
  pygame.display.update()
  clock.tick(60)