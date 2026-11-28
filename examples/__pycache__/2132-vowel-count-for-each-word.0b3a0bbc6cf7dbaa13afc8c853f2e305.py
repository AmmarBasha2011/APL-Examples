
# apl-source:1
# مثال 2132 — عدد أحرف العلة في كل كلمة
# apl-source:2
# Vowel count per word
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2132-vowel-count-for-each-word.apl
# apl-source:6

# apl-source:7
# # نعد a وe وi وo وu
# apl-source:8
# # كل كلمة على حدة
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
def علل(س):
  # apl-source:19
  خرج = []
  # apl-source:20
  for ك in س.split():
    # apl-source:21
    عدد = 0
    # apl-source:22
    for ح in ك:
      # apl-source:23
      if ح in "aeiou":
        # apl-source:24
        عدد = عدد + 1
    # apl-source:25
    خرج = خرج + [عدد]
  # apl-source:26
  return خرج
# apl-source:27

# apl-source:28
تأكد_يساوي(علل("hello big world"), [2, 1, 1], "ثلاث كلمات")
# apl-source:29
تأكد_يساوي(علل(""), [], "فارغ")
# apl-source:30
تأكد_يساوي(علل("sky"), [0], "بلا علل")
# apl-source:31
