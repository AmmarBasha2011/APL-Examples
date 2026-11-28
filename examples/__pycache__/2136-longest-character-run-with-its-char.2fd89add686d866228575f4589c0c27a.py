
# apl-source:1
# مثال 2136 — أطول تتابع لحرف مع الحرف
# apl-source:2
# Longest character run with char
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2136-longest-character-run-with-its-char.apl
# apl-source:6

# apl-source:7
# # نمسح النص مرة واحدة
# apl-source:8
# # أول أطول مجموعة تفوز
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
def اطول(س):
  # apl-source:19
  حرف = ""
  # apl-source:20
  افضل = 0
  # apl-source:21
  ك = 0
  # apl-source:22
  while ك < len(س):
    # apl-source:23
    ي = ك
    # apl-source:24
    while ي < len(س) and س[ي] == س[ك]:
      # apl-source:25
      ي = ي + 1
    # apl-source:26
    if ي - ك > افضل:
      # apl-source:27
      افضل = ي - ك
      # apl-source:28
      حرف = س[ك]
    # apl-source:29
    ك = ي
  # apl-source:30
  return [حرف, افضل]
# apl-source:31

# apl-source:32
تأكد_يساوي(اطول("aabbbcc"), ["b", 3], "b")
# apl-source:33
تأكد_يساوي(اطول("xyz"), ["x", 1], "أول حرف")
# apl-source:34
تأكد_يساوي(اطول(""), ["", 0], "فارغ")
# apl-source:35
