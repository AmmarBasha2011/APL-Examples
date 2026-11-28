
# apl-source:1
# مثال 2037 — ترتيب الحروف حسب التكرار
# apl-source:2
# Sort characters by frequency
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2037-characters-sorted-by-frequency-desc.apl
# apl-source:6

# apl-source:7
# # نعد الحروف ونرتب بزوج السالب والحرف
# apl-source:8
# # ثم نكرر كل حرف بعدده
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
def رتب(س):
  # apl-source:19
  عد = {}
  # apl-source:20
  for ح in س:
    # apl-source:21
    عد[ح] = عد.get(ح, 0) + 1
  # apl-source:22
  ازواج = []
  # apl-source:23
  for ح in عد:
    # apl-source:24
    ازواج = ازواج + [[-عد[ح], ح]]
  # apl-source:25
  ازواج = sorted(ازواج)
  # apl-source:26
  خرج = ""
  # apl-source:27
  for ز in ازواج:
    # apl-source:28
    خرج = خرج + ز[1] * (-ز[0])
  # apl-source:29
  return خرج
# apl-source:30

# apl-source:31
تأكد_يساوي(رتب("tree"), "eert", "tree")
# apl-source:32
تأكد_يساوي(رتب("cccaaa"), "aaaccc", "تعادل")
# apl-source:33
تأكد_يساوي(رتب(""), "", "فارغ")
# apl-source:34
