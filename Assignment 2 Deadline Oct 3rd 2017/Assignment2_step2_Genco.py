#determination of the total thermal resistance and the heat transfer rate throw a Composite Wall

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

#Resistence 
Rconv = {"total height of the unit":0.25,"convenction heat trasfer":10}
R1 = {"name":"foam","area":0.25,"lenght": 0.03,"k":0.026} 
R2 = {"name":"plaster series","area":0.25,"lenght":0.02,"k":0.22} 
R6 = {"name":"plaster series1","area":0.25,"lenght":0.02,"k":0.22}
R3 = {"name":"plaster parallel","area":0.015,"lenght":0.16,"k":0.22}
R5 = {"name":"plaster parallel1","area":0.015,"lenght":0.16,"k":0.22}  
R4 = {"area":0.22,"lenght":0.16,"k":0.72}     
R0 = {"total height of the unit":0.25,"convenction heat trasfer":25}             
series = [R1,R2,R3]
parallel = [R3,R5,R4]
convseries = [Rconv,R0]

conv = 0
for anyelement in convseries:
    A = anyelement["total height of the unit"]
    h = anyelement["convenction heat trasfer"]
    Rconv = 1/(A*h)
CONVENCTION = conv + Rconv

serie = 0
for anyelement in series:
    A1 = anyelement["area"]
    h1 = anyelement["lenght"]
    k1= anyelement["k"]
    Rconv = h1/(A1*k1)
SERIES = serie + Rconv
    
paral= 0
for aanyelement in parallel:
    A2= aanyelement["area"]
    h2 = aanyelement["lenght"]
    k2 = aanyelement["k"]
    Rpar = h2/(A2*k2)
    Rparal = paral + 1/Rpar
PARALLELL = 1/Rparal

RTOT= PARALLELL + CONVENCTION + SERIES


print"The amount of thermal resistence of the brick is "+str (RTOT)+" W"