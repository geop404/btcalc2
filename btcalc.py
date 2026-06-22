from tkinter import *
from tkinter import ttk
import random

amount_missel = 0
hit_counter = 0
dice10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dice6 = [1, 2, 3, 4, 5, 6]

def hit_calculator(shot_count,trefferwurf):
    print("----------------------------")
    hit_counter = 0
    shot = 0
    print(f"Der Trefferwurf lautet: {trefferwurf}")
    while shot_count > 0:
        shot = shot + 1
        print(f"Salve nummer {shot} !")
        dice_row1 = random.choice(dice10)
        dice_row2 = random.choice(dice10)
        print(f"Würfel 1: {dice_row1}")
        print(f"Würfel 2: {dice_row2}")
        dice_sum = dice_row1 + dice_row2
        if dice_sum >= trefferwurf:
            hit_counter = hit_counter + 1
            print("--- Treffer ---")
        else:
            print("--- Daneben ---")
        shot_count = shot_count - 1
    print("----------------------------")
    print(f"{hit_counter} von {shot} haben getroffen!")
    return hit_counter

def missel_count(hit_counter,waffe_typ):
    print("----------------------------")
    real_missel = 0
    rounds = 0
    print(f"{hit_counter} Waffen haben getroffen, berechne die Anzahl der Raketen")
    print("----------------------------")
    if waffe_typ == "SRM2":
        while hit_counter > 0:
            rounds = rounds + 1
            hit_counter = hit_counter - 1
            dice_row1 = random.choice(dice6)
            print(f"Würfel 1: {dice_row1}")
            dice_row2 = random.choice(dice6)
            print(f"Würfel 2: {dice_row2}")
            dice_sum = dice_row1 + dice_row2
            if dice_sum == 2:
                real_missel = real_missel + 1
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 1")
            if dice_sum == 3:
                real_missel = real_missel + 1
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 1")
            if dice_sum == 4:
                real_missel = real_missel + 1
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 1")
            if dice_sum == 5:
                real_missel = real_missel + 1
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 1")
            if dice_sum == 6:
                real_missel = real_missel + 1
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 1")
            if dice_sum == 7:
                real_missel = real_missel + 1
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 1")
            if dice_sum == 8:
                real_missel = real_missel + 2
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 2")
            if dice_sum == 9:
                real_missel = real_missel + 2
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 2")
            if dice_sum == 10:
                real_missel = real_missel + 2
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 2")
            if dice_sum == 11:
                real_missel = real_missel + 2
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 2")
            if dice_sum == 12:
                real_missel = real_missel + 2
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 2")
        print(f"--- Anzahl Raketen gesamt: {real_missel} ---")
    if waffe_typ == "SRM4":
        while hit_counter > 0:
            rounds = rounds + 1
            hit_counter = hit_counter - 1
            dice_row1 = random.choice(dice6)
            print(f"Würfel 1: {dice_row1}")
            dice_row2 = random.choice(dice6)
            print(f"Würfel 2: {dice_row2}")
            dice_sum = dice_row1 + dice_row2
            if dice_sum == 2:
                real_missel = real_missel + 1
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 1")
            if dice_sum == 3:
                real_missel = real_missel + 2
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 2")
            if dice_sum == 4:
                real_missel = real_missel + 2
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 2")
            if dice_sum == 5:
                real_missel = real_missel + 2
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 2")
            if dice_sum == 6:
                real_missel = real_missel + 2
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 2")
            if dice_sum == 7:
                real_missel = real_missel + 3
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 3")
            if dice_sum == 8:
                real_missel = real_missel + 3
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 3")
            if dice_sum == 9:
                real_missel = real_missel + 3
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 3")
            if dice_sum == 10:
                real_missel = real_missel + 4
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 4")
            if dice_sum == 11:
                real_missel = real_missel + 4
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 4")
            if dice_sum == 12:
                real_missel = real_missel + 4
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 4")
        print(f"--- Anzahl Raketen gesamt: {real_missel} ---")
    if waffe_typ == "SRM6":
        while hit_counter > 0:
            rounds = rounds + 1
            hit_counter = hit_counter - 1
            dice_row1 = random.choice(dice6)
            print(f"Würfel 1: {dice_row1}")
            dice_row2 = random.choice(dice6)
            print(f"Würfel 2: {dice_row2}")
            dice_sum = dice_row1 + dice_row2
            if dice_sum == 2:
                real_missel = real_missel + 2
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 2")
            if dice_sum == 3:
                real_missel = real_missel + 2
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 2")
            if dice_sum == 4:
                real_missel = real_missel + 3
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 3")
            if dice_sum == 5:
                real_missel = real_missel + 3
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 3")
            if dice_sum == 6:
                real_missel = real_missel + 4
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 4")
            if dice_sum == 7:
                real_missel = real_missel + 4
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 4")
            if dice_sum == 8:
                real_missel = real_missel + 4
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 4")
            if dice_sum == 9:
                real_missel = real_missel + 5
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 5")
            if dice_sum == 10:
                real_missel = real_missel + 5
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 5")
            if dice_sum == 11:
                real_missel = real_missel + 6
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 6")
            if dice_sum == 12:
                real_missel = real_missel + 6
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 6")
        print(f"--- Anzahl Raketen gesamt: {real_missel} ---")
    if waffe_typ == "LRM5":
        while hit_counter > 0:
            rounds = rounds + 1
            hit_counter = hit_counter - 1
            dice_row1 = random.choice(dice6)
            print(f"Würfel 1: {dice_row1}")
            dice_row2 = random.choice(dice6)
            print(f"Würfel 2: {dice_row2}")
            dice_sum = dice_row1 + dice_row2
            if dice_sum == 2:
                real_missel = real_missel + 1
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 1")
            if dice_sum == 3:
                real_missel = real_missel + 2
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 2")
            if dice_sum == 4:
                real_missel = real_missel + 2
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 2")
            if dice_sum == 5:
                real_missel = real_missel + 3
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 3")
            if dice_sum == 6:
                real_missel = real_missel + 3
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 3")
            if dice_sum == 7:
                real_missel = real_missel + 3
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 3")
            if dice_sum == 8:
                real_missel = real_missel + 3
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 3")
            if dice_sum == 9:
                real_missel = real_missel + 4
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 4")
            if dice_sum == 10:
                real_missel = real_missel + 4
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 4")
            if dice_sum == 11:
                real_missel = real_missel + 5
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 5")
            if dice_sum == 12:
                real_missel = real_missel + 5
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 5")
        print(f"--- Anzahl Raketen gesamt: {real_missel} ---")
    if waffe_typ == "LRM10":
        while hit_counter > 0:
            rounds = rounds + 1
            hit_counter = hit_counter - 1
            dice_row1 = random.choice(dice6)
            print(f"Würfel 1: {dice_row1}")
            dice_row2 = random.choice(dice6)
            print(f"Würfel 2: {dice_row2}")
            dice_sum = dice_row1 + dice_row2
            if dice_sum == 2:
                real_missel = real_missel + 3
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 3")
            if dice_sum == 3:
                real_missel = real_missel + 3
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 3")
            if dice_sum == 4:
                real_missel = real_missel + 4
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 4")
            if dice_sum == 5:
                real_missel = real_missel + 6
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 6")
            if dice_sum == 6:
                real_missel = real_missel + 6
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 6")
            if dice_sum == 7:
                real_missel = real_missel + 6
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 6")
            if dice_sum == 8:
                real_missel = real_missel + 6
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 6")
            if dice_sum == 9:
                real_missel = real_missel + 8
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 8")
            if dice_sum == 10:
                real_missel = real_missel + 8
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 8")
            if dice_sum == 11:
                real_missel = real_missel + 10
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 10")
            if dice_sum == 12:
                real_missel = real_missel + 10
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 10")
        print(f"--- Anzahl Raketen gesamt: {real_missel} ---")
    if waffe_typ == "LRM15":
        while hit_counter > 0:
            rounds = rounds + 1
            hit_counter = hit_counter - 1
            dice_row1 = random.choice(dice6)
            print(f"Würfel 1: {dice_row1}")
            dice_row2 = random.choice(dice6)
            print(f"Würfel 2: {dice_row2}")
            dice_sum = dice_row1 + dice_row2
            if dice_sum == 2:
                real_missel = real_missel + 5
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 5")
            if dice_sum == 3:
                real_missel = real_missel + 5
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 5")
            if dice_sum == 4:
                real_missel = real_missel + 6
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 6")
            if dice_sum == 5:
                real_missel = real_missel + 9
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 9")
            if dice_sum == 6:
                real_missel = real_missel + 9
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 9")
            if dice_sum == 7:
                real_missel = real_missel + 9
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 9")
            if dice_sum == 8:
                real_missel = real_missel + 9
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 9")
            if dice_sum == 9:
                real_missel = real_missel + 12
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 12")
            if dice_sum == 10:
                real_missel = real_missel + 12
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 12")
            if dice_sum == 11:
                real_missel = real_missel + 15
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 15")
            if dice_sum == 12:
                real_missel = real_missel + 15
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 15")
        print(f"--- Anzahl Raketen gesamt: {real_missel} ---")
    if waffe_typ == "LRM20":
        while hit_counter > 0:
            rounds = rounds + 1
            hit_counter = hit_counter - 1
            dice_row1 = random.choice(dice6)
            print(f"Würfel 1: {dice_row1}")
            dice_row2 = random.choice(dice6)
            print(f"Würfel 2: {dice_row2}")
            dice_sum = dice_row1 + dice_row2
            if dice_sum == 2:
                real_missel = real_missel + 6
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 6")
            if dice_sum == 3:
                real_missel = real_missel + 6
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 6")
            if dice_sum == 4:
                real_missel = real_missel + 9
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 9")
            if dice_sum == 5:
                real_missel = real_missel + 12
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 12")
            if dice_sum == 6:
                real_missel = real_missel + 12
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 12")
            if dice_sum == 7:
                real_missel = real_missel + 12
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 12")
            if dice_sum == 8:
                real_missel = real_missel + 12
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 12")
            if dice_sum == 9:
                real_missel = real_missel + 16
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 16")
            if dice_sum == 10:
                real_missel = real_missel + 16
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 16")
            if dice_sum == 11:
                real_missel = real_missel + 20
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 20")
            if dice_sum == 12:
                real_missel = real_missel + 20
                print(f"Treffer Nummer {rounds} - Anzahl Raketen: 20")
        print(f"--- Anzahl Raketen gesamt: {real_missel} ---")
    return real_missel

