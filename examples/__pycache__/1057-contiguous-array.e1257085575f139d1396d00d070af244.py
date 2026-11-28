
# apl-source:1
# مثال 1057 — مصفوفة متوازنة
# apl-source:2
# Contiguous array equal zeros and ones
# apl-source:3
# Demonstrates: مجموع تراكمي بإشارة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1057-contiguous-array.apl
# apl-source:6

# apl-source:7
# نعد الصفر بسالب واحد والواحد بموجب واحد
# apl-source:8
# جزء مجموعه صفر هو جزء متوازن، وتكرار المجموع يحدد طوله من أول ظهور له
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
def اطول_متوازن(ق):
  # apl-source:19
  قيم = [0]
  # apl-source:20
  اوائل = [-1]
  # apl-source:21
  تراكم = 0
  # apl-source:22
  افضل = 0
  # apl-source:23
  for ع in range(len(ق)):
    # apl-source:24
    if ق[ع] == 1:
      # apl-source:25
      تراكم = تراكم + 1
    # apl-source:26
    else:
      # apl-source:27
      تراكم = تراكم - 1
    # apl-source:28
    if تراكم in قيم:
      # apl-source:29
      ف = 0
      # apl-source:30
      while قيم[ف] != تراكم:
        # apl-source:31
        ف = ف + 1
      # apl-source:32
      if (ع - اوائل[ف]) > افضل:
        # apl-source:33
        افضل = ع - اوائل[ف]
    # apl-source:34
    else:
      # apl-source:35
      قيم = قيم + [تراكم]
      # apl-source:36
      اوائل = اوائل + [ع]
  # apl-source:37
  return افضل
# apl-source:38

# apl-source:39
تأكد_يساوي(اطول_متوازن([0, 1]), 2, "زوج")
# apl-source:40
تأكد_يساوي(اطول_متوازن([0, 1, 0]), 2, "ثلاثة")
# apl-source:41
تأكد_يساوي(اطول_متوازن([0, 0, 1, 0, 0, 0, 1, 1]), 6, "ثمانية")
# apl-source:42
تأكد_يساوي(اطول_متوازن([1, 1, 1]), 0, "لا توازن")
# apl-source:43
