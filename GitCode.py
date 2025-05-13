nm = input("CMO T LLAMAS?")

print(f'BIENVENID@ AL SIMULADOR DE CARRERAS, {nm.upper()}!!')

kg = int(input("CUANTO PESA TU AUTO????? (DE 1 A 150KG)"))
lol = True 

while lol:
    if 0 >= kg:
        print("Era inexistente, wtf? Cambia de auto mejor")
        kg = int(input("CUANTO PESA TU AUTO????? (DE 0 A 150KG, NO SEAI)"))
    elif kg > 15
    0:
        print("AA te gusta poco, eh? Cambia de auto mejor")
        kg = int(input("CUANTO PESA TU AUTO????? (DE 0 A 150KG, NO SEAI)"))
    else:
        lol = False
    
if kg < 50:
    print("Tienes un auto livianito, será bueno o malo?")
elif 100 > kg >= 50:
    print("Tienes un auto medianito, ni fu ni fa!")
else:
    print("Tienes un auto pesadito, ns está curiosito..")
    
rds = int(input("CUANTAS RUEDAS TIENE, O NO TIENE??! ESO SERÍA RARO"))
lol = True 

while lol:
    if 0 == rds:
        print("Osea...quizás vuela, pero mejor busca uno con ruedas si no quieres ser descalificado:/")
        rds = int(input("CUANTAS RUEDAS TIENE, OTRA OPORTUNIDAD"))
    elif 0 > rds:
        print("POCO SERIOOO, ESO NO TIENE SENTIDO, PONELE RUEDAS")
        rds = int(input("CUANTAS RUEDAS TIENE, OTRA OPORTUNIDAD"))
    else:
        lol = False

vlc_auto = int(input("CUAL ES LA VELOCIDADMAX D TU AUTO? RAYO MCQUEEN SIONO?"))

print(f'Tu velocidad para la carrera sera {vlc_auto}, YIPPIEEEE!!')

lrg_m = int(input("Di un num random mayor a 200 pa más acción, fuaa"))
lol = True

while lol:
    if 200 > lrg_m:
        print("OOO QUE ERI FOMEE, cambia de num mejor (siosi lolol)")
        lrg_m = int(input("DI UN NUM MAYOR A 200!!!"))
    else:
        lol = False
        
n_vls = int(input("Otro num entre 3 y 5"))
lol = True

while lol:
    if 3 <= n_vls <= 5 :
        lol = False
    else:
        print("Y la de seguir instrucciones te la sabes? No se nota")
        n_vls = int(input("Otro num entre 3 y 5"))
        
print(f'Inicio de la carrera de {nm.lower()}, rompete una pierna!!')
print(f'Longitud de la pista: {lrg_m}')
print("EVENTOS POSIBLES SIN LIMITE DE USO: Platano, agua, caparazon")
print("EVENTOS POSIBLES CON LIMITE DE USO: Estrella, 2 usos max; bala, sólo puede usarse en la segunda mitad de la carrera!")

sgur = True
rcd = 0
tmp = 0
min_stla = 0
max_stla = 2
drn_stla = 0
dst_bl_s = ""

for act_vls in range(1, (n_vls+1)):
    print(f'Inicio de la vuelta {act_vls} / {n_vls}!!!')
    sgur = True
    while sgur:
        ev = input()
        if drn_stla > 0:
            if ev == "estrella":
                print(f'[ {rcd} m ] Te encontraste con el evento {ev}, pero no hace efecto porque viajas con el poder de la goat!')
            elif ev in ("platano", "agua", "caparazon", "bala"):
                print(f'[ {rcd} m ] Te encontraste con el evento {ev}, pero no hace efecto porque viajas con el poder de la goat!')
            else:
                print(f'[ {rcd} m ] Avanzas con el poder de la goat!')
            drn_stla -= 1
            rcd += vlc_auto * 1.5


        else:
            if ev == "estrella":
                if min_stla < max_stla:
                    print(f'[ {rcd} m ] RECOGISTE LA ESTRELLA, LA GOAT! Tu velocidad aumenta 50% y no te afectan los otros eventos yujuu')
                    drn_stla = 4
                    min_stla += 1
                    rcd += vlc_auto * 1.5
                else:
                    print(f'[ {rcd} m ] Te encontraste con una estrella, si, pero ya usaste el max permitido :((')
                    rcd += vlc_auto
            elif ev == "platano":
                print(f'[ {rcd} m ] Upsie, resbalaste con un platano! Tu velocidad se reduce al 25%')
                rcd += vlc_auto * 0.25
            elif ev == "agua":
                print(f'[ {rcd} m ] Hiciste la witsi witsi araña irl (irl virtual o qsy)! Tu velocidad se reduce al 50%')
                rcd += vlc_auto * 0.5
            elif ev == "caparazon":
                print(f'[ {rcd} m ] Chocaste con un caparazon! Tu velocidad se redujo a 0 LOLOL')
                rcd += 0
            elif ev == "bala":
                if rcd > (lrg_m * n_vls)/2:
                    bl = (input())
                    bl_nmr = int(bl)
                    for e in bl[0:3]:
                        dst_bl_s += e
                    dst_bl = int(dst_bl_s)
                    print(f'[ {rcd} m ] TE SUBISTE A LA BALAA! Avanzaste {dst_bl} metros!?!')
                    rcd += dst_bl
                    dst_bl_s = ""
                else:
                    print(f'[ {rcd} m ] Aún nopodi, avanzas a velocidad normal')
                    rcd += vlc_auto
            else:
                print(f'[ {rcd} m ] Avanzas con normalidad, lol q mal')
                rcd += vlc_auto

        if rcd >= lrg_m*act_vls:
                sgur = False
            
        tmp += 1

    print(f'Completaste la vuelta {act_vls} / {n_vls} en {tmp} segundos!')
    print(f'Llevas {rcd} / {lrg_m * n_vls} metros recorridos')

print(f'¡ESOOOOO, DEVORASTE! {nm} completó la carrera en {tmp} segundos :D')