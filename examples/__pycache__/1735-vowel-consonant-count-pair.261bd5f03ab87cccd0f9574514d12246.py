
# apl-source:1
# مثال 1735 — عدد الحروف المتحركة والساكنة
# apl-source:2
# Count vowels and consonants
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1735-vowel-consonant-count-pair.apl
# apl-source:6

# apl-source:7
# نحدد الحروف المتحركة بقائمة
# apl-source:8
# غير المتحركة من الحروف ساكنة
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
def عد_الحروف(س):
  # apl-source:19
  متحركة = "aeiou"
  # apl-source:20
  م = 0
  # apl-source:21
  ك = 0
  # apl-source:22
  for ح in س.lower():
    # apl-source:23
    if ح.isalpha():
      # apl-source:24
      if ح in متحركة:
        # apl-source:25
        م = م + 1
      # apl-source:26
      else:
        # apl-source:27
        ك = ك + 1
  # apl-source:28
  return [م, ك]
# apl-source:29

# apl-source:30
تأكد_يساوي(عد_الحروف("Hello"), [2, 3], "مرحبا")
# apl-source:31
تأكد_يساوي(عد_الحروف("a e i"), [3, 0], "متحركات")
# apl-source:32
تأكد_يساوي(عد_الحروف("123"), [0, 0], "أرقام")
# apl-source:33
