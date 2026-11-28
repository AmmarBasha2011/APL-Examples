
# apl-source:1
# مثال 1681 — كومة صغرى يدوية
# apl-source:2
# Manual min heap push and pop
# apl-source:3
# Demonstrates: هياكل بيانات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1681-min-heap-manual-push-pop.apl
# apl-source:6

# apl-source:7
# الإضافة تصعد العنصر
# apl-source:8
# الحذف ينقل الأخير للجذر وينزله
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
def ادفع(كومة, قيمة):
  # apl-source:19
  كومة.append(قيمة)
  # apl-source:20
  ك = len(كومة) - 1
  # apl-source:21
  while ك > 0:
    # apl-source:22
    أب = (ك - 1) // 2
    # apl-source:23
    if كومة[أب] > كومة[ك]:
      # apl-source:24
      ت = كومة[أب]
      # apl-source:25
      كومة[أب] = كومة[ك]
      # apl-source:26
      كومة[ك] = ت
      # apl-source:27
      ك = أب
    # apl-source:28
    else:
      # apl-source:29
      ك = 0
# apl-source:30

# apl-source:31
def اسحب(كومة):
  # apl-source:32
  أول = كومة[0]
  # apl-source:33
  أخير = كومة.pop()
  # apl-source:34
  if len(كومة) > 0:
    # apl-source:35
    كومة[0] = أخير
    # apl-source:36
    ك = 0
    # apl-source:37
    while True:
      # apl-source:38
      يسار = 2 * ك + 1
      # apl-source:39
      يمين = 2 * ك + 2
      # apl-source:40
      صغير = ك
      # apl-source:41
      if يسار < len(كومة):
        # apl-source:42
        if كومة[يسار] < كومة[صغير]:
          # apl-source:43
          صغير = يسار
      # apl-source:44
      if يمين < len(كومة):
        # apl-source:45
        if كومة[يمين] < كومة[صغير]:
          # apl-source:46
          صغير = يمين
      # apl-source:47
      if صغير == ك:
        # apl-source:48
        return أول
      # apl-source:49
      ت = كومة[ك]
      # apl-source:50
      كومة[ك] = كومة[صغير]
      # apl-source:51
      كومة[صغير] = ت
      # apl-source:52
      ك = صغير
  # apl-source:53
  return أول
# apl-source:54

# apl-source:55
ك = []
# apl-source:56
for ع in [5, 3, 8, 1, 9, 2]:
  # apl-source:57
  ادفع(ك, ع)
# apl-source:58
خرج = []
# apl-source:59
while len(ك) > 0:
  # apl-source:60
  خرج.append(اسحب(ك))
# apl-source:61
تأكد_يساوي(خرج, [1, 2, 3, 5, 8, 9], "ترتيب")
# apl-source:62
