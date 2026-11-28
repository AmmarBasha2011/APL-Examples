
# apl-source:1
# مثال 1220 — رقمان مفردان
# apl-source:2
# Two single numbers among pairs
# apl-source:3
# Demonstrates: عمليات بتات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1220-single-number-three.apl
# apl-source:6

# apl-source:7
# XOR الكل يعطي xor الرقمين
# apl-source:8
# وبت مختلف بينهما يفرق القائمة إلى مجموعتين
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
def مفردان(أ):
  # apl-source:19
  س = 0
  # apl-source:20
  for ع in أ:
    # apl-source:21
    س = س ^ ع
  # apl-source:22
  بت = س & (-س)
  # apl-source:23
  ا = 0
  # apl-source:24
  ب = 0
  # apl-source:25
  for ع in أ:
    # apl-source:26
    if ع & بت:
      # apl-source:27
      ا = ا ^ ع
    # apl-source:28
    else:
      # apl-source:29
      ب = ب ^ ع
  # apl-source:30
  return sorted([ا, ب])
# apl-source:31

# apl-source:32
تأكد_يساوي(مفردان([1,2,1,3,2,5]), [3, 5], "مثال أول")
# apl-source:33
تأكد_يساوي(مفردان([0,1]), [0, 1], "صفر وواحد")
# apl-source:34
تأكد_يساوي(مفردان([4,4,9,6]), [6, 9], "مختلط")
# apl-source:35
