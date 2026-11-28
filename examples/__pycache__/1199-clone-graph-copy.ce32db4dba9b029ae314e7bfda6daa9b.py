import copy
# apl-source:1
# مثال 1199 — نسخ رسم بياني
# apl-source:2
# Clone graph adjacency
# apl-source:3
# Demonstrates: نسخ عميق
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1199-clone-graph-copy.apl
# apl-source:6

# apl-source:7
# نبني قائمة جيران جديدة لكل عقدة
# apl-source:8
# ونتأكد أن تعديل النسخة لا يغير الأصل
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
def انسخ(رسم):
  # apl-source:19
  جديد = {}
  # apl-source:20
  for ع in رسم:
    # apl-source:21
    جديد[ع] = list(رسم[ع])
  # apl-source:22
  return جديد
# apl-source:23

# apl-source:24
أصل = {1: [2, 4], 2: [1, 3], 3: [2, 4], 4: [1, 3]}
# apl-source:25
نسخة = انسخ(أصل)
# apl-source:26
تأكد_يساوي(نسخة, أصل, "متساويان")
# apl-source:27
نسخة[1] = نسخة[1] + [3]
# apl-source:28
تأكد_يساوي(أصل[1], [2, 4], "الأصل لم يتغير")
# apl-source:29
تأكد_يساوي(نسخة[1], [2, 4, 3], "النسخة تغيرت")
# apl-source:30
تأكد_يساوي(انسخ({}), {}, "فارغ")
# apl-source:31
