
# apl-source:1
# مثال 2449 — تكرار النص 5 مرات بشرطة
# apl-source:2
# Repeat text 5 times
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2449-repeat-text-5-times-with-dash.apl
# apl-source:6

# apl-source:7
# # ندخل النص
# apl-source:8
# # ونقارن النتيجة
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
def ف(ن):
  # apl-source:19
  ر = []
  # apl-source:20
  for ي in range(5):
    # apl-source:21
    ر = ر + [ن]
  # apl-source:22
  return "-".join(ر)
# apl-source:23

# apl-source:24
تأكد_يساوي(ف("a"), "a-a-a-a-a", "حالة 1")
# apl-source:25
تأكد_يساوي(ف("ab"), "ab-ab-ab-ab-ab", "حالة 2")
# apl-source:26
تأكد_يساوي(ف("xyz"), "xyz-xyz-xyz-xyz-xyz", "حالة 3")
# apl-source:27
