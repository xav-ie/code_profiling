CC=gcc
CFLAGS=-g -Wall
LFLAGS=-L. -lfunction_profiler

all: prof_example

prof_example: myprofilerexample.c libfunction_profiler.a
	$(CC) $(CFLAGS) -finstrument-functions -o $@ $^ $(LFLAGS)

libfunction_profiler.a: libfunction_profiler.o
	ar rcs $@ $^

function_profiler.o: libfunction_profiler.c libfunction_profiler.h
	$(CC) $(CFLAGS) -c libfunction_profiler.c -fPIC

clean:
	rm prof_example *.o
