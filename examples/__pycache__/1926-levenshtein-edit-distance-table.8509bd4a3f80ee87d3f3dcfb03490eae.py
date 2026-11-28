
# apl-source:1
# مثال 1926 — مسافة التعديل بين نصين
# apl-source:2
# Levenshtein edit distance
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1926-levenshtein-edit-distance-table.apl
# apl-source:6

# apl-source:7
# نملأ الجدول من الصف الأول والعمود الأول
# apl-source:8
# نأخذ أقل تكلفة من ثلاث عمليات
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
def مسافة(أ, ب):
  # apl-source:19
  ج = []
  # apl-source:20
  for ي in range(len(أ) + 1):
    # apl-source:21
    صف = []
    # apl-source:22
    for ك in range(len(ب) + 1):
      # apl-source:23
      صف = صف + [0]
    # apl-source:24
    ج = ج + [صف]
  # apl-source:25
  for ي in range(len(أ) + 1):
    # apl-source:26
    ج[ي][0] = ي
  # apl-source:27
  for ك in range(len(ب) + 1):
    # apl-source:28
    ج[0][ك] = ك
  # apl-source:29
  for ي in range(1, len(أ) + 1):
    # apl-source:30
    for ك in range(1, len(ب) + 1):
      # apl-source:31
      تكلفة = 1
      # apl-source:32
      if أ[ي - 1] == ب[ك - 1]:
        # apl-source:33
        تكلفة = 0
      # apl-source:34
      ج[ي][ك] = min(ج[ي - 1][ك] + 1, ج[ي][ك - 1] + 1, ج[ي - 1][ك - 1] + تكلفة)
  # apl-source:35
  return ج[len(أ)][len(ب)]
# apl-source:36

# apl-source:37
تأكد_يساوي(مسافة("kitten", "sitting"), 3, "kitten")
# apl-source:38
تأكد_يساوي(مسافة("", "abc"), 3, "فارغ")
# apl-source:39
تأكد_يساوي(مسافة("same", "same"), 0, "متطابق")
# apl-source:40
