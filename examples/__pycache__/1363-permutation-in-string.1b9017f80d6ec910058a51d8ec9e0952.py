
# apl-source:1
# مثال 1363 — تبديل داخل نص
# apl-source:2
# Permutation in string
# apl-source:3
# Demonstrates: نافذة منزلقة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1363-permutation-in-string.apl
# apl-source:6

# apl-source:7
# نقارن عدادات الحروف في نافذة بطول النص الأول
# apl-source:8
# ننزلق نافذة واحدة في كل خطوة
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
def يحتوي_تبديل(أ, ب):
  # apl-source:19
  if len(أ) > len(ب):
    # apl-source:20
    return False
  # apl-source:21
  مطلوب_ = [0] * 26
  # apl-source:22
  نافذة = [0] * 26
  # apl-source:23
  for ع in range(len(أ)):
    # apl-source:24
    مطلوب_[ord(أ[ع]) - 97] = مطلوب_[ord(أ[ع]) - 97] + 1
    # apl-source:25
    نافذة[ord(ب[ع]) - 97] = نافذة[ord(ب[ع]) - 97] + 1
  # apl-source:26
  if نافذة == مطلوب_:
    # apl-source:27
    return True
  # apl-source:28
  for ع in range(len(أ), len(ب)):
    # apl-source:29
    نافذة[ord(ب[ع]) - 97] = نافذة[ord(ب[ع]) - 97] + 1
    # apl-source:30
    نافذة[ord(ب[ع - len(أ)]) - 97] = نافذة[ord(ب[ع - len(أ)]) - 97] - 1
    # apl-source:31
    if نافذة == مطلوب_:
      # apl-source:32
      return True
  # apl-source:33
  return False
# apl-source:34

# apl-source:35
تأكد_يساوي(يحتوي_تبديل("ab", "eidbaooo"), True, "موجود")
# apl-source:36
تأكد_يساوي(يحتوي_تبديل("ab", "eidboaoo"), False, "غير موجود")
# apl-source:37
تأكد_يساوي(يحتوي_تبديل("a", "a"), True, "حرف")
# apl-source:38
