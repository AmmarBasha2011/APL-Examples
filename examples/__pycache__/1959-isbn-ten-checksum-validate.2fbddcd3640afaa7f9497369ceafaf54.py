
# apl-source:1
# مثال 1959 — التحقق من رقم ISBN-10
# apl-source:2
# ISBN-10 validation
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1959-isbn-ten-checksum-validate.apl
# apl-source:6

# apl-source:7
# # الرمز X في الآخر يساوي 10
# apl-source:8
# # نرفض أي طول غير عشرة
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
def صحيح_isbn(س):
  # apl-source:19
  if len(س) != 10:
    # apl-source:20
    return False
  # apl-source:21
  مج = 0
  # apl-source:22
  for ك in range(10):
    # apl-source:23
    ح = س[ك]
    # apl-source:24
    if ح == "X":
      # apl-source:25
      ق = 10
    # apl-source:26
    else:
      # apl-source:27
      ق = int(ح)
    # apl-source:28
    مج = مج + ق * (10 - ك)
  # apl-source:29
  return مج % 11 == 0
# apl-source:30

# apl-source:31
تأكد_يساوي(صحيح_isbn("0306406152"), True, "صحيح")
# apl-source:32
تأكد_يساوي(صحيح_isbn("0306406153"), False, "خاطئ")
# apl-source:33
تأكد_يساوي(صحيح_isbn("080442957X"), True, "X في الآخر")
# apl-source:34
تأكد_يساوي(صحيح_isbn("123"), False, "قصير")
# apl-source:35
