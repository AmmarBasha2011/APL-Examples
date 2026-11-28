
# apl-source:1
# مثال 1249 — إعادة ترتيب النص
# apl-source:2
# Reorganize string no adjacent equal
# apl-source:3
# Demonstrates: جشع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1249-reorganize-string.apl
# apl-source:6

# apl-source:7
# نضع الحرف الأكثر تكراراً في المواضع الزوجية
# apl-source:8
# ثم نكمل بباقي الحروف
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
def اعد_ترتيب(س):
  # apl-source:19
  عد = {}
  # apl-source:20
  for ح in س:
    # apl-source:21
    عد[ح] = عد.get(ح, 0) + 1
  # apl-source:22
  ازواج = []
  # apl-source:23
  for ح in عد:
    # apl-source:24
    ازواج = ازواج + [[-عد[ح], ح]]
  # apl-source:25
  ازواج = sorted(ازواج)
  # apl-source:26
  if -ازواج[0][0] > (len(س) + 1) // 2:
    # apl-source:27
    return ""
  # apl-source:28
  حروف = []
  # apl-source:29
  for ز in ازواج:
    # apl-source:30
    for ك in range(-ز[0]):
      # apl-source:31
      حروف = حروف + [ز[1]]
  # apl-source:32
  ناتج = [""] * len(س)
  # apl-source:33
  موضع = 0
  # apl-source:34
  for ح in حروف:
    # apl-source:35
    if موضع >= len(س):
      # apl-source:36
      موضع = 1
    # apl-source:37
    ناتج[موضع] = ح
    # apl-source:38
    موضع = موضع + 2
  # apl-source:39
  return "".join(ناتج)
# apl-source:40

# apl-source:41
def سليم(س):
  # apl-source:42
  for ع in range(len(س) - 1):
    # apl-source:43
    if س[ع] == س[ع + 1]:
      # apl-source:44
      return False
  # apl-source:45
  return True
# apl-source:46

# apl-source:47
تأكد_يساوي(سليم(اعد_ترتيب("aab")), True, "سليم")
# apl-source:48
تأكد_يساوي(اعد_ترتيب("aaab"), "", "مستحيل")
# apl-source:49
تأكد_يساوي(سليم(اعد_ترتيب("aabbcc")), True, "ثلاثة حروف")
# apl-source:50
تأكد_يساوي(len(اعد_ترتيب("vvvlo")), 5, "الطول")
# apl-source:51
