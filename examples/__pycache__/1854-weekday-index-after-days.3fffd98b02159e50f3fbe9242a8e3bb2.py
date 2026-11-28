
# apl-source:1
# مثال 1854 — موضع اليوم بعد عدد أيام
# apl-source:2
# Weekday index after n days
# apl-source:3
# Demonstrates: وقت
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1854-weekday-index-after-days.apl
# apl-source:6

# apl-source:7
# الأيام كأرقام من صفر إلى ستة
# apl-source:8
# نستخدم الباقي على سبعة
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
def موضع_اليوم(بداية, ن):
  # apl-source:19
  return (بداية + ن) % 7
# apl-source:20

# apl-source:21
def اسم_اليوم(م):
  # apl-source:22
  أسماء = ["الأحد", "الاثنين", "الثلاثاء", "الأربعاء", "الخميس", "الجمعة", "السبت"]
  # apl-source:23
  return أسماء[م]
# apl-source:24

# apl-source:25
تأكد_يساوي(اسم_اليوم(موضع_اليوم(0, 10)), "الأربعاء", "عشرة أيام")
# apl-source:26
تأكد_يساوي(اسم_اليوم(موضع_اليوم(6, 1)), "الأحد", "التفاف")
# apl-source:27
تأكد_يساوي(موضع_اليوم(3, 14), 3, "أسبوعان")
# apl-source:28
