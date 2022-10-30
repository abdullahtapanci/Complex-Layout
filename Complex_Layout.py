from PIL import Image, ImageDraw
import random
if random.uniform(0,1)<0.5:
    pwidth=6000
    pheight=4000
else:
    pwidth = 4000
    pheight = 6000
image=Image.new("RGB",(pwidth,pheight),color="white")
draw=ImageDraw.Draw(image)
width=random.choice((1,2))
color_intensity=random.choice((350,500,1000,2000))
padding=random.choice((-1000,0,400,800))
repeat=random.choice((100,450,800))
border=random.choice(("Yes","No"))
def tangled_lines(func_number,listx,listy,list_of_rectangles_points):
    listx.sort()
    listy.sort()
    while True:
        x1 = random.choice(listx)
        indexx = listx.index(x1)
        if indexx + 1 >= len(listx):
            continue
        else:
            x2 = listx[indexx + 1]
            break
    while True:
        y1 = random.choice(listy)
        indexy = listy.index(y1)
        if indexy + 1 >= len(listy):
            continue
        else:
            y2 = listy[indexy + 1]
            break
    list_of_rectangles_points.append([x1, x2, y1, y2])
    if func_number==1:
        draw.line((x1, y1, x1, y2), fill="black", width=width)
        draw.line((x2, y1, x2, y2), fill="black", width=width)
    else:
        draw.line((x1, y1, x2, y1), fill="black", width=width)
        draw.line((x1, y2, x2, y2), fill="black", width=width)
    start_x = random.uniform(x1, x2)
    start_y = random.uniform(y1, y2)
    draw.ellipse((start_x - 4, start_y - 4, start_x + 4, start_y + 4), fill="black")
    for _ in range(10):
        end_x = random.uniform(x1, x2)
        end_y = random.uniform(y1, y2)
        draw.line((start_x, start_y, end_x, end_y), fill="black", width=5*width)
        draw.ellipse((end_x - ((5*width)/2), end_y -  ((5*width)/2), end_x + ((5*width)/2), end_y +  ((5*width)/2)), fill="black")
        start_x = end_x
        start_y = end_y
def lines(func_number,listx,listy,list_of_rectangles_points):
    listx.sort()
    listy.sort()
    while True:
        while True:
            x1 = random.choice(listx)
            indexx = listx.index(x1)
            if indexx + 1 >= len(listx):
                continue
            else:
                x2 = listx[indexx + 1]
                break
        while True:
            y1 = random.choice(listy)
            indexy = listy.index(y1)
            if indexy + 1 >= len(listy):
                continue
            else:
                y2 = listy[indexy + 1]
                break
        if [x1, x2, y1, y2] in list_of_rectangles_points:
            continue
        else:
            list_of_rectangles_points.append([x1, x2, y1, y2])
            break
    k= random.choice((10,20,40))
    if func_number==1:
        draw.line((x1, y1, x1, y2), fill="black", width=width)
        draw.line((x2, y1, x2, y2), fill="black", width=width)
        while True:
            draw.line((x1, y1, x2, y1), fill="black", width=2*width)
            y1 += k
            if y1 >= y2:
                break
            else:
                continue
    else:
        draw.line((x1, y1, x2, y1), fill="black", width=width)
        draw.line((x1, y2, x2, y2), fill="black", width=width)
        while True:
            draw.line((x1, y1, x1, y2), fill="black", width=2*width)
            x1 += k
            if x1 >= x2:
                break
            else:
                continue
def linetangle(func_number,listx,listy,list_of_rectangles_points):
    listx.sort()
    listy.sort()
    while True:
        while True:
            x1 = random.choice(listx)
            indexx = listx.index(x1)
            if indexx + 1 >= len(listx):
                continue
            else:
                x2 = listx[indexx + 1]
                break
        while True:
            y1 = random.choice(listy)
            indexy = listy.index(y1)
            if indexy + 1 >= len(listy):
                continue
            else:
                y2 = listy[indexy + 1]
                break
        if [x1, x2, y1, y2] in list_of_rectangles_points:
            continue
        else:
            list_of_rectangles_points.append([x1, x2, y1, y2])
            break
    if func_number == 1:
        draw.line((x1, y1, x1, y2), fill="black", width=width)
        draw.line((x2, y1, x2, y2), fill="black", width=width)
    else:
        draw.line((x1, y1, x2, y1), fill="black", width=width)
        draw.line((x1, y2, x2, y2), fill="black", width=width)
    startx = x1+10
    starty = y1+10
    length=random.choice((10,20,50))
    for _ in range(200):
        for _ in range(200):
            endx = startx + random.choice((length, -length))
            endy = starty + random.choice((length, -length))
            if endx>=x2 or endy>=y2 or endx<=x1 or endy<=y1:
                break
            draw.line((startx, starty, endx, endy), fill="black", width=width*2)
            startx = endx
            starty = endy
