import pygame as pg
import sys
import random
import tkinter as Tk
import tkinter.messagebox as tkm



    


class Screen:
  def __init__(self, fn, wh, title):
   
    pg.display.set_caption(title)
    self.width, self.height = wh                   #(1000, 900)
    self.disp = pg.display.set_mode((self.width, self.height))   #Surface
    self.rect = self.disp.get_rect()               #Rect
    self.image = pg.image.load(fn)                 #Surface


class Bird(pg.sprite.Sprite):
  key_delta = {pg.K_UP  : [0, -1],
              pg.K_DOWN : [0, +1],
              pg.K_LEFT : [-1, 0],
              pg.K_RIGHT: [+1, 0],
              }

  def __init__(self, fn, r, xy):
    #fn: 画像のパス, r:拡大率, xy:初期配置座標のタプル
    super().__init__()
    self.image = pg.image.load(fn)                 #Surface
    self.image = pg.transform.rotozoom(self.image, 0, r)
    self.rect= self.image.get_rect()               #Rect
    self.rect.center = xy

  def update(self, screen):
    key_states = pg.key.get_pressed()
    for key, delta in Bird.key_delta.items():
      if key_states[key]:
        print(self.rect.center)
        self.rect.centerx += delta[0]
        self.rect.centery += delta[1]
        print(self.rect.center)
          # 練習7
        if check_bound(screen.rect, self.rect) != (1,1): 
          self.rect.centerx -= delta[0]
          self.rect.centery -= delta[1]

class Teki(pg.sprite.Sprite):
 def __init__(self, fn, r, ab, screen):
   super().__init__()
   self.image = pg.image.load(fn)                 #敵のSurface
   self.image = pg.transform.rotozoom(self.image, 0, r)
   self.rect= self.image.get_rect()               #敵のRect
   self.rect.centerx = random.randint(0, screen.rect.width)
   self.rect.centery = random.randint(0, screen.rect.height)
   screen.disp.blit(self.image, self.rect)                   # 敵用のSurfaceを画面用Surfaceに貼り付ける
   self.vx, self.vy = ab

 def update(self, screen):
   self.rect.move_ip(self.vx, self.vy)
   a, b = check_bound(screen.rect, self.rect)
   self.vx *= a 
   self.vy *= b 



class Bomb(pg.sprite.Sprite):
  def __init__(self, color, r, vxy, screen):
    #color: 爆弾の色, r:爆弾円の半径 vxy:爆弾円の速度タプル, screen:
    super().__init__()
    self.image = pg.Surface((2*r,2*r))                     # 爆弾用のSurface
    self.image.set_colorkey((0,0,0))                     # 黒色部分を透過する
    pg.draw.circle(self.image, color, (r,r), r)   # 爆弾用Surfaceに円を描く
    self.rect = self.image.get_rect()                    # 爆弾用Rect
    self.rect.centerx = random.randint(0, screen.rect.width)
    self.rect.centery = random.randint(0, screen.rect.height)
    screen.disp.blit(self.image, self.rect)                   # 爆弾用のSurfaceを画面用Surfaceに貼り付ける
    self.vx, self.vy = vxy

  def update(self, screen):
    self.rect.move_ip(self.vx, self.vy)
    x, y = check_bound(screen.rect, self.rect)
    self.vx *= x*1 
    self.vy *= y*1 


def main():
    root=Tk.Tk()
    root.withdraw()
    clock = pg.time.Clock()
    
    # 練習1
    screen = Screen('fig/pg_bg.jpg', (1600, 900), ('逃げろ！こうかとん') )  #コンストラクタを呼び出す
    screen.disp.blit(screen.image, (0,0))     

    # 練習3
    tori = pg.sprite.Group()
    # tori = Bird("fig/3.png", 2, (900, 400))
    # screen.disp.blit(tori.image, tori.rect)               # こうかとん画像用のSurfaceを画面用Surfaceに貼り付ける
    tori.add(Bird("fig/3.png", 2, (900, 400)))
    tori.draw(screen.disp)

    teki = pg.sprite.Group()
    teki.add(Teki("fig/images.jfif", 1, (+5, +5),screen))
    teki.draw(screen.disp)

    # 練習5
    bomb = Bomb((0,0,0), 10, (+5, +5), screen)
    screen.disp.blit(bomb.image, bomb.rect)               # 爆弾用のSurfaceを画面用Surfaceに貼り付ける
    bombs = pg.sprite.Group()
    for _ in range(5):
      bombs.add(Bomb((255,0,255), random.randint(1,50), (+2, +2), screen))
    bombs.draw(screen.disp)

    while True:
        # 練習2
        screen.disp.blit(screen.image, (0,0))
        for event in pg.event.get():
            if event.type == pg.QUIT: return       # ✕ボタンでmain関数から戻る

        # 練習4
        tori.update(screen)
        # screen.disp.blit(tori.image, tori.rect)
        tori.draw(screen.disp)

        teki.update(screen)
        teki.draw(screen.disp)

        # 練習6
        bombs.update(screen)
        #screen.disp.blit(bomb.image, bomb.rect)
        bombs.draw(screen.disp)

        # 練習8 
        if len(pg.sprite.groupcollide(tori, bombs, False, False))  != 0: return    
        #if pg.sprite.collide_rect(tori, bomb): return
        #collide_rect(Sprite, Sprite)
        if len(pg.sprite.groupcollide(tori, teki, False, False))  != 0: return
        # こうかとん用のRectが爆弾用のRectと衝突していたらreturn

          #練習8
       
        pg.display.update()  # 画面の更新
        clock.tick(1000) 
    
# 練習7
def check_bound(sc_r, obj_r): # 画面用Rect, ｛こうかとん，爆弾｝Rect
    # 画面内：+1 / 画面外：-1
    x, y = +1, +1
    if obj_r.left < sc_r.left or sc_r.right  < obj_r.right : x = -1
    if obj_r.top  < sc_r.top  or sc_r.bottom < obj_r.bottom: y = -1
    return x, y


if __name__ == "__main__":
    pg.init() 
    main()
    pg.quit()
    sys.exit()