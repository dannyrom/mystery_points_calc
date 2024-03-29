import tkinter as tk

root = tk.Tk()

root.geometry("420x700")
root.title("Mystery Seed Points Calculator")

label = tk.Label(root, text="Mystery Seed Points Calculator", font=("Arial", 18))
label.pack()

points = 0
trace_vars = []

textbox = tk.Text(root, height=1, width=30, font=("Arial", 16))
textbox.pack()
textbox.insert("1.0", "Points Remaining: {}".format(str(points)))
textbox.config(state="disabled")


def hide_entrance():
    frame15.pack_forget()
    frame14.pack(fill="y")
    frame16.pack(fill="y")
    for var in entrance_vars:
        if var in trace_vars:
            trace_vars.remove(var)
    for var in no_entrance_vars:
        if var not in trace_vars:
            trace_vars.append(var)
    points_calc(0, 0, 0)


def hide_non_entrance():
    frame14.pack_forget()
    frame16.pack_forget()
    frame15.pack(fill="y")
    for var in no_entrance_vars:
        if var in trace_vars:
            trace_vars.remove(var)
    for var in entrance_vars:
        if var not in trace_vars:
            trace_vars.append(var)
    points_calc(0, 0, 0)

frame1 = tk.Frame(root)
tk_max_points = tk.IntVar()
trace_vars.append(tk_max_points)
btn_ERoff = tk.Radiobutton(frame1, variable=tk_max_points, value=-150, text="Non-Entrance", font=("Arial", 12, "bold"), command=hide_entrance)
btn_ERoff.grid(row=1, column=1, padx=2, pady=10)
btn_ERon = tk.Radiobutton(frame1, variable=tk_max_points, value=-80, text="Entrance", font=("Arial", 12, "bold"), command=hide_non_entrance)
btn_ERon.grid(row=1, column=2, padx=2, pady=10)
btn_OHKO = tk.Radiobutton(frame1, variable=tk_max_points, value=-50, text="OHKO", font=("Arial", 12, "bold"), command=hide_entrance)
btn_OHKO.grid(row=1, column=3, padx=2, pady=10)
frame1.pack(fill="y")


frame2 = tk.Frame(root)
tk_world_state = tk.IntVar()
trace_vars.append(tk_world_state)
btn_Open = tk.Radiobutton(frame2, variable=tk_world_state, value=1, text="Open", font=("Arial", 10))
btn_Open.grid(row=1, column=1, padx=2, pady=2)
btn_Standard = tk.Radiobutton(frame2, variable=tk_world_state, value=2, text="Standard", font=("Arial", 10))
btn_Standard.grid(row=1, column=2, padx=2, pady=2)
btn_Retro = tk.Radiobutton(frame2, variable=tk_world_state, value=21, text="Retro (20)", font=("Arial", 10))
btn_Retro.grid(row=1, column=3, padx=2, pady=2)
btn_Inverted = tk.Radiobutton(frame2, variable=tk_world_state, value=22, text="Inverted (20)", font=("Arial", 10))
btn_Inverted.grid(row=1, column=4, padx=2, pady=2)
frame2.pack(fill="x")

frame3 = tk.Frame(root)
tk_goal = tk.IntVar()
trace_vars.append(tk_goal)
btn_Ganon = tk.Radiobutton(frame3, variable=tk_goal, value=1, text="Ganon", font=("Arial", 10))
btn_Ganon.grid(row=1, column=1, padx=2, pady=2)
btn_Fast = tk.Radiobutton(frame3, variable=tk_goal, value=2, text="Fast G.", font=("Arial", 10))
btn_Fast.grid(row=1, column=2, padx=2, pady=2)
btn_AD = tk.Radiobutton(frame3, variable=tk_goal, value=11, text="AD (10)", font=("Arial", 10))
btn_AD.grid(row=1, column=3, padx=2, pady=2)
btn_Pedestal = tk.Radiobutton(frame3, variable=tk_goal, value=12, text="Ped. (10)", font=("Arial", 10))
btn_Pedestal.grid(row=1, column=4, padx=2, pady=2)
btn_Triforce = tk.Radiobutton(frame3, variable=tk_goal, value=20, text="Triforce (20)", font=("Arial", 10))
btn_Triforce.grid(row=1, column=5, padx=2, pady=2)
frame3.pack(fill="x")