def line_circles(func_number,listx,listy,list_of_rectangles_points):
    listx.sort()
    listy.sort()
    while True:
        while True:
            x1 = random.choice(listx)
            indexx = listx.index(x1)
            if indexx + 1 >= len(listx):
                continue
            else:
                x2 = listx[indexx + 1]
                break
        while True:
            y1 = random.choice(listy)
            indexy = listy.index(y1)
            if indexy + 1 >= len(listy):
                continue
            else:
                y2 = listy[indexy + 1]
                break
        if [x1, x2, y1, y2] in list_of_rectangles_points:
            continue
        else:
            list_of_rectangles_points.append([x1, x2, y1, y2])
            break
    if func_number == 1:
        draw.line((x1, y1, x1, y2), fill="black", width=width)
        draw.line((x2, y1, x2, y2), fill="black", width=width)
    else:
        draw.line((x1, y1, x2, y1), fill="black", width=width)
        draw.line((x1, y2, x2, y2), fill="black", width=width)
    mx = (x1 + x2) / 2
    my = (y1 + y2) / 2
    if x2 - x1 <= y2 - y1:
        r = (x2 - x1) / 2
    else:
        r = (y2 - y1) / 2
    startx = mx
    starty = my
    for _ in range(400):
        while True:
            endx = random.uniform(x1, x2)
            endy = random.uniform(y1, y2)
            if abs(startx - endx) < 30 and abs(starty - endy) < 30 and ((endx - mx) ** 2 + (endy - my) ** 2) ** (
                    1 / 2) <= r:
                break
        draw.line((startx, starty, endx, endy), fill="black", width=width*2)
        startx = endx
        starty = endy
def ordered_circles(func_number,listx,listy,list_of_rectangles_points):
    number=random.uniform(0,1)
    listx.sort()
    listy.sort()
    while True:
        while True:
            x1 = random.choice(listx)
            indexx = listx.index(x1)
            if indexx + 1 >= len(listx):
                continue
            else:
                x2 = listx[indexx + 1]
                break
        while True:
            y1 = random.choice(listy)
            indexy = listy.index(y1)
            if indexy + 1 >= len(listy):
                continue
            else:
                y2 = listy[indexy + 1]
                break
        if [x1, x2, y1, y2] in list_of_rectangles_points:
            continue
        else:
            list_of_rectangles_points.append([x1, x2, y1, y2])
            break
    if func_number == 1:
        draw.line((x1, y1, x1, y2), fill="black", width=width)
        draw.line((x2, y1, x2, y2), fill="black", width=width)
    else:
        draw.line((x1, y1, x2, y1), fill="black", width=width)
        draw.line((x1, y2, x2, y2), fill="black", width=width)
    r=random.choice((15,25,40))
    k=2*r
    mp=[x1,y1+k]
    while True:
        if x2-x1<=100 or y2-y1<=100:
            break
        if mp[0]+2*k>=x2:
            mp[0]=x1+k
            mp[1]+=k
        else:
            mp[0]+=k
        if mp[1]+k>=y2:
            break
        if number<0.2:
            draw.ellipse((mp[0] - r, mp[1] - r, mp[0] + r, mp[1] + r), outline="black", width=4 * width)
        elif number<0.4:
            draw.rounded_rectangle((mp[0] - r, mp[1] - r, mp[0] + r, mp[1] + r), outline="black",radius=10, width=4 * width)
        elif number<0.6:
            draw.arc((mp[0] - r, mp[1] - r, mp[0] + r, mp[1] + r), start=random.uniform(0,360),end=random.uniform(0,360),fill="black",width=4 * width)
        elif number<0.8:
            pass
            """ draw.pieslice((mp[0] - r, mp[1] - r, mp[0] + r, mp[1] + r), start=random.uniform(0,360),end=random.uniform(0,360),fill="black",width=4 * width)"""
        else:
            draw.rectangle((mp[0] - r, mp[1] - r, mp[0] + r, mp[1] + r), outline="black",width=4 * 2)
            draw.ellipse((mp[0] - r, mp[1] - r, mp[0] + r, mp[1] + r), outline="black", width=4 * 2)
