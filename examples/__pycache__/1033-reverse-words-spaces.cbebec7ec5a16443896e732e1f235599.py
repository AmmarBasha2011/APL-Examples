
# apl-source:1
# مثال 1033 — عكس الكلمات
# apl-source:2
# Reverse words in a sentence
# apl-source:3
# Demonstrates: مسح حرفاً حرفاً
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1033-reverse-words-spaces.apl
# apl-source:6

# apl-source:7
# نجمع الحروف في كلمة حتى فراغ ثم نضعها في أول القائمة
# apl-source:8
# فتخرج الكلمات بترتيب معكوس بلا فراغات زائدة
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
def اعكس_كلمات(جملة):
  # apl-source:19
  كلمات = []
  # apl-source:20
  حالية = ""
  # apl-source:21
  for ح in جملة + " ":
    # apl-source:22
    if ح == " ":
      # apl-source:23
      if حالية != "":
        # apl-source:24
        كلمات = [حالية] + كلمات
        # apl-source:25
        حالية = ""
    # apl-source:26
    else:
      # apl-source:27
      حالية = حالية + ح
  # apl-source:28
  return " ".join(كلمات)
# apl-source:29

# apl-source:30
تأكد_يساوي(اعكس_كلمات("the sky is blue"), "blue is sky the", "أربع كلمات")
# apl-source:31
تأكد_يساوي(اعكس_كلمات("  hello world  "), "world hello", "فراغات زائدة")
# apl-source:32
تأكد_يساوي(اعكس_كلمات("a  good   example"), "example good a", "فراغات متعددة")
# apl-source:33
