
# apl-source:1
# مثال 734 — كتلة ببتيد
# apl-source:2
# Peptide mass
# apl-source:3
# Demonstrates: جدول كتل، جزيء ماء، جمع تراكمي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/734-protein-mass.apl
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
# حساب كتلة ببتيد من حروف الأحماض الأمينية
# apl-source:25
# Demonstrates: جدول كتل ثابت, قاموس.get بقيمة افتراضية, جمع تراكمي
# apl-source:26
# الكتلة الكلية = مجموع كتل البقايا + كتلة جزيء ماء (طرفا الببتيد)
# apl-source:27

# apl-source:28
كتلة_ماء = 18.0153
# apl-source:29

# apl-source:30
كتل = {
  # apl-source:31
  "A": 71.0788, "R": 156.1875, "N": 114.1038, "D": 115.0886,
  # apl-source:32
  "C": 103.1388, "E": 129.1155, "Q": 128.1307, "G": 57.0519,
  # apl-source:33
  "H": 137.1411, "I": 113.1594, "L": 113.1594, "K": 128.1741,
  # apl-source:34
  "M": 131.1926, "F": 147.1766, "P": 97.1167, "S": 87.0782,
  # apl-source:35
  "T": 101.1051, "W": 186.2132, "Y": 163.1760, "V": 99.1326
# apl-source:36
}
# apl-source:37

# apl-source:38
def كتلة_ببتيد(ببتيد):
  # apl-source:39
  مجموع = 0.0
  # apl-source:40
  for ي in range(len(ببتيد)):
    # apl-source:41
    مجموع = مجموع + كتل.get(ببتيد[ي], 0.0)
  # apl-source:42
  return مجموع + كتلة_ماء
# apl-source:43

# apl-source:44
def متوسط_كتلة_بقية(ببتيد):
  # apl-source:45
  if len(ببتيد) == 0:
    # apl-source:46
    return 0.0
  # apl-source:47
  return (كتلة_ببتيد(ببتيد) - كتلة_ماء) / len(ببتيد)
# apl-source:48

# apl-source:49
def عدد_حرف(ببتيد, حرف):
  # apl-source:50
  عدد = 0
  # apl-source:51
  for ي in range(len(ببتيد)):
    # apl-source:52
    if ببتيد[ي] == حرف:
      # apl-source:53
      عدد = عدد + 1
  # apl-source:54
  return عدد
# apl-source:55

# apl-source:56
تأكد_يساوي(round(كتلة_ببتيد("G"), 4), 75.0672, "غلايسين وحيد")
# apl-source:57
تأكد_يساوي(round(كتلة_ببتيد("AC"), 4), 192.2329, "ثنائي")
# apl-source:58
تأكد_يساوي(round(كتلة_ببتيد("GLY"), 4), 351.4026, "ثلاثي")
# apl-source:59
تأكد_يساوي(round(كتلة_ببتيد("PEPTIDE"), 4), 799.8328, "سباعي")
# apl-source:60
تأكد_يساوي(round(كتلة_ببتيد("MKWVTFISLL"), 4), 1237.5659, "عشاري")
# apl-source:61

# apl-source:62
تأكد_يساوي(round(متوسط_كتلة_بقية("GLY"), 4), 111.1291, "متوسط البقايا")
# apl-source:63
تأكد_يساوي(عدد_حرف("PEPTIDE", "E"), 2, "تكرار E")
# apl-source:64
تأكد_يساوي(عدد_حرف("PEPTIDE", "W"), 0, "بلا W")
# apl-source:65

# apl-source:66
# حروف غير معروفة تُهمل عبر .get
# apl-source:67
تأكد_يساوي(round(كتلة_ببتيد("GXG"), 4), round(132.1191, 4), "حرف مجهول مهمل")
# apl-source:68

# apl-source:69
print("كتلة PEPTIDE:", round(كتلة_ببتيد("PEPTIDE"), 2))
# apl-source:70
