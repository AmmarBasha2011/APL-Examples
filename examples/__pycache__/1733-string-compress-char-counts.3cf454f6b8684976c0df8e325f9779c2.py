
# apl-source:1
# مثال 1733 — ضغط النص بالعدّ
# apl-source:2
# Run length encode a string
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1733-string-compress-char-counts.apl
# apl-source:6

# apl-source:7
# نتتبع الحرف الحالي
# apl-source:8
# نكتب العدد عند التغير
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
def اضغط(س):
  # apl-source:19
  if len(س) == 0:
    # apl-source:20
    return ""
  # apl-source:21
  ناتج = ""
  # apl-source:22
  حالي = س[0]
  # apl-source:23
  عد = 1
  # apl-source:24
  for ك in range(1, len(س)):
    # apl-source:25
    if س[ك] == حالي:
      # apl-source:26
      عد = عد + 1
    # apl-source:27
    else:
      # apl-source:28
      ناتج = ناتج + حالي + str(عد)
      # apl-source:29
      حالي = س[ك]
      # apl-source:30
      عد = 1
  # apl-source:31
  ناتج = ناتج + حالي + str(عد)
  # apl-source:32
  return ناتج
# apl-source:33

# apl-source:34
تأكد_يساوي(اضغط("aaabcc"), "a3b1c2", "ثلاثة")
# apl-source:35
تأكد_يساوي(اضغط(""), "", "فارغ")
# apl-source:36
تأكد_يساوي(اضغط("z"), "z1", "حرف")
# apl-source:37