def hit_location_vorne(hit_counter,srm,fhitze):
    print("----------------------------")
    hd = 0
    rl = 0
    ra = 0
    rt = 0
    ct = 0
    lt = 0
    ll = 0
    la = 0
    ct_crit = 0
    labelKopfergebnis.config(text='')
    labelRechtesbeinergebnis.config(text='')
    labelLinkesbeinergebnis.config(text='')
    labelRechterarmergebnis.config(text='')
    labelRechtertorsoergebnis.config(text='')
    labelCentertorsoergebnis.config(text='')
    labelLinkerarmergebnis.config(text='')
    labelLinkertorsoergebnis.config(text='')
    labelCentertorsocritergebnis.config(text='')
    labelHitzeergebnis.config(text='')
    print("Berechne die Trefferzonen:")
    while hit_counter > 0:
        dice_row1 = random.choice(dice6)
        dice_row2 = random.choice(dice6)
        print(f"Würfel 1: {dice_row1}")
        print(f"Würfel 2: {dice_row2}")
        dice_sum = dice_row1 + dice_row2
        hit_counter = hit_counter - 1
        if dice_sum == 2:
            ct_crit = ct_crit + 1
            print(f"{dice_sum} Center Torso Kritisch")
        if dice_sum == 3:
            ra = ra + 1
            print(f"{dice_sum} Rechter Arm")
        if dice_sum == 4:
            ra = ra + 1
            print(f"{dice_sum} Rechter Arm")
        if dice_sum == 5:
            rl = rl + 1
            print(f"{dice_sum} Rechtes Bein")
        if dice_sum == 6:
            rt = rt + 1
            print(f"{dice_sum} Rechter Torso")
        if dice_sum == 7:
            ct = ct + 1
            print(f"{dice_sum} Center Torso")
        if dice_sum == 8:
            lt = lt + 1
            print(f"{dice_sum} Linker Torso")
        if dice_sum == 9:
            ll = ll + 1
            print(f"{dice_sum} Linkes Bein")
        if dice_sum == 10:
            la = la + 1
            print(f"{dice_sum} Linker Arm")
        if dice_sum == 11:
            la = la + 1
            print(f"{dice_sum} Linker Arm")
        if dice_sum == 12:
            hd = hd + 1
            print(f"{dice_sum} Kopftreffer")
    print("----------------------------")
    labelHitzeergebnis.config(text=fhitze)
    if hd > 0:
        print(f"Kopftreffer: {hd} {srm}")
        hd_erg = str(hd) + srm
        labelKopfergebnis.config(text=hd_erg)
    if rl > 0:
        print(f"Beintreffer Rechts: {rl} {srm}")
        rl_erg = str(rl) + srm
        labelRechtesbeinergebnis.config(text=rl_erg)
    if ll > 0:
        print(f"Beintreffer Links: {ll} {srm}")
        ll_erg = str(ll) + srm
        labelLinkesbeinergebnis.config(text=ll_erg)
    if ra > 0:
        print(f"Armtreffer Rechts: {ra} {srm}")
        ra_erg = str(ra) + srm
        labelRechterarmergebnis.config(text=ra_erg)
    if rt > 0:
        print(f"Torsotreffer Rechts: {rt} {srm}")
        rt_erg = str(rt) + srm
        labelRechtertorsoergebnis.config(text=rt_erg)
    if ct > 0:
        print(f"Torsotreffer Mitte: {ct} {srm}")
        ct_erg = str(ct) + srm
        labelCentertorsoergebnis.config(text=ct_erg)
    if lt > 0:
        print(f"Torsotreffer Links: {lt} {srm}")
        lt_erg = str(lt) + srm
        labelLinkertorsoergebnis.config(text=lt_erg)
    if la > 0:
        print(f"Armtreffer Links: {la} {srm}")
        la_erg = str(la) + srm
        labelLinkerarmergebnis.config(text=la_erg)
    if ct_crit > 0:
        print(f"Torsotreffer Mitte Kritisch: {ct_crit} {srm}")
        ct_crit_erg = str(ct_crit) + srm
        labelCentertorsocritergebnis.config(text=ct_crit_erg)
    labelCentertorsocrit.config(text="Center Torso Kritisch:")
    print("----------------------------")

