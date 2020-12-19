grammar ap;

start: T0 '\n' {print("yay!")};
T0: T4 T1 T5; 
T5: 'b';
T4: 'a';
T3: (T4 T5) | (T5 T4);
T2: (T4 T4) | (T5 T5);
T1: (T2 T3) | (T3 T2);

