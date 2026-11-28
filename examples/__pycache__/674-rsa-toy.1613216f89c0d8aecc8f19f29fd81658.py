
# apl-source:1
# مثال 674 — تشفير RSA التعليمي
# apl-source:2
# Toy RSA
# apl-source:3
# Demonstrates: أولية، معكوس ضربي، أس معياري
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/674-rsa-toy.apl
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
# RSA مصغر: تعليمي بأعداد صغيرة
# apl-source:25
# Demonstrates: مفتاح عام وخاص, أس معياري, توقيع مقلوب
# apl-source:26
# مثال ويكيبيديا الشهير بأعداد صحيحة صغيرة
# apl-source:27

# apl-source:28
def أس_معياري(قاعدة, أس, معيار):
  # apl-source:29
  ناتج = 1
  # apl-source:30
  قاعدة = قاعدة % معيار
  # apl-source:31
  while أس > 0:
    # apl-source:32
    if أس % 2 == 1:
      # apl-source:33
      ناتج = (ناتج * قاعدة) % معيار
    # apl-source:34
    قاعدة = (قاعدة * قاعدة) % معيار
    # apl-source:35
    أس = أس // 2
  # apl-source:36
  return ناتج
# apl-source:37

# apl-source:38
أولي1 = 61
# apl-source:39
أولي2 = 53
# apl-source:40
ن = أولي1 * أولي2
# apl-source:41
فاي = (أولي1 - 1) * (أولي2 - 1)
# apl-source:42
عام = 17
# apl-source:43
خاص = 2753
# apl-source:44

# apl-source:45
تأكد_يساوي(ن, 3233, "المعيار")
# apl-source:46
تأكد_يساوي((عام * خاص) % فاي, 1, "المفتاحان معكوسان")
# apl-source:47

# apl-source:48
رسالة = 65
# apl-source:49
مشفرة = أس_معياري(رسالة, عام, ن)
# apl-source:50
تأكد_يساوي(مشفرة, 2790, "التشفير بالمفتاح العام")
# apl-source:51
تأكد_يساوي(أس_معياري(مشفرة, خاص, ن), رسالة, "الفك بالمفتاح الخاص")
# apl-source:52

# apl-source:53
توقيع = أس_معياري(رسالة, خاص, ن)
# apl-source:54
تأكد_يساوي(أس_معياري(توقيع, عام, ن), رسالة, "التوقيع بالمقلوب")
# apl-source:55
print("مشفرة:", مشفرة)
# apl-source:56
