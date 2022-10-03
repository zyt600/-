class ojbk:
    uuu = 999

    def __init__(self):
        self.ppp = 0
        self.lll = 888


uu = ojbk()
yy = ojbk()
yy.uuu = 222
print(uu.uuu)
print(yy.uuu)
print(ojbk.uuu)
