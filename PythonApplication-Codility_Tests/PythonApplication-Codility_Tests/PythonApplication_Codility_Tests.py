import pytest #https://docs.pytest.org/en/stable/
from Medium import MediumFunctions
from Easy import EasyFunctions
from Others import OthersFunctions

#****************************************************************
#Codility START
#Read all test values for Tests from the file:
file_lines = OthersFunctions.read_file()


#Codility - EASY - LongestPassword --> 100%
test_name = OthersFunctions.get_info(EasyFunctions.solution_LongestPassword)
print(f"\nCodility - {test_name[0].upper()} - {test_name[2]} --> 100%")
OthersFunctions.test_check(file_lines, test_name)


#Codility - EASY - TennisTournament --> 100%
test_name = OthersFunctions.get_info(EasyFunctions.solution_TennisTournament)
print(f"\nCodility - {test_name[0].upper()} - {test_name[2]} --> 100%")
OthersFunctions.test_check(file_lines, test_name)   


#Codility - EASY -  FirstUnique --> 100%
test_name = OthersFunctions.get_info(EasyFunctions.solution_FirstUnique)
print(f"\nCodility - {test_name[0].upper()} - {test_name[2]} --> 100%")
OthersFunctions.test_check(file_lines, test_name)   


#Codility - EASY -  StrSymmetryPoint --> 50%
test_name = OthersFunctions.get_info(EasyFunctions.solution_StrSymmetryPoint)
print(f"\nCodility - {test_name[0].upper()} - {test_name[2]} --> 50%")
OthersFunctions.test_check(file_lines, test_name)   


#Codility - EASY -  ArrListLen --> 100%
test_name = OthersFunctions.get_info(EasyFunctions.solution_ArrListLen)
print(f"\nCodility - {test_name[0].upper()} - {test_name[2]} --> 100%")
OthersFunctions.test_check(file_lines, test_name)


#Codility - EASY - BinaryGap --> 100%
test_name = OthersFunctions.get_info(EasyFunctions.solution_BinaryGap)
print(f"\nCodility - {test_name[0].upper()} - {test_name[2]} --> 100%")
OthersFunctions.test_check(file_lines, test_name)


#Codility - MEDIUM - FloodDepth --> 100%
test_name = OthersFunctions.get_info(MediumFunctions.solution_FloodDepth)
print(f"\nCodility - {test_name[0].upper()} - {test_name[2]} --> 100%")
OthersFunctions.test_check(file_lines, test_name)
#print(f"vysledek: {MediumFunctions.solution_FloodDepth([1, 6, 2, 4, 3, 5, 1])}") # -> 3
#print(f"vysledek: {MediumFunctions.solution_FloodDepth([1, 2, 1, 2, 1, 4, 3, 2, 3, 6, 2, 4, 3, 5, 1])}") # -> 3
#print(f"vysledek: {MediumFunctions.solution_FloodDepth([1, 2, 1, 2, 1, 4, 3, 2, 3, 6, 2, 4, 3, 6, 1])}") # -> 4
#print(f"vysledek: {MediumFunctions.solution_FloodDepth([1, 3, 2, 1, 2, 1, 5, 3, 3, 4, 2])}") # -> 2
#print(f"vysledek: {MediumFunctions.solution_FloodDepth([1, 4, 3, 2, 3, 1, 5, 3, 3, 4, 2])}") # -> 3
#print(f"vysledek: {MediumFunctions.solution_FloodDepth([1, 4, 3, 2, 3, 2, 5, 3, 3, 4, 2, 5, 2])}") # -> 3
#print(f"vysledek: {MediumFunctions.solution_FloodDepth([1, 2, 1, 2, 1, 4, 3, 2, 3, 6, 2, 4, 3, 5, 1])}") # -> 3
#print(f"vysledek: {MediumFunctions.solution_FloodDepth([1, 2, 1, 2, 1, 4, 3, 2, 3, 7, 2, 4, 3, 5, 1])}") # -> 3
#print(f"vysledek: {MediumFunctions.solution_FloodDepth([1, 2, 1, 8, 1, 5, 3, 2, 3, 5, 2, 4, 3, 5, 1])}") # -> 4
#print(f"vysledek: {MediumFunctions.solution_FloodDepth([1, 2, 1, 8, 1, 5, 3, 2, 3, 10, 2, 4, 3, 7, 1])}") # -> 7
#print(f"vysledek: {MediumFunctions.solution_FloodDepth([1, 12, 1, 7, 2, 5, 2, 10, 2, 4, 3, 7, 1])}") # -> 9
#print(f"vysledek: {MediumFunctions.solution_FloodDepth([1, 4, 1, 10, 2, 10, 1, 3, 4])}") # -> 8
#print(f"vysledek: {MediumFunctions.solution_FloodDepth([1, 4, 1, 10, 2, 8, 1, 3, 4])}") # -> 6
#print(f"vysledek: {MediumFunctions.solution_FloodDepth([1, 4, 1, 10, 2, 8, 1, 3, 4, 1, 5, 1, 8])}") # -> 7
#print(f"vysledek: {MediumFunctions.solution_FloodDepth([1, 4, 1, 10, 2, 8, 1, 3, 4, 1, 5, 1, 8, 2])}") # -> 7
#print(f"vysledek: {MediumFunctions.solution_FloodDepth([1, 20, 1, 10, 2, 8, 1, 3, 4, 1, 5, 1, 8, 2])}") # -> 9
#print(f"vysledek: {MediumFunctions.solution_FloodDepth([1, 4, 1, 10, 1, 2, 1, 4, 5, 3, 9])}") # -> 8
#print(f"vysledek: {MediumFunctions.solution_FloodDepth([1, 4, 1, 10, 1, 2, 1, 4, 5, 3, 11])}") # -> 9
#print(f"vysledek: {MediumFunctions.solution_FloodDepth([1, 2, 1, 10, 8, 7, 6, 9, 1, 2])}") # -> 3
#print(f"vysledek: {MediumFunctions.solution_FloodDepth([1, 2, 1, 10, 8, 7, 6, 9, 1, 2, 1, 9])}") # -> 8
#print(f"vysledek: {MediumFunctions.solution_FloodDepth([1, 2, 1, 10, 8, 7, 6, 9, 8, 7, 8, 9])}") # -> 3
#print(f"vysledek: {MediumFunctions.solution_FloodDepth([1, 2, 1, 10, 8, 7, 6, 9, 0, 2, 1, 9])}") # -> 3
#print(f"vysledek: {MediumFunctions.solution_FloodDepth([1, 3, 2, 1, 2, 1, 5, 3, 3, 4, 2])}") # -> 2
#print(f"vysledek: {MediumFunctions.solution_FloodDepth([5, 8])}") # -> 0
#print(f"vysledek: {MediumFunctions.solution_FloodDepth([1, 2, 3, 4, 5])}") # -> 0
#print(f"vysledek: {MediumFunctions.solution_FloodDepth([10, 3, 10, 2, 10, 3, 10])}") # -> 8
#print(f"vysledek: {MediumFunctions.solution_FloodDepth([9, 3, 10, 2, 10, 3, 8])}") # -> 8
#print(f"vysledek: {MediumFunctions.solution_FloodDepth([2, 1, 2, 4, 0, 2, 1, 2, 1, 10])}") # -> 1
#print(f"vysledek: {MediumFunctions.solution_FloodDepth([4,2,3,2,5,1,6,2,20,2,20,10,11])}")  # -> 18