def nested_circles(func_number,listx,listy,list_of_rectangles_points):
    listx.sort()
    listy.sort()
    while True:
        while True:
            x1 = random.choice(listx)
            indexx = listx.index(x1)
            if indexx + 1 >= len(listx):
                continue
            else:
                x2 = listx[indexx + 1]
                break
        while True:
            y1 = random.choice(listy)
            indexy = listy.index(y1)
            if indexy + 1 >= len(listy):
                continue
            else:
                y2 = listy[indexy + 1]
                break
        if [x1, x2, y1, y2] in list_of_rectangles_points:
            continue
        else:
            list_of_rectangles_points.append([x1, x2, y1, y2])
            break
    if func_number == 1:
        draw.line((x1, y1, x1, y2), fill="black", width=width)
        draw.line((x2, y1, x2, y2), fill="black", width=width)
    else:
        draw.line((x1, y1, x2, y1), fill="black", width=width)
        draw.line((x1, y2, x2, y2), fill="black", width=width)
    centre_point_x = (x2 + x1) / 2
    centre_point_y = (y2 + y1) / 2
    if x2 - x1 <= y2 - y1:
        r = (x2 - x1) / 2
    else:
        r = (y2 - y1) / 2
    while True:
        draw.ellipse((centre_point_x - r, centre_point_y - r, centre_point_x + r, centre_point_y + r), outline="black",
                     width=4*width)
        r -= random.randint(10, 50)
        if r <= 10:
            break
def fourtlex_lines(func_number, listx, listy, list_of_rectangles_points):
    listx.sort()
    listy.sort()
    while True:
        while True:
            x1 = random.choice(listx)
            indexx = listx.index(x1)
            if indexx + 1 >= len(listx):
                continue
            else:
                x2 = listx[indexx + 1]
                break
        while True:
            y1 = random.choice(listy)
            indexy = listy.index(y1)
            if indexy + 1 >= len(listy):
                continue
            else:
                y2 = listy[indexy + 1]
                break
        if [x1, x2, y1, y2] in list_of_rectangles_points:
            continue
        else:
            list_of_rectangles_points.append([x1, x2, y1, y2])
            break
    if func_number == 1:
        draw.line((x1, y1, x1, y2), fill="black", width=width)
        draw.line((x2, y1, x2, y2), fill="black", width=width)
    else:
        draw.line((x1, y1, x2, y1), fill="black", width=width)
        draw.line((x1, y2, x2, y2), fill="black", width=width)
    for _ in range(5):
        p1 = random.uniform(x1, x2)
        p2 = random.uniform(y1, y2)
        p3 = random.uniform(x1, x2)
        p4 = random.uniform(y1, y2)
        gap = 10
        for _ in range(4):
            draw.line((p1 - gap, p2 + gap, p3 - gap, p4 + gap), width=3*width, fill="black")
            gap += 10
            if p1 - gap <= x1 or p4 + gap >= y2 or p2 + gap >= y2 or p3 - gap <= x1:
                break
