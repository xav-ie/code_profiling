#include "libfunction_profiler.h"
#include <stdio.h>

void __cyg_profile_func_exit(void *this_func, void *call_site) {
    printf("--> %p %p\n", this_func, call_site);
} 
void __cyg_profile_func_enter(void *this_fn, void *call_site) {
    printf("<-- %p %p\n", this_fn, call_site);
} 