def hit_location_links(hit_counter,srm,fhitze):
    print("----------------------------")
    hd = 0
    rl = 0
    ra = 0
    rt = 0
    ct = 0
    lt = 0
    ll = 0
    la = 0
    lt_crit = 0
    labelKopfergebnis.config(text='')
    labelRechtesbeinergebnis.config(text='')
    labelLinkesbeinergebnis.config(text='')
    labelRechterarmergebnis.config(text='')
    labelRechtertorsoergebnis.config(text='')
    labelCentertorsoergebnis.config(text='')
    labelLinkerarmergebnis.config(text='')
    labelLinkertorsoergebnis.config(text='')
    labelCentertorsocritergebnis.config(text='')
    labelHitzeergebnis.config(text='')
    print("Berechne die Trefferzonen:")
    while hit_counter > 0:
        dice_row1 = random.choice(dice6)
        dice_row2 = random.choice(dice6)
        print(f"Würfel 1: {dice_row1}")
        print(f"Würfel 2: {dice_row2}")
        dice_sum = dice_row1 + dice_row2
        hit_counter = hit_counter - 1
        if dice_sum == 2:
            lt_crit = lt_crit + 1
            print(f"{dice_sum} Linker Torso Kritisch")
        if dice_sum == 3:
            ll = ll + 1
            print(f"{dice_sum} Linkes Bein")
        if dice_sum == 4:
            la = la + 1
            print(f"{dice_sum} Linker Arm")
        if dice_sum == 5:
            la = la + 1
            print(f"{dice_sum} Linker Arm")
        if dice_sum == 6:
            ll = ll + 1
            print(f"{dice_sum} Linkes Bein")
        if dice_sum == 7:
            lt = lt + 1
            print(f"{dice_sum} Linker Torso")
        if dice_sum == 8:
            ct = ct + 1
            print(f"{dice_sum} Center Torso")
        if dice_sum == 9:
            rt = rt + 1
            print(f"{dice_sum} Rechter Torso")
        if dice_sum == 10:
            ra = ra + 1
            print(f"{dice_sum} Rechter Arm")
        if dice_sum == 11:
            rl = rl + 1
            print(f"{dice_sum} Rechtes Bein")
        if dice_sum == 12:
            hd = hd + 1
            print(f"{dice_sum} Kopftreffer")
    print("----------------------------")
    labelHitzeergebnis.config(text=fhitze)
    if hd > 0:
        print(f"Kopftreffer: {hd} {srm}")
        hd_erg = str(hd) + srm
        labelKopfergebnis.config(text= hd_erg)
    if rl > 0:
        print(f"Beintreffer Rechts: {rl} {srm}")
        rl_erg = str(rl) + srm
        labelRechtesbeinergebnis.config(text=rl_erg)
    if ll > 0:
        print(f"Beintreffer Links: {ll} {srm}")
        ll_erg = str(ll) + srm
        labelLinkesbeinergebnis.config(text=ll_erg)
    if ra > 0:
        print(f"Armtreffer Rechts: {ra} {srm}")
        ra_erg = str(ra) + srm
        labelRechterarmergebnis.config(text=ra_erg)
    if rt > 0:
        print(f"Torsotreffer Rechts: {rt} {srm}")
        rt_erg = str(rt) + srm
        labelRechtertorsoergebnis.config(text=rt_erg)
    if ct > 0:
        print(f"Torsotreffer Mitte: {ct} {srm}")
        ct_erg = str(ct) + srm
        labelCentertorsoergebnis.config(text=ct_erg)
    if lt > 0:
        print(f"Torsotreffer Links: {lt} {srm}")
        lt_erg = str(lt) + srm
        labelLinkertorsoergebnis.config(text=lt_erg)
    if la > 0:
        print(f"Armtreffer Links: {la} {srm}")
        la_erg = str(la) + srm
        labelLinkerarmergebnis.config(text=la_erg)
    if lt_crit > 0:
        print(f"Torsotreffer Links Kritisch: {lt_crit} {srm}")
        lt_crit_erg = str(lt_crit) + srm
        labelCentertorsocritergebnis.config(text=lt_crit_erg)
    labelCentertorsocrit.config(text="Linker Torso Kritisch:")
    print("----------------------------")