frame4 = tk.Frame(root)
tk_swords = tk.IntVar()
trace_vars.append(tk_swords)
btn_Sword = tk.Radiobutton(frame4, variable=tk_swords, value=1, text="Rand. Swords", font=("Arial", 10))
btn_Sword.grid(row=1, column=1, padx=2, pady=2)
btn_Assured = tk.Radiobutton(frame4, variable=tk_swords, value=2, text="Assured", font=("Arial", 10))
btn_Assured.grid(row=1, column=2, padx=2, pady=2)
btn_Vanilla = tk.Radiobutton(frame4, variable=tk_swords, value=10, text="Vanilla (10)", font=("Arial", 10))
btn_Vanilla.grid(row=1, column=3, padx=2, pady=2)
btn_Swordless = tk.Radiobutton(frame4, variable=tk_swords, value=20, text="Swordless (20)", font=("Arial", 10))
btn_Swordless.grid(row=1, column=4, padx=2, pady=2)
frame4.pack(fill="x")

frame5 = tk.Frame(root)
tk_item_pool = tk.IntVar()
trace_vars.append(tk_item_pool)
btn_NItems = tk.Radiobutton(frame5, variable=tk_item_pool, value=1, text="Normal Items", font=("Arial", 10))
btn_NItems.grid(row=1, column=1, padx=2, pady=2)
btn_HItems = tk.Radiobutton(frame5, variable=tk_item_pool, value=20, text="Hard Items (20)", font=("Arial", 10))
btn_HItems.grid(row=1, column=2, padx=2, pady=2)
btn_EItems = tk.Radiobutton(frame5, variable=tk_item_pool, value=40, text="Expert Items (40)", font=("Arial", 10))
btn_EItems.grid(row=1, column=3, padx=2, pady=2)
frame5.pack(fill="x")

frame6 = tk.Frame(root)
tk_accessibility = tk.IntVar()
trace_vars.append(tk_accessibility)
btn_100 = tk.Radiobutton(frame6, variable=tk_accessibility, value=1, text="100% Accessibility", font=("Arial", 10))
btn_100.grid(row=1, column=1, padx=2, pady=2)
btn_Beat = tk.Radiobutton(frame6, variable=tk_accessibility, value=10, text="Beatable Only (10)", font=("Arial", 10))
btn_Beat.grid(row=1, column=2, padx=2, pady=2)
frame6.pack(fill="x")

frame7 = tk.Frame(root)
tk_GT_open = tk.IntVar()
trace_vars.append(tk_GT_open)
btn_Tower5 = tk.Radiobutton(frame7, variable=tk_GT_open, value=1, text="5-7 Crystal GT", font=("Arial", 10))
btn_Tower5.grid(row=1, column=1, padx=2, pady=2)
btn_Tower2 = tk.Radiobutton(frame7, variable=tk_GT_open, value=10, text="2-4 Crystal GT (10)", font=("Arial", 10))
btn_Tower2.grid(row=1, column=2, padx=2, pady=2)
btn_Tower0 = tk.Radiobutton(frame7, variable=tk_GT_open, value=20, text="0-1 Crystal GT (20)", font=("Arial", 10))
btn_Tower0.grid(row=1, column=3, padx=2, pady=2)
frame7.pack(fill="x")

frame8 = tk.Frame(root)
tk_vuln = tk.IntVar()
trace_vars.append(tk_vuln)
btn_Vuln5 = tk.Radiobutton(frame8, variable=tk_vuln, value=1, text="3-4 Crystal Ganon Vuln.", font=("Arial", 10))
btn_Vuln5.grid(row=1, column=1, padx=2, pady=2)
btn_Vuln3 = tk.Radiobutton(frame8, variable=tk_vuln, value=10, text="5-7 Crystal Ganon Vuln. (10)", font=("Arial", 10))
btn_Vuln3.grid(row=1, column=2, padx=2, pady=2)
frame8.pack(fill="x")

