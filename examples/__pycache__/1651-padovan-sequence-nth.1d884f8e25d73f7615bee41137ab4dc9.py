
# apl-source:1
# مثال 1651 — متتالية بادوفان
# apl-source:2
# Padovan sequence
# apl-source:3
# Demonstrates: متتاليات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1651-padovan-sequence-nth.apl
# apl-source:6

# apl-source:7
# أول ثلاثة حدود واحد
# apl-source:8
# ثم ف(ن) = ف(ن-2) + ف(ن-3)
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
def بادوفان(ن):
  # apl-source:19
  if ن < 3:
    # apl-source:20
    return 1
  # apl-source:21
  ق = [1, 1, 1]
  # apl-source:22
  for ع in range(3, ن + 1):
    # apl-source:23
    ق.append(ق[ع - 2] + ق[ع - 3])
  # apl-source:24
  return ق[ن]
# apl-source:25

# apl-source:26
تأكد_يساوي(بادوفان(0), 1, "الأول")
# apl-source:27
تأكد_يساوي(بادوفان(3), 2, "الرابع")
# apl-source:28
تأكد_يساوي(بادوفان(10), 12, "الحادي عشر")
# apl-source:29
تأكد_يساوي(بادوفان(15), 49, "السادس عشر")
# apl-source:30
