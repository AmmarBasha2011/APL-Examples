
# apl-source:1
# مثال 427 — فلويد وارشال
# apl-source:2
# Floyd-Warshall
# apl-source:3
# Demonstrates: كل أزواج المسارات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/427-floyd-warshall.apl
# apl-source:6

# apl-source:7
ن = 4
# apl-source:8
بعيد = 999
# apl-source:9
مسافة = []
# apl-source:10
for ي in range(ن):
    # apl-source:11
    سطر = []
    # apl-source:12
    for ز in range(ن):
        # apl-source:13
        if ي == ز:
            # apl-source:14
            سطر.append(0)
        # apl-source:15
        else:
            # apl-source:16
            سطر.append(بعيد)
    # apl-source:17
    مسافة.append(سطر)
# apl-source:18

# apl-source:19
مسافة[0][1] = 3
# apl-source:20
مسافة[0][2] = 8
# apl-source:21
مسافة[1][2] = 2
# apl-source:22
مسافة[2][3] = 1
# apl-source:23
مسافة[1][3] = 7
# apl-source:24

# apl-source:25
for ك in range(ن):
    # apl-source:26
    for ي in range(ن):
        # apl-source:27
        for ز in range(ن):
            # apl-source:28
            if مسافة[ي][ك] + مسافة[ك][ز] < مسافة[ي][ز]:
                # apl-source:29
                مسافة[ي][ز] = مسافة[ي][ك] + مسافة[ك][ز]
# apl-source:30

# apl-source:31
for سطر in مسافة:
    # apl-source:32
    print(سطر)
# apl-source:33