frame9 = tk.Frame(root)
tk_hints = tk.IntVar()
trace_vars.append(tk_hints)
btn_HintsOff = tk.Radiobutton(frame9, variable=tk_hints, value=1, text="Hints Off", font=("Arial", 10))
btn_HintsOff.grid(row=1, column=1, padx=2, pady=2)
btn_HintsOn = tk.Radiobutton(frame9, variable=tk_hints, value=2, text="Hints On", font=("Arial", 10))
btn_HintsOn.grid(row=1, column=2, padx=2, pady=2)
frame9.pack(fill="x")

frame10 = tk.Frame(root)
tk_boss = tk.IntVar()
trace_vars.append(tk_boss)
btn_NoBoss = tk.Radiobutton(frame10, variable=tk_boss, value=1, text="No Boss Shuffle", font=("Arial", 10))
btn_NoBoss.grid(row=1, column=1, padx=2, pady=2)
btn_FullBoss = tk.Radiobutton(frame10, variable=tk_boss, value=20, text="Full Boss S. (20)", font=("Arial", 10))
btn_FullBoss.grid(row=1, column=2, padx=2, pady=2)
btn_ChaosBoss = tk.Radiobutton(frame10, variable=tk_boss, value=30, text="Chaos Boss S. (30)", font=("Arial", 10))
btn_ChaosBoss.grid(row=1, column=3, padx=2, pady=2)
frame10.pack(fill="x")

frame11 = tk.Frame(root)
tk_enemizer = tk.IntVar()
trace_vars.append(tk_enemizer)
btn_NoEnemy = tk.Radiobutton(frame11, variable=tk_enemizer, value=1, text="No Enemizer", font=("Arial", 10))
btn_NoEnemy.grid(row=1, column=1, padx=2, pady=2)
btn_Enemizer = tk.Radiobutton(frame11, variable=tk_enemizer, value=20, text="Enemizer (20)", font=("Arial", 10))
btn_Enemizer.grid(row=1, column=2, padx=2, pady=2)
frame11.pack(fill="x")

frame12 = tk.Frame(root)
tk_damage = tk.IntVar()
trace_vars.append(tk_damage)
btn_NoDamage = tk.Radiobutton(frame12, variable=tk_damage, value=1, text="Normal Enemy Damage", font=("Arial", 10))
btn_NoDamage.grid(row=1, column=1, padx=2, pady=2)
btn_DamageShuffle = tk.Radiobutton(frame12, variable=tk_damage, value=30, text="Shuffled (30)", font=("Arial", 10))
btn_DamageShuffle.grid(row=1, column=2, padx=2, pady=2)
frame12.pack(fill="x")

frame13 = tk.Frame(root)
tk_health = tk.IntVar()
trace_vars.append(tk_health)
btn_NormalHealth = tk.Radiobutton(frame13, variable=tk_health, value=1, text="Normal Enemy Health", font=("Arial", 10))
btn_NormalHealth.grid(row=1, column=1, padx=2, pady=2)
btn_EasyHealth = tk.Radiobutton(frame13, variable=tk_health, value=-20, text="Easy (-20)", font=("Arial", 10))
btn_EasyHealth.grid(row=1, column=2, padx=2, pady=2)
btn_HardHealth = tk.Radiobutton(frame13, variable=tk_health, value=30, text="Hard (30)", font=("Arial", 10))
btn_HardHealth.grid(row=1, column=3, padx=2, pady=2)
frame13.pack(fill="x")

frame14 = tk.Frame(root)
tk_maps = tk.IntVar()
trace_vars.append(tk_maps)
tk_compasses = tk.IntVar()
trace_vars.append(tk_compasses)
tk_big_keys = tk.IntVar()
trace_vars.append(tk_big_keys)
tk_small_keys = tk.IntVar()
trace_vars.append(tk_small_keys)
btn_Maps = tk.Checkbutton(frame14, variable=tk_maps, onvalue=10, text="Maps (10)", font=("Arial", 10))
btn_Maps.grid(row=1, column=1, padx=2, pady=2)
btn_Compasses = tk.Checkbutton(frame14, variable=tk_compasses, onvalue=10, text="Compasses (10)", font=("Arial", 10))
btn_Compasses.grid(row=1, column=2, padx=2, pady=2)
btn_BKs = tk.Checkbutton(frame14, variable=tk_big_keys, onvalue=10, text="BKs (10)", font=("Arial", 10))
btn_BKs.grid(row=1, column=3, padx=2, pady=2)
btn_SKs = tk.Checkbutton(frame14, variable=tk_small_keys, onvalue=10, text="SKs (10)", font=("Arial", 10))
btn_SKs.grid(row=1, column=4, padx=2, pady=2)
frame14.pack(fill="y")

