
# apl-source:1
# مثال 2034 — هل تكفي الأحرف لبناء الرسالة
# apl-source:2
# Ransom note letter budget
# apl-source:3
# Demonstrates: قواميس
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2034-ransom-note-letter-budget.apl
# apl-source:6

# apl-source:7
# # نعد حروف المجلة
# apl-source:8
# # ونخصم لكل حرف في الرسالة
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
def تكفي(رسالة, مجلة):
  # apl-source:19
  رصيد = {}
  # apl-source:20
  for ح in مجلة:
    # apl-source:21
    رصيد[ح] = رصيد.get(ح, 0) + 1
  # apl-source:22
  for ح in رسالة:
    # apl-source:23
    if رصيد.get(ح, 0) == 0:
      # apl-source:24
      return False
    # apl-source:25
    رصيد[ح] = رصيد[ح] - 1
  # apl-source:26
  return True
# apl-source:27

# apl-source:28
تأكد_يساوي(تكفي("a", "b"), False, "ناقص")
# apl-source:29
تأكد_يساوي(تكفي("aa", "aab"), True, "كاف")
# apl-source:30
تأكد_يساوي(تكفي("aa", "ab"), False, "حرف واحد")
# apl-source:31
