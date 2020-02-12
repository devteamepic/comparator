#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const char* getField(char* line, int num) {
  const char* tok;
  for (tok = strtok(line, ";"); tok && *tok; tok = strtok(NULL, ";")) {
    if (!--num) {
      return tok;
    }
  }

  return NULL;
}


int compareArrays(int a[], int b[], int size) {
  int i;
  for (i = 0; i < size; i++) {
    if (a[i] != b[i]) {
      return 1;
    }
  }
  
  return 0;
}

int main(){
  FILE* stream = fopen("data.csv", "r");

  char line[2048];
  while(fgets(line, 2048, stream)) {
    char* tmp = strdup(line);
    printf("Field 10 %s\n", getField(tmp, 10));

    free(tmp);
  }
  return 0;
}
