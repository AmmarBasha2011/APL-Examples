
# apl-source:1
# مثال 2096 — أعداد بيل بمثلث بيل
# apl-source:2
# Bell numbers triangle
# apl-source:3
# Demonstrates: توافيق
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2096-bell-numbers-triangle-method.apl
# apl-source:6

# apl-source:7
# # كل صف يبدأ بآخر عنصر في السابق
# apl-source:8
# # ثم نجمع جارا بجار
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
def بيل(ن):
  # apl-source:19
  صف = [1]
  # apl-source:20
  for م in range(ن):
    # apl-source:21
    جديد = [صف[len(صف) - 1]]
    # apl-source:22
    for ع in صف:
      # apl-source:23
      جديد = جديد + [جديد[len(جديد) - 1] + ع]
    # apl-source:24
    صف = جديد
  # apl-source:25
  return صف[0]
# apl-source:26

# apl-source:27
تأكد_يساوي(بيل(0), 1, "٠")
# apl-source:28
تأكد_يساوي(بيل(3), 5, "٣")
# apl-source:29
تأكد_يساوي(بيل(5), 52, "٥")
# apl-source:30
تأكد_يساوي(بيل(6), 203, "٦")
# apl-source:31
