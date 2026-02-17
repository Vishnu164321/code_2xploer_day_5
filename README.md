
# Code2Xplore – Day 5

## Challenge Title
Smart Transport Load Balancing System

## Student Details
Name: Vishnu Mattakoyya  
Register Number: AP24110011648  
Section: J  

---

## Problem Description
This program analyzes a list of package weights and classifies them into different load categories to ensure safe and balanced transportation.

---

## Classification Rules

- < 0 → Invalid Entry  
- 0 – 5 → Very Light  
- 6 – 25 → Normal Load  
- 26 – 60 → Heavy Load  
- > 60 → Overload  

---

## Personalization Logic (PLI)

Name Length (excluding spaces): 16  
PLI Value = 16 % 3 = 1  

Applied Rule: **Rule B**  
(Removed all Very Light items from the final loading plan)

---

## Additional Features

- Counts total valid weights  
- Counts affected items due to PLI  
- Displays final categorized loading lists  
- Uses only:
  - for loop
  - list
  - conditional statements  

---

## Constraints Followed

- No list comprehension  
- No dictionary or set  
- No max(), min(), sum()  
- No sorting functions  
- No hard-coded output  

---

## Output
The program prints:
- Final categorized loading plan  
- Total valid weights  
- Total affected items due to personalization  

---

## Learning Outcome

Through this challenge, I learned how to:
- Use lists for classification
- Apply conditional logic effectively
- Implement personalized rule-based modifications
- Structure a clean loading analysis system
