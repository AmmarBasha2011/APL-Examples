
# apl-source:1
# مثال 2115 — الأولي المعكوس
# apl-source:2
# Emirp check v2
# apl-source:3
# Demonstrates: نظرية الأعداد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2115-emirp-prime-whose-reverse-is-prime.apl
# apl-source:6

# apl-source:7
# # المتماثلات مثل 11 مستبعدة
# apl-source:8
# # 13 و31 مثال
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
def اولي(ن):
  # apl-source:19
  if ن < 2:
    # apl-source:20
    return False
  # apl-source:21
  د = 2
  # apl-source:22
  while د * د <= ن:
    # apl-source:23
    if ن % د == 0:
      # apl-source:24
      return False
    # apl-source:25
    د = د + 1
  # apl-source:26
  return True
# apl-source:27

# apl-source:28
def ايمرب(ن):
  # apl-source:29
  م = int(str(ن)[::-1])
  # apl-source:30
  return اولي(ن) and اولي(م) and م != ن
# apl-source:31

# apl-source:32
تأكد_يساوي(ايمرب(13), True, "١٣")
# apl-source:33
تأكد_يساوي(ايمرب(11), False, "١١")
# apl-source:34
تأكد_يساوي(ايمرب(17), True, "١٧")
# apl-source:35
تأكد_يساوي(ايمرب(23), False, "٢٣")
# apl-source:36
تأكد_يساوي(ايمرب(2), False, "٢")
# apl-source:37
