
# apl-source:1
# مثال 1521 — عد الحروف المتحركة والساكنة
# apl-source:2
# Vowel and consonant counts
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1521-vowel-consonant-split.apl
# apl-source:6

# apl-source:7
# نعد aeiou حروف علة
# apl-source:8
# وبقية الحروف الأبجدية ساكنة
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
def عد_الحروف(نص_):
  # apl-source:19
  علة = 0
  # apl-source:20
  ساكنة = 0
  # apl-source:21
  for ح in نص_.lower():
    # apl-source:22
    if ح.isalpha():
      # apl-source:23
      if ح in "aeiou":
        # apl-source:24
        علة = علة + 1
      # apl-source:25
      else:
        # apl-source:26
        ساكنة = ساكنة + 1
  # apl-source:27
  return [علة, ساكنة]
# apl-source:28

# apl-source:29
تأكد_يساوي(عد_الحروف("Hello World"), [3, 7], "جملة")
# apl-source:30
تأكد_يساوي(عد_الحروف("AEIOU"), [5, 0], "علة فقط")
# apl-source:31
تأكد_يساوي(عد_الحروف("123"), [0, 0], "أرقام")
# apl-source:32