def hit_location_rechts(hit_counter,srm,fhitze):
    print("----------------------------")
    hd = 0
    rl = 0
    ra = 0
    rt = 0
    ct = 0
    lt = 0
    ll = 0
    la = 0
    rt_crit = 0
    labelKopfergebnis.config(text='')
    labelRechtesbeinergebnis.config(text='')
    labelLinkesbeinergebnis.config(text='')
    labelRechterarmergebnis.config(text='')
    labelRechtertorsoergebnis.config(text='')
    labelCentertorsoergebnis.config(text='')
    labelLinkerarmergebnis.config(text='')
    labelLinkertorsoergebnis.config(text='')
    labelCentertorsocritergebnis.config(text='')
    labelHitzeergebnis.config(text='')
    print("Berechne die Trefferzonen:")
    while hit_counter > 0:
        dice_row1 = random.choice(dice6)
        dice_row2 = random.choice(dice6)
        print(f"Würfel 1: {dice_row1}")
        print(f"Würfel 2: {dice_row2}")
        dice_sum = dice_row1 + dice_row2
        hit_counter = hit_counter - 1
        if dice_sum == 2:
            rt_crit = rt_crit + 1
            print(f"{dice_sum} Rechter Torso Kritisch")
        if dice_sum == 3:
            rl = rl + 1
            print(f"{dice_sum} Rechtes Bein")
        if dice_sum == 4:
            ra = ra + 1
            print(f"{dice_sum} Rechter Arm")
        if dice_sum == 5:
            ra = ra + 1
            print(f"{dice_sum} Rechter Arm")
        if dice_sum == 6:
            rl = rl + 1
            print(f"{dice_sum} Rechtes Bein")
        if dice_sum == 7:
            rt = rt + 1
            print(f"{dice_sum} Rechter Torso")
        if dice_sum == 8:
            ct = ct + 1
            print(f"{dice_sum} Center Torso")
        if dice_sum == 9:
            lt = lt + 1
            print(f"{dice_sum} Linker Torso")
        if dice_sum == 10:
            la = la + 1
            print(f"{dice_sum} Linker Arm")
        if dice_sum == 11:
            ll = ll + 1
            print(f"{dice_sum} Linkes Bein")
        if dice_sum == 12:
            hd = hd + 1
            print(f"{dice_sum} Kopftreffer")
    print("----------------------------")
    labelHitzeergebnis.config(text=fhitze)
    if hd > 0:
        print(f"Kopftreffer: {hd} {srm}")
        hd_erg = str(hd) + srm
        labelKopfergebnis.config(text= hd_erg)
    if rl > 0:
        print(f"Beintreffer Rechts: {rl} {srm}")
        rl_erg = str(rl) + srm
        labelRechtesbeinergebnis.config(text=rl_erg)
    if ll > 0:
        print(f"Beintreffer Links: {ll} {srm}")
        ll_erg = str(ll) + srm
        labelLinkesbeinergebnis.config(text=ll_erg)
    if ra > 0:
        print(f"Armtreffer Rechts: {ra} {srm}")
        ra_erg = str(ra) + srm
        labelRechterarmergebnis.config(text=ra_erg)
    if rt > 0:
        print(f"Torsotreffer Rechts: {rt} {srm}")
        rt_erg = str(rt) + srm
        labelRechtertorsoergebnis.config(text=rt_erg)
    if ct > 0:
        print(f"Torsotreffer Mitte: {ct} {srm}")
        ct_erg = str(ct) + srm
        labelCentertorsoergebnis.config(text=ct_erg)
    if lt > 0:
        print(f"Torsotreffer Links: {lt} {srm}")
        lt_erg = str(lt) + srm
        labelLinkertorsoergebnis.config(text=lt_erg)
    if la > 0:
        print(f"Armtreffer Links: {la} {srm}")
        la_erg = str(la) + srm
        labelLinkerarmergebnis.config(text=la_erg)
    if rt_crit > 0:
        print(f"Torsotreffer Rechts Kritisch: {rt_crit} {srm}")
        rt_crit_erg = str(rt_crit) + srm
        labelCentertorsocritergebnis.config(text=rt_crit_erg)
    labelCentertorsocrit.config(text="Rechter Torso Kritisch:")
    print("----------------------------")

