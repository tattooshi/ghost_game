import pyxel
import random
move = [0,0,1,1,2,2,3,3,2,2,1,1,-1,-1,-2,-2,-3,-3,-2,-2,-1,-1]
class App:
    def __init__(self):     
        # 画面の大きさ
        pyxel.init(200, 200, "幽霊退治",fps=24) # fps は画面が切り替わる頻度        # 初期画面を         
        
        #音楽
        self.music_flug =False        

        # マウスを使えるようにする
        pyxel.mouse(True)
        
        # リソースファイルの読み込み
        pyxel.load("chiko_game.pyxres")
                      
        # もぐらの座標
        self.mogura1_x, self.mogura1_y = 300, 300    # もぐら1 の座標
        self.mogura2_x, self.mogura2_y = 300, 300    # もぐら2 の座標
        self.mogura3_x, self.mogura3_y = 300, 300    # もぐら3 の座標
        self.hito_x, self.hito_y = 300, 300    # 人間の座標
        
        # 人魂1の値（変数を定義)
        self.bx = 100   # x 座標用
        self.by = 100   # y 座標用
        self.vx = 1   # x スピード用
        self.vy = 0.5   # y スピード用
        
        # 人魂2の値（変数を定義)
        self.cx = 150   # x 座標用
        self.cy = 50   # y 座標用
        self.wx = -0.4   # x スピード用
        self.wy = -0.6   # y スピード用
        
        # 時間のカウント
        self.time = 0   # 時間のカウント
        
        # ヒットの座標
        self.hitt_x, self.hitt_y = 300, 300    # ヒット の座標
        
        # スコア表示
        self.score = 0
        
        pyxel.run(self.update, self.draw)

    def update(self):
         # Q ボタンで終了
        if pyxel.btnp(pyxel.KEY_Q): # Qキーで終了
            pyxel.quit()
        
        if self.music_flug == False:
            pyxel.playm(0,loop=True)
            self.music_flug=True
        
        # もぐらヒットの座標
        self.hitt1_x, self.hitt1_y = 300, 300    # ヒットもぐら1 の座標
        self.hitt2_x, self.hitt2_y = 300, 300    # ヒットもぐら2 の座標
        self.hitt3_x, self.hitt3_y = 300, 300    # ヒットもぐら3 の座標 
        self.hitt4_x, self.hitt4_y = 300, 300    # ヒット死神 の座標  
        
        self.time += 1   # もぐら１の時間
        
            
        if self.time % 60 == 30:
            self.mogura1_x, self.mogura1_y = random.randint(20, 180), random.randint(20, 180)    # もぐら1 の座標
        if self.time % 70 == 35:
            self.mogura2_x, self.mogura2_y = random.randint(20, 180), random.randint(20, 180)    # もぐら2 の座標
        if self.time % 80 == 40:
            self.mogura3_x, self.mogura3_y = random.randint(20, 180), random.randint(20, 180)    # もぐら3 の座標
        if self.time % 120 == 40:
            self.hito_x, self.hito_y = random.randint(20, 180), random.randint(20, 180)    # 人 の座標        
        if self.time % 60 == 0:
            self.mogura1_x, self.mogura1_y = 300, 300    # もぐら1 の座標
        if self.time % 70 == 0:
            self.mogura2_x, self.mogura2_y = 300, 300    # もぐら2 の座標
        if self.time % 80 == 0:
            self.mogura3_x, self.mogura3_y = 300, 300    # もぐら3 の座標
        if self.time % 120 == 0:
            self.hito_x, self.hito_y = 300, 300    # 死神の座標
            
        
            
        # マウスをクリックしたときの座標
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            mx = pyxel.mouse_x
            my = pyxel.mouse_y            
            dist1 = ((self.mogura1_x - mx)**2 + (self.mogura1_y - my)**2)**0.5
            dist2 = ((self.mogura2_x - mx)**2 + (self.mogura2_y - my)**2)**0.5
            dist3 = ((self.mogura3_x - mx)**2 + (self.mogura3_y - my)**2)**0.5
            dist4 = ((self.hito_x - mx)**2 + (self.hito_y - my)**2)**0.5
            
            if dist3 <= 10:
                self.hitt3_x, self.hitt3_y = self.mogura3_x, self.mogura3_y    # ヒット の座標
                self.mogura3_x, self.mogura3_y = 300, 300 
                self.score += 30
            elif dist2 <= 15:
                self.hitt2_x, self.hitt2_y = self.mogura2_x, self.mogura2_y    # ヒット の座標
                self.mogura2_x, self.mogura2_y = 300, 300 
                self.score += 25
            elif dist1 <= 20:
                self.hitt1_x, self.hitt1_y = self.mogura1_x, self.mogura1_y    # ヒット の座標
                self.mogura1_x, self.mogura1_y = 300, 300
                self.score += 20
            else:
                self.score -= 5
                #死神のヒット時
            if dist4 <= 20:
                self.hitt4_x, self.hitt4_y = self.hito_x, self.hito_y    # ヒット の座標
                self.hito_x, self.hito_y = 300, 300
                self.score -= 100      

        # 人魂1の動くスピード
        if self.bx >= 193:
            self.vx *= -1
        
        if self.bx <= 7:
            self.vx *= -1
        
        if self.by >= 190:
            self.vy *= -1
        
        if self.by <= 10:
            self.vy *= -1
        
        self.bx += self.vx
        self.by += self.vy
        
        # 人魂2の動くスピード
        if self.cx >= 193:
            self.wx *= -1
        
        if self.cx <= 7:
            self.wx *= -1
        
        if self.cy >= 190:
            self.wy *= -1
        
        if self.cy <= 10:
            self.wy *= -1
        
        self.cx += self.wx
        self.cy += self.wy
                            
                        
    def draw(self):
                
        # pyxel edit chiko_game.pyxres        
        # 画面の色
        pyxel.cls(0)           
        pyxel.blt(-3,105,0,48,152,203,90,0)
        pyxel.blt(20,80,0,64,3,15,9,0)
        pyxel.blt(100,60,0,64,3,15,9,0)
        pyxel.blt(160,70,0,64,3,15,9,0)
        
        # 人魂1を描く
        pyxel.blt(self.bx-7,self.by-10,0,82,25,12,20,0)
        # 人魂2を描く
        pyxel.blt(self.cx-7,self.cy-10,0,82,25,12,20,0)
        
        # 時間で終了
        if self.time >= 1000:
            pyxel.rect(0,0,200,200,2)
            pyxel.text(80,60, "TIME UP", 10)   # (始点座標 x, 始点座標 y, 文字（アルファベット限定）, 色)
            pyxel.text(80,80, f"SCORE : {self.score}", 10)   # (始点座標 x, 始点座標 y, 文字（アルファベット限定）, 色)
            if self.score >= 800:
                pyxel.text(70,130, "You are genius", 10)
                pyxel.blt(150+move[self.time%20],130+move[self.time%20], 0,35,40,25,20,0)   # 大きな幽霊
            elif self.score >= 550:
                pyxel.text(65,130, "You are not bad", 10) 
                pyxel.blt(150+move[self.time%20],130,0,6,18,20,11,0)     # ネコ 
            else:
                pyxel.text(50,130, "You are not good enough", 10) 
                pyxel.blt(150+move[self.time%20], 130,1 ,63, 14, 43, 50, 0)  # 死神
                
        else:    
            # goastを描く
            pyxel.blt(self.mogura1_x-7, self.mogura1_y-7+move[self.time%20], 0,40,96,15,15,0)    # 小さな幽霊 
            pyxel.blt(self.mogura2_x-12+move[self.time%20], self.mogura2_y-10+move[self.time%20], 0,35,40,25,20,0)  # 大きな幽霊  
            pyxel.blt(self.mogura3_x-9+move[self.time%20], self.mogura3_y-10,0,6,18,20,11,0)     # ネコ
            # 死神を描く
            pyxel.blt(self.hito_x-21, self.hito_y-25+move[self.time%20], 1 ,8, 14, 43, 50, 0)
            
            # ヒットしたときを描く            
            pyxel.blt(self.hitt1_x-7, self.hitt1_y-7,0,40,112,15,15,0)   # 小さな幽霊
            pyxel.blt(self.hitt2_x-12, self.hitt2_y-10,0,35,64,25,20,0)  # 大きな幽霊            
            pyxel.blt(self.hitt3_x-9, self.hitt3_y-10,0,6,35,20,11,0)    # ネコ
            pyxel.blt(self.hitt4_x-21, self.hitt4_y-25,1 ,63, 14, 43, 50, ) # 死神
            
            
            
            
            # イメージの描画：(x, y, img, u, v, w, h, [colkey])
            # xy:コピー先の座標、img:イメージバンクの番号
            # uv:コピー元の座標、wh:コピー範囲、colkey:透明色
            
            
            # 点数を表示
            pyxel.text(10, 10, f" SCORE::{self.score} 点", 10)     # (始点座標 x, 始点座標 y, 文字（アルファベット限定）, 色)

App()