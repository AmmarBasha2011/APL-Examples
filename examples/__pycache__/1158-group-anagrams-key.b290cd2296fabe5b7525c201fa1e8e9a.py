
# apl-source:1
# مثال 1158 — تجميع المتجانسات
# apl-source:2
# Group anagrams by key
# apl-source:3
# Demonstrates: مفتاح مرتب
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1158-group-anagrams-key.apl
# apl-source:6

# apl-source:7
# نرتب حروف كل كلمة لتصبح مفتاحاً
# apl-source:8
# ونجمع الكلمات حسب المفتاح
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
def جمّع(كلمات):
  # apl-source:19
  مجموعات = {}
  # apl-source:20
  ترتيب = []
  # apl-source:21
  for ك in كلمات:
    # apl-source:22
    مفتاح = "".join(sorted(ك))
    # apl-source:23
    if مفتاح not in مجموعات:
      # apl-source:24
      مجموعات[مفتاح] = []
      # apl-source:25
      ترتيب = ترتيب + [مفتاح]
    # apl-source:26
    مجموعات[مفتاح] = مجموعات[مفتاح] + [ك]
  # apl-source:27
  ناتج = []
  # apl-source:28
  for م in ترتيب:
    # apl-source:29
    ناتج = ناتج + [مجموعات[م]]
  # apl-source:30
  return ناتج
# apl-source:31

# apl-source:32
تأكد_يساوي(جمّع(["eat","tea","tan","ate","nat","bat"]), [["eat","tea","ate"],["tan","nat"],["bat"]], "مثال أول")
# apl-source:33
تأكد_يساوي(جمّع([""]), [[""]], "فارغة")
# apl-source:34
تأكد_يساوي(جمّع(["a"]), [["a"]], "حرف")
# apl-source:35
