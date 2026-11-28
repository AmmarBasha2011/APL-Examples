
# apl-source:1
# مثال 1699 — أطول جزء متناظر
# apl-source:2
# Longest palindromic substring length
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1699-longest-palindromic-substring-length.apl
# apl-source:6

# apl-source:7
# نجرب مركزاً فردياً وزوجياً
# apl-source:8
# نوسع ما دام الطرفان متساويين
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
def توسيع(س, ي, ك):
  # apl-source:19
  while ي >= 0 and ك < len(س) and س[ي] == س[ك]:
    # apl-source:20
    ي = ي - 1
    # apl-source:21
    ك = ك + 1
  # apl-source:22
  return ك - ي - 1
# apl-source:23

# apl-source:24
def أطول_متناظر(س):
  # apl-source:25
  أفضل = 0
  # apl-source:26
  for م in range(len(س)):
    # apl-source:27
    أفضل = max(أفضل, توسيع(س, م, م))
    # apl-source:28
    أفضل = max(أفضل, توسيع(س, م, م + 1))
  # apl-source:29
  return أفضل
# apl-source:30

# apl-source:31
تأكد_يساوي(أطول_متناظر("babad"), 3, "ثلاثة")
# apl-source:32
تأكد_يساوي(أطول_متناظر("cbbd"), 2, "اثنان")
# apl-source:33
تأكد_يساوي(أطول_متناظر("a"), 1, "حرف")
# apl-source:34
