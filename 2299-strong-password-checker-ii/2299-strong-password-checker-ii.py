class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False

        has_lower = any(ch.islower() for ch in password)
        has_upper = any(ch.isupper() for ch in password)
        has_digit = any(ch.isdigit() for ch in password)
        special = '!@#$%^&*()-+'
        has_special = any(ch in special for ch in password)

        for i in range(1,len(password)):
            if password[i] == password[i-1]:
                return False

        return has_lower and has_upper and has_digit and has_special