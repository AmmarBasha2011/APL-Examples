
# apl-source:1
# مثال 1278 — الترتيب k بالاختيار السريع
# apl-source:2
# Kth largest with partition
# apl-source:3
# Demonstrates: تقسيم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1278-kth-largest-quickselect.apl
# apl-source:6

# apl-source:7
# نقسم حول محور
# apl-source:8
# ونكمل في الجهة التي فيها الترتيب
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
def الاكبر_ك(أ, ك):
  # apl-source:19
  ق = list(أ)
  # apl-source:20
  هدف = len(ق) - ك
  # apl-source:21
  يسار = 0
  # apl-source:22
  يمين = len(ق) - 1
  # apl-source:23
  while يسار < يمين:
    # apl-source:24
    محور = ق[يمين]
    # apl-source:25
    ع = يسار
    # apl-source:26
    for ج in range(يسار, يمين):
      # apl-source:27
      if ق[ج] < محور:
        # apl-source:28
        ت = ق[ع]
        # apl-source:29
        ق[ع] = ق[ج]
        # apl-source:30
        ق[ج] = ت
        # apl-source:31
        ع = ع + 1
    # apl-source:32
    ت = ق[ع]
    # apl-source:33
    ق[ع] = ق[يمين]
    # apl-source:34
    ق[يمين] = ت
    # apl-source:35
    if ع == هدف:
      # apl-source:36
      return ق[ع]
    # apl-source:37
    elif ع < هدف:
      # apl-source:38
      يسار = ع + 1
    # apl-source:39
    else:
      # apl-source:40
      يمين = ع - 1
  # apl-source:41
  return ق[هدف]
# apl-source:42

# apl-source:43
تأكد_يساوي(الاكبر_ك([3,2,1,5,6,4], 2), 5, "الثاني")
# apl-source:44
تأكد_يساوي(الاكبر_ك([3,2,3,1,2,4,5,5,6], 4), 4, "الرابع")
# apl-source:45
تأكد_يساوي(الاكبر_ك([1], 1), 1, "عنصر")
# apl-source:46
