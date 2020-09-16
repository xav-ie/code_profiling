#include <stdio.h>
#include "libfunction_profiler.h"

void f1() {
    printf("f1\n");
}


void f2() {
    printf("f2\n");
    f1();
}

int main() {
    f1();
    f2();
    return 0;
}