frame15 = tk.Frame(root)
tk_EKeys = tk.IntVar()
trace_vars.append(tk_EKeys)
tk_ERest = tk.IntVar()
trace_vars.append(tk_ERest)
btn_EKeys = tk.Checkbutton(frame15, variable=tk_EKeys, onvalue=10, text="Entrance Keysanity (10)", font=("Arial", 10))
btn_EKeys.grid(row=1, column=1, padx=2, pady=2)
btn_ERest = tk.Checkbutton(frame15, variable=tk_ERest, onvalue=10, text="Restricted Entrances (10)", font=("Arial", 10))
btn_ERest.grid(row=1, column=2, padx=2, pady=2)
frame15.pack(fill="y")

frame16 = tk.Frame(root)
tk_hookshot = tk.IntVar()
trace_vars.append(tk_hookshot)
tk_fire_rod = tk.IntVar()
trace_vars.append(tk_fire_rod)
tk_ice_rod = tk.IntVar()
trace_vars.append(tk_ice_rod)
tk_flippers = tk.IntVar()
trace_vars.append(tk_flippers)
tk_flute = tk.IntVar()
trace_vars.append(tk_flute)
tk_mirror = tk.IntVar()
trace_vars.append(tk_mirror)
tk_boots = tk.IntVar()
trace_vars.append(tk_boots)
starting_text = tk.Label(frame16, text="Starting Items", font=("Arial", 10, "underline", "bold"))
starting_text.grid(row=1, column=1, columnspan=3, padx=2, pady=2)
btn_Hookshot = tk.Checkbutton(frame16, variable=tk_hookshot, onvalue=-2, text="Hookshot", font=("Arial", 10))
btn_FireRod = tk.Checkbutton(frame16, variable=tk_fire_rod, onvalue=-1, text="Fire Rod", font=("Arial", 10))
btn_IceRod = tk.Checkbutton(frame16, variable=tk_ice_rod, onvalue=-3, text="Ice Rod", font=("Arial", 10))
btn_Flippers = tk.Checkbutton(frame16, variable=tk_flippers, onvalue=1, text="Flippers", font=("Arial", 10))
btn_Flute = tk.Checkbutton(frame16, variable=tk_flute, onvalue=2, text="Flute", font=("Arial", 10))
btn_Mirror = tk.Checkbutton(frame16, variable=tk_mirror, onvalue=3, text="Mirror", font=("Arial", 10))
btn_Boots = tk.Checkbutton(frame16, variable=tk_boots, onvalue=4, text="Boots", font=("Arial", 10))
btn_Hookshot.grid(row=2, column=1, padx=2, pady=2)
btn_FireRod.grid(row=2, column=2, padx=2, pady=2)
btn_IceRod.grid(row=2, column=3, padx=2, pady=2)
btn_Flippers.grid(row=3, column=1, padx=2, pady=2)
btn_Flute.grid(row=3, column=2, padx=2, pady=2)
btn_Mirror.grid(row=3, column=3, padx=2, pady=2)
btn_Boots.grid(row=4, column=2, padx=2, pady=2)
frame16.pack(fill="y")

credit = tk.Label(root, text="by dannymusic", font=("Arial", 7))
credit.place(x="350", y="684")

entrance_vars = [tk_EKeys, tk_ERest]
no_entrance_vars = [tk_maps, tk_compasses, tk_big_keys, tk_small_keys, tk_hookshot, tk_fire_rod, tk_ice_rod, tk_flippers, tk_flute, tk_mirror, tk_boots]


def points_calc(a, b, c):
    newpoints = 0
    textbox.config(state="normal")
    for var in trace_vars:
        newpoints -= round(var.get(), -1)
    points = newpoints
    textbox.delete("1.0", tk.END)
    textbox.insert("1.0", "Points Remaining: {}".format(str(points-10))+"-"+str(points+10))
    textbox.config(state="disabled")
    return textbox


for var in trace_vars:
    var.trace_add("write", points_calc)

root.mainloop()
