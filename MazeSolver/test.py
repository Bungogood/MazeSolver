start_colour = [255,0,0]
end_colour = [0,0,255]
steps = 25

colour = start_colour
step = [(e-s)/(steps-1) for s,e in zip(start_colour,end_colour)]
for i in range(steps):
    print((int(v) for v in colour))
    colour = [c+s for c,s in zip(colour,step)]

