#include <stdio.h>

#include "reverse.h"

#define SWAP(a, b) { char t = *a; *a = *b; *b = t; }

void
swap_substring(char *start, char *end)
{
    while (start < end) {
        SWAP(start, end);
        ++start;
        --end;
    }
}

void
swap_words(char *s)
{
    char *end = s;
    while (*end)
        ++end;

    swap_substring(s, end-1);

    char *w = s;
    while (*w) {
        if (*w == ' ') {
            swap_substring(s, w-1);
            ++w;
            s = w;
        } else {
            ++w;
        }
    }
    swap_substring(s, w-1);
}

/*
int
main(int argc, char *argv[])
{
    if (argc != 2)
        return 1;

    printf("%s\n", argv[1]);
    swap_words(argv[1]);
    printf("%s\n", argv[1]);

    return 0;
}
*/
