
/***********************************************************************************************/
#ifndef DEBUG_C
#define DEBUG_C
/***********************************************************************************************/
#include "syscall.h"
#include "directory.c"
#include "syscallstubs.c"
#include <stdlib.h>
#include <stdint.h>
#include <stdio.h>
/***********************************************************************************************/
#define RED "\033[1;31m"
#define CYAN "\033[1;36m"
#define GREEN "\033[1;32m"
#define BLUE "\033[1;34m"
#define BLACK "\033[1;30m"
#define BROWN "\033[1;33m"
#define MAGENTA "\033[1;35m"
#define GRAY "\033[1;37m"
#define DARKGRAY "\033[1;30m"
#define YELLOW "\033[1;33m"
#define NORMAL "\033[0m"
#define CLEAR	"\033[2J"
/***********************************************************************************************/
void dump_all_dirs(void) {
  struct dir* current = dir_head;
  while(current != NULL) {
    printf("dir : %d : ", current->dirfd);
    if (current->dir_name) printf("%s\n", current->dir_name);
    current = current->next;
  }
}

void visualize_fs(void) {
  struct dir* current = dir_head;
  struct dir* base = dir_head;
  while(current != NULL) {
    printf("%s --> ", current->dir_name);
    if (current->parent_dir) current = current->parent_dir;
    else {
      current = base->next;
      base = base->next;
      printf("\n");
    }
    //current = current->next;
  }
}
/***********************************************************************************************/
#endif
/***********************************************************************************************/

