
# apl-source:1
# مثال 1010 — رسالة الفدية
# apl-source:2
# Ransom note
# apl-source:3
# Demonstrates: جرد الحروف
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1010-ransom-note.apl
# apl-source:6

# apl-source:7
# نجرد حروف المجلة في قائمة ثم نستهلك منها حروف الرسالة
# apl-source:8
# لو نفد حرف فالرسالة لا تُبنى
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
def تكفي(رسالة, مجلة):
  # apl-source:19
  متاح = []
  # apl-source:20
  for ح in مجلة:
    # apl-source:21
    متاح = متاح + [ح]
  # apl-source:22
  for ح in رسالة:
    # apl-source:23
    if ح in متاح:
      # apl-source:24
      ف = 0
      # apl-source:25
      while متاح[ف] != ح:
        # apl-source:26
        ف = ف + 1
      # apl-source:27
      متاح[ف] = ""
    # apl-source:28
    else:
      # apl-source:29
      return False
  # apl-source:30
  return True
# apl-source:31

# apl-source:32
تأكد_يساوي(تكفي("a", "b"), False, "حرف ناقص")
# apl-source:33
تأكد_يساوي(تكفي("aa", "ab"), False, "حرف مكرر ناقص")
# apl-source:34
تأكد_يساوي(تكفي("aa", "aab"), True, "يكفي")
# apl-source:35
تأكد_يساوي(تكفي("", "x"), True, "رسالة فارغة")
# apl-source:36
