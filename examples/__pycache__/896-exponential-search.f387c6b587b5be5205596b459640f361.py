
# apl-source:1
# مثال 896 — البحث الأسي
# apl-source:2
# Exponential search
# apl-source:3
# Demonstrates: تضاعف المدى ثم ثنائي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/896-exponential-search.apl
# apl-source:6

# apl-source:7
# البحث الأسي: تضاعف المدى 1,2,4,8... ثم ثنائي داخله
# apl-source:8
# مثالي للمصفوفات غير المحدودة الطول: O(log i) حيث i موضع الهدف
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
def بحث_أسي(مصفوفة, هدف):
  # apl-source:19
  if مصفوفة[0] == هدف:
    # apl-source:20
    return 0
  # apl-source:21
  ن = len(مصفوفة)
  # apl-source:22
  حد = 1
  # apl-source:23
  while حد < ن and مصفوفة[حد] <= هدف:
    # apl-source:24
    حد = حد * 2
  # apl-source:25
  أدنى = حد // 2
  # apl-source:26
  أعلى = حد
  # apl-source:27
  if أعلى > ن - 1:
    # apl-source:28
    أعلى = ن - 1
  # apl-source:29
  while أدنى <= أعلى:
    # apl-source:30
    وسط = (أدنى + أعلى) // 2
    # apl-source:31
    if مصفوفة[وسط] == هدف:
      # apl-source:32
      return وسط
    # apl-source:33
    if مصفوفة[وسط] < هدف:
      # apl-source:34
      أدنى = وسط + 1
    # apl-source:35
    else:
      # apl-source:36
      أعلى = وسط - 1
  # apl-source:37
  return -1
# apl-source:38

# apl-source:39
مصفوفة = [1, 3, 4, 6, 7, 8, 10, 13, 14]
# apl-source:40
print("موضع 7:", بحث_أسي(مصفوفة, 7))
# apl-source:41
print("موضع 14:", بحث_أسي(مصفوفة, 14))
# apl-source:42
print("موضع 5:", بحث_أسي(مصفوفة, 5))
# apl-source:43

# apl-source:44
تأكد_يساوي(بحث_أسي(مصفوفة, 1), 0, "الأول")
# apl-source:45
تأكد_يساوي(بحث_أسي(مصفوفة, 7), 4, "الهدف الأوسط")
# apl-source:46
تأكد_يساوي(بحث_أسي(مصفوفة, 14), 8, "الأخير")
# apl-source:47
تأكد_يساوي(بحث_أسي(مصفوفة, 5), -1, "غير موجود")
# apl-source:48
تأكد_يساوي(بحث_أسي(مصفوفة, 100), -1, "أكبر من الكل")
# apl-source:49

# apl-source:50
# يطابق البحث الخطي على كل القيم الموجودة
# apl-source:51
for i in range(len(مصفوفة)):
  # apl-source:52
  تأكد_يساوي(بحث_أسي(مصفوفة, مصفوفة[i]), i, "موضع " + str(مصفوفة[i]))
# apl-source:53
