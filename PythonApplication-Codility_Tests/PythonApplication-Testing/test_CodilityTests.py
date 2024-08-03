import sys
import ast
import pytest
import os

#sys.path.append("C:/Users/jizdnmar/source/repos/PythonApplication-Codility_Tests/PythonApplication-Codility_Tests/Medium")
#from MediumFunctions import solution_FloodDepth
sys.path.append("C:/Users/jizdnmar/source/repos/PythonApplication-Codility_Tests/PythonApplication-Codility_Tests")
from Easy import EasyFunctions
from Medium import MediumFunctions


def read_file():
    #file_path = open(r'C:\Users\jizdnmar\source\repos\PythonApplication-Codility_Tests\PythonApplication-Codility_Tests\!inputs.txt', 'r')    
    #with open(file_path.name, 'r') as fp:
    #with open('!inputs.txt', 'r') as fp:
    path = r'C:\Users\jizdnmar\source\repos\PythonApplication-Codility_Tests\PythonApplication-Codility_Tests'
    file_name = '!inputs.txt'
    #input_file_name = 'C:\Users\jizdnmar\source\repos\PythonApplication-Codility_Tests\PythonApplication-Codility_Tests\!inputs.txt'
    with open(os.path.join(path, file_name)) as fp:
        content = fp.read()
        file_lines = content.splitlines()    
    return file_lines

def read_test_data(test_name):    
    lines = read_file()
    test_name_bool = False
    #input_values = output_expected = ""
    test_cases = []
    for line in lines:
        line = line.strip()
        if line == test_name:
            test_name_bool = True
        elif test_name_bool == True and line != "":                    
            input_values = ast.literal_eval(line.split(';')[0])

            if type(input_values) is tuple:
                input_values = list(input_values)
            elif type(input_values) is str:
                input_values = [input_values]
            elif type(input_values) is int:
                input_values = [input_values]

            input_values = str(input_values)
            output_expected = int(line.split(';')[-1])
            test_cases.append((eval(input_values), int(output_expected)))
        elif test_name_bool == True and line == "":            
            break
    return test_cases



#@pytest.mark.parametrize("input_values, output_expected", [([1, 2, 1, 2, 1, 4, 3, 2, 3, 6, 2, 4, 3, 5, 1],3)])
@pytest.mark.parametrize("input_values, output_expected", read_test_data("Medium.solution_FloodDepth"))
def test_solution_FloodDepth(input_values, output_expected):
    result = MediumFunctions.solution_FloodDepth(input_values)
    assert result == output_expected

@pytest.mark.parametrize("input_values, output_expected", read_test_data("Easy.solution_LongestPassword"))
def test_solution_LongestPassword(input_values, output_expected):
    result = EasyFunctions.solution_LongestPassword(input_values[0])
    assert result == output_expected

@pytest.mark.parametrize("input_values, output_expected", read_test_data("Easy.solution_TennisTournament"))
def test_solution_TennisTournament(input_values, output_expected):    
    result = EasyFunctions.solution_TennisTournament(*input_values)
    assert result == output_expected

#@pytest.mark.parametrize("input_values, output_expected", [([4, 10, 5, 4, 2, 10], 5)])
@pytest.mark.parametrize("input_values, output_expected", read_test_data("Easy.solution_FirstUnique"))
def test_solution_FirstUnique(input_values, output_expected):
    result = EasyFunctions.solution_FirstUnique(input_values)
    assert result == output_expected

@pytest.mark.parametrize("input_values, output_expected", read_test_data("Easy.solution_StrSymmetryPoint"))
def test_solution_StrSymmetryPoint(input_values, output_expected):
    result = EasyFunctions.solution_StrSymmetryPoint(input_values[0])
    assert result == output_expected

@pytest.mark.parametrize("input_values, output_expected", read_test_data("Easy.solution_BinaryGap"))
def test_solution_BinaryGap(input_values, output_expected):
    result = EasyFunctions.solution_BinaryGap(input_values[0])
    assert result == output_expected

@pytest.mark.parametrize("input_values, output_expected", read_test_data("Easy.solution_ArrListLen"))
def test_solution_ArrListLen(input_values, output_expected):
    result = EasyFunctions.solution_ArrListLen(input_values)
    assert result == output_expected