# This function returns a list of skills.
# This is the list that the user will choose from
# Add at least 3 random skills for the user to select from
def get_skills():
    skills = ["Python", "C++", "JavaScript", "Soft Skills"]
    return skills


# This function pretty prints the skills to the user
# It takes the list of skills as an argument and prints them numbered
# This function doesn't return anything
def show_skills(skills):
    print("\nSkills")
    num = 0
    for skill in skills:
        print(f"{num+1}. {skill}")
        num += +1


# Shows the available skills and have user pick from them two skills
# HINT: Use previous built functions to show the skills
# For example, if the user enters 1, the first skill in your list of skills will be added to the list
# Return a list of the two skills that the user inputted
def get_user_skills(skills):
    user_skills = []
    show_skills(skills)
    skill1 = int(input("\nChoose a skill from above by entering its number: "))
    index1 = skill1 -1
    user_skills.append(skills[index1])
    skill2 = int(input("Choose another skill from above by entering its number: "))
    index2 = skill2 -1
    user_skills.append(skills[index2])
    return user_skills
    


# This function will get the user's cv from their inputs
# HINT: Use previous built functions to get the skills from the user
def get_user_cv(skills):
    cv = {}
    cv["name"] = input("What's your name? ")
    cv["age"] = int(input("What's your age? "))
    cv["experience"] = int(input("How many years of experience do you have? "))
    cv["skills"] = get_user_skills(skills)
    return cv


# This functions checks if the cv is acceptable or not, by checking the age, experience and skills and return a boolean (True or False) based on that
def check_acceptance(cv, desired_skill):
    if (25 <= cv["age"] <= 40) and (cv["experience"] > 3) and (desired_skill in cv["skills"]):
        return True
    return False


def main():
    # Write your main logic here by combining the functions above into the
    # desired outcome
    print("Welcome to the special recruitment program, please answer the following questions:")
    
    skills = get_skills()
    cv = get_user_cv(skills)
    desired_skill = skills[2]
    if check_acceptance(cv, desired_skill):
        print("accepted")
    else:
        print("rejected")
    
   

if __name__ == "__main__":
    main()
