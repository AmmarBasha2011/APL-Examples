
# apl-source:1
# مثال 537 — بحث A* على شبكة
# apl-source:2
# A* grid search
# apl-source:3
# Demonstrates: A*، استدلال مانهاتن، إعادة بناء المسار
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/537-a-star.apl
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
# بحث A* على شبكة بعوائق (استدلال مانهاتن)
# apl-source:15
شبكة = [[0,0,0,0,0],[1,1,0,1,0],[0,0,0,1,0],[0,1,1,1,0],[0,0,0,0,0]]
# apl-source:16
بداية = [0, 0]
# apl-source:17
هدف = [4, 4]
# apl-source:18

# apl-source:19
def استدلال(ن):
    # apl-source:20
    return مطلق_قيمة(ن[0] - هدف[0]) + مطلق_قيمة(ن[1] - هدف[1])
# apl-source:21

# apl-source:22
def مطلق_قيمة(س):
    # apl-source:23
    if س < 0:
        # apl-source:24
        return 0 - س
    # apl-source:25
    return س
# apl-source:26

# apl-source:27
مفتوح = [[استدلال(بداية), 0, بداية]]
# apl-source:28
أصل = dict()
# apl-source:29
كلفة = {"0,0": 0}
# apl-source:30
وجد = False
# apl-source:31

# apl-source:32
while len(مفتوح) > 0:
    # apl-source:33
    أقل_i = 0
    # apl-source:34
    for i in range(len(مفتوح)):
        # apl-source:35
        if مفتوح[i][0] < مفتوح[أقل_i][0]:
            # apl-source:36
            أقل_i = i
    # apl-source:37
    حالي = مفتوح.pop(أقل_i)
    # apl-source:38
    if حالي[2] == هدف:
        # apl-source:39
        وجد = True
        # apl-source:40
        break
    # apl-source:41
    for حركة in [[1,0],[-1,0],[0,1],[0,-1]]:
        # apl-source:42
        جار = [حالي[2][0] + حركة[0], حالي[2][1] + حركة[1]]
        # apl-source:43
        if جار[0] >= 0 and جار[0] <= 4 and جار[1] >= 0 and جار[1] <= 4 and شبكة[جار[0]][جار[1]] == 0:
            # apl-source:44
            مفتاح = str(جار[0]) + "," + str(جار[1])
            # apl-source:45
            كلفة_جديدة = حالي[1] + 1
            # apl-source:46
            if مفتاح not in كلفة or كلفة_جديدة < كلفة[مفتاح]:
                # apl-source:47
                كلفة[مفتاح] = كلفة_جديدة
                # apl-source:48
                أصل[مفتاح] = حالي[2]
                # apl-source:49
                مفتوح.append([كلفة_جديدة + استدلال(جار), كلفة_جديدة, جار])
# apl-source:50

# apl-source:51
مسار = list()
# apl-source:52
if وجد:
    # apl-source:53
    ن = هدف
    # apl-source:54
    while ن != بداية:
        # apl-source:55
        مسار.append(ن)
        # apl-source:56
        ن = أصل[str(ن[0]) + "," + str(ن[1])]
    # apl-source:57
    مسار.append(بداية)
    # apl-source:58
    مسار = مسار[::-1]
# apl-source:59
print("المسار:", مسار)
# apl-source:60
تأكد_يساوي(وجد, True, "يوجد مسار")
# apl-source:61
تأكد_يساوي(len(مسار) - 1, 8, "أقصر مسار 8 خطوات")
# apl-source:62
