#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk, messagebox

def beregn_tilbud(antal_emblemer, antal_magneter):
    # Pris-trin for emblemer
    if antal_emblemer >= 100:
        pris_emblem = 31
    elif antal_emblemer >= 50:
        pris_emblem = 33
    else:
        pris_emblem = 35

    # Pris-trin for magneter
    if antal_magneter >= 100:
        pris_magnet = 21
    elif antal_magneter >= 50:
        pris_magnet = 23
    else:
        pris_magnet = 25

    # Butikkens salgspriser til kunder (faste)
    butik_emblem = 50
    butik_magnet = 45

    # Beregninger
    indkoeb = (antal_emblemer * pris_emblem) + (antal_magneter * pris_magnet)
    salg = (antal_emblemer * butik_emblem) + (antal_magneter * butik_magnet)
    fortjeneste = salg - indkoeb
    roi = (fortjeneste / indkoeb * 100) if indkoeb > 0 else 0

    return indkoeb, salg, fortjeneste, roi, pris_emblem, pris_magnet


def beregn():
    try:
        antal_emblemer = int(entry_emblemer.get() or 0)
        antal_magneter = int(entry_magneter.get() or 0)

        indkoeb, salg, fortjeneste, roi, pris_emblem, pris_magnet = beregn_tilbud(antal_emblemer, antal_magneter)

        resultat_text.set(
            f"Antal emblemer: {antal_emblemer} (stykpris {pris_emblem} kr.)\n"
            f"Antal magneter: {antal_magneter} (stykpris {pris_magnet} kr.)\n"
            f"Butikkens indkøbspris: {indkoeb} kr.\n"
            f"Butikkens salgspris: {salg} kr.\n"
            f"Butikkens fortjeneste: {fortjeneste} kr.\n"
            f"ROI: {roi:.1f} %"
        )
    except ValueError:
        messagebox.showerror("Fejl", "Indtast venligst gyldige tal.")


# GUI opsætning
root = tk.Tk()
root.title("Souvenir Beregner – TURISTFÆLDEN")

# Indtastningsfelter
frame = ttk.Frame(root, padding="100")
frame.grid(row=0, column=0, sticky="nsew")

ttk.Label(frame, text="Antal emblemer:").grid(row=0, column=0, sticky="w", pady=5)
entry_emblemer = ttk.Entry(frame, width=10)
entry_emblemer.grid(row=0, column=1, pady=5)

ttk.Label(frame, text="Antal magneter:").grid(row=1, column=0, sticky="w", pady=5)
entry_magneter = ttk.Entry(frame, width=10)
entry_magneter.grid(row=1, column=1, pady=5)

# Beregn knap
btn_beregn = ttk.Button(frame, text="Beregn", command=beregn)
btn_beregn.grid(row=2, column=0, columnspan=2, pady=10)

# Resultatfelt
resultat_text = tk.StringVar()
label_resultat = ttk.Label(frame, textvariable=resultat_text, justify="left", padding="5")
label_resultat.grid(row=3, column=0, columnspan=2, sticky="w")

# Start GUI
root.mainloop()
