from PIL import Image

m0 = Image.open("0.jpeg")
m1 = Image.open("1.jpeg")
m2 = Image.open("2.jpeg")
m3 = Image.open("3.jpeg")
m4 = Image.open("4.jpeg")
m5 = Image.open("5.jpeg")
m6 = Image.open("6.jpeg")
m7 = Image.open("7.jpeg")
m8 = Image.open("8.jpeg")
m9 = Image.open("9.jpeg")
ma = Image.open("a.jpeg") #nombre de la imagen de la letra a
mb = Image.open("b.jpeg")
mc = Image.open("c.jpeg")
md = Image.open("d.jpeg")
me = Image.open("e.jpeg")
mf = Image.open("f.jpeg")
mg = Image.open("g.jpeg")
mh = Image.open("h.jpeg")
mi = Image.open("i.jpeg")
mj = Image.open("j.jpeg")
mk = Image.open("k.jpeg")
ml = Image.open("l.jpeg")
mm = Image.open("m.jpeg")
mn = Image.open("n.jpeg")
mo = Image.open("o.jpeg")
mp = Image.open("p.jpeg")
mq = Image.open("q.jpeg")
mr = Image.open("r.jpeg")
ms = Image.open("s.jpeg")
mt = Image.open("t.jpeg")
mu = Image.open("u.jpeg")
mv = Image.open("v.jpeg")
mw = Image.open("w.jpeg")
mx = Image.open("x.jpeg")
my = Image.open("y.jpeg")
mz = Image.open("z.jpeg")
mcoma = Image.open("coma.jpeg")
mblank = Image.open("blank.jpeg")
mperiod = Image.open("period.jpeg")
mdoubledot = Image.open("doubledot.jpeg")
msemicolon = Image.open("semicolon.jpeg")

#TODO: crear las imagenes para cada letra.
#TODO: enable on production
#mA = ma.resize((n, m)) #letra mayuscula
m0 = m0.resize((8, 16)) #cambiar el tamano de la letra minuscula
m1 = m1.resize((8, 16))
m2 = m2.resize((8, 16))
m3 = m3.resize((8, 16))
m4 = m4.resize((8, 16))
m5 = m5.resize((8, 16))
m6 = m6.resize((8, 16))
m7 = m7.resize((8, 16))
m8 = m8.resize((8, 16))
m9 = m9.resize((8, 16))
ma = ma.resize((8, 16))
mb = mb.resize((8, 16))
mc = mc.resize((8, 16))
md = md.resize((8, 16))
me = me.resize((8, 16))
mf = mf.resize((8, 16))
mg = mg.resize((8, 16))
mh = mh.resize((8, 16))
mi = mi.resize((8, 16))
mj = mj.resize((8, 16))
mk = mk.resize((8, 16))
ml = ml.resize((8, 16))
mm = mm.resize((8, 16))
mn = mn.resize((8, 16))
mo = mo.resize((8, 16))
mp = mp.resize((8, 16))
mq = mq.resize((8, 16))
mr = mr.resize((8, 16))
ms = ms.resize((8, 16))
mt = mt.resize((8, 16))
mu = mu.resize((8, 16))
mv = mv.resize((8, 16))
mw = mw.resize((8, 16))
mx = mx.resize((8, 16))
my = my.resize((8, 16))
mz = mz.resize((8, 16))
mcoma = mcoma.resize((8, 16))
mblank = mblank.resize((8, 16))
mperiod = mperiod.resize((8, 16))
mdoubledot = mdoubledot.resize((8, 16))
msemicolon = msemicolon.resize((8, 16))
#TODO: determinar el size de las imagenes tanto para minuscula y mayuscula
#TODO: crear la imagen del size del texto
#TODO: calcular el size de de la imagen resultante a partir de la cantidad de letras.
def cambio(f):
    F = open(f, "r")
    i = 0
    j = 0
    lines = F.readlines()
    for line in lines:
        line = lines.split(" ")
        document = Image.new('RGB',(8*len(F[0]), 16*len(F)), (250,250,250))
        while i < len(F):
            while j < len(F[j]):
                if F[i][j] == "a":
                    document.paste(ma,(i,j))
                if F[i][j] == "b":
                    document.paste(mb,(i,j))
                if F[i][j] == "c":
                    document.paste(mc,(i,j))
                if F[i][j] == "d":
                    document.paste(md,(i,j)) 
                if F[i][j] == "e":
                    document.paste(me,(i,j))    