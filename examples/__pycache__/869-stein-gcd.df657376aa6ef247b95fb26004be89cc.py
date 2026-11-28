
# apl-source:1
# مثال 869 — قاسم شتاين الثنائي
# apl-source:2
# Binary GCD (Stein)
# apl-source:3
# Demonstrates: إزاحات وطرح بلا قسمة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/869-stein-gcd.apl
# apl-source:6

# apl-source:7
# خوارزمية شتاين (GCD الثنائي): قاسم مشترك أكبر بالإزاحات فقط
# apl-source:8
# بلا قسمة: طرح وإزاحة بتات، مناسب للعتاد
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
def شتاين(أ, ب):
  # apl-source:19
  if أ == 0:
    # apl-source:20
    return ب
  # apl-source:21
  if ب == 0:
    # apl-source:22
    return أ
  # apl-source:23
  # عامل 2 مشترك
  # apl-source:24
  ك = 0
  # apl-source:25
  while أ % 2 == 0 and ب % 2 == 0:
    # apl-source:26
    أ = أ // 2
    # apl-source:27
    ب = ب // 2
    # apl-source:28
    ك = ك + 1
  # apl-source:29
  while أ % 2 == 0:
    # apl-source:30
    أ = أ // 2
  # apl-source:31
  while ب != 0:
    # apl-source:32
    while ب % 2 == 0:
      # apl-source:33
      ب = ب // 2
    # apl-source:34
    if أ > ب:
      # apl-source:35
      مؤقت = أ
      # apl-source:36
      أ = ب
      # apl-source:37
      ب = مؤقت
    # apl-source:38
    ب = ب - أ
  # apl-source:39
  return أ * (2 ** ك)
# apl-source:40

# apl-source:41
print("شتاين(48, 18) =", شتاين(48, 18))
# apl-source:42
print("شتاين(1071, 462) =", شتاين(1071, 462))
# apl-source:43

# apl-source:44
تأكد_يساوي(شتاين(48, 18), 6, "قاسم 48 و18")
# apl-source:45
تأكد_يساوي(شتاين(1071, 462), 21, "قاسم 1071 و462")
# apl-source:46
تأكد_يساوي(شتاين(17, 5), 1, "أوليان نسبياً")
# apl-source:47
تأكد_يساوي(شتاين(100, 0), 100, "مع صفر")
# apl-source:48
تأكد_يساوي(شتاين(1024, 128), 128, "قوى اثنين")
# apl-source:49
