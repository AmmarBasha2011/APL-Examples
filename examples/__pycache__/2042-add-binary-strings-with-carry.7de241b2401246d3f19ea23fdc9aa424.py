
# apl-source:1
# مثال 2042 — جمع عددين ثنائيين نصيين
# apl-source:2
# Add binary strings
# apl-source:3
# Demonstrates: بتات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2042-add-binary-strings-with-carry.apl
# apl-source:6

# apl-source:7
# # نمشي على الخانات من الأقل أهمية
# apl-source:8
# # ونكتب الناتج من اليمين
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
def اجمع(ا, ب):
  # apl-source:19
  ي = len(ا) - 1
  # apl-source:20
  ل = len(ب) - 1
  # apl-source:21
  حمل = 0
  # apl-source:22
  خرج = ""
  # apl-source:23
  while ي >= 0 or ل >= 0 or حمل > 0:
    # apl-source:24
    م = حمل
    # apl-source:25
    if ي >= 0:
      # apl-source:26
      م = م + int(ا[ي])
      # apl-source:27
      ي = ي - 1
    # apl-source:28
    if ل >= 0:
      # apl-source:29
      م = م + int(ب[ل])
      # apl-source:30
      ل = ل - 1
    # apl-source:31
    خرج = str(م % 2) + خرج
    # apl-source:32
    حمل = م // 2
  # apl-source:33
  return خرج
# apl-source:34

# apl-source:35
تأكد_يساوي(اجمع("11", "1"), "100", "حمل")
# apl-source:36
تأكد_يساوي(اجمع("1010", "1011"), "10101", "أربع خانات")
# apl-source:37
تأكد_يساوي(اجمع("0", "0"), "0", "صفران")
# apl-source:38