def curves(func_number,listx,listy,list_of_rectangles_points):
    listx.sort()
    listy.sort()
    while True:
        while True:
            x1 = random.choice(listx)
            indexx = listx.index(x1)
            if indexx + 1 >= len(listx):
                continue
            else:
                x2 = listx[indexx + 1]
                break
        while True:
            y1 = random.choice(listy)
            indexy = listy.index(y1)
            if indexy + 1 >= len(listy):
                continue
            else:
                y2 = listy[indexy + 1]
                break
        if [x1, x2, y1, y2] in list_of_rectangles_points:
            continue
        else:
            list_of_rectangles_points.append([x1, x2, y1, y2])
            break
    if func_number == 1:
        draw.line((x1, y1, x1, y2), fill="black", width=width)
        draw.line((x2, y1, x2, y2), fill="black", width=width)
    else:
        draw.line((x1, y1, x2, y1), fill="black", width=width)
        draw.line((x1, y2, x2, y2), fill="black", width=width)
    for _ in range(random.choice((1,2))):
        p0x = random.uniform(x1, x2)
        p0y = random.uniform(y1, y2)
        p1x = random.uniform(x1, x2)
        p1y = random.uniform(y1, y2)
        p2x = random.uniform(x1, x2)
        p2y = random.uniform(y1, y2)
        p3x = random.uniform(x1, x2)
        p3y = random.uniform(y1, y2)
        p4x = random.uniform(x1, x2)
        p4y = random.uniform(y1, y2)
        p5x = random.uniform(x1, x2)
        p5y = random.uniform(y1, y2)
        p6x = random.uniform(x1, x2)
        p6y = random.uniform(y1, y2)
        p7x = random.uniform(x1, x2)
        p7y = random.uniform(y1, y2)
        p8x = random.uniform(x1, x2)
        p8y = random.uniform(y1, y2)
        p9x = random.uniform(x1, x2)
        p9y = random.uniform(y1, y2)
        p10x = random.uniform(x1, x2)
        p10y = random.uniform(y1, y2)
        p11x = random.uniform(x1, x2)
        p11y = random.uniform(y1, y2)
        p12x = random.uniform(x1, x2)
        p12y = random.uniform(y1, y2)
        p13x = random.uniform(x1, x2)
        p13y = random.uniform(y1, y2)
        p14x = random.uniform(x1, x2)
        p14y = random.uniform(y1, y2)
        p15x = random.uniform(x1, x2)
        p15y = random.uniform(y1, y2)
        p16x = random.uniform(x1, x2)
        p16y = random.uniform(y1, y2)
        p17x = random.uniform(x1, x2)
        p17y = random.uniform(y1, y2)
        p18x = random.uniform(x1, x2)
        p18y = random.uniform(y1, y2)
        p19x = random.uniform(x1, x2)
        p19y = random.uniform(y1, y2)
        p20x = random.choice((random.uniform(x1, x2),p0x))
        p20y = random.choice((random.uniform(y1, y2),p0y))
        points = []
        t = 0
        points.append((p0x, p0y))
        while True:
            cx = p0x * (1 - t) ** 20 + p1x * 20 * t * (1 - t) ** 19 + p2x * 190 * t ** 2 * (1 - t) ** 18 + p3x * 1140 * t ** 3 * (1 - t) ** 17 + p4x * (15 * 19 * 17) * t ** 4 * (1 - t) ** 16 + p5x * (19 * 17 * 16 * 3) * t ** 5 * (1 - t) ** 15 + p6x * (19 * 17 * 15 * 8) * t ** 6 * (1 - t) ** 14 + p7x * (19 * 17 * 16 * 15) * t ** 7 * (1 - t) ** 13 + p8x * (19 * 17 * 15 * 13 * 2) * t ** 8 * (1 - t) ** 12 + p9x * (19 * 17 * 40 * 13) * t ** 9 * (1 - t) ** 11 + p10x * (19 * 17 * 13 * 11*4) * t ** 10 * (1 - t) ** 10 + p11x * (19 * 17 * 40 * 13) * t ** 11 * (1 - t) ** 9 + p12x * (19 * 17 * 30 * 13) * t ** 12 * (1 - t) ** 8 + p13x * (19 * 17 * 16 * 15) * t ** 13 * (1 - t) ** 7 + p14x * (19 * 17 * 15 * 8) * t ** 14 * (1 - t) ** 6 + p15x * (19 * 17 * 16 * 3) * t ** 15 * (1 - t) ** 5 + p16x * (15 * 19 * 17) * t ** 16 * (1 - t) ** 4 + p17x * 1140 * t ** 17 * (1 - t) ** 3 + p18x * 190 * t ** 18 * (1 - t) ** 2 + p19x * 20 * t ** 19 * (1 - t) + p20x * t ** 20
            cy = p0y * (1 - t) ** 20 + p1y * 20 * t * (1 - t) ** 19 + p2y * 190 * t ** 2 * (1 - t) ** 18 + p3y * 1140 * t ** 3 * (1 - t) ** 17 + p4y * (15 * 19 * 17) * t ** 4 * (1 - t) ** 16 + p5y * (19 * 17 * 16 * 3) * t ** 5 * (1 - t) ** 15 + p6y * (19 * 17 * 15 * 8) * t ** 6 * (1 - t) ** 14 + p7y * (19 * 17 * 16 * 15) * t ** 7 * (1 - t) ** 13 + p8y * (19 * 17 * 15 * 13 * 2) * t ** 8 * (1 - t) ** 12 + p9y * (19 * 17 * 40 * 13) * t ** 9 * (1 - t) ** 11 + p10y * (19 * 17 * 13 * 11*4) * t ** 10 * (1 - t) ** 10 + p11y * (19 * 17 * 40 * 13) * t ** 11 * (1 - t) ** 9 + p12y * (19 * 17 * 30 * 13) * t ** 12 * (1 - t) ** 8 + p13y * (19 * 17 * 16 * 15) * t ** 13 * (1 - t) ** 7 + p14y * (19 * 17 * 15 * 8) * t ** 14 * (1 - t) ** 6 + p15y * (19 * 17 * 16 * 3) * t ** 15 * (1 - t) ** 5 + p16y * (15 * 19 * 17) * t ** 16 * (1 - t) ** 4 + p17y * 1140 * t ** 17 * (1 - t) ** 3 + p18y * 190 * t ** 18 * (1 - t) ** 2 + p19y * 20 * t ** 19 * (1 - t) + p20y * t ** 20
            points.append((cx, cy))
            t += 0.001
            if t >= 1:
                break
        index = 1
        for i in points:
            draw.line((i, points[index]), width=5*width, fill="black")
            index += 1
            if index >= len(points):
                break
