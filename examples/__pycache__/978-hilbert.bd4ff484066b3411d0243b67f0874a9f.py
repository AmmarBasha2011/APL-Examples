
# apl-source:1
# مثال 978 — منحنى هيلبرت
# apl-source:2
# Hilbert curve
# apl-source:3
# Demonstrates: تدوير وانعكاس بالبتات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/978-hilbert.apl
# apl-source:6

# apl-source:7
# منحنى هيلبرت: تحويل إحداثيات الشبكة إلى موضع على المنحنى
# apl-source:8
# خوارزمية بتية بالتدوير والانعكاس عند كل مستوى
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
def دوّر(ن, س, ص, ر_س, ر_ص):
  # apl-source:19
  if ر_ص == 0:
    # apl-source:20
    if ر_س == 1:
      # apl-source:21
      س = (ن - 1) - س
      # apl-source:22
      ص = (ن - 1) - ص
    # apl-source:23
    مؤقت = س
    # apl-source:24
    س = ص
    # apl-source:25
    ص = مؤقت
  # apl-source:26
  return [س, ص]
# apl-source:27

# apl-source:28
def هيلبرت(ن, س, ص):
  # apl-source:29
  د = 0
  # apl-source:30
  ش = ن // 2
  # apl-source:31
  while ش > 0:
    # apl-source:32
    if (س & ش) > 0:
      # apl-source:33
      ر_س = 1
    # apl-source:34
    else:
      # apl-source:35
      ر_س = 0
    # apl-source:36
    if (ص & ش) > 0:
      # apl-source:37
      ر_ص = 1
    # apl-source:38
    else:
      # apl-source:39
      ر_ص = 0
    # apl-source:40
    د = د + ((ش * ش) * ((3 * ر_س) ^ ر_ص))
    # apl-source:41
    م = دوّر(ش, س, ص, ر_س, ر_ص)
    # apl-source:42
    س = م[0]
    # apl-source:43
    ص = م[1]
    # apl-source:44
    ش = ش // 2
  # apl-source:45
  return د
# apl-source:46

# apl-source:47
تأكد_يساوي(هيلبرت(4, 0, 0), 0, "الزاوية السفلى اليسرى")
# apl-source:48
تأكد_يساوي(هيلبرت(4, 0, 1), 3, "فوق الأولى")
# apl-source:49
تأكد_يساوي(هيلبرت(4, 1, 1), 2, "النقطة المركزية للربع")
# apl-source:50
تأكد_يساوي(هيلبرت(4, 1, 0), 1, "يمين الأولى")
# apl-source:51
تأكد_يساوي(هيلبرت(4, 2, 0), 14, "بداية الربع الثاني")
# apl-source:52
تأكد_يساوي(هيلبرت(4, 3, 3), 10, "الزاوية العليا اليمنى")
# apl-source:53
