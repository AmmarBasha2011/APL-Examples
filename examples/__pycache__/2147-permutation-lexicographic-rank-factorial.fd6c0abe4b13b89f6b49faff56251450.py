
# apl-source:1
# مثال 2147 — رتبة التبديلة بالترتيب المعجمي
# apl-source:2
# Permutation rank
# apl-source:3
# Demonstrates: توافيق
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2147-permutation-lexicographic-rank-factorial.apl
# apl-source:6

# apl-source:7
# # الرتبة تبدأ من صفر
# apl-source:8
# # نحذف الحرف بعد استخدامه
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
def رتبة(س):
  # apl-source:19
  باقي = sorted(س)
  # apl-source:20
  رتب = 0
  # apl-source:21
  مض = 1
  # apl-source:22
  for ك in range(2, len(س)):
    # apl-source:23
    مض = مض * ك
  # apl-source:24
  for ك in range(len(س)):
    # apl-source:25
    موضع = باقي.index(س[ك])
    # apl-source:26
    رتب = رتب + موضع * مض
    # apl-source:27
    باقي.pop(موضع)
    # apl-source:28
    if len(س) - 1 - ك > 0:
      # apl-source:29
      مض = مض // (len(س) - 1 - ك)
  # apl-source:30
  return رتب
# apl-source:31

# apl-source:32
تأكد_يساوي(رتبة("abc"), 0, "الأولى")
# apl-source:33
تأكد_يساوي(رتبة("bca"), 3, "الرابعة")
# apl-source:34
تأكد_يساوي(رتبة("cba"), 5, "الأخيرة")
# apl-source:35