def buttonBerechnenClick():
    #waffe_typ = entryWaffentyp.get()
    waffe_typ = optionWeapon.get()
    shot_count = int(entryAnzahl.get())
    trefferwurf = int(entryTrefferwert.get())
    #treffer_zone = entryTrefferzone.get()
    treffer_zone = optionTrefferzone.get()
    srm = "  Treffer"
    ghitze = 0
    fhitze = 0
    amount_missel = 0
    if waffe_typ == "SRM2":
        srm = "  Treffer x2 Dmg"
        ghitze = 2
        hit_counter = hit_calculator(shot_count, trefferwurf)
        amount_missel = missel_count(hit_counter, waffe_typ)
    if waffe_typ == "SRM4":
        srm = "  Treffer x2 Dmg"
        ghitze = 3
        hit_counter = hit_calculator(shot_count, trefferwurf)
        amount_missel = missel_count(hit_counter, waffe_typ)
    if waffe_typ == "SRM6":
        srm = "  Treffer x2 Dmg"
        ghitze = 4
        hit_counter = hit_calculator(shot_count, trefferwurf)
        amount_missel = missel_count(hit_counter, waffe_typ)
    if waffe_typ == "LRM5":
        srm = "  Treffer x1 Dmg"
        ghitze = 2
        hit_counter = hit_calculator(shot_count, trefferwurf)
        amount_missel = missel_count(hit_counter, waffe_typ)
    if waffe_typ == "LRM10":
        srm = "  Treffer x1 Dmg"
        ghitze = 4
        hit_counter = hit_calculator(shot_count, trefferwurf)
        amount_missel = missel_count(hit_counter, waffe_typ)
    if waffe_typ == "LRM15":
        srm = "  Treffer x1 Dmg"
        ghitze = 5
        hit_counter = hit_calculator(shot_count, trefferwurf)
        amount_missel = missel_count(hit_counter, waffe_typ)
    if waffe_typ == "LRM20":
        srm = "  Treffer x1 Dmg"
        ghitze = 6
        hit_counter = hit_calculator(shot_count, trefferwurf)
        amount_missel = missel_count(hit_counter, waffe_typ)
    if waffe_typ == "SLASER":
        srm = "  Treffer x3 Dmg"
        ghitze = 1
        hit_counter = hit_calculator(shot_count, trefferwurf)
        amount_missel = hit_counter
    if waffe_typ == "MLASER":
        srm = "  Treffer x5 Dmg"
        ghitze = 3
        hit_counter = hit_calculator(shot_count, trefferwurf)
        amount_missel = hit_counter
    if waffe_typ == "LLASER":
        srm = "  Treffer x8 Dmg"
        ghitze = 8
        hit_counter = hit_calculator(shot_count, trefferwurf)
        amount_missel = hit_counter
    if waffe_typ == "ERSLASER":
        srm = "  Treffer x3 Dmg"
        ghitze = 2
        hit_counter = hit_calculator(shot_count, trefferwurf)
        amount_missel = hit_counter
    if waffe_typ == "ERMLASER":
        srm = "  Treffer x5 Dmg"
        ghitze = 5
        hit_counter = hit_calculator(shot_count, trefferwurf)
        amount_missel = hit_counter
    if waffe_typ == "ERLLASER":
        srm = "  Treffer x8 Dmg"
        ghitze = 12
        hit_counter = hit_calculator(shot_count, trefferwurf)
        amount_missel = hit_counter
    if waffe_typ == "PPC":
        srm = "  Treffer x10 Dmg"
        ghitze = 10
        hit_counter = hit_calculator(shot_count, trefferwurf)
        amount_missel = hit_counter
    if waffe_typ == "ERPPC":
        srm = "  Treffer x10 Dmg"
        ghitze = 15
        hit_counter = hit_calculator(shot_count, trefferwurf)
        amount_missel = hit_counter
    if waffe_typ == "AC2":
        srm = "  Treffer x2 Dmg"
        ghitze = 1
        hit_counter = hit_calculator(shot_count, trefferwurf)
        amount_missel = hit_counter
    if waffe_typ == "AC5":
        srm = "  Treffer x5 Dmg"
        ghitze = 1
        hit_counter = hit_calculator(shot_count, trefferwurf)
        amount_missel = hit_counter
    if waffe_typ == "AC10":
        srm = "  Treffer x10 Dmg"
        ghitze = 3
        hit_counter = hit_calculator(shot_count, trefferwurf)
        amount_missel = hit_counter
    if waffe_typ == "AC20":
        srm = "  Treffer x20 Dmg"
        ghitze = 7
        hit_counter = hit_calculator(shot_count, trefferwurf)
        amount_missel = hit_counter
    if waffe_typ == "ULTRAAC2":
        srm = "  Treffer x2 Dmg"
        ghitze = 1
        hit_counter = hit_calculator(shot_count, trefferwurf)
        amount_missel = hit_counter
    if waffe_typ == "ULTRAAC5":
        srm = "  Treffer x5 Dmg"
        ghitze = 1
        hit_counter = hit_calculator(shot_count, trefferwurf)
        amount_missel = hit_counter
    if waffe_typ == "ULTRAAC10":
        srm = "  Treffer x10 Dmg"
        ghitze = 4
        hit_counter = hit_calculator(shot_count, trefferwurf)
        amount_missel = hit_counter
    if waffe_typ == "ULTRAAC20":
        srm = "  Treffer x20 Dmg"
        ghitze = 8
        hit_counter = hit_calculator(shot_count, trefferwurf)
        amount_missel = hit_counter
    if waffe_typ == "GAUS":
        srm = "  Treffer x15 Dmg"
        ghitze = 1
        hit_counter = hit_calculator(shot_count, trefferwurf)
        amount_missel = hit_counter
    if waffe_typ == "MGUN":
        srm = "  Treffer x2 Dmg"
        ghitze = 0
        hit_counter = hit_calculator(shot_count, trefferwurf)
        amount_missel = hit_counter


    if ghitze == 0:
        fhitze = 0
    if ghitze >= 1:
        fhitze = shot_count * ghitze

    if treffer_zone == "vorne":
        print("----------------------------")
        print("Wende vordere Trefferzonen an")
        hit_location_vorne(amount_missel, srm, fhitze)
    if treffer_zone == "rechts":
        print("----------------------------")
        print("Wende rechte Trefferzonen an")
        hit_location_rechts(amount_missel, srm, fhitze)
    if treffer_zone == "links":
        print("----------------------------")
        print("Wende linke Trefferzonen an")
        hit_location_links(amount_missel, srm, fhitze)



