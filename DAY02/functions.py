# Function 1
def calculate_experience(start_year, current_year=2026):
    return current_year - start_year


# Function 2
def build_profile(**details):
    return " | ".join([f"{key.capitalize()}: {value}" for key, value in details.items()])


# Function 3
def apply_bonus(salary, bonus_percent):
    return salary + (salary * bonus_percent / 100)


# Calling functions
exp = calculate_experience(2022)
profile = build_profile(name="Alex", role="Engineer", company="ABC")
new_salary = apply_bonus(50000, 10)

print(exp)
print(profile)
print(new_salary)