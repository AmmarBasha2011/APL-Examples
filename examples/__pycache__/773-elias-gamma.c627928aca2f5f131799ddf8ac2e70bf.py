
# apl-source:1
# مثال 773 — ترميز إلياس جاما
# apl-source:2
# Elias gamma coding
# apl-source:3
# Demonstrates: بادئة أحادية، تمثيل ثنائي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/773-elias-gamma.apl
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
# ترميز إلياس جاما: أصفار بقدار الطول-1 ثم التمثيل الثنائي
# apl-source:25
# Demonstrates: شفرة أحادية البادئة, فك بقراءة البادئة أولاً
# apl-source:26

# apl-source:27
def جاما_ترميز(ن):
  # apl-source:28
  ثنائي = ""
  # apl-source:29
  م = ن
  # apl-source:30
  while م > 0:
    # apl-source:31
    if م % 2 == 1:
      # apl-source:32
      ثنائي = "1" + ثنائي
    # apl-source:33
    else:
      # apl-source:34
      ثنائي = "0" + ثنائي
    # apl-source:35
    م = م // 2
  # apl-source:36
  بادئة = ""
  # apl-source:37
  for ي in range(len(ثنائي) - 1):
    # apl-source:38
    بادئة = بادئة + "0"
  # apl-source:39
  return بادئة + ثنائي
# apl-source:40

# apl-source:41
def جاما_فك(شفرة):
  # apl-source:42
  أصفار = 0
  # apl-source:43
  while شفرة[أصفار] == "0":
    # apl-source:44
    أصفار = أصفار + 1
  # apl-source:45
  قيمة = 0
  # apl-source:46
  for ي in range(أصفار + 1):
    # apl-source:47
    قيمة = قيمة * 2
    # apl-source:48
    if شفرة[أصفار + ي] == "1":
      # apl-source:49
      قيمة = قيمة + 1
  # apl-source:50
  return قيمة
# apl-source:51

# apl-source:52
تأكد_يساوي(جاما_ترميز(1), "1", "جاما 1")
# apl-source:53
تأكد_يساوي(جاما_ترميز(2), "010", "جاما 2")
# apl-source:54
تأكد_يساوي(جاما_ترميز(13), "0001101", "جاما 13")
# apl-source:55
تأكد_يساوي(جاما_ترميز(100), "0000001100100", "جاما 100")
# apl-source:56
تأكد_يساوي(جاما_فك("1"), 1, "فك جاما 1")
# apl-source:57
تأكد_يساوي(جاما_فك("010"), 2, "فك جاما 2")
# apl-source:58
تأكد_يساوي(جاما_فك("0001101"), 13, "فك جاما 13")
# apl-source:59
تأكد_يساوي(جاما_فك("0000001100100"), 100, "فك جاما 100")
# apl-source:60
تأكد_يساوي(جاما_فك(جاما_ترميز(777)), 777, "ذهاب وإياب 777")
# apl-source:61
