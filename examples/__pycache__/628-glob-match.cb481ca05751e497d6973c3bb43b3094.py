
# apl-source:1
# مثال 628 — مطابقة glob
# apl-source:2
# Glob matching
# apl-source:3
# Demonstrates: نجمة، استفهام، أنماط ملفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/628-glob-match.apl
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
# مطابقة أنماط glob: النجمة وعلامة الاستفهام
# apl-source:25
# Demonstrates: مطابقة عودية, نجمة متعددة الأحرف, استفهام أحادي
# apl-source:26
# نفس منطق أسماء الملفات في الأنظمة
# apl-source:27

# apl-source:28
def طابق(نمط, نص):
  # apl-source:29
  if نمط == "":
    # apl-source:30
    return نص == ""
  # apl-source:31
  if نمط[0] == "*":
    # apl-source:32
    for ك in range(len(نص) + 1):
      # apl-source:33
      if طابق(نمط[1:], نص[ك:]):
        # apl-source:34
        return True
    # apl-source:35
    return False
  # apl-source:36
  if نص == "":
    # apl-source:37
    return False
  # apl-source:38
  if نمط[0] == "?" or نمط[0] == نص[0]:
    # apl-source:39
    return طابق(نمط[1:], نص[1:])
  # apl-source:40
  return False
# apl-source:41

# apl-source:42
تأكد_يساوي(طابق("*.apl", "test.apl"), True, "امتداد")
# apl-source:43
تأكد_يساوي(طابق("*.apl", "test.py"), False, "امتداد مختلف")
# apl-source:44
تأكد_يساوي(طابق("م?رحبا", "مرحبا"), False, "استفهام يتطلب حرفا")
# apl-source:45
تأكد_يساوي(طابق("م?رحبا", "مبرحبا"), True, "استفهام يطابق حرفا")
# apl-source:46
تأكد_يساوي(طابق("*", "أي شيء"), True, "نجمة وحدها")
# apl-source:47
تأكد_يساوي(طابق("abc*def", "abcdef"), True, "نجمة صفرية")
# apl-source:48
print("*.apl مع test.apl:", طابق("*.apl", "test.apl"))
# apl-source:49
