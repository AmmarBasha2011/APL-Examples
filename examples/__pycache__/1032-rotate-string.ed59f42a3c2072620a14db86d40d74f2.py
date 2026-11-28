
# apl-source:1
# مثال 1032 — تدوير النص
# apl-source:2
# Rotate string check
# apl-source:3
# Demonstrates: النص مضاعفاً
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1032-rotate-string.apl
# apl-source:6

# apl-source:7
# نص هو دوران لنص آخر لو ظهر داخل الآخر مكرراً مرتين
# apl-source:8
# وبشرط تساوي الطولين
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
def دوران(أ, ب):
  # apl-source:19
  if len(أ) != len(ب):
    # apl-source:20
    return False
  # apl-source:21
  مضاعف = ب + ب
  # apl-source:22
  return أ in مضاعف
# apl-source:23

# apl-source:24
تأكد_يساوي(دوران("abcde", "cdeab"), True, "دوران ثلاثة")
# apl-source:25
تأكد_يساوي(دوران("abcde", "abced"), False, "ليس دوراناً")
# apl-source:26
تأكد_يساوي(دوران("", ""), True, "فارغان")
# apl-source:27
تأكد_يساوي(دوران("ab", "abc"), False, "طولان مختلفان")
# apl-source:28
