from simpleeval import simple_eval

operators = '+-/*'

while True:
    equation = input("what is your equation (type 'exit' when done): ")

    if equation.lower() == "exit":
        print("Goodbye!")
        break

    if equation == "": 
        print("Input cannot be empty")
        continue
    if not any(char in operators for char in equation):
        print("Input must contain at least one operator (+, -, /, *).")
        continue

    try:
        result = simple_eval(equation)
        print(f"{equation} = {result}")
    except Exception as e:
        print("Invalid equation:", e)