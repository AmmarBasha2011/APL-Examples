
# apl-source:1
# مثال 1715 — أقصى عمق في قوائم متداخلة
# apl-source:2
# Maximum nesting depth of lists
# apl-source:3
# Demonstrates: أشجار
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1715-nested-list-flatten-depth.apl
# apl-source:6

# apl-source:7
# القائمة تضيف مستوى
# apl-source:8
# نأخذ أكبر عمق للأبناء
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
def أقصى_عمق(ش):
  # apl-source:19
  if type(ش) != type([]):
    # apl-source:20
    return 0
  # apl-source:21
  أفضل = 0
  # apl-source:22
  for ع in ش:
    # apl-source:23
    أفضل = max(أفضل, أقصى_عمق(ع))
  # apl-source:24
  return أفضل + 1
# apl-source:25

# apl-source:26
تأكد_يساوي(أقصى_عمق([1, [2, [3]]]), 3, "ثلاثة")
# apl-source:27
تأكد_يساوي(أقصى_عمق([]), 1, "فارغة")
# apl-source:28
تأكد_يساوي(أقصى_عمق(5), 0, "رقم")
# apl-source:29
