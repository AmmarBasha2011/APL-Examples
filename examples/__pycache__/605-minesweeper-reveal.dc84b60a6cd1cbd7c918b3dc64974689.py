
# apl-source:1
# مثال 605 — كشف كاسحة الألغام
# apl-source:2
# Minesweeper reveal
# apl-source:3
# Demonstrates: كاسحة ألغام، كشف متتال، BFS
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/605-minesweeper-reveal.apl
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
# كاسحة الألغام: كشف متتالي للخلايا الفارغة
# apl-source:25
# Demonstrates: BFS/DFS للكشف, عد الجيران الملغومة, تتالي الأصفار
# apl-source:26
# كشف خلية صفرية يكشف جيرانها تلقائيا
# apl-source:27

# apl-source:28
لغم = -1
# apl-source:29
لوحة = [
  # apl-source:30
  [0, 0, 0, 0],
  # apl-source:31
  [0, 1, 1, 1],
  # apl-source:32
  [0, 1, لغم, 1],
  # apl-source:33
  [0, 1, 1, 1]
# apl-source:34
]
# apl-source:35
ن = 4
# apl-source:36
مكشوف = []
# apl-source:37
for ي in range(ن):
  # apl-source:38
  مكشوف.append([False] * ن)
# apl-source:39

# apl-source:40
def اكشف(س, ص):
  # apl-source:41
  طابور = [[س, ص]]
  # apl-source:42
  عدد = 0
  # apl-source:43
  while len(طابور) > 0:
    # apl-source:44
    خلية = طابور.pop(0)
    # apl-source:45
    أ = خلية[0]
    # apl-source:46
    ب = خلية[1]
    # apl-source:47
    if أ >= 0 and أ < ن and ب >= 0 and ب < ن and مكشوف[أ][ب] == False:
      # apl-source:48
      مكشوف[أ][ب] = True
      # apl-source:49
      عدد = عدد + 1
      # apl-source:50
      if لوحة[أ][ب] == 0:
        # apl-source:51
        for ف in range(-1, 2):
          # apl-source:52
          for ج in range(-1, 2):
            # apl-source:53
            طابور.append([أ + ف, ب + ج])
  # apl-source:54
  return عدد
# apl-source:55

# apl-source:56
عدد = اكشف(0, 0)
# apl-source:57
print("خلايا مكشوفة:", عدد)
# apl-source:58
تأكد_يساوي(عدد, 12, "تتالي الكشف يغطي المنطقة الآمنة")
# apl-source:59
تأكد_يساوي(مكشوف[2][2], False, "اللغم غير مكشوف")
# apl-source:60
