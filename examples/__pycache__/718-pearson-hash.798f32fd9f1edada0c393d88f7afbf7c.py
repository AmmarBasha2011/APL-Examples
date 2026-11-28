
# apl-source:1
# مثال 718 — هاش بيرسون
# apl-source:2
# Pearson hashing
# apl-source:3
# Demonstrates: جدول تبديل، XOR، بايت واحد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/718-pearson-hash.apl
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
# تجزئة بيرسون: بايت واحد بجدول تبديل
# apl-source:25
# Demonstrates: جدول تبديل 256, XOR تراكمي, تجزئة متعددة البايتات
# apl-source:26
# الجدول هنا دالة حتمية بدل تخزين 256 ثابتا
# apl-source:27

# apl-source:28
def جدول(ي):
  # apl-source:29
  ح = (ي * 2654435761 + 1013904223) % 4294967296
  # apl-source:30
  ح = ح ^ (ح // 65536)
  # apl-source:31
  ح = (ح * 2246822519) % 4294967296
  # apl-source:32
  return ح % 256
# apl-source:33

# apl-source:34
def بيرسون(نص, إزاحة):
  # apl-source:35
  ح = إزاحة
  # apl-source:36
  for ي in range(len(نص)):
    # apl-source:37
    ح = جدول((ح ^ ord(نص[ي])) % 256)
  # apl-source:38
  return ح
# apl-source:39

# apl-source:40
def بيرسون64(نص):
  # apl-source:41
  مجموع = 0
  # apl-source:42
  for إزاحة in range(8):
    # apl-source:43
    مجموع = مجموع * 256 + بيرسون(نص, إزاحة)
  # apl-source:44
  return مجموع
# apl-source:45

# apl-source:46
تأكد_يساوي(بيرسون("hello", 0), بيرسون("hello", 0), "حتمي")
# apl-source:47
تأكد_يساوي(بيرسون("hello", 0) != بيرسون("hellp", 0), True, "حرف يغير")
# apl-source:48
تأكد_يساوي(بيرسون("hello", 0) != بيرسون("hello", 1), True, "الإزاحة تغير")
# apl-source:49
م = بيرسون64("hello")
# apl-source:50
تأكد_يساوي(م, بيرسون64("hello"), "64-بت حتمي")
# apl-source:51
تأكد_يساوي(م != بيرسون64("hellp"), True, "64-بت حساس")
# apl-source:52
توزيع = [0] * 8
# apl-source:53
for ي in range(800):
  # apl-source:54
  توزيع[بيرسون("عنصر" + str(ي), 0) % 8] = توزيع[بيرسون("عنصر" + str(ي), 0) % 8] + 1
# apl-source:55
تأكد_يساوي(توزيع[0] > 60 and توزيع[0] < 140, True, "الدلو الأول متوازن")
# apl-source:56
print("بيرسون64(hello):", م)
# apl-source:57
