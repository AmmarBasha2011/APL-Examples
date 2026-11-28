
# apl-source:1
# مثال 1898 — توسيط نص بحشو
# apl-source:2
# Center text with padding
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1898-text-center-with-padding.apl
# apl-source:6

# apl-source:7
# نحسب الحشو الكلي
# apl-source:8
# اليسار نصف والباقي لليمين
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
def كرر(ح, ن):
  # apl-source:19
  خرج = ""
  # apl-source:20
  for ك in range(ن):
    # apl-source:21
    خرج = خرج + ح
  # apl-source:22
  return خرج
# apl-source:23

# apl-source:24
def وسط(نص, عرض, ح):
  # apl-source:25
  if len(نص) >= عرض:
    # apl-source:26
    return نص
  # apl-source:27
  كلي = عرض - len(نص)
  # apl-source:28
  يسار = كلي // 2
  # apl-source:29
  return كرر(ح, يسار) + نص + كرر(ح, كلي - يسار)
# apl-source:30

# apl-source:31
تأكد_يساوي(وسط("hi", 6, "*"), "**hi**", "زوجي")
# apl-source:32
تأكد_يساوي(وسط("abc", 6, "-"), "-abc--", "فردي")
# apl-source:33
تأكد_يساوي(وسط("long", 2, "*"), "long", "أطول من العرض")
# apl-source:34
