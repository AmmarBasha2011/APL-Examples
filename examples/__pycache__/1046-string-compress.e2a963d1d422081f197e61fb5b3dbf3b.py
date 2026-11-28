
# apl-source:1
# مثال 1046 — ضغط النص
# apl-source:2
# String compression
# apl-source:3
# Demonstrates: عد الحروف المتتالية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1046-string-compress.apl
# apl-source:6

# apl-source:7
# نكتب كل حرف وبعده عدد تكراره لو زاد عن واحد
# apl-source:8
# ولا نغير الحرف المفرد
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
def اضغط(نص_):
  # apl-source:19
  ناتج = ""
  # apl-source:20
  ع = 0
  # apl-source:21
  while ع < len(نص_):
    # apl-source:22
    ك = ع
    # apl-source:23
    while (ك < len(نص_)) and (نص_[ك] == نص_[ع]):
      # apl-source:24
      ك = ك + 1
    # apl-source:25
    ناتج = ناتج + نص_[ع]
    # apl-source:26
    if (ك - ع) > 1:
      # apl-source:27
      ناتج = ناتج + str(ك - ع)
    # apl-source:28
    ع = ك
  # apl-source:29
  return ناتج
# apl-source:30

# apl-source:31
تأكد_يساوي(اضغط("aabcccccaaa"), "a2bc5a3", "مثال")
# apl-source:32
تأكد_يساوي(اضغط("abc"), "abc", "بلا تكرار")
# apl-source:33
تأكد_يساوي(اضغط("zzzzzzzzzzzz"), "z12", "عدد بخانتين")
# apl-source:34
تأكد_يساوي(اضغط(""), "", "فارغ")
# apl-source:35
