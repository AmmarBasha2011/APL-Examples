
# apl-source:1
# مثال 629 — محرك تعبيرات نمطية مصغر
# apl-source:2
# Mini regex engine
# apl-source:3
# Demonstrates: تعبيرات نمطية، نجمة كلفن، بدل
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/629-regex-nfa-lite.apl
# apl-source:6

# apl-source:7
# Assertion style:
# apl-source:8
#   دالة تأكد_يساوي(فعلي, متوقع, اسم):
# apl-source:9
#     لو فعلي != متوقع:
# apl-source:10
#       اطبع "فشل:", اسم
# apl-source:11
#       اطبع "  متوقع:", متوقع
# apl-source:12
#       اطبع "  فعلي:", فعلي
# apl-source:13
#       قياسي_نظام_اخرج(1)
# apl-source:14
#     اطبع "ناجح:", اسم
# apl-source:15

# apl-source:16
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:17
  if فعلي != متوقع:
    # apl-source:18
    print("فشل:", اسم)
    # apl-source:19
    print("  متوقع:", متوقع)
    # apl-source:20
    print("  فعلي:", فعلي)
    # apl-source:21
    قياسي_نظام_اخرج(1)
  # apl-source:22
  print("ناجح:", اسم)
# apl-source:23

# apl-source:24
# محرك تعبيرات نمطية مصغر: حرف ونقطة ونجمة
# apl-source:25
# Demonstrates: مطابقة عودية, كلفن نجمة, نقطة البدل
# apl-source:26
# جوهر التعبيرات النمطية بثلاث قواعد فقط
# apl-source:27

# apl-source:28
def طابق(نمط, نص):
  # apl-source:29
  if نمط == "":
    # apl-source:30
    return نص == ""
  # apl-source:31
  أول = نص != "" and (نمط[0] == نص[0] or نمط[0] == ".")
  # apl-source:32
  if len(نمط) >= 2 and نمط[1] == "*":
    # apl-source:33
    if طابق(نمط[2:], نص):
      # apl-source:34
      return True
    # apl-source:35
    return أول and طابق(نمط, نص[1:])
  # apl-source:36
  return أول and طابق(نمط[1:], نص[1:])
# apl-source:37

# apl-source:38
تأكد_يساوي(طابق("aab", "aab"), True, "حرفي")
# apl-source:39
تأكد_يساوي(طابق("a*b", "b"), True, "نجمة صفرية")
# apl-source:40
تأكد_يساوي(طابق("a*b", "aaab"), True, "نجمة متكررة")
# apl-source:41
تأكد_يساوي(طابق("a.b", "acb"), True, "نقطة بدل")
# apl-source:42
تأكد_يساوي(طابق("a*b", "aaa"), False, "يجب أن ينتهي بباء")
# apl-source:43
تأكد_يساوي(طابق("c*a*b", "aab"), True, "نجمتان متتاليتان")
# apl-source:44
print("c*a*b مع aab:", طابق("c*a*b", "aab"))
# apl-source:45
