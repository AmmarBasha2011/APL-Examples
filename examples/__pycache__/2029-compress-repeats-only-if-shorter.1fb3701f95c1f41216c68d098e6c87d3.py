
# apl-source:1
# مثال 2029 — ضغط التكرارات إذا قصر النص
# apl-source:2
# Compress repeats if shorter
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2029-compress-repeats-only-if-shorter.apl
# apl-source:6

# apl-source:7
# # نبني النص المضغوط من مجموعات متتالية
# apl-source:8
# # ونقارن الطول مع الأصل
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
def اضغط(س):
  # apl-source:19
  خرج = ""
  # apl-source:20
  ك = 0
  # apl-source:21
  while ك < len(س):
    # apl-source:22
    ي = ك
    # apl-source:23
    while ي < len(س) and س[ي] == س[ك]:
      # apl-source:24
      ي = ي + 1
    # apl-source:25
    خرج = خرج + س[ك] + str(ي - ك)
    # apl-source:26
    ك = ي
  # apl-source:27
  if len(خرج) < len(س):
    # apl-source:28
    return خرج
  # apl-source:29
  return س
# apl-source:30

# apl-source:31
تأكد_يساوي(اضغط("aabcccccaaa"), "a2b1c5a3", "مضغوط")
# apl-source:32
تأكد_يساوي(اضغط("abc"), "abc", "أطول")
# apl-source:33
تأكد_يساوي(اضغط("aabb"), "aabb", "مساو")
# apl-source:34
