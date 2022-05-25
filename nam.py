m = 15
a = [[12,12],[9,8],[8,8],[13,12],[8,7],[3,4],[9,10],[10,10],[10,9],[6,6],[12,12],[7,8]]
cum1 = []
cum2 = []
x1 = int(input("X1 = "))
y1 = int(input("Y2 = "))
x2 = int(input("X2 = "))
y2 = int(input("Y2 = "))
while True:
    cum1 = []
    cum2 = []
    kc1 = 0
    kc2 = 0
    x11 = y11 = x22 = y22 = 0
    for i in a:
        kc1 = (i[0] - x1)**2 + (i[1]-y1)**2
        kc2 = (i[0] - x2)**2 + (i[1]-y2)**2
        if(kc1<kc2):
            cum1.append(i)
        else:
            cum2.append(i)
    sumx = 0
    sumy = 0
    for i in cum1:
        sumx = sumx + i[0]
        sumy = sumy + i[1]
    if len(cum1) != 0:
        x11 = sumx/len(cum1)
        y11 = sumy/len(cum1) 
    sumx = 0
    sumy = 0
    for i in cum2:
        sumx = sumx + i[0]
        sumy = sumy + i[1]
    if(len(cum2) != 0):
        x22 = sumx/len(cum2)
        y22 = sumy/len(cum2) 
    if round(x1,3) == round(x11,3) and round(x2,3) == round(x22,3) and round(y1,3) == round(y11) and round(y2,3) == round(y22,3):
        break
    else:
        if len(cum1) != 0:
            x1 = x11
            y1 = y11
        if(len(cum2) != 0):
            x2 = x22
            y2 = y22
    print(x1," ",y1)
    print(x2," ", y2)
print(cum1)
print(cum2)
