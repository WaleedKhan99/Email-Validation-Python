# # =============================================================
# 1st Method to validate a email.
# # =============================================================

# email = input("Enter the Email: ")
# k, j, d = 0, 0, 0

# if len(email) >= 6:
#     if email[0].isalpha():
#         if "@" in email and email.count("@") == 1:
#             if (email[-4] == ".") ^ (email[-3] == "."):
#                 for i in email:
#                     if i == i.isspace():
#                         k = 1
#                     elif i.isalpha():
#                         if i == i.upper():
#                             j = 1
#                     elif i.isdigit():
#                         continue
#                     elif i == "_" or i == "." or i == "@":
#                         continue
#                     else:
#                         d = 1

#                 if k == 1 or j == 1 or d == 1:
#                     print("Invalid Email, Please type the right Email")
#                 else:
#                     print("Email verified")
#             else:
#                 print("Invalid Email, Please type the right Email")
#         else:
#             print("Invalid Email, Please type the right Email")
#     else:
#         print("Invalid Email, Please type the right Email")
# else:
#     print("Invalid Email, Please type the right Email")

# # =============================================================
# 2nd Method to validate a email.
# # =============================================================

import re

email = input("Enter the Email: ")

email_pattern = r"^[a-zA-Z][a-zA-Z0-9_.-]*@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$"

if re.match(email_pattern, email):
    print("Email verified")
else:
    print("Invalid Email, Please type the right Email")
