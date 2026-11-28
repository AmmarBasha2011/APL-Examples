
# apl-source:1
# مثال 1640 — الجذر النوني بالبحث الثنائي
# apl-source:2
# Integer nth root by binary search
# apl-source:3
# Demonstrates: بحث ثنائي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1640-nth-root-binary-search.apl
# apl-source:6

# apl-source:7
# نبحث بين 1 والعدد
# apl-source:8
# نقارن القوة بالعدد
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
def جذر_نوني(عدد, ن):
  # apl-source:19
  if عدد < 2:
    # apl-source:20
    return عدد
  # apl-source:21
  ي = 1
  # apl-source:22
  ج = عدد
  # apl-source:23
  نتيجة = 1
  # apl-source:24
  while ي <= ج:
    # apl-source:25
    م = (ي + ج) // 2
    # apl-source:26
    if م ** ن <= عدد:
      # apl-source:27
      نتيجة = م
      # apl-source:28
      ي = م + 1
    # apl-source:29
    else:
      # apl-source:30
      ج = م - 1
  # apl-source:31
  return نتيجة
# apl-source:32

# apl-source:33
تأكد_يساوي(جذر_نوني(27, 3), 3, "تكعيبي")
# apl-source:34
تأكد_يساوي(جذر_نوني(30, 3), 3, "تقريب")
# apl-source:35
تأكد_يساوي(جذر_نوني(1024, 10), 2, "أس عشرة")
# apl-source:36
تأكد_يساوي(جذر_نوني(0, 2), 0, "صفر")
# apl-source:37
