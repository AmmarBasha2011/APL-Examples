
# apl-source:1
# مثال 1471 — توسيط نص بالحشو
# apl-source:2
# Center text with padding
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1471-center-text-padding.apl
# apl-source:6

# apl-source:7
# الحشو الكلي هو الفرق بين العرضين
# apl-source:8
# النصف على كل جانب والزائد يمين
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
def وسّط(نص_, عرض, حشو):
  # apl-source:19
  if len(نص_) >= عرض:
    # apl-source:20
    return نص_
  # apl-source:21
  كلي = عرض - len(نص_)
  # apl-source:22
  يسار = كلي // 2
  # apl-source:23
  يمين = كلي - يسار
  # apl-source:24
  return حشو * يسار + نص_ + حشو * يمين
# apl-source:25

# apl-source:26
تأكد_يساوي(وسّط("ab", 6, "*"), "**ab**", "زوجي")
# apl-source:27
تأكد_يساوي(وسّط("abc", 6, "-"), "-abc--", "فردي")
# apl-source:28
تأكد_يساوي(وسّط("abcdef", 3, "*"), "abcdef", "أطول")
# apl-source:29
