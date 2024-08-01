#import json
import importlib
import ast

def read_file():
    #file_path = open(r'C:\Users\jizdnmar\source\repos\PythonApplication-Codility_Tests\PythonApplication-Codility_Tests\!inputs.txt', 'r')    
    #with open(file_path.name, 'r') as fp:
    with open('!inputs.txt', 'r') as fp:    
        content = fp.read()
        file_lines = content.splitlines()
    return file_lines

def get_info(function_full_path_name):
    package_name = function_full_path_name.__module__.rsplit('.', 1)[0]
    module_name = function_full_path_name.__module__.rsplit('.', 1)[-1]
    function_name = function_full_path_name.__name__.split('.')[-1]
    return (package_name, module_name, function_name)

def test_check(lines, test_name):
    package_name = test_name[0] 
    module_name = test_name[1] 
    function_name = test_name[2]    
    test_name_bool = False
    input_values = output_expected = ""
    full_name = (package_name + "." + function_name)
    for line in lines:
        line = line.strip()
        if line == full_name:
            test_name_bool = True
        elif test_name_bool == True and line != "":                    
            #input_values = json.loads(line.split(';')[0])
            #output_expected = json.loads(line.split(';')[-1])
            input_values = ast.literal_eval(line.split(';')[0])
            output_expected = int(line.split(';')[-1])
            
            module = importlib.import_module(package_name + "." + module_name)
            test = getattr(module, function_name)
            
            if type(input_values) is tuple:
                result = test(*input_values)
            else:
                result = test(input_values)

            if output_expected == result:
                print(f"OK: {package_name}.{function_name} and expected result is: {output_expected} and actual result is: {result}")
            else:
                print(f"!!! ERROR !!!: {package_name}.{function_name} and expected result is: {output_expected} and actual result is: {result}")
        elif test_name_bool == True and line == "":
            print("----------------------------------")
            break
