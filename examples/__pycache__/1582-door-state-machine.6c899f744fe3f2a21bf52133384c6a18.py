
# apl-source:1
# مثال 1582 — آلة حالات الباب
# apl-source:2
# Door state machine
# apl-source:3
# Demonstrates: محاكاة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1582-door-state-machine.apl
# apl-source:6

# apl-source:7
# الحالة والحدث يحددان الحالة التالية
# apl-source:8
# الحدث غير الممكن لا يغيّر الحالة
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
def شغّل_الباب(أحداث):
  # apl-source:19
  انتقال = {"مغلق": {"افتح": "مفتوح", "اقفل": "مقفول"}, "مفتوح": {"اغلق": "مغلق"}, "مقفول": {"افتح_القفل": "مغلق"}}
  # apl-source:20
  حالة = "مغلق"
  # apl-source:21
  for ح in أحداث:
    # apl-source:22
    if ح in انتقال[حالة]:
      # apl-source:23
      حالة = انتقال[حالة][ح]
  # apl-source:24
  return حالة
# apl-source:25

# apl-source:26
تأكد_يساوي(شغّل_الباب(["افتح", "اغلق", "اقفل"]), "مقفول", "تسلسل")
# apl-source:27
تأكد_يساوي(شغّل_الباب(["اقفل", "افتح"]), "مقفول", "حدث مرفوض")
# apl-source:28
تأكد_يساوي(شغّل_الباب(["اقفل", "افتح_القفل", "افتح"]), "مفتوح", "فتح القفل")
# apl-source:29
تأكد_يساوي(شغّل_الباب([]), "مغلق", "بلا أحداث")
# apl-source:30
