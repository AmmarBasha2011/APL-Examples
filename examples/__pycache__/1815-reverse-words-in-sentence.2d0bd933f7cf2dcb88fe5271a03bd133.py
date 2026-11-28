
# apl-source:1
# مثال 1815 — عكس ترتيب الكلمات
# apl-source:2
# Reverse words in a sentence
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1815-reverse-words-in-sentence.apl
# apl-source:6

# apl-source:7
# نقسم بالمسافة
# apl-source:8
# نجمع من النهاية
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
def اعكس_الجملة(س):
  # apl-source:19
  كلمات = س.split(" ")
  # apl-source:20
  كلمات.reverse()
  # apl-source:21
  return " ".join(كلمات)
# apl-source:22

# apl-source:23
تأكد_يساوي(اعكس_الجملة("the sky is blue"), "blue is sky the", "أربع")
# apl-source:24
تأكد_يساوي(اعكس_الجملة("hello"), "hello", "كلمة")
# apl-source:25
تأكد_يساوي(اعكس_الجملة("a b"), "b a", "اثنتان")
# apl-source:26
