
# apl-source:1
# مثال 724 — ترميز زجزاج
# apl-source:2
# ZigZag encoding
# apl-source:3
# Demonstrates: إشارة مطوية، إزاحة، فك
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/724-zigzag-encoding.apl
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
# ترميز زجزاج: السالب يصبح فرديا والموجب زوجيا
# apl-source:25
# Demonstrates: تحويل إشارة إلى موجب, فك بالنصف والإشارة
# apl-source:26
# مع varint يصبح -1 بايتا واحدا بدل عشرة
# apl-source:27

# apl-source:28
def زجزاج_شفر(عدد):
  # apl-source:29
  if عدد >= 0:
    # apl-source:30
    return عدد * 2
  # apl-source:31
  return -عدد * 2 - 1
# apl-source:32

# apl-source:33
def زجزاج_فك(عدد):
  # apl-source:34
  if عدد % 2 == 0:
    # apl-source:35
    return عدد // 2
  # apl-source:36
  return -(عدد + 1) // 2
# apl-source:37

# apl-source:38
تأكد_يساوي(زجزاج_شفر(0), 0, "صفر")
# apl-source:39
تأكد_يساوي(زجزاج_شفر(-1), 1, "سالب واحد")
# apl-source:40
تأكد_يساوي(زجزاج_شفر(1), 2, "موجب واحد")
# apl-source:41
تأكد_يساوي(زجزاج_شفر(-2), 3, "سالب اثنان")
# apl-source:42
تأكد_يساوي(زجزاج_شفر(2), 4, "موجب اثنان")
# apl-source:43
تأكد_يساوي(زجزاج_شفر(2147483647), 4294967294, "أعلى 32-بت")
# apl-source:44
تأكد_يساوي(زجزاج_شفر(-2147483648), 4294967295, "أدنى 32-بت")
# apl-source:45
تأكد_يساوي(زجزاج_فك(4294967295), -2147483648, "فك الأدنى")
# apl-source:46
سلسلة = [-3, -1, 0, 1, 5, -100]
# apl-source:47
for ق in سلسلة:
  # apl-source:48
  تأكد_يساوي(زجزاج_فك(زجزاج_شفر(ق)), ق, "ذهاب وعودة")
# apl-source:49
مشفرة = []
# apl-source:50
for ق in سلسلة:
  # apl-source:51
  مشفرة.append(زجزاج_شفر(ق))
# apl-source:52
print("سلسلة مشفرة:", مشفرة)
# apl-source:53
