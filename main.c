#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const char* getField(char* line, int num) {
  const char* tok;
  for (tok = strtok(line, ","); tok && *tok; tok = strtok(NULL, ",\n")) {
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
  FILE* stream = fopen("./data/data.csv", "r");

  char line[1024];
  while(fgets(line, 1024, stream)) {
    char* tmp = strdup(line);
    printf("Field 8 %s\n", getField(tmp, 8));

    free(tmp);
  }
  return 0;
}
