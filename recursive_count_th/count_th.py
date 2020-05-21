'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # returning count so we need to store our counts in a var
    count = 0
    # if word str is empty "" return 0
    if len(word) == 0:
        return 0

    # update count by 1 if the first two indecies == `th`
    # use the slice method to check 0 index up to 1st index (inclusive)
    if word[:2] == 'th':
        count = 1
    else:
        count = 0
    # recursing through the string strting at the first index aka next index each time will then allow us to use the slice method above properly
    return count + count_th(word[1:])


print(count_th("THtHThth"))
