
# apl-source:1
# مثال 1492 — تحليل نص الاستعلام
# apl-source:2
# Parse URL query string
# apl-source:3
# Demonstrates: تحليل
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1492-query-string-parse.apl
# apl-source:6

# apl-source:7
# نفصل على & ثم على أول =
# apl-source:8
# المفتاح بلا قيمة يأخذ نصاً فارغاً
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
def حلل_الاستعلام(س):
  # apl-source:19
  ناتج = {}
  # apl-source:20
  if س == "":
    # apl-source:21
    return ناتج
  # apl-source:22
  for جزء in س.split("&"):
    # apl-source:23
    if "=" in جزء:
      # apl-source:24
      ك = جزء.split("=")
      # apl-source:25
      ناتج[ك[0]] = ك[1]
    # apl-source:26
    else:
      # apl-source:27
      ناتج[جزء] = ""
  # apl-source:28
  return ناتج
# apl-source:29

# apl-source:30
تأكد_يساوي(حلل_الاستعلام("a=1&b=2"), {"a": "1", "b": "2"}, "مفتاحان")
# apl-source:31
تأكد_يساوي(حلل_الاستعلام("flag&x=5"), {"flag": "", "x": "5"}, "بلا قيمة")
# apl-source:32
تأكد_يساوي(حلل_الاستعلام(""), {}, "فارغ")
# apl-source:33
