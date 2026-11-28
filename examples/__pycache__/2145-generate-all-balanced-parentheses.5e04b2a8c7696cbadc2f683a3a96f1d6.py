
# apl-source:1
# مثال 2145 — توليد كل الأقواس المتوازنة
# apl-source:2
# Generate balanced parentheses
# apl-source:3
# Demonstrates: تراجع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2145-generate-all-balanced-parentheses.apl
# apl-source:6

# apl-source:7
# # نتفرع على الاختيارين
# apl-source:8
# # عدد النتائج هو عدد كاتالان
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
def ولد(فتح, اغلق, حالي, خرج):
  # apl-source:19
  if فتح == 0 and اغلق == 0:
    # apl-source:20
    خرج = خرج + [حالي]
    # apl-source:21
    return خرج
  # apl-source:22
  if فتح > 0:
    # apl-source:23
    خرج = ولد(فتح - 1, اغلق + 1, حالي + "(", خرج)
  # apl-source:24
  if اغلق > 0:
    # apl-source:25
    خرج = ولد(فتح, اغلق - 1, حالي + ")", خرج)
  # apl-source:26
  return خرج
# apl-source:27

# apl-source:28
تأكد_يساوي(ولد(1, 0, "", []), ["()"], "واحد")
# apl-source:29
تأكد_يساوي(ولد(2, 0, "", []), ["(())", "()()"], "اثنان")
# apl-source:30
تأكد_يساوي(len(ولد(3, 0, "", [])), 5, "ثلاثة")
# apl-source:31
تأكد_يساوي(len(ولد(5, 0, "", [])), 42, "خمسة")
# apl-source:32