tkFenster = Tk()
tkFenster.title('BTcalc')
tkFenster.geometry('335x640')

all_weapons = ["SRM2", "SRM4", "SRM6", "LRM5", "LRM10", "LRM15", "LRM20", "SLASER", "MLASER", "LLASER", "ERSLASER", "ERMLASER", "ERLLASER", "PPC", "ERPPC", "AC2", "AC5", "AC10", "AC20", "ULTRAAC2", "ULTRAAC5", "ULTRAAC10", "ULTRAAC20", "GAUS", "MGUN"]
all_trefferzone = ["vorne", "rechts", "links"]

labelWaffentyp = Label(master=tkFenster, text='Waffentyp:', bg='lightgrey')
labelWaffentyp.place(x=54, y=24, width=140, height=27)
#labelWaffentypbsp = Label(master=tkFenster, text='Bsp: srm_4 oder lrm_20')
#labelWaffentypbsp.place(x=254, y=24, width=140, height=27)

#entryWaffentyp = Entry(master=tkFenster, bg='white')
#entryWaffentyp.place(x=204, y=24, width=40, height=27)
optionWeapon = ttk.Combobox(master=tkFenster, values=all_weapons)
optionWeapon.set("SRM2")
optionWeapon.place(x=204, y=24, width=90, height=27)


