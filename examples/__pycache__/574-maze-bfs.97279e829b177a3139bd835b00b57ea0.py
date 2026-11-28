
# apl-source:1
# مثال 574 — حل متاهة ببحث الاتساع
# apl-source:2
# Maze solver BFS
# apl-source:3
# Demonstrates: متاهة، BFS، إعادة بناء الطريق
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/574-maze-bfs.apl
# apl-source:6

# apl-source:7
def تأكد_يساوي(فعلي, متوقع, اسم):
    # apl-source:8
    if فعلي != متوقع:
        # apl-source:9
        print("فشل:", اسم, "| متوقع:", متوقع, "| فعلي:", فعلي)
        # apl-source:10
        قياسي_نظام_اخرج(1)
    # apl-source:11
    print("ناجح:", اسم)
# apl-source:12

# apl-source:13

# apl-source:14
# أقصر طريق في متاهة بـ BFS مع رسم المسار
# apl-source:15
متاهة = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0],[1,1,0,0,0],[0,0,0,1,0]]
# apl-source:16
بداية = [0, 0]
# apl-source:17
نهاية = [4, 4]
# apl-source:18

# apl-source:19
def مفتاح(ن):
    # apl-source:20
    return str(ن[0]) + "," + str(ن[1])
# apl-source:21

# apl-source:22
طابور = [بداية]
# apl-source:23
أصل = dict()
# apl-source:24
أصل[مفتاح(بداية)] = ""
# apl-source:25
while len(طابور) > 0:
    # apl-source:26
    حالي = طابور.pop(0)
    # apl-source:27
    if حالي == نهاية:
        # apl-source:28
        break
    # apl-source:29
    for حركة in [[1,0],[-1,0],[0,1],[0,-1]]:
        # apl-source:30
        جار = [حالي[0] + حركة[0], حالي[1] + حركة[1]]
        # apl-source:31
        if جار[0] >= 0 and جار[0] <= 4 and جار[1] >= 0 and جار[1] <= 4:
            # apl-source:32
            if متاهة[جار[0]][جار[1]] == 0 and مفتاح(جار) not in أصل:
                # apl-source:33
                أصل[مفتاح(جار)] = مفتاح(حالي)
                # apl-source:34
                طابور.append(جار)
# apl-source:35

# apl-source:36
مسار = list()
# apl-source:37
if مفتاح(نهاية) in أصل:
    # apl-source:38
    ن = نهاية
    # apl-source:39
    while أصل[مفتاح(ن)] != "":
        # apl-source:40
        مسار.append(ن)
        # apl-source:41
        جزأين = أصل[مفتاح(ن)].split(",")
        # apl-source:42
        ن = [int(جزأين[0]), int(جزأين[1])]
    # apl-source:43
    مسار.append(بداية)
    # apl-source:44
    مسار = مسار[::-1]
# apl-source:45
print("طول المسار:", len(مسار) - 1)
# apl-source:46
تأكد_يساوي(len(مسار) - 1, 8, "أقصر طريق 8 خطوات")
# apl-source:47
تأكد_يساوي(مسار[0], بداية, "يبدأ من البداية")
# apl-source:48
تأكد_يساوي(مسار[len(مسار) - 1], نهاية, "ينتهي عند النهاية")
# apl-source:49
