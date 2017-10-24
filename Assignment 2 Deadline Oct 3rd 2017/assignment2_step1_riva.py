#ASSIGNMENT 2

H = 3 #height of the wall
W = 5 #width of the wall
t1 = 20 #temperature inside
t2 = -10 #temperature outside
ht = 0.25 #total height of the unit
hb = 0.22 #height of the brick
hp = 0.015 #height of the plaster
wf = 0.03 #width of the foam
wp = 0.02 #width of the plaster layers
wb = 0.16 #width of the brick
k1 = 0.026 #foam conduction heat transfer
k2 = 0.22 #plaster conduction heat transfer
k3 = 0.72 #brick conduction heat transfer
h1 = 10 #inside convenction heat trasfer
h2 = 25 #outside convenction heat trasfer

#Res
Rconv = [0.25,10]
R1 = [0.25, 0.03, 0.026]  #foam Res
R2 = R6 = [0.25,0.02,0.22]  #the two plaster side res
R3 = R5 = [0.015,0.16,0.22]  #Plaster center Res
R4 = [0.22,0.16,0.72]     #Brick Res
R0 = [0.25,25]             #second convention res

series = [R1,R2,R3]
parallel = [R3,R5,R4]
convseries = [Rconv,R0]

conv = 0
for anyelement in convseries:
    A = anyelement[0]
    h = anyelement[1]
    Rconv = 1/(A*h)
CONVENCTION = conv + Rconv

serie = 0
for aanyelement in series:
    A_ = aanyelement[0]
    h_ = aanyelement[1]
    k_= aanyelement[2]
    Rconv = h_/(A_*k_)
SERIES = serie + Rconv
    
paral= 0
for anyelement in parallel:
    A__ = anyelement[0]
    h__ = anyelement[1]
    k__ = anyelement[2]
    Rpar = h__/(A__*k__)
    Rparal = paral + 1/Rpar
PARALLELL = 1/Rparal

RTOT= PARALLELL + CONVENCTION + SERIES


print"The amount of thermal resistence of the brick is "+str (RTOT)+" W"