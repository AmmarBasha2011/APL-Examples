
# apl-source:1
# مثال 538 — ترتيب طوبولوجي معجمي
# apl-source:2
# Lexicographic topological sort
# apl-source:3
# Demonstrates: ترتيب طوبولوجي، خوارزمية كان، أصغر أولاً
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/538-topological-lex.apl
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
# ترتيب طوبولوجي بأصغر تسمية أولاً (خوارزمية كان)
# apl-source:15
جيران = {"أ": ["ج"], "ب": ["ج", "د"], "ج": ["هـ"], "د": ["هـ"], "هـ": []}
# apl-source:16
درجات = dict()
# apl-source:17
for عقدة in جيران:
    # apl-source:18
    درجات[عقدة] = 0
# apl-source:19
for عقدة in جيران:
    # apl-source:20
    for جار in جيران[عقدة]:
        # apl-source:21
        درجات[جار] = درجات[جار] + 1
# apl-source:22

# apl-source:23
جاهز = list()
# apl-source:24
for عقدة in جيران:
    # apl-source:25
    if درجات[عقدة] == 0:
        # apl-source:26
        جاهز.append(عقدة)
# apl-source:27

# apl-source:28
ترتيب = list()
# apl-source:29
while len(جاهز) > 0:
    # apl-source:30
    جاهز = sorted(جاهز)
    # apl-source:31
    عقدة = جاهز.pop(0)
    # apl-source:32
    ترتيب.append(عقدة)
    # apl-source:33
    for جار in جيران[عقدة]:
        # apl-source:34
        درجات[جار] = درجات[جار] - 1
        # apl-source:35
        if درجات[جار] == 0:
            # apl-source:36
            جاهز.append(جار)
# apl-source:37

# apl-source:38
print("الترتيب:", ترتيب)
# apl-source:39
تأكد_يساوي(ترتيب, ["أ", "ب", "ج", "د", "هـ"], "ترتيب طوبولوجي معجمي")
# apl-source:40
