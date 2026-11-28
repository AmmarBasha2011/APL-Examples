
# apl-source:1
# مثال 2103 — متتالية بادوفان
# apl-source:2
# Padovan sequence
# apl-source:3
# Demonstrates: متتاليات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2103-padovan-sequence-terms-list.apl
# apl-source:6

# apl-source:7
# # P(n) = P(n-2) + P(n-3)
# apl-source:8
# # نبدأ بثلاثة آحاد
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
  ق = [1, 1, 1]
  # apl-source:20
  for ك in range(3, ن):
    # apl-source:21
    ق = ق + [ق[ك - 2] + ق[ك - 3]]
  # apl-source:22
  return ق[:ن]
# apl-source:23

# apl-source:24
تأكد_يساوي(بادوفان(11), [1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12], "أحد عشر")
# apl-source:25
تأكد_يساوي(بادوفان(2), [1, 1], "اثنان")
# apl-source:26