labelAnzahl = Label(master=tkFenster, text='Anzahl Waffen:', bg='lightgrey')
labelAnzahl.place(x=54, y=64, width=140, height=27)
#labelAnzahlbsp = Label(master=tkFenster, text='Bsp.: 5 oder 10')
#labelAnzahlbsp.place(x=254, y=64, width=140, height=27)

entryAnzahl = Entry(master=tkFenster, bg='white')
entryAnzahl.place(x=204, y=64, width=90, height=27)
labelTrefferwert = Label(master=tkFenster, text='Trefferwert:', bg='lightgrey')
labelTrefferwert.place(x=54, y=104, width=140, height=27)
#labelTrefferwert = Label(master=tkFenster, text='Bsp.: 8 oder 12')
#labelTrefferwert.place(x=254, y=104, width=140, height=27)

entryTrefferwert = Entry(master=tkFenster, bg='white')
entryTrefferwert.place(x=204, y=104, width=90, height=27)
labelTrefferzone = Label(master=tkFenster, text='Trefferzone:', bg='lightgrey')
labelTrefferzone.place(x=54, y=144, width=140, height=27)
#labelTrefferzonebsp = Label(master=tkFenster, text='vorne,rechts,links')
#labelTrefferzonebsp.place(x=254, y=144, width=140, height=27)

