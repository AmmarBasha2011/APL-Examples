
# apl-source:1
# مثال 1973 — من snake_case إلى كلمات بحروف كبيرة
# apl-source:2
# Snake case to title words
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1973-snake-case-to-title-words.apl
# apl-source:6

# apl-source:7
# # نستخدم الدالة split ثم capitalize
# apl-source:8
# # ونجمع الأجزاء بمسافة
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
def عنوان(س):
  # apl-source:19
  اجزاء = س.split("_")
  # apl-source:20
  خرج = []
  # apl-source:21
  for ج in اجزاء:
    # apl-source:22
    if ج != "":
      # apl-source:23
      خرج = خرج + [ج.capitalize()]
  # apl-source:24
  return " ".join(خرج)
# apl-source:25

# apl-source:26
تأكد_يساوي(عنوان("hello_big_world"), "Hello Big World", "ثلاث كلمات")
# apl-source:27
تأكد_يساوي(عنوان("a_b"), "A B", "حرفان")
# apl-source:28
تأكد_يساوي(عنوان(""), "", "فارغ")
# apl-source:29
تأكد_يساوي(عنوان("__x__y_"), "X Y", "شرطات زائدة")
# apl-source:30
