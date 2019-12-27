print()
print()

skill=["team work","proplem solving","critical thinking","comunication skill","coding"]
#defining skill list
cv={}
#adding empty cv dictinary

print ("Welcome to the special recruitment program, please answer the following questions:")
print()

name_input= input ("What's your name?  ")
cv["name"]= name_input
#adding name to cv dic.

age_input= int(input ("How old are you?  "))
cv["age"]=age_input
#adding age to cv dic.

experience_input= int(input ("How many years of experience do you have?  "))
cv["experience"]=experience_input
#adding experiance to cv dic.

print()
print ("Skills:")
for skills in skill:
	itration= skill.index(skills)+1
	print("%s. %s" %(itration,skills))
	#loop to print the defined skills
print()

Candidate_Skill_List=[]
cv["skills"]=Candidate_Skill_List
#intredusing choosen skill list to the dic

first_skill= int(input ("Choose a skill from above by entering its number:"))
first_skill=skill[first_skill-1]
Candidate_Skill_List.append(first_skill)
#appending list items to Candidate_Skill_List 
print()

second_skill= int(input ("Choose another skill from above by entering its number:"))
second_skill=skill[second_skill-1]
Candidate_Skill_List.append(second_skill)
#appending list items to Candidate_Skill_List
print()

#my criteria is 
#1-age>25
#2-exp>3 
#3-skills at least coding

age_chck= age_input >= 25
experiance_check= experience_input >=3
skill_check= "coding" in Candidate_Skill_List
if age_chck and experiance_check and skill_check == True:
	print ("congratulations, "+name_input +" You have been accepted.")
else:
	print ("sorry " + name_input + " your aplication was rejected")