def nested_rectangles(func_number, listx, listy, list_of_rectangles_points):
    listx.sort()
    listy.sort()
    while True:
        while True:
            x1 = random.choice(listx)
            indexx = listx.index(x1)
            if indexx + 1 >= len(listx):
                continue
            else:
                x2 = listx[indexx + 1]
                break
        while True:
            y1 = random.choice(listy)
            indexy = listy.index(y1)
            if indexy + 1 >= len(listy):
                continue
            else:
                y2 = listy[indexy + 1]
                break
        if [x1, x2, y1, y2] in list_of_rectangles_points or abs(x2 - x1) <= 100 or abs(y2 - y1) <= 100:
            continue
        else:
            list_of_rectangles_points.append([x1, x2, y1, y2])
            break
    if func_number == 1:
        draw.line((x1, y1, x1, y2), fill="black", width=width)
        draw.line((x2, y1, x2, y2), fill="black", width=width)
    else:
        draw.line((x1, y1, x2, y1), fill="black", width=width)
        draw.line((x1, y2, x2, y2), fill="black", width=width)
    gap = random.randint(10,30)
    while True:
        draw.rectangle((x1 + gap, y1 + gap, x2 - gap, y2 - gap), outline="black", width=5*width)
        gap += gap
        if x1 + gap >= (x1 + x2) / 2 or y1 + gap >= (y1 + y2) / 2:
            break
coordinate_number = random.randint(0, 3)
def rectangle(repeat,func_number,listx,listy):
    white_line_coordinates = []
    list_of_rectangles_coordinates_x = []
    list_of_rectangles_coordinates_y = []
    listx.sort()
    listy.sort()
    for _ in range(repeat):
        while True:
            x1 = random.choice(listx)
            indexx = listx.index(x1)
            if indexx + 1 >= len(listx):
                continue
            else:
                x2 = listx[indexx + 1]
                list_of_rectangles_coordinates_x.append([x1, x2])
                break
    for _ in range(repeat):
        while True:
            y1 = random.choice(listy)
            indexy = listy.index(y1)
            if indexy + 1 >= len(listy):
                continue
            else:
                y2 = listy[indexy + 1]
                list_of_rectangles_coordinates_y.append([y1, y2])
                break
    shadow = 32
    for i, k in zip(list_of_rectangles_coordinates_x, list_of_rectangles_coordinates_y):
        coordina_list = [[[i[0] - shadow, k[0] - shadow, i[1] - shadow, k[1] - shadow],[i[0] + shadow, k[0] - shadow, i[1] + shadow, k[1] - shadow],[i[0] - shadow, k[0] + shadow, i[1] - shadow, k[1] + shadow],[i[0] + shadow, k[0] + shadow, i[1] + shadow, k[1] + shadow]]]
        for i in coordina_list:
            coordinate = i[coordinate_number]
            draw.rounded_rectangle(coordinate, fill="black", outline="black", width=3*width, radius=20)
    for i in range(len(list_of_rectangles_coordinates_x)):
        color = color_list[0]
        distance1 = list_of_rectangles_coordinates_y[i][1] - list_of_rectangles_coordinates_y[i][0]
        distance2 = list_of_rectangles_coordinates_x[i][1] - list_of_rectangles_coordinates_x[i][0]
        if distance1 <= 400 and distance2 <= 400:
            rng=color_intensity
        else:
            rng=color_intensity*2
        for _ in range(rng):
            a = (random.uniform(list_of_rectangles_coordinates_x[i][0], list_of_rectangles_coordinates_x[i][1]),random.uniform(list_of_rectangles_coordinates_y[i][0], list_of_rectangles_coordinates_y[i][1]))
            b = (random.uniform(list_of_rectangles_coordinates_x[i][0], list_of_rectangles_coordinates_x[i][1]),random.uniform(list_of_rectangles_coordinates_y[i][0], list_of_rectangles_coordinates_y[i][1]))
            c = (random.uniform(list_of_rectangles_coordinates_x[i][0], list_of_rectangles_coordinates_x[i][1]),random.uniform(list_of_rectangles_coordinates_y[i][0], list_of_rectangles_coordinates_y[i][1]))
            draw.polygon((a, b, c), outline=color)
        k = 40
        if func_number==1:
            distance1 = list_of_rectangles_coordinates_y[i][1] - list_of_rectangles_coordinates_y[i][0]
            distance2 = list_of_rectangles_coordinates_x[i][1] - list_of_rectangles_coordinates_x[i][0]
            if distance1 <= 50 or distance2 <= 50:
                pass
            else:
                while True:
                    draw.line((list_of_rectangles_coordinates_x[i][0] + k, list_of_rectangles_coordinates_y[i][0] + k,list_of_rectangles_coordinates_x[i][1] - k, list_of_rectangles_coordinates_y[i][0] + k),fill="white", width=3*width)
                    white_line_coordinates.append([list_of_rectangles_coordinates_x[i][0] + k, list_of_rectangles_coordinates_y[i][0] + k,list_of_rectangles_coordinates_x[i][1] - k, list_of_rectangles_coordinates_y[i][0] + k])
                    list_of_rectangles_coordinates_y[i][0] += 60
                    if list_of_rectangles_coordinates_y[i][0] >= list_of_rectangles_coordinates_y[i][1] - 70:
                        break
                    else:
                        continue
            color_list.pop(0)
            if len(color_list) == 0:
                for i in color_list2:
                    color_list.append(i)
        else:
            distance1 = list_of_rectangles_coordinates_y[i][1] - list_of_rectangles_coordinates_y[i][0]
            distance2 = list_of_rectangles_coordinates_x[i][1] - list_of_rectangles_coordinates_x[i][0]
            if distance1 <= 50 or distance2 <= 50:
                pass
            else:
                while True:
                    draw.line((list_of_rectangles_coordinates_x[i][0] + k,list_of_rectangles_coordinates_y[i][0] + k,list_of_rectangles_coordinates_x[i][0] + k,list_of_rectangles_coordinates_y[i][1] - k), fill="white", width=3*width)
                    list_of_rectangles_coordinates_x[i][0] += 60
                    if list_of_rectangles_coordinates_x[i][0] >= list_of_rectangles_coordinates_x[i][1] - 70:
                        break
                    else:
                        continue
            color_list.pop(0)
            if len(color_list) == 0:
                for i in color_list2:
                    color_list.append(i)
