
# apl-source:1
# مثال 1049 — أول موجب مفقود
# apl-source:2
# First missing positive
# apl-source:3
# Demonstrates: وضع كل عدد في مكانه
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1049-first-missing-positive.apl
# apl-source:6

# apl-source:7
# نضع كل عدد ع بين 1 وطول القائمة في الفهرس ع ناقص واحد
# apl-source:8
# أول موضع لا يطابق عدده هو الجواب
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
def مفقود_موجب(ق):
  # apl-source:19
  ن = len(ق)
  # apl-source:20
  ع = 0
  # apl-source:21
  while ع < ن:
    # apl-source:22
    ه = ق[ع] - 1
    # apl-source:23
    if (ق[ع] >= 1) and (ق[ع] <= ن) and (ق[ه] != ق[ع]):
      # apl-source:24
      مؤقت = ق[ه]
      # apl-source:25
      ق[ه] = ق[ع]
      # apl-source:26
      ق[ع] = مؤقت
    # apl-source:27
    else:
      # apl-source:28
      ع = ع + 1
  # apl-source:29
  for ع in range(ن):
    # apl-source:30
    if ق[ع] != (ع + 1):
      # apl-source:31
      return ع + 1
  # apl-source:32
  return ن + 1
# apl-source:33

# apl-source:34
تأكد_يساوي(مفقود_موجب([1, 2, 0]), 3, "ثلاثة")
# apl-source:35
تأكد_يساوي(مفقود_موجب([3, 4, -1, 1]), 2, "اثنان")
# apl-source:36
تأكد_يساوي(مفقود_موجب([7, 8, 9, 11, 12]), 1, "واحد")
# apl-source:37
تأكد_يساوي(مفقود_موجب([1]), 2, "عنصر واحد")
# apl-source:38
