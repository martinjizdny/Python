#Codility - EASY - LongestPassword --> 100%
#https://app.codility.com/programmers/trainings/1/longest_password/
#You would like to set a password for a bank account. However, there are three restrictions on the format of the password:
#- it has to contain only alphanumerical characters (a−z, A−Z, 0−9);
#- there should be an even number of letters;
#- there should be an odd number of digits.
#You are given a string S consisting of N characters. String S can be divided into words by splitting it at, and removing, the spaces. The goal is to choose the longest word that is a valid password. You can assume that if there are K spaces in string S then there are exactly K + 1 words.

#For example, given "test 5 a0A pass007 ?xy1", there are five words and three of them are valid passwords: "5", "a0A" and "pass007". Thus the longest password is "pass007" and its length is 7. Note that neither "test" nor "?xy1" is a valid password, because "?" is not an alphanumerical character and "test" contains an even number of digits (zero).

#Write a function: def solution(S)
#that, given a non-empty string S consisting of N characters, returns the length of the longest word from the string that is a valid password. If there is no such word, your function should return −1.

#For example, given S = "test 5 a0A pass007 ?xy1", your function should return 7, as explained above.

#Assume that:
#- N is an integer within the range [1..200];
#- string S consists only of printable ASCII characters and spaces.
#In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.
def solution_LongestPassword(S):
    size = 0

    for item in S.split():
        letters = 0
        numbers = 0
       
        for char in item:
            if char.isalpha():
                letters += 1
            elif char.isdigit():
                numbers += 1
        
        if letters % 2 == 0 and numbers % 2 != 0 and numbers != 0 and len(item) == (letters + numbers):            
            if size < len(item):
                size = len(item)
            
            #print(f"item {item} ... letters {letters}, numbers {numbers}")               
    return size if size > 0 else -1



#Codility - EASY - TennisTournament --> 100%
#https://app.codility.com/programmers/trainings/3/tennis_tournament/
#You are hosting a tennis tournament. P players, who will take part in the first round of this tournament, are already registered and you have reserved C tennis courts for the matches. Exactly two players play in each game and only one game can be played on each court at any given time. You want to host the maximum possible number of games starting at the same time (in order to finish the first round quickly).

#How many games can be hosted in parallel simultaneously?

#Write a function: def solution(P, C)

#that, given the number of players P and the number of reserved courts C, returns the maximum number of games that can be played in parallel.

#Examples:
#1. Given P = 5 players and C = 3 available courts, the function should return 2. Two games can be played simultaneously (for instance, the first and second players can play on the first court, and the third and fourth players on the second court, and the third court will be empty because the fifth player does not have a partner to play with).
#2. Given P = 10 players and C = 3 courts, the function should return 3. At most three games can be hosted in parallel.

#Assume that:
#- P and C are integers within the range [1..30,000].
#In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.
def solution_TennisTournament(*args):
#def solution_TennisTournament(P, C):
    P = args[0]  # added in case of *args
    C = args[1]  # added in case of *args
    if (C - int(P/2)) >= 0:
        return int(P/2)
    elif (int(P/2) - C) > 0:
        return C



#Codility - EASY -  FirstUnique --> 100%
#https://app.codility.com/programmers/trainings/4/first_unique/
#A non-empty array A consisting of N integers is given. The unique number is the number that occurs exactly once in array A.

#For example, the following array A:
#  A[0] = 4
#  A[1] = 10
#  A[2] = 5
#  A[3] = 4
#  A[4] = 2
#  A[5] = 10
#contains two unique numbers (5 and 2).

#You should find the first unique number in A. In other words, find the unique number with the lowest position in A.

#For above example, 5 is in second position (because A[2] = 5) and 2 is in fourth position (because A[4] = 2). So, the first unique number is 5.

#Write a function: def solution(A)

#that, given a non-empty array A of N integers, returns the first unique number in A. The function should return −1 if there are no unique numbers in A.

#For example, given:
#  A[0] = 1
#  A[1] = 4
#  A[2] = 3
#  A[3] = 3
#  A[4] = 1
#  A[5] = 2
#the function should return 4. There are two unique numbers (4 and 2 occur exactly once). The first one is 4 in position 1 and the second one is 2 in position 5. The function should return 4 bacause it is unique number with the lowest position.

#Given array A such that:
#  A[0] = 6
#  A[1] = 4
#  A[2] = 4
#  A[3] = 6
#the function should return −1. There is no unique number in A (4 and 6 occur more than once).

