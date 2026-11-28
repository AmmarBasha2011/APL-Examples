
# apl-source:1
# مثال 1933 — فك ضغط النص بالتكرار
# apl-source:2
# Run length decode single digit counts
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1933-run-length-decode-single-digit.apl
# apl-source:6

# apl-source:7
# نقرأ الأزواج حرف ورقم
# apl-source:8
# نكرر الحرف بقدر الرقم
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
def افك(س):
  # apl-source:19
  خرج = ""
  # apl-source:20
  ك = 0
  # apl-source:21
  while ك < len(س):
    # apl-source:22
    ح = س[ك]
    # apl-source:23
    ن = 0
    # apl-source:24
    for ت in range(10):
      # apl-source:25
      if str(ت) == س[ك + 1]:
        # apl-source:26
        ن = ت
    # apl-source:27
    for ت in range(ن):
      # apl-source:28
      خرج = خرج + ح
    # apl-source:29
    ك = ك + 2
  # apl-source:30
  return خرج
# apl-source:31

# apl-source:32
تأكد_يساوي(افك("a3b1c2"), "aaabcc", "مثال")
# apl-source:33
تأكد_يساوي(افك("z1"), "z", "حرف")
# apl-source:34
تأكد_يساوي(افك(""), "", "فارغ")
# apl-source:35
