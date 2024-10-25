class cha():
    def __init__(self, pro): #設定角色數值
        h = {"K" : 9, "T" : 12, "B" : 6}
        a = {"K" : 2, "T" : 1, "B" : 4}
        d = {"K" : 1, "T" : 2, "B" : 0}
        self.HEA = h[pro]
        self.ATK = a[pro]
        self.DEF = d[pro]
        self.pause = False
        self.last = "END" #可用此判斷第一輪為END代號的違規
        self.ERR = False

    def fight(self, ano, X): #角色行動
        if self.last == X: #處理違規
            self.HEA = 0
            self.ERR = True
            return
        elif self.pause == True:
            return
        else: #可縮可不縮, 縮了比較好
            self.last = X
            if X == "A1":
                ATK = 0 if self.ATK - ano.DEF < 0 else self.ATK - ano.DEF
                ano.HEA -= ATK
            if X == "A2":
                ATK = 0 if round(self.ATK * 1.5) - ano.DEF < 0 else round(self.ATK * 1.5) - ano.DEF
                ano.HEA -= ATK
            if X == "H":
                self.HEA += 3
            if X == "R1":
                self.ATK += 2
            if X == "R2":
                self.DEF += 1
            if X == "P":
                ano.pause = True
            if X == "M1":
                ATK = 0 if self.ATK - ano.DEF < 0 else self.ATK - ano.DEF
                ano.HEA -= ATK
                self.HEA += 1
            if X == "M2":
                ATK = 0 if self.ATK - ano.DEF < 0 else self.ATK - ano.DEF
                ano.HEA -= ATK
                self.ATK += 1
            if X == "END":
                ATK = 0 if self.ATK * 2 - ano.DEF < 0 else self.ATK * 2 - ano.DEF
                ano.HEA -= ATK
                self.ATK += 1

f = input().split()
l = input().split()
first = cha(f[0])
last = cha(l[0])
for i in range(1, len(f)): #取 f 或 i 的長度皆可, f = i
    last.pause = False #在A位角色攻擊之前可解除B位角色暫停
    if first.HEA * last.HEA <= 0:
        break
    first.fight(last, f[i])
    first.pause = False
    if first.HEA * last.HEA <= 0:
        break
    last.fight(first, l[i])

if first.ERR == True: #違規處分
    c = 1
elif last.ERR == True:
    c = 2
else:
    c = 0
if first.HEA > last.HEA: #贏局判斷
    win = 1
elif first.HEA < last.HEA:
    win = 2
else:
    win = 0
#若輸家血量為負，則改為0
first.HEA = 0 if first.HEA < 0 else first.HEA
last.HEA = 0 if last.HEA < 0 else last.HEA
print(first.HEA, last.HEA, c, win)


