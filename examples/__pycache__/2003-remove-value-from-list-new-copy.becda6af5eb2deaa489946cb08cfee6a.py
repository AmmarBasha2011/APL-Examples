import copy
# apl-source:1
# مثال 2003 — حذف قيمة من القائمة بنسخة جديدة
# apl-source:2
# Remove value copy
# apl-source:3
# Demonstrates: قوائم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2003-remove-value-from-list-new-copy.apl
# apl-source:6

# apl-source:7
# # لا نعدل القائمة الأصلية
# apl-source:8
# # ونرجع النسخة الجديدة
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
def احذف(ق, قيمة):
  # apl-source:19
  خرج = []
  # apl-source:20
  for ع in ق:
    # apl-source:21
    if ع != قيمة:
      # apl-source:22
      خرج = خرج + [ع]
  # apl-source:23
  return خرج
# apl-source:24

# apl-source:25
أصل = [3, 2, 2, 3]
# apl-source:26
تأكد_يساوي(احذف(أصل, 3), [2, 2], "حذف ٣")
# apl-source:27
تأكد_يساوي(أصل, [3, 2, 2, 3], "الأصل سليم")
# apl-source:28
تأكد_يساوي(احذف([1, 1], 1), [], "كلها")
# apl-source:29
