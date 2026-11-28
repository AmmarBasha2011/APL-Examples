
# apl-source:1
# مثال 1967 — ترميز طول التكرار كأزواج
# apl-source:2
# Run-length encode as pairs
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1967-run-length-encode-pairs-list.apl
# apl-source:6

# apl-source:7
# # نمر على النص ونعد المجموعات المتتالية
# apl-source:8
# # ونرجع قائمة من الأزواج
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
def رمز(س):
  # apl-source:19
  خرج = []
  # apl-source:20
  ك = 0
  # apl-source:21
  while ك < len(س):
    # apl-source:22
    ي = ك
    # apl-source:23
    while ي < len(س) and س[ي] == س[ك]:
      # apl-source:24
      ي = ي + 1
    # apl-source:25
    خرج = خرج + [[س[ك], ي - ك]]
    # apl-source:26
    ك = ي
  # apl-source:27
  return خرج
# apl-source:28

# apl-source:29
تأكد_يساوي(رمز("aaabcc"), [["a", 3], ["b", 1], ["c", 2]], "ثلاث مجموعات")
# apl-source:30
تأكد_يساوي(رمز(""), [], "فارغ")
# apl-source:31
تأكد_يساوي(رمز("zzzz"), [["z", 4]], "مجموعة واحدة")
# apl-source:32