#entryTrefferzone = Entry(master=tkFenster, bg='white')
#entryTrefferzone.place(x=204, y=144, width=40, height=27)
#entryTrefferzone.insert(10,'vorne')

optionTrefferzone = ttk.Combobox(master=tkFenster, values=all_trefferzone)
optionTrefferzone.set("vorne")
optionTrefferzone.place(x=204, y=144, width=90, height=27)

buttonBerechnen = Button(master=tkFenster, bg='grey', text='Feuer frei!', command=buttonBerechnenClick)
buttonBerechnen.place(x=54, y=184, width=240, height=27)

labelKopf = Label(master=tkFenster, text='Kopf:', bg='lightgrey')
labelKopf.place(x=54, y=224, width=140, height=27)

labelKopfergebnis = Label(master=tkFenster, text='', fg="red")
labelKopfergebnis.place(x=204, y=224, width=100, height=27)

labelLinkerarm = Label(master=tkFenster, text='Linker Arm:', bg='lightgrey')
labelLinkerarm.place(x=54, y=264, width=140, height=27)

labelLinkerarmergebnis = Label(master=tkFenster, text='')
labelLinkerarmergebnis.place(x=204, y=264, width=100, height=27)

labelRechterarm = Label(master=tkFenster, text='Rechter Arm:', bg='lightgrey')
labelRechterarm.place(x=54, y=304, width=140, height=27)

labelRechterarmergebnis = Label(master=tkFenster, text='')
labelRechterarmergebnis.place(x=204, y=304, width=100, height=27)

labelLinketorso = Label(master=tkFenster, text='Linker Torso:', bg='lightgrey')
labelLinketorso.place(x=54, y=344, width=140, height=27)

labelLinkertorsoergebnis = Label(master=tkFenster, text='')
labelLinkertorsoergebnis.place(x=204, y=344, width=100, height=27)

labelRechtertorso = Label(master=tkFenster, text='Rechter Torso:', bg='lightgrey')
labelRechtertorso.place(x=54, y=384, width=140, height=27)

labelRechtertorsoergebnis = Label(master=tkFenster, text='')
labelRechtertorsoergebnis.place(x=204, y=384, width=100, height=27)

labelCentertorso = Label(master=tkFenster, text='Center Torso:', bg='lightgrey')
labelCentertorso.place(x=54, y=424, width=140, height=27)

labelCentertorsoergebnis = Label(master=tkFenster, text='')
labelCentertorsoergebnis.place(x=204, y=424, width=100, height=27)

labelCentertorsocrit = Label(master=tkFenster, text='Torso Kritisch:', bg='lightgrey')
labelCentertorsocrit.place(x=54, y=464, width=140, height=27)

labelCentertorsocritergebnis = Label(master=tkFenster,text='', fg="red")
labelCentertorsocritergebnis.place(x=204, y=464, width=100, height=27)

labelLinkesbein = Label(master=tkFenster, text='Linkes Bein:', bg='lightgrey')
labelLinkesbein.place(x=54, y=504, width=140, height=27)

labelLinkesbeinergebnis = Label(master=tkFenster, text='')
labelLinkesbeinergebnis.place(x=204, y=504, width=100, height=27)

labelRechtesbein = Label(master=tkFenster, text='Rechtes Bein:', bg='lightgrey')
labelRechtesbein.place(x=54, y=544, width=140, height=27)

labelRechtesbeinergebnis = Label(master=tkFenster, text='')
labelRechtesbeinergebnis.place(x=204, y=544, width=100, height=27)

labelHitze = Label(master=tkFenster, text='Generierte Hitze:', bg='lightgrey')
labelHitze.place(x=54, y=584, width=140, height=27)

labelHitzeergebnis = Label(master=tkFenster, text='')
labelHitzeergebnis.place(x=204, y=584, width=100, height=27)



tkFenster.mainloop()