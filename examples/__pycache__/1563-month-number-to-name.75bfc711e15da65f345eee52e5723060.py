
# apl-source:1
# مثال 1563 — اسم الشهر من رقمه
# apl-source:2
# Month number to name
# apl-source:3
# Demonstrates: وقت
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1563-month-number-to-name.apl
# apl-source:6

# apl-source:7
# نخزن الأسماء في قائمة
# apl-source:8
# الشهر ن هو العنصر ن ناقص واحد
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
def اسم_الشهر(ن):
  # apl-source:19
  أسماء = ["يناير", "فبراير", "مارس", "أبريل", "مايو", "يونيو", "يوليو", "أغسطس", "سبتمبر", "أكتوبر", "نوفمبر", "ديسمبر"]
  # apl-source:20
  if ن < 1 or ن > 12:
    # apl-source:21
    return "غير صالح"
  # apl-source:22
  return أسماء[ن - 1]
# apl-source:23

# apl-source:24
تأكد_يساوي(اسم_الشهر(1), "يناير", "أول")
# apl-source:25
تأكد_يساوي(اسم_الشهر(9), "سبتمبر", "تاسع")
# apl-source:26
تأكد_يساوي(اسم_الشهر(13), "غير صالح", "خارج")
# apl-source:27