#Write an efficient algorithm for the following assumptions:
#- N is an integer within the range [1..100,000];
#- each element of array A is an integer within the range [0..1,000,000,000].
def solution_FirstUnique(A):
    counts = {}
    for item in A:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1

    for item in A:
        if counts[item] == 1:
            return item

    return -1
    
    #performance issue otherwise OK:
    for item in A:        
        count_all_same = A.count(item)
        if count_all_same > 1:        
            continue
        elif count_all_same == 1:
            return item
        
    return -1



#Codility - EASY -  StrSymmetryPoint --> 50%
#https://app.codility.com/programmers/trainings/4/str_symmetry_point/
#Write a function: def solution(S)

#that, given a string S, returns the index (counting from 0) of a character such that the part of the string to the left of that character is a reversal of the part of the string to its right. The function should return −1 if no such index exists.

#Note: reversing an empty string (i.e. a string whose length is zero) gives an empty string.

#For example, given a string:
#"racecar"
#the function should return 3, because the substring to the left of the character "e" at index 3 is "rac", and the one to the right is "car".

#Given a string:
#"x"
#the function should return 0, because both substrings are empty.

#Write an efficient algorithm for the following assumptions:
#- the length of string S is within the range [0..2,000,000].
def solution_StrSymmetryPoint(S):
    S = str(S)
    string_reverse = str(S) [::-1]  
    counter = 0
    lenght = int(len(S)/2)
    if len(string_reverse) == 0:
        return -1

    for char1, char2 in zip(S, string_reverse):
        if char1 == char2:
            if counter == lenght:
                return counter
            counter += 1
        elif counter == 0:
            return -1
        else:
            return counter

    return 0
        

#Codility - EASY -  ArrListLen --> 100%
#https://app.codility.com/programmers/trainings/7/arr_list_len/
#A non-empty array A consisting of N integers is given.

#Array A represents a linked list. A list is constructed from this array as follows:
#- the first node (the head) is located at index 0;
#- the value of a node located at index K is A[K];
#- if the value of a node is −1 then it is the last node of the list;
#- otherwise, the successor of a node located at index K is located at index A[K] (you can assume that A[K] is a valid index, that is 0 ≤ A[K] < N).

#For example, for array A such that:
#  A[0] =  1
#  A[1] =  4
#  A[2] = -1
#  A[3] =  3
#  A[4] =  2

#the following list is constructed:
#- the first node (the head) is located at index 0 and has a value of 1;
#- the second node is located at index 1 and has a value of 4;
#- the third node is located at index 4 and has a value of 2;
#- the fourth node is located at index 2 and has a value of −1.

#Write a function: def solution(A)
#that, given a non-empty array A consisting of N integers, returns the length of the list constructed from A in the above manner.

#For example, given array A such that:
#  A[0] =  1
#  A[1] =  4
#  A[2] = -1
#  A[3] =  3
#  A[4] =  2
#the function should return 4, as explained in the example above.

#Assume that:
#- N is an integer within the range [1..200,000];
#- each element of array A is an integer within the range [−1..N-1];
#- it will always be possible to construct the list and its length will be finite.
#In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.
def solution_ArrListLen(A):
    counter = 1
    index_array = 0

    for i in range(len(A)):        
        if A[index_array] > 0 and len(A) > 1:
            item_current = A[index_array]
            item_next = A[item_current]
            counter += 1

            if item_next == -1:
                return counter
            
            index_array = item_current
    return counter



#Codility - EASY - BinaryGap --> 100%
#https://app.codility.com/programmers/trainings/9/binary_gap/
#A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

#For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.

#Write a function: def solution(N)
#that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

#For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.

#Write an efficient algorithm for the following assumptions:
#- N is an integer within the range [1..2,147,483,647].
def solution_BinaryGap(N):
    #https://www.rapidtables.com/convert/number/binary-to-decimal.html?x=1001100001000001
    binary_number = bin(N)[2:]
    counter = 0
    one_first = False
    one_second = False
    biggest_space = 0
    
    for bit in binary_number:
        if bit == '1' and one_first == False:
            one_first = True
            continue
        elif one_first == True and bit != '1':
            counter += 1
        elif one_first == True and bit == '1':
            if counter > biggest_space:
                biggest_space = counter
            one_second = True
            counter = 0

    return biggest_space if one_second == True else 0
