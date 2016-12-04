#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "reverse.h"

void
run_test(const char *input, const char *output)
{
    char *string = (char *) malloc (strlen(input));
    strcpy(string, input);
    swap_words(string);
    //printf("%s\n%s\n", input, string);
    assert(strcmp(string, output) == 0);
    putchar('.');
}

void
run_tests()
{
    run_test("", "");
    run_test("a", "a");
    run_test("abc", "abc");
    run_test("a b c", "c b a");
    run_test("aa bbb cccc", "cccc bbb aa");
    run_test("ab bcd cdef", "cdef bcd ab");
}

int
main()
{
    run_tests();
    printf("\nOK\n");
}
