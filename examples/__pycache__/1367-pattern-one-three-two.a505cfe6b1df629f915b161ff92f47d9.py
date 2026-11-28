
# apl-source:1
# مثال 1367 — نمط واحد ثلاثة اثنين
# apl-source:2
# Pattern 132 detection
# apl-source:3
# Demonstrates: مكدس أحادي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1367-pattern-one-three-two.apl
# apl-source:6

# apl-source:7
# نمر من اليمين مع مكدس متناقص
# apl-source:8
# نحتفظ بأكبر قيمة كانت وسطاً
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
def نمط_132(أرقام):
  # apl-source:19
  ثالث = -1000000000
  # apl-source:20
  مكدس = []
  # apl-source:21
  for ع in range(len(أرقام) - 1, -1, -1):
    # apl-source:22
    if أرقام[ع] < ثالث:
      # apl-source:23
      return True
    # apl-source:24
    while (len(مكدس) > 0) and (مكدس[len(مكدس) - 1] < أرقام[ع]):
      # apl-source:25
      ثالث = مكدس.pop()
    # apl-source:26
    مكدس = مكدس + [أرقام[ع]]
  # apl-source:27
  return False
# apl-source:28

# apl-source:29
تأكد_يساوي(نمط_132([1,2,3,4]), False, "لا نمط")
# apl-source:30
تأكد_يساوي(نمط_132([3,1,4,2]), True, "يوجد")
# apl-source:31
تأكد_يساوي(نمط_132([-1,3,2,0]), True, "سالبة")
# apl-source:32