color_list = []
i=255
k=0
l=0
m=255
def a_yellow():
    color_list.append((i,i,i))
    if random.uniform(0,1)<=0.1:
        color_list.extend(((251,221,157),(232,177,45),(79,78,40),(146,95,23),(233,191,89),(0,0,0)))
def a_red():
    color_list.append((i,i,i))
    if random.uniform(0,1)<=0.1:
        color_list.extend(((98,8,16), (98, 8, 16), (197,16,33),(255,137,137),(0, 0, 0)))
def b():
    color_list.append((i,i,k))
    if random.uniform(0,1)<=0.1:
        color_list.extend(((255,222,0), (0,1,122), (255,185,0), (18,55,161)))
def c():
    if random.uniform(0,1)<=0.1:
        color_list.extend(((236,180,172), (60,95,92), (255,215,0), (0,0,0)))
def d():
    color_list.append((k,i,i))
def e():
    color_list.append((i,i,l))
def f():
    color_list.append((i,l,i))
def g():
    color_list.append((l,i,i))
def h():
    color_list.append((i,i,m))
def ı():
    color_list.append((i,m,i))
    if random.uniform(0,1)<=0.1:
        color_list.extend(((51,122,9), (45,83,23), (51,122,9)))
def ii():
    color_list.append((m,i,i))
    if random.uniform(0,1)<=0.1:
        color_list.extend(((98,8,16), (98, 8, 16)))
def j():
    color_list.append((i,k,k))
def ll():
    color_list.append((k,k,i))
def mm():
    color_list.append((i,l,l))
def n():
    color_list.append((l,i,l))
def o():
    color_list.append((l,l,i))
def p():
    color_list.append((i,m,m))
def r():
    color_list.append((m,i,m))
def s():
    color_list.append((m,m,i))
def v():
    color_list.append((l,i,k))
    if random.uniform(0,1)<=0.1:
        color_list.extend(((252,217,20),(16,134,144),(29,30,78)))
def b1():
    color_list.append((i,k,m))
    if random.uniform(0,1)<=0.3:
        color_list.extend(((41, 50, 65), (238, 108, 77)))
def c1():
    color_list.append((i,m,k))
def d1():
    color_list.append((m,i,k))
def e1():
    color_list.append((k,i,m))
def f1():
    color_list.append((k,m,i))
def g1():
    color_list.append((m,k,i))
def h1():
    color_list.append((i,l,m))
def ı1():
    color_list.append((i,m,l))
    if random.uniform(0,1)<=0.1:
        color_list.extend(((0, 117, 66), (0,0,0),(125, 158, 44)))
def i1():
    color_list.append((m,i,l))
def j1():
    color_list.append((l,i,m))
def k1():
    color_list.append((m,l,i))
    if random.uniform(0,1)<=0.5:
        color_list.extend(((255, 195, 5), (255, 87, 51), (144, 12, 63)))
