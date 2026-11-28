
# apl-source:1
# مثال 1473 — عنوان إلى رابط مختصر
# apl-source:2
# Title to URL slug
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1473-title-to-slug.apl
# apl-source:6

# apl-source:7
# نصغر الحروف
# apl-source:8
# نستبدل كل ما ليس حرفاً أو رقماً بشرطة واحدة
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
def رابط(عنوان):
  # apl-source:19
  ناتج = ""
  # apl-source:20
  سابق_شرطة = False
  # apl-source:21
  for ح in عنوان.lower():
    # apl-source:22
    if ح.isalpha() or ح.isdigit():
      # apl-source:23
      ناتج = ناتج + ح
      # apl-source:24
      سابق_شرطة = False
    # apl-source:25
    elif سابق_شرطة == False and ناتج != "":
      # apl-source:26
      ناتج = ناتج + "-"
      # apl-source:27
      سابق_شرطة = True
  # apl-source:28
  if ناتج.endswith("-"):
    # apl-source:29
    ناتج = ناتج[0:len(ناتج) - 1]
  # apl-source:30
  return ناتج
# apl-source:31

# apl-source:32
تأكد_يساوي(رابط("Hello World"), "hello-world", "مسافة")
# apl-source:33
تأكد_يساوي(رابط("  Hi,  there!! "), "hi-there", "رموز ومسافات")
# apl-source:34
تأكد_يساوي(رابط("APL 2024"), "apl-2024", "أرقام")
# apl-source:35
