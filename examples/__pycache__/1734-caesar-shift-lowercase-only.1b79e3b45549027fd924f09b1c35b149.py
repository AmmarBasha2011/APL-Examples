
# apl-source:1
# مثال 1734 — إزاحة قيصر للحروف الصغيرة
# apl-source:2
# Caesar shift lowercase letters
# apl-source:3
# Demonstrates: تشفير
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1734-caesar-shift-lowercase-only.apl
# apl-source:6

# apl-source:7
# نحول الحرف إلى موضعه
# apl-source:8
# نترك غير الحروف كما هي
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
def ازح(س, ك):
  # apl-source:19
  أبجد = "abcdefghijklmnopqrstuvwxyz"
  # apl-source:20
  ناتج = ""
  # apl-source:21
  for ح in س:
    # apl-source:22
    م = أبجد.find(ح)
    # apl-source:23
    if م == -1:
      # apl-source:24
      ناتج = ناتج + ح
    # apl-source:25
    else:
      # apl-source:26
      ناتج = ناتج + أبجد[(م + ك) % 26]
  # apl-source:27
  return ناتج
# apl-source:28

# apl-source:29
تأكد_يساوي(ازح("abc", 1), "bcd", "واحد")
# apl-source:30
تأكد_يساوي(ازح("xyz", 3), "abc", "التفاف")
# apl-source:31
تأكد_يساوي(ازح("a b!", 2), "c d!", "رموز")
# apl-source:32
