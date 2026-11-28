
# apl-source:1
# مثال 1382 — متتالية متعرجة
# apl-source:2
# Wiggle subsequence length
# apl-source:3
# Demonstrates: جشع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1382-wiggle-subsequence-length.apl
# apl-source:6

# apl-source:7
# نتتبع أطول متتالية تنتهي بصعود أو هبوط
# apl-source:8
# كل تغير في الاتجاه يمدها
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
def اطول_متعرجة(أرقام):
  # apl-source:19
  if len(أرقام) == 0:
    # apl-source:20
    return 0
  # apl-source:21
  صعود = 1
  # apl-source:22
  هبوط = 1
  # apl-source:23
  for ع in range(1, len(أرقام)):
    # apl-source:24
    if أرقام[ع] > أرقام[ع - 1]:
      # apl-source:25
      صعود = هبوط + 1
    # apl-source:26
    elif أرقام[ع] < أرقام[ع - 1]:
      # apl-source:27
      هبوط = صعود + 1
  # apl-source:28
  return max(صعود, هبوط)
# apl-source:29

# apl-source:30
تأكد_يساوي(اطول_متعرجة([1,7,4,9,2,5]), 6, "ستة")
# apl-source:31
تأكد_يساوي(اطول_متعرجة([1,17,5,10,13,15,10,5,16,8]), 7, "سبعة")
# apl-source:32
تأكد_يساوي(اطول_متعرجة([1,2,3,4,5,6,7,8,9]), 2, "صاعدة")
# apl-source:33
