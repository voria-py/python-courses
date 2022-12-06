x = "Python"

match x:
    case "Pyhton" | "py":
        print("It's python.")
    case "Java":
        print("It's java.")
    case "C++":
        print("It's c plus plus.")
    case other: # or _ 
        print("No programming language!")



# Have to user (|) for or operator
# Can use _(underscore) for other also 
