
# apl-source:1
# مثال 792 — مربع بوليبيوس
# apl-source:2
# Polybius square
# apl-source:3
# Demonstrates: شبكة 5x5، دمج I/J، إحداثيات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/792-polybius-square.apl
# apl-source:6

# apl-source:7
# Assertion style:
# apl-source:8
#   دالة تأكد_يساوي(فعلي, متوقع, اسم):
# apl-source:9
#     لو فعلي != متوقع:
# apl-source:10
#       اطبع "فشل:", اسم
# apl-source:11
#       اطبع "  متوقع:", متوقع
# apl-source:12
#       اطبع "  فعلي:", فعلي
# apl-source:13
#       قياسي_نظام_اخرج(1)
# apl-source:14
#     اطبع "ناجح:", اسم
# apl-source:15

# apl-source:16
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:17
  if فعلي != متوقع:
    # apl-source:18
    print("فشل:", اسم)
    # apl-source:19
    print("  متوقع:", متوقع)
    # apl-source:20
    print("  فعلي:", فعلي)
    # apl-source:21
    قياسي_نظام_اخرج(1)
  # apl-source:22
  print("ناجح:", اسم)
# apl-source:23

# apl-source:24
# شيفرة مربع بوليبيوس: حرف إلى زوج إحداثيات في شبكة 5x5
# apl-source:25
# Demonstrates: دمج I/J, بحث بالموقع, قسمة وباقي للإحداثيات
# apl-source:26

# apl-source:27
مربع = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
# apl-source:28

# apl-source:29
def موقع(ح):
  # apl-source:30
  if ح == "J":
    # apl-source:31
    ح = "I"
  # apl-source:32
  for ي in range(25):
    # apl-source:33
    if مربع[ي] == ح:
      # apl-source:34
      return ي
  # apl-source:35
  return -1
# apl-source:36

# apl-source:37
def تشفير_بوليبيوس(مدخل):
  # apl-source:38
  أزواج = []
  # apl-source:39
  for ح in مدخل:
    # apl-source:40
    if ح != " ":
      # apl-source:41
      م = موقع(ح)
      # apl-source:42
      أزواج.append(str(م // 5 + 1) + str(م % 5 + 1))
  # apl-source:43
  return " ".join(أزواج)
# apl-source:44

# apl-source:45
def فك_بوليبيوس(شيفرة):
  # apl-source:46
  ناتج = ""
  # apl-source:47
  أزواج = شيفرة.split(" ")
  # apl-source:48
  for زوج in أزواج:
    # apl-source:49
    ص = int(زوج[0]) - 1
    # apl-source:50
    ع = int(زوج[1]) - 1
    # apl-source:51
    ناتج = ناتج + مربع[ص * 5 + ع]
  # apl-source:52
  return ناتج
# apl-source:53

# apl-source:54
تأكد_يساوي(موقع("A"), 0, "موقع A")
# apl-source:55
تأكد_يساوي(موقع("K"), 9, "K بعد دمج J")
# apl-source:56
تأكد_يساوي(تشفير_بوليبيوس("HELLO"), "23 15 31 31 34", "تشفير HELLO")
# apl-source:57
تأكد_يساوي(تشفير_بوليبيوس("I J"), "24 24", "دمج I وJ")
# apl-source:58
تأكد_يساوي(فك_بوليبيوس("23 15 31 31 34"), "HELLO", "فك التشفير")
# apl-source:59
تأكد_يساوي(فك_بوليبيوس(تشفير_بوليبيوس("SECRET MESSAGE")), "SECRETMESSAGE", "دورة كاملة")
# apl-source:60
