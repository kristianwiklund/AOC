void insert(int x, int position) {

  int len;
  
  if (position==0) {
    //    printf("insert memmove\n");
    memmove(bop+1,bop,INPUT*sizeof(int));
    *bop=x;
    return;
  }

  len=1+INPUT-position;
  
  memmove(bop+position+1,bop+position,len*sizeof(int));
  *(bop+position)=x;    
}

// remove whatever is at position and compress the list
// will leave junk at the end
void kill(int position) {
  int len=INPUT-position+1;
  //  printf("memmove\n");
  //  pp();
  memmove(bop+position,bop+position+1,len*sizeof(int));
  //pp();
    
}

// move the int at position old to position new
// no error checking whatsoever
void move(int old, int new) {
  int t;

  t = bop[old];
  //  printf("Kill old %d\n",old);
  kill(old);
  //pp();
  //  printf("Insert new %d\n",new);
  insert(t, new);
  //pp();

}

void shoffle(int what) {
  //printf("Shuffle %d\n",what);
  
  int pos=-1, newpos;

  if (what==0)
    return;
  
  for (int i=0;i<INPUT;i++) {
    if (bop[i]==what) {
      pos=i;
      break;
    }
  }
  if (pos<0) // fail
    return;

  newpos=(pos+what);
  //  printf("Newpos %d\n",newpos);
  while(newpos<0) {
    newpos = newpos+INPUT-1;
  }
  //  printf("Newpos negcorr %d\n",newpos);
  newpos = newpos % (INPUT-1);
  //  printf("Newpos mod %d %d\n",INPUT-1,newpos);


  if (newpos<0 || newpos>=INPUT) {
    printf("Danger will robinson %d\n",newpos);
    exit(0);
  }
 
  //  printf("Move %d from  %d to %d\n", what, pos, newpos);
  if (newpos==0 && what<0) {
    //  printf("We fell off the tape to the left\n");
    newpos=INPUT-1;
    exit(0);
  }

  if (newpos>=(INPUT-1) && what>0) {
    //printf("We fell off the tape to the right\n");
    newpos=0;
    exit(0);
  }

  move(pos, newpos);

}
