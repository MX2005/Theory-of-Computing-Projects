
def regex_to_nfa_line(regex):
    state_count = 0
    output = ""
    epsilon = "ε"
    
    for char in regex:
        
        next_state = f"q{state_count}"
        output += f"{next_state}:{char} ---> "
        state_count += 1
        
        # epsilon after each character
        next_state = f"q{state_count}"
        output += f"{next_state}:{epsilon} ---> "
        state_count += 1
        
    return output.rstrip(f"{next_state}:{epsilon} ---> ")

regex = str(input("Enter a regex: "))
print(regex_to_nfa_line(regex))