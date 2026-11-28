
# apl-source:1
# مثال 1428 — فرز حروف العلة
# apl-source:2
# Sort vowels keeping consonants
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1428-sort-vowels-in-string.apl
# apl-source:6

# apl-source:7
# نجمع حروف العلة ونرتبها بحسب ترتيب الحروف
# apl-source:8
# ثم نعيدها إلى مواضع حروف العلة
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
def فرز_العلة(نص_):
  # apl-source:19
  علة = "aeiouAEIOU"
  # apl-source:20
  حروف = []
  # apl-source:21
  for ح in نص_:
    # apl-source:22
    if ح in علة:
      # apl-source:23
      حروف = حروف + [ح]
  # apl-source:24
  حروف = sorted(حروف)
  # apl-source:25
  ناتج = ""
  # apl-source:26
  ك = 0
  # apl-source:27
  for ح in نص_:
    # apl-source:28
    if ح in علة:
      # apl-source:29
      ناتج = ناتج + حروف[ك]
      # apl-source:30
      ك = ك + 1
    # apl-source:31
    else:
      # apl-source:32
      ناتج = ناتج + ح
  # apl-source:33
  return ناتج
# apl-source:34

# apl-source:35
تأكد_يساوي(فرز_العلة("lEetcOde"), "lEOtcede", "مثال أول")
# apl-source:36
تأكد_يساوي(فرز_العلة("lYmph"), "lYmph", "بلا علة")
# apl-source:37
تأكد_يساوي(فرز_العلة("aA"), "Aa", "حرفان")
# apl-source:38
