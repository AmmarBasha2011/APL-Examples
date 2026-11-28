
# apl-source:1
# مثال 1817 — هل نص تدوير لآخر
# apl-source:2
# String rotation check
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1817-string-rotation-check.apl
# apl-source:6

# apl-source:7
# الطول متساو
# apl-source:8
# نبحث في النص مكرراً مرتين
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
def تدوير(أ, ب):
  # apl-source:19
  if len(أ) != len(ب):
    # apl-source:20
    return False
  # apl-source:21
  return (أ + أ).find(ب) != -1
# apl-source:22

# apl-source:23
تأكد_يساوي(تدوير("abcde", "cdeab"), True, "تدوير")
# apl-source:24
تأكد_يساوي(تدوير("abcde", "abced"), False, "ليس تدويراً")
# apl-source:25
تأكد_يساوي(تدوير("a", "a"), True, "حرف")
# apl-source:26
