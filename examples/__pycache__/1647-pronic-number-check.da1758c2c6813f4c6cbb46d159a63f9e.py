
# apl-source:1
# مثال 1647 — العدد المستطيلي
# apl-source:2
# Pronic number check
# apl-source:3
# Demonstrates: نظرية الأعداد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1647-pronic-number-check.apl
# apl-source:6

# apl-source:7
# نجرب ك حتى يزيد ك×(ك+1) عن العدد
# apl-source:8
# إن ساواه فهو مستطيلي
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
def مستطيلي(ن):
  # apl-source:19
  ك = 0
  # apl-source:20
  while ك * (ك + 1) < ن:
    # apl-source:21
    ك = ك + 1
  # apl-source:22
  return ك * (ك + 1) == ن
# apl-source:23

# apl-source:24
تأكد_يساوي(مستطيلي(0), True, "صفر")
# apl-source:25
تأكد_يساوي(مستطيلي(12), True, "اثنا عشر")
# apl-source:26
تأكد_يساوي(مستطيلي(20), True, "عشرون")
# apl-source:27
تأكد_يساوي(مستطيلي(15), False, "خمسة عشر")
# apl-source:28