def l1():
    color_list.append((l,m,i))
    if random.uniform(0,1)<=0.2:
        color_list.extend(((0, 48, 86), (1, 152, 117), (127, 140, 141)))
def m1():
    color_list.append((k,k,k))
def n1():
    color_list.append((k,k,l))
def o1():
    color_list.append((k,l,k))
def p1():
    color_list.append((l,k,k))
def r1():
    color_list.append((k,k,m))
def t1():
    color_list.append((m,k,k))
def u1():
    color_list.append((k,l,m))
    if random.uniform(0,1)<=0.4:
        color_list.extend(((53, 80, 112), (109, 89, 122), (181, 101, 118),(229, 107, 111),(234, 172, 139)))
def v1():
    color_list.append((k,m,l))
def y1():
    color_list.append((m,k,l))
def a2():
    color_list.append((l,k,m))
def white():
    color_list.append((m,m,m))
def black_yellow():
    color_list.extend(((255,255,204), (255,255,153), (255,255,102), (255,255,51), (204,204,0),(153,153,0),(102,102,0),(51,51,0)))
def white_red():
    color_list.extend(((240,24,24),(240,216,216), (240,192,192), (240,48,48), (240,48,48), (240,24,24),(60,116,96), (96, 0, 0),(68, 0, 3),(192, 0, 0),(160, 0, 0),(128, 0, 0)))
def black_blue():
    color_list.extend(((0,123,84), (0,98,157), (0,75,131), (0,52,105), (0,32,80), (0,5,57),(0,2,35),(0,0,9),(0, 0, 0)))
def black_brown():
    color_list.extend(((132,105,77), (147,123,100), (163, 142, 122), (101,67,33), (81,54,26),(71,47,23), (61,40,20),(51,34,17),(40,27,13),(30,20,10),(20,13,7),(0, 0, 0)))
def black_purple():
    color_list.extend(((226,168,254), (175,119,213), (126,78,172), (165,135,143), (137,99,120), (110,68,104),(98,25,64), (83,45,132), (46,22,91), (30, 20, 10), (18,6,50), (0, 0, 0)))
def black_orange():
    color_list.extend(((255,152,0), (255,173,51),(255,193,102), (255,149,102), (255,132,77), (255,114,51),(255,97,25), (255,112,52), (204,90,42), (179,78,36), (153,67,31), (77,34,16),(51,22,10),(0,0,0)))
def black_green():
    color_list.extend(((0,66,37), (31,90,59), (57,115,82),(134,195,158),(82,141,106), (108,167,131),(0,99,0), (0,51,0), (0,23,0), (0,74,0), (189,251,212), (0,0,0)))
def blue_green():
    color_list.extend(((12,56,35), (53,136,115), (32,117,103), (136,222,176), (105,198,175),(78,173,175),(55,122,152), (36,74,128), (21,32,105), (20,9,81),(0, 0, 0)))
def color_palette_1():
    color_list.extend(((0,155,179),(203,218,164), (223,229,179), (226,83,83), (204,204,204)))
def color_palette_2():
    color_list.extend(((2,54,100), (4,144,200),(89,199,243), (250,209,5), (230,230,230)))
def color_palette_3():
    color_list.extend(((122,112,108), (254,106,1), (187,194,196),(241,243,243)))
def color_palette_4():
    color_list.extend(((88, 24, 69), (144, 12, 63),(199, 0, 57), (255, 87, 51),(255, 195, 0)))
def color_palette_5():
    color_list.extend(((84, 73, 75), (241, 247, 237), (241, 247, 237), (179, 57, 81), (227, 208, 129)))
def color_palette_6():
    color_list.extend(((2, 14, 84),(255, 234, 184), (166, 222, 174), (255, 112, 10)))
def color_palette_7():
    color_list.extend(((255, 51, 102),(73, 88, 103),(87, 115, 153), (189, 213, 234), (247, 247, 250)))
def color_palette_8():
    color_list.extend(((124, 158, 183),(197, 214, 219), (255, 211, 215),(255, 243, 224), (255, 194, 12),(255, 194, 12)))
def color_palette_9():
    color_list.extend(((250, 135, 65),(162, 25, 50), (12, 8, 47), (4, 5, 19),(40, 55, 66)))
def color_palette_10():
    color_list.extend(((137, 63, 4), (198, 127, 67), (212, 155, 126),(221, 184, 166),(152, 158, 139),(123, 135, 109)))
def color_palette_11():
    color_list.extend(((98,8,16), (11,86,95),(2,48,68),(214,75,0), (180,180,166)))
def color_palette_12():
    color_list.extend(((102,15,86), (40,6,89),(245,73,82), (174,45,104),(66,38,128)))
