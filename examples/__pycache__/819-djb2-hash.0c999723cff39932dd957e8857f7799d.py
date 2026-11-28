
# apl-source:1
# مثال 819 — تجزية djb2
# apl-source:2
# djb2 hash
# apl-source:3
# Demonstrates: 5381 مضروباً 33، التفاف 32-بت
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/819-djb2-hash.apl
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
# تجزية djb2 لدان برنستاين: حاصل 5381 مضروباً في 33 زائد المحرف
# apl-source:25
# Demonstrates: ضرب متكرر ب33, التفاف 32-بت, جدول تجزئة بسيط
# apl-source:26

# apl-source:27
م32 = 4294967296
# apl-source:28

# apl-source:29
def دجب2(نص):
  # apl-source:30
  ه = 5381
  # apl-source:31
  for حرف in نص:
    # apl-source:32
    ه = (ه * 33 + ord(حرف)) % م32
  # apl-source:33
  return ه
# apl-source:34

# apl-source:35
تأكد_يساوي(دجب2(""), 5381, "نص فارغ")
# apl-source:36
تأكد_يساوي(دجب2("hello"), 261238937, "hello")
# apl-source:37
تأكد_يساوي(دجب2("APL"), 193450498, "APL")
# apl-source:38
تأكد_يساوي(دجب2("a") != دجب2("b") == False, False, "حرفان مختلفان")
# apl-source:39

# apl-source:40
def دلو(مفاتيح, حجم):
  # apl-source:41
  جدول = []
  # apl-source:42
  for ي in range(حجم):
    # apl-source:43
    جدول.append([])
  # apl-source:44
  for ك in مفاتيح:
    # apl-source:45
    جدول[دجب2(ك) % حجم].append(ك)
  # apl-source:46
  return جدول
# apl-source:47

# apl-source:48
دلاء = دلو(["apple", "banana", "cherry", "date"], 8)
# apl-source:49
مجموع = 0
# apl-source:50
for خلية in دلاء:
  # apl-source:51
  مجموع = مجموع + len(خلية)
# apl-source:52
تأكد_يساوي(مجموع, 4, "كل المفاتيح مدخلة")
# apl-source:53
تأكد_يساوي(len(دلاء), 8, "حجم الجدول")
# apl-source:54
