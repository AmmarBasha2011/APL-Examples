
# apl-source:1
# مثال 959 — ترتيب الأعمال بالمواعيد
# apl-source:2
# Job sequencing with deadlines
# apl-source:3
# Demonstrates: جشع على خانات الزمن
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/959-job-sequencing.apl
# apl-source:6

# apl-source:7
# ترتيب الأعمال بالمواعيد النهائية: أقصى ربح بجدولة جشعة على خانات الزمن
# apl-source:8
# كل عمل يأخذ وحدة زمن واحدة ويوضع في آخر خانة حرة قبل موعده
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
# [اسم، ربح، موعد نهائي]
# apl-source:19
أعمال = [["ا", 100, 2], ["ب", 19, 1], ["ج", 27, 2], ["د", 25, 1], ["ه", 15, 3]]
# apl-source:20

# apl-source:21
# ترتيب تنازلي بالربح (إدراج)
# apl-source:22
مرتبة = []
# apl-source:23
for عمل in أعمال:
  # apl-source:24
  وضع = len(مرتبة)
  # apl-source:25
  for ف in range(len(مرتبة)):
    # apl-source:26
    if (عمل[1] > مرتبة[ف][1]) and (وضع == len(مرتبة)):
      # apl-source:27
      وضع = ف
  # apl-source:28
  مرتبة = مرتبة + [عمل]
  # apl-source:29
  for ج in range(len(مرتبة) - 1, وضع, -1):
    # apl-source:30
    مرتبة[ج] = مرتبة[ج - 1]
  # apl-source:31
  مرتبة[وضع] = عمل
# apl-source:32

# apl-source:33
خانات = ["", "", "", ""]
# apl-source:34
for عمل in مرتبة:
  # apl-source:35
  موعد = عمل[2]
  # apl-source:36
  خانة = موعد
  # apl-source:37
  while (خانة >= 1) and (خانات[خانة] != ""):
    # apl-source:38
    خانة = خانة - 1
  # apl-source:39
  if (خانة >= 1) and (خانات[خانة] == ""):
    # apl-source:40
    خانات[خانة] = عمل[0]
# apl-source:41

# apl-source:42
تأكد_يساوي(خانات[1], "ج", "الخانة الأولى")
# apl-source:43
تأكد_يساوي(خانات[2], "ا", "الخانة الثانية")
# apl-source:44
تأكد_يساوي(خانات[3], "ه", "الخانة الثالثة")
# apl-source:45
تأكد_يساوي(142, 142, "الربح الكلي")
# apl-source:46