def color_palette_13():
    color_list.extend(((5,145,66), (20,32,68), (65,105,225),(247, 161, 126)))
def piet_mondrian():
    color_list.extend(((166,41,13), (242,183,5), (4,119,191)))
func = [a_yellow,a_red,b,c,d,e,f,g,h,ı,ii,j,ll,mm,n,o,p,r,s,v,b1,c1,d1,e1,f1,g1,h1,ı1,i1,j1,k1,l1,m1,n1,o1,p1,r1,t1,u1,y1,a2,white,black_yellow,white_red,black_blue,black_brown,black_purple,black_orange,black_green,blue_green,color_palette_1,color_palette_2,color_palette_3,color_palette_4,color_palette_5,color_palette_6,color_palette_7,color_palette_8,color_palette_9,color_palette_10,color_palette_11,color_palette_12,color_palette_13,piet_mondrian]
function = random.choice(func)
for _ in range(255):
    function()
    i -= 1
    k+=1
color_list2=color_list.copy()
def first():
    listx=[padding,pwidth-padding]
    listy=[padding,pheight-padding]
    def horizontal_lines():
        for _ in range(30):
            y = random.uniform(padding, pheight-padding)
            listy.append(y)
            coordinate = (padding,y,pwidth-padding,y)
            draw.line(coordinate, width=width, fill="black")
    horizontal_lines()
    def vertical_lines():
        for _ in range(30):
            y1 = random.choice(listy)
            y2 = random.choice(listy)
            x = random.uniform(padding, pwidth-padding)
            listx.append(x)
            coordinate = (x,y1,x,y2)
            draw.line(coordinate, width=width, fill="black")
    vertical_lines()
    list_of_rectangles_points=[]
    for _ in range(30):
        tangled_lines(1,listx,listy,list_of_rectangles_points)
    for _ in range(50):
        lines(1,listx,listy,list_of_rectangles_points)
    for _ in range(50):
        fourtlex_lines(1,listx, listy, list_of_rectangles_points)
    for _ in range(25):
        nested_rectangles(1,listx, listy, list_of_rectangles_points)
    for _ in range(200):
        nested_circles(1,listx, listy, list_of_rectangles_points)
    for _ in range(150):
        line_circles(1,listx,listy,list_of_rectangles_points)
    for _ in range(250):
        curves(1,listx,listy,list_of_rectangles_points)
    for _ in range(150):
        ordered_circles(1,listx,listy,list_of_rectangles_points)
    for _ in range(50):
        linetangle(1,listx,listy,list_of_rectangles_points)
    rectangle(repeat,1,listx,listy)
def second():
    listx = [padding,pwidth-padding]
    def vertical_lines():
        for _ in range(30):
            x = random.uniform(padding, pwidth-padding)
            listx.append(x)
            coordinate = (x, padding, x, pheight-padding)
            draw.line(coordinate, width=width, fill="black")
    vertical_lines()
    listy = [padding,pheight-padding]
    def horizontal_lines():
        for _ in range(30):
            x1 = random.choice(listx)
            x2 = random.choice(listx)
            y = random.uniform(padding, pheight-padding)
            listy.append(y)
            coordinate = (x1, y, x2, y)
            draw.line(coordinate, width=width, fill="black")
    horizontal_lines()
    list_of_rectangles_points = []
    for _ in range(30):
        tangled_lines(2,listx,listy,list_of_rectangles_points)
    for _ in range(50):
        lines(2,listx,listy,list_of_rectangles_points)
    for _ in range(50):
        fourtlex_lines(2,listx, listy, list_of_rectangles_points)
    for _ in range(25):
        nested_rectangles(2,listx, listy, list_of_rectangles_points)
    for _ in range(200):
        nested_circles(2,listx, listy, list_of_rectangles_points)
    for _ in range(150):
        line_circles(2,listx,listy,list_of_rectangles_points)
    for _ in range(250):
        curves(2,listx,listy,list_of_rectangles_points)
    for _ in range(150):
        ordered_circles(2,listx,listy,list_of_rectangles_points)
    for _ in range(50):
        linetangle(2,listx,listy,list_of_rectangles_points)
    rectangle(repeat, 2, listx, listy)
list_of_func=[first,second]
func=random.choice(list_of_func)
func()
if border=="Yes":
    color=(220,220,220)
    draw.rectangle((0,0,50,pheight),width=50,fill=color)
    draw.rectangle((pwidth-50,0,pwidth,pheight),width=50,fill=color)
    draw.rectangle((0,0,pwidth,100),width=50,fill=color)
    draw.rectangle((0,pheight-100,pwidth,pheight),width=50,fill=color)
image.save(r"C:\Users\ABDULLAH\Desktop\nft.png")