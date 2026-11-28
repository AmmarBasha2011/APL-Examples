
# apl-source:1
# مثال 712 — إزالة التشكيل
# apl-source:2
# Arabic diacritics stripping
# apl-source:3
# Demonstrates: يونيكود، حركات، تطويل
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/712-tashkeel-strip.apl
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
# إزالة التشكيل العربي (الحركات) من النص
# apl-source:25
# Demonstrates: مدى يونيكود 064B-0652, آلف مدودة 0670, تطويل 0640
# apl-source:26
# يفيد البحث والفهرسة: المُعَدَّل يطابق المعدل
# apl-source:27

# apl-source:28
def رمز_تشكيل(ح):
  # apl-source:29
  ر = ord(ح)
  # apl-source:30
  return (ر >= 1611 and ر <= 1618) or ر == 1648
# apl-source:31

# apl-source:32
def جرد(نص):
  # apl-source:33
  ناتج = ""
  # apl-source:34
  for ي in range(len(نص)):
    # apl-source:35
    if رمز_تشكيل(نص[ي]) == False:
      # apl-source:36
      ناتج = ناتج + نص[ي]
  # apl-source:37
  return ناتج
# apl-source:38

# apl-source:39
def أزل_تطويل(نص):
  # apl-source:40
  ناتج = ""
  # apl-source:41
  for ي in range(len(نص)):
    # apl-source:42
    if ord(نص[ي]) != 1600:
      # apl-source:43
      ناتج = ناتج + نص[ي]
  # apl-source:44
  return ناتج
# apl-source:45

# apl-source:46
تأكد_يساوي(جرد("بَسْمِ"), "بسم", "فتحة وسكون وكسرة")
# apl-source:47
تأكد_يساوي(جرد("الْعَرَبِيَّةُ"), "العربية", "كلمة مشكولة كاملة")
# apl-source:48
تأكد_يساوي(جرد("مُحَمَّدٌ"), "محمد", "شدة وتنوين")
# apl-source:49
تأكد_يساوي(جرد("بلا تشكيل"), "بلا تشكيل", "نص أصلا بلا تشكيل")
# apl-source:50
تأكد_يساوي(جرد("ٱللَّٰهِ"), "ٱلله", "ألف خنجرية وآلف مدودة")
# apl-source:51
تأكد_يساوي(أزل_تطويل("العـــربية"), "العربية", "التطويل يزال")
# apl-source:52
print(جرد("بِسْمِ ٱللَّٰهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ"))
# apl-source:53
