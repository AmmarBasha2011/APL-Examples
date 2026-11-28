
# apl-source:1
# مثال 784 — منحنى Z
# apl-source:2
# Z-order (Morton)
# apl-source:3
# Demonstrates: تشابك بتات، حفظ الجوار
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/784-z-order-curve.apl
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
# منحنى Z (ترميز مورتون): تشابك بتات الإحداثيين
# apl-source:25
# Demonstrates: interleave بتات x و y, فك التشابك, ترتيب يحفظ الجوار
# apl-source:26

# apl-source:27
def قوة2(ن):
  # apl-source:28
  ق = 1
  # apl-source:29
  for ي in range(ن):
    # apl-source:30
    ق = ق * 2
  # apl-source:31
  return ق
# apl-source:32

# apl-source:33
def مورتون(س, ص):
  # apl-source:34
  ز = 0
  # apl-source:35
  for ي in range(16):
    # apl-source:36
    بت_س = (س // قوة2(ي)) % 2
    # apl-source:37
    بت_ص = (ص // قوة2(ي)) % 2
    # apl-source:38
    ز = ز + بت_س * قوة2(2 * ي) + بت_ص * قوة2(2 * ي + 1)
  # apl-source:39
  return ز
# apl-source:40

# apl-source:41
def فك_مورتون(ز):
  # apl-source:42
  س = 0
  # apl-source:43
  ص = 0
  # apl-source:44
  for ي in range(16):
    # apl-source:45
    س = س + ((ز // قوة2(2 * ي)) % 2) * قوة2(ي)
    # apl-source:46
    ص = ص + ((ز // قوة2(2 * ي + 1)) % 2) * قوة2(ي)
  # apl-source:47
  return [س, ص]
# apl-source:48

# apl-source:49
تأكد_يساوي(مورتون(0, 0), 0, "مورتون الأصل")
# apl-source:50
تأكد_يساوي(مورتون(1, 0), 1, "مورتون 1,0")
# apl-source:51
تأكد_يساوي(مورتون(0, 1), 2, "مورتون 0,1")
# apl-source:52
تأكد_يساوي(مورتون(1, 1), 3, "مورتون 1,1")
# apl-source:53
تأكد_يساوي(مورتون(2, 0), 4, "مورتون 2,0")
# apl-source:54
تأكد_يساوي(مورتون(3, 5), 39, "مورتون 3,5")
# apl-source:55
ن1 = فك_مورتون(39)
# apl-source:56
تأكد_يساوي(ن1[0], 3, "فك س")
# apl-source:57
تأكد_يساوي(ن1[1], 5, "فك ص")
# apl-source:58
ن2 = فك_مورتون(مورتون(7, 13))
# apl-source:59
تأكد_يساوي(ن2[0], 7, "ذهاب وإياب س")
# apl-source:60
تأكد_يساوي(ن2[1], 13, "ذهاب وإياب ص")
# apl-source:61
تأكد_يساوي(مورتون(4, 4) > مورتون(3, 7), True, "ترتيب Z بين رباعين")
# apl-source:62
