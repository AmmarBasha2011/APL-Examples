
# apl-source:1
# مثال 1896 — كل التوافيق من قائمة
# apl-source:2
# List all k combinations
# apl-source:3
# Demonstrates: تراجع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1896-list-combinations-n-choose-k.apl
# apl-source:6

# apl-source:7
# نختار عنصرا ثم نكمل من بعده
# apl-source:8
# نجمع التوافيق بالترتيب
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
def توافيق(ق, ك, بداية):
  # apl-source:19
  if ك == 0:
    # apl-source:20
    return [[]]
  # apl-source:21
  نتيجة = []
  # apl-source:22
  for ي in range(بداية, len(ق)):
    # apl-source:23
    for بقية in توافيق(ق, ك - 1, ي + 1):
      # apl-source:24
      نتيجة = نتيجة + [[ق[ي]] + بقية]
  # apl-source:25
  return نتيجة
# apl-source:26

# apl-source:27
ج = توافيق([1, 2, 3, 4], 2, 0)
# apl-source:28
تأكد_يساوي(len(ج), 6, "ستة توافيق")
# apl-source:29
تأكد_يساوي(ج[0], [1, 2], "الأول")
# apl-source:30
تأكد_يساوي(ج[5], [3, 4], "الأخير")
# apl-source:31
