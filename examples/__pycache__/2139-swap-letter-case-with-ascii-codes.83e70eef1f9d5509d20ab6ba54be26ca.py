
# apl-source:1
# مثال 2139 — عكس حالة الأحرف بأكواد ASCII
# apl-source:2
# Swap case with ASCII
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2139-swap-letter-case-with-ascii-codes.apl
# apl-source:6

# apl-source:7
# # الأحرف الأخرى تبقى
# apl-source:8
# # نستخدم ord وchr
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
def اعكس(س):
  # apl-source:19
  خرج = ""
  # apl-source:20
  for ح in س:
    # apl-source:21
    ر = ord(ح)
    # apl-source:22
    if ر >= 65 and ر <= 90:
      # apl-source:23
      خرج = خرج + chr(ر + 32)
    # apl-source:24
    elif ر >= 97 and ر <= 122:
      # apl-source:25
      خرج = خرج + chr(ر - 32)
    # apl-source:26
    else:
      # apl-source:27
      خرج = خرج + ح
  # apl-source:28
  return خرج
# apl-source:29

# apl-source:30
تأكد_يساوي(اعكس("Hello World"), "hELLO wORLD", "عبارة")
# apl-source:31
تأكد_يساوي(اعكس("a1B2"), "A1b2", "أرقام")
# apl-source:32
تأكد_يساوي(اعكس(""), "", "فارغ")
# apl-source:33
