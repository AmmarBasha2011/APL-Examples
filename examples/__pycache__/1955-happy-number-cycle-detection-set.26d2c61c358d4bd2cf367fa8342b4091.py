
# apl-source:1
# مثال 1955 — العدد السعيد
# apl-source:2
# Happy number check
# apl-source:3
# Demonstrates: نظرية الأعداد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1955-happy-number-cycle-detection-set.apl
# apl-source:6

# apl-source:7
# # نحفظ الأعداد التي مررنا بها في قاموس
# apl-source:8
# # إن تكرر عدد فقد دخلنا دورة
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
def سعيد(ن):
  # apl-source:19
  رأينا = {}
  # apl-source:20
  while ن != 1 and (ن in رأينا) == False:
    # apl-source:21
    رأينا[ن] = 1
    # apl-source:22
    مج = 0
    # apl-source:23
    for ر in str(ن):
      # apl-source:24
      مج = مج + int(ر) * int(ر)
    # apl-source:25
    ن = مج
  # apl-source:26
  return ن == 1
# apl-source:27

# apl-source:28
تأكد_يساوي(سعيد(19), True, "١٩")
# apl-source:29
تأكد_يساوي(سعيد(2), False, "٢")
# apl-source:30
تأكد_يساوي(سعيد(7), True, "٧")
# apl-source:31
تأكد_يساوي(سعيد(1), True, "١")
# apl-source:32
