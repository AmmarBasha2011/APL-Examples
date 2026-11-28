
# apl-source:1
# مثال 976 — سرخس بارنسلي
# apl-source:2
# Barnsley fern
# apl-source:3
# Demonstrates: تحويلات أفينية مرجحة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/976-barnsley-fern.apl
# apl-source:6

# apl-source:7
# سرخس بارنسلي: نظام دوال متكررة بأربع تحويلات أفينية
# apl-source:8
# مولد حتمي يجعل النقاط قابلة للتحقق
# apl-source:9

# apl-source:10
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:11
  if فعلي != متوقع:
    # apl-source:12
    print("فشل:", اسم)
    # apl-source:13
    print("  متوقع:", متوقع)
    # apl-source:14
    print("  فعلي:", فعلي)
    # apl-source:15
    قياسي_نظام_اخرج(1)
  # apl-source:16
  print("ناجح:", اسم)
# apl-source:17

# apl-source:18
بذرة = [7]
# apl-source:19
def عشوائي100():
  # apl-source:20
  بذرة[0] = (بذرة[0] * 1103515245 + 12345) % 2147483648
  # apl-source:21
  return بذرة[0] % 100
# apl-source:22

# apl-source:23
س = 0
# apl-source:24
ص = 0
# apl-source:25
نقاط = []
# apl-source:26
for i in range(50):
  # apl-source:27
  ر = عشوائي100()
  # apl-source:28
  if ر < 1:
    # apl-source:29
    س_ج = 0
    # apl-source:30
    ص_ج = 0.16 * ص
  # apl-source:31
  elif ر < 86:
    # apl-source:32
    س_ج = (0.85 * س) + (0.04 * ص)
    # apl-source:33
    ص_ج = (((-0.04) * س) + (0.85 * ص)) + 1.6
  # apl-source:34
  elif ر < 93:
    # apl-source:35
    س_ج = (0.2 * س) - (0.26 * ص)
    # apl-source:36
    ص_ج = ((0.23 * س) + (0.22 * ص)) + 1.6
  # apl-source:37
  else:
    # apl-source:38
    س_ج = ((-0.15) * س) + (0.28 * ص)
    # apl-source:39
    ص_ج = ((0.26 * س) + (0.24 * ص)) + 0.44
  # apl-source:40
  س = س_ج
  # apl-source:41
  ص = ص_ج
  # apl-source:42
  نقاط = نقاط + [[س, ص]]
# apl-source:43

# apl-source:44
تأكد_يساوي(len(نقاط), 50, "عدد النقاط")
# apl-source:45
تأكد_يساوي(round(نقاط[10][0], 4), 0.9831, "س النقطة العاشرة")
# apl-source:46
تأكد_يساوي(round(نقاط[10][1], 4), 3.4579, "ص النقطة العاشرة")
# apl-source:47
تأكد_يساوي(round(نقاط[25][0], 4), 1.2448, "س النقطة الخامسة والعشرين")
# apl-source:48
تأكد_يساوي(round(نقاط[25][1], 4), 8.3391, "ص النقطة الخامسة والعشرين")
# apl-source:49
تأكد_يساوي(round(نقاط[49][0], 4), 1.507, "س النقطة الأخيرة")
# apl-source:50
تأكد_يساوي(round(نقاط[49][1], 4), 9.3219, "ص النقطة الأخيرة")
# apl-source:51
