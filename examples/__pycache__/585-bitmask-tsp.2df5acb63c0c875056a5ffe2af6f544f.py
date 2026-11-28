
# apl-source:1
# مثال 585 — جولة بأقنعة البتات
# apl-source:2
# Bitmask TSP
# apl-source:3
# Demonstrates: TSP، أقنعة بتات، برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/585-bitmask-tsp.apl
# apl-source:6

# apl-source:7
# Assertion style:
# apl-source:8
#   دالة تأكد_يساوي(فعلي, متوقع, اسم):
# apl-source:9
#     لو فعلي != متوقع:
# apl-source:10
#       اطبع "فشل:", اسم
# apl-source:11
#       اطبع "  متوقع:", متوقع
# apl-source:12
#       اطبع "  فعلي:", فعلي
# apl-source:13
#       قياسي_نظام_اخرج(1)
# apl-source:14
#     اطبع "ناجح:", اسم
# apl-source:15

# apl-source:16
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:17
  if فعلي != متوقع:
    # apl-source:18
    print("فشل:", اسم)
    # apl-source:19
    print("  متوقع:", متوقع)
    # apl-source:20
    print("  فعلي:", فعلي)
    # apl-source:21
    قياسي_نظام_اخرج(1)
  # apl-source:22
  print("ناجح:", اسم)
# apl-source:23

# apl-source:24
# أقصر جولة تزور كل المدن (TSP) ببرمجة ديناميكية على أقنعة البتات
# apl-source:25
# Demonstrates: bitmask DP, حالات 2^n, مسألة البائع المتجول
# apl-source:26
# يعمل على 5 مدن كمثال صغير
# apl-source:27

# apl-source:28
مسافات = [
  # apl-source:29
  [0, 10, 15, 20, 25],
  # apl-source:30
  [10, 0, 35, 25, 30],
  # apl-source:31
  [15, 35, 0, 30, 10],
  # apl-source:32
  [20, 25, 30, 0, 15,],
  # apl-source:33
  [25, 30, 10, 15, 0]
# apl-source:34
]
# apl-source:35
ن = 5
# apl-source:36
كامل = (2 ** ن) - 1
# apl-source:37
لا_نهاية = 1000000000
# apl-source:38

# apl-source:39
# م[قناع][آخر] = أقصر طريق يبدأ من 0 ويزور مدن القناع وينتهي عند «آخر»
# apl-source:40
م = []
# apl-source:41
for سطر_ي in range(كامل + 1):
  # apl-source:42
  م.append([لا_نهاية] * ن)
# apl-source:43
م[1][0] = 0
# apl-source:44

# apl-source:45
for قناع in range(كامل + 1):
  # apl-source:46
  for آخر in range(ن):
    # apl-source:47
    if م[قناع][آخر] < لا_نهاية:
      # apl-source:48
      for تال in range(ن):
        # apl-source:49
        بت = 2 ** تال
        # apl-source:50
        if (قناع // بت) % 2 == 0:
          # apl-source:51
          قناع_جديد = قناع + بت
          # apl-source:52
          مرشح = م[قناع][آخر] + مسافات[آخر][تال]
          # apl-source:53
          if مرشح < م[قناع_جديد][تال]:
            # apl-source:54
            م[قناع_جديد][تال] = مرشح
# apl-source:55

# apl-source:56
أفضل = لا_نهاية
# apl-source:57
for آخر in range(1, ن):
  # apl-source:58
  if م[كامل][آخر] + مسافات[آخر][0] < أفضل:
    # apl-source:59
    أفضل = م[كامل][آخر] + مسافات[آخر][0]
# apl-source:60

# apl-source:61
print("أقصر جولة:", أفضل)
# apl-source:62
تأكد_يساوي(أفضل, 75, "أقصر جولة 5 مدن")
# apl-source:63
تأكد_يساوي(م[1][0], 0, "الحالة الابتدائية")
# apl-source:64
