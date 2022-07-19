import sys
import time
import random
import pygame
from pygame.locals import *
 
SURFACE  = Rect(0, 0, 1200, 600) 
R_H_SIZE = 120             
R_W_SIZE = 120               
R_B_POS  = 30                   
B_SIZE   = 95                
F_RATE   = 60                  
K_REPEAT = 30                  
R_SPEED  = 10                   
B_SPEED  = 8                 
F_SIZE   = 60                  
S_TIME   = 2     



# ラケットクラス

class Racket(pygame.sprite.Sprite):
 

    # 初期化メソッド

    def __init__(self, name):
        pygame.sprite.Sprite.__init__(self)
 
        # ファイル読み込み
        self.image = pygame.image.load(name).convert()
        
 
        # 画像サイズ変更
        self.image = pygame.transform.scale(self.image, (R_W_SIZE, R_H_SIZE))
 
        # ラケットオブジェクト生成
        self.rect = self.image.get_rect()
 
    
    # ラケット更
    def update(self, racket_pos):
 
        # ラケット位置
        self.rect.centerx = racket_pos
        self.rect.centery = SURFACE.bottom - R_B_POS
 
        # 画面内に収める
        self.rect.clamp_ip(SURFACE)
        
 
    # ラケット描画
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)
 

# ボールクラス

class Ball(pygame.sprite.Sprite):
 

    # 初期化メソッド
    def __init__(self, name, racket):
        pygame.sprite.Sprite.__init__(self)
 
        # ファイル読み込み
        self.image = pygame.image.load(name).convert_alpha()
 
        # 画像サイズ変更
        self.image = pygame.transform.scale(self.image, (B_SIZE, B_SIZE))
 
        # ボールオブジェクト生成
        self.rect = self.image.get_rect()
 
        self.sp_x = 0              
        self.sp_y = 0            
        self.racket = racket      
        self.update = self.setup   
 
    
     #ゲーム初期状態
    
    def setup(self, surface):
        
        # ボールの初期位置
        self.sp_x = B_SPEED / 2
        self.sp_y = B_SPEED
        self.update = self.move
 
    
    # ボールの挙動
    
    def move(self, surface):
        self.rect.centerx += int(self.sp_x)
        self.rect.centery += int(self.sp_y)
 
     #左壁の反射
        if self.rect.left  < SURFACE.left:
            self.rect.left  = SURFACE.left
            self.sp_x = -self.sp_x
        # 右壁の反射
        if self.rect.right > SURFACE.right:
            self.rect.right = SURFACE.right
            self.sp_x = -self.sp_x
        # 上壁の反射
        if self.rect.top   < SURFACE.top:
            self.rect.top   = SURFACE.top
            self.sp_y = -self.sp_y
 
        # ラケットとボールの接触判定
        if self.rect.colliderect(self.racket.rect):
 
            # 接触位置取得
            dist = self.rect.centerx - self.racket.rect.centerx
 
            # X軸移動距離設定
            if   dist < 0:
                self.sp_x = -B_SPEED * (1 + dist / R_W_SIZE/2)
            elif dist > 0:
                self.sp_x =  B_SPEED * (1 - dist / R_W_SIZE/2)
            else:
                self.sp_x = random.randint(-5, 5)
 
	        # Y軸移動
            self.sp_y = -B_SPEED
 
        # ボールを落とした場合
        if self.rect.bottom > SURFACE.bottom:
 
            #  失敗時の文字を表示
            font = pygame.font.Font(None, F_SIZE)
            text = font.render("You Loss", True, (0,0,255))
            surface.blit(text, [520,150])
 

    # ボール描画
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)
 

# メイン関数 

def main():
    


    
       

 
    ### 画面初期化
    pygame.init()
    surface = pygame.display.set_mode(SURFACE.size)
    
    bg=pygame.image.load("fig/bg.png")
    
 
    # スプライトを作成
    racket = Racket("fig/star-removebg-preview.png")
    ball   = Ball("fig/images__1_-removebg-preview.png", racket)
 
    # 時間オブジェクト生成
    clock = pygame.time.Clock()
 
    # ラケット初期位置
    racket_pos = int(SURFACE.width / 2)
 
    # キーリピート有効
    pygame.key.set_repeat(K_REPEAT)
 
    # STARTを表示
    font = pygame.font.Font(None, F_SIZE)
    text = font.render("START", True, (0,0,255))
    surface.fill((0,0,0))
    surface.blit(text, [520,150])
    pygame.display.update()
 
    # 一時停止
    time.sleep(S_TIME)
 
    # 無限ループ
    while True:
 
        # フレームレート設定
        clock.tick(F_RATE)
 
        # 背景色設定
        surface.fill((0,0,0))
        surface.blit(bg,(0,0))
 
        # スプライトを更新
        racket.update(racket_pos)
        ball.update(surface)
 
        # スプライトを描画
        racket.draw(surface)
        ball.draw(surface)
 
        # 画面更新
        pygame.display.update()
 
        # イベント処理
        for event in pygame.event.get():
 
            #終了処理
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exit()
 
                ### キー操作
                if event.key == K_LEFT:
                    racket_pos -= R_SPEED
                if event.key == K_RIGHT:
                    racket_pos += R_SPEED
 
# 終了関数

def exit():
    pygame.quit()
    sys.exit()
# メイン関数呼び出し

if __name__ == "__main__":
 
    # 処理開始
   
    

    main()