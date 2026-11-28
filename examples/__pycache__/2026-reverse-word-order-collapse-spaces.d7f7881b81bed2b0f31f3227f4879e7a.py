
# apl-source:1
# مثال 2026 — عكس ترتيب الكلمات مع إزالة المسافات الزائدة
# apl-source:2
# Reverse word order
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2026-reverse-word-order-collapse-spaces.apl
# apl-source:6

# apl-source:7
# # split بلا وسيط تتجاهل المسافات المتكررة
# apl-source:8
# # ثم نعكس القائمة
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
  كلمات = س.split()
  # apl-source:20
  كلمات.reverse()
  # apl-source:21
  return " ".join(كلمات)
# apl-source:22

# apl-source:23
تأكد_يساوي(اعكس("  hello   world "), "world hello", "مسافات زائدة")
# apl-source:24
تأكد_يساوي(اعكس("a b c"), "c b a", "ثلاث")
# apl-source:25
تأكد_يساوي(اعكس(""), "", "فارغ")
# apl-source:26
