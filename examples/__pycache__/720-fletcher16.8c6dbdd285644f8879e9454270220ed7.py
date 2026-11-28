
# apl-source:1
# مثال 720 — مجموع فليتشر-16
# apl-source:2
# Fletcher-16 checksum
# apl-source:3
# Demonstrates: مجموعان متوازيان، التفاف، بايتات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/720-fletcher16.apl
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
# مجموع فليتشر-16 الاختباري
# apl-source:25
# Demonstrates: مجموعان بباقي 255, حساسية للترتيب, معيار RFC 1146
# apl-source:26
# أبسط من أدلر: باقي 255 بدل عدد أولي
# apl-source:27

# apl-source:28
def فليتشر(بايتات):
  # apl-source:29
  ج1 = 0
  # apl-source:30
  ج2 = 0
  # apl-source:31
  for بايت in بايتات:
    # apl-source:32
    ج1 = (ج1 + بايت) % 255
    # apl-source:33
    ج2 = (ج2 + ج1) % 255
  # apl-source:34
  return ج2 * 256 + ج1
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
تأكد_يساوي(فليتشر(بايتات("abcde")), 51440, "مثال المعيار abcde")
# apl-source:43
تأكد_يساوي(فليتشر(بايتات("abcdef")), 8279, "مثال المعيار abcdef")
# apl-source:44
تأكد_يساوي(فليتشر(بايتات("abcdefgh")), 1575, "مثال المعيار abcdefgh")
# apl-source:45
تأكد_يساوي(فليتشر(بايتات("")), 0, "الفارغ صفر")
# apl-source:46
تأكد_يساوي(فليتشر(بايتات("abc")) != فليتشر(بايتات("acb")), True, "الترتيب يهم")
# apl-source:47
تأكد_يساوي(فليتشر(بايتات("abc")) != فليتشر(بايتات("abd")), True, "حرف يغير")
# apl-source:48
print("فليتشر(abcde):", فليتشر(بايتات("abcde")))
# apl-source:49
