
# apl-source:1
# مثال 1889 — تشفير قيصر للحروف الصغيرة
# apl-source:2
# Caesar shift for lowercase text
# apl-source:3
# Demonstrates: تشفير
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1889-caesar-shift-lowercase-text.apl
# apl-source:6

# apl-source:7
# نجد موقع الحرف في الأبجدية
# apl-source:8
# نضيف الإزاحة ونلف حول الطرف
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
الحروف = "abcdefghijklmnopqrstuvwxyz"
# apl-source:19

# apl-source:20
def قيصر(نص, ز):
  # apl-source:21
  خرج = ""
  # apl-source:22
  for ح in نص:
    # apl-source:23
    ك = الحروف.find(ح)
    # apl-source:24
    if ك < 0:
      # apl-source:25
      خرج = خرج + ح
    # apl-source:26
    else:
      # apl-source:27
      خرج = خرج + الحروف[(ك + ز) % 26]
  # apl-source:28
  return خرج
# apl-source:29

# apl-source:30
تأكد_يساوي(قيصر("abc", 3), "def", "إزاحة ٣")
# apl-source:31
تأكد_يساوي(قيصر("xyz", 3), "abc", "لف حول الطرف")
# apl-source:32
تأكد_يساوي(قيصر("a b", 1), "b c", "مسافة")
# apl-source:33
