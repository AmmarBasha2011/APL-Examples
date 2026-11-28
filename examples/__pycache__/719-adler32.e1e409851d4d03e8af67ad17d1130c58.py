
# apl-source:1
# مثال 719 — مجموع أدلر-32
# apl-source:2
# Adler-32 checksum
# apl-source:3
# Demonstrates: مجاميع متراكمة، مودولو، دمج
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/719-adler32.apl
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
# مجموع أدلر-32 الاختباري (كما في zlib)
# apl-source:25
# Demonstrates: مجموعان متدحرجان, باقي 65521, دمج 16-بتين
# apl-source:26
# أسرع من CRC لكنه أضعف ضد التبديلات البعيدة
# apl-source:27

# apl-source:28
def أدلر(بايتات):
  # apl-source:29
  أ = 1
  # apl-source:30
  ب = 0
  # apl-source:31
  for بايت in بايتات:
    # apl-source:32
    أ = (أ + بايت) % 65521
    # apl-source:33
    ب = (ب + أ) % 65521
  # apl-source:34
  return ب * 65536 + أ
# apl-source:35

# apl-source:36
def بايتات(نص):
  # apl-source:37
  ناتج = []
  # apl-source:38
  for ي in range(len(نص)):
    # apl-source:39
    ناتج.append(ord(نص[ي]) % 256)
  # apl-source:40
  return ناتج
# apl-source:41

# apl-source:42
تأكد_يساوي(أدلر(بايتات("Wikipedia")), 300286872, "مثال ويكيبيديا الرسمي")
# apl-source:43
تأكد_يساوي(أدلر(بايتات("")), 1, "الفارغ واحد")
# apl-source:44
تأكد_يساوي(أدلر(بايتات("a")), 6422626, "حرف واحد")
# apl-source:45
تأكد_يساوي(أدلر(بايتات("abc")) != أدلر(بايتات("acb")), True, "الترتيب يهم")
# apl-source:46
تأكد_يساوي(أدلر(بايتات("abc")) != أدلر(بايتات("abd")), True, "آخر حرف يهم")
# apl-source:47
# النسخة المجزأة تطابق الكاملة
# apl-source:48
كامل = بايتات("hello world")
# apl-source:49
جزء1 = بايتات("hello ")
# apl-source:50
جزء2 = بايتات("world")
# apl-source:51
تأكد_يساوي(أدلر(كامل), أدلر(جزء1 + جزء2), "التقسيم لا يغير")
# apl-source:52
print("أدلر(Wikipedia):", أدلر(بايتات("Wikipedia")))
# apl-source:53
