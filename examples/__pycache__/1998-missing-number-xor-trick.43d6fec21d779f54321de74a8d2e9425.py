
# apl-source:1
# مثال 1998 — العدد الناقص بالـ XOR
# apl-source:2
# Missing number with XOR
# apl-source:3
# Demonstrates: بتات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1998-missing-number-xor-trick.apl
# apl-source:6

# apl-source:7
# # الأعداد المتساوية تلغي بعضها في XOR
# apl-source:8
# # نبدأ بطول القائمة لأنه أكبر عدد محتمل
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
def ناقص(ق):
  # apl-source:19
  خ = len(ق)
  # apl-source:20
  for ك in range(len(ق)):
    # apl-source:21
    خ = خ ^ ك ^ ق[ك]
  # apl-source:22
  return خ
# apl-source:23

# apl-source:24
تأكد_يساوي(ناقص([3, 0, 1]), 2, "ثلاثة")
# apl-source:25
تأكد_يساوي(ناقص([0, 1]), 2, "الأخير")
# apl-source:26
تأكد_يساوي(ناقص([9, 6, 4, 2, 3, 5, 7, 0, 1]), 8, "تسعة")
# apl-source:27
