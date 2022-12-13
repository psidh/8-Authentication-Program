#include <stdio.h> 
#include <conio.h> 
#include <string.h> 
 
void main() 
{ 
  printf("THIS PROGRAM CHECKS YOUR AUTHENTICATION\n") ;
  printf("\n");
  char username[20]; 
  char userpwd[8]; 

  //  ^
  //  |
  //  |
  //  |
  //  |
  //  WARE - HOUSE FOR MY USER AND PASSWORD 


  int i; 
   
  printf("Enter your ID CARD NUMBER : "); 
  //gets(username); 
  scanf("%s",username); 
   
  printf("Enter your GITAM PASSWORD : "); 
  scanf("%s",userpwd);
  /* accept password */ 
 
  for(i=0;i<8;i++) 
  { 
   userpwd[i]=getch(); 
   printf("*");   	 
  } 
  userpwd[i]='\0'; 
 
/*------------------*/ 
 
  printf("\n\n Press any key to continue"); 
  getch(); 
 
 if(strcmp(username,"VU22CSE0101626") && strcmp(userpwd,"12345")) 
 { 
  printf("\n\            ACCESSD GRANTED "); 
 } else 
 { 
  printf("\n\n           ACCESS DENIED "); 
 } 