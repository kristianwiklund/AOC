grammar ap;
start: T0 '\n' {print("yay!")};
T0: T8 T11;
T8: T42 | T42 T8;
T11: T42 T31 | T42 T11 T31;
T120: 'b';
T117: T120 T51 | T2 T10;
T37: T120 T96 | T2 T94;
T19: T110 T2 | T52 T120;
T26: T120 T102 | T2 T79;
T2: 'a';
T32: T120 T57 | T2 T55;
T22: T64 T2 | T12 T120;
T3: T120 T18 | T2 T82;
T5: T2 T81 | T120 T34;
T1: T2 T120 | T120 T131;
T63: T2 T120;
T71: T120 T78 | T2 T45;
T128: T120 T46 | T2 T62;
T9: T118 T2 | T91 T120;
T36: T82 T2 | T63 T120;
T64: T50 T2 | T38 T120;
T16: T69 T120 | T80 T2;
T92: T96 T2 | T50 T120;
T113: T131 T18;
T38: T120 T120 | T120 T2;
T6: T2 T112 | T120 T15;
T24: T2 T1 | T120 T18;
T111: T120 T70 | T2 T115;
T34: T2 T119 | T120 T96;
T104: T50 T120 | T91 T2;
T85: T117 T2 | T74 T120;
T12: T2 T82 | T120 T118;
T79: T100 T2 | T56 T120;
T78: T120 T118 | T2 T119;
T116: T2 T75 | T120 T22;
T55: T89 T2 | T107 T120;
T82: T2 T2;
T119: T2 T120 | T2 T2;
T100: T2 T23 | T120 T68;
T50: T131 T131;
T102: T39 T2 | T6 T120;
T95: T120 T38 | T2 T94;
T21: T119 T2 | T63 T120;
T69: T124 T120 | T32 T2;
T10: T84 T120 | T104 T2;
T49: T96 T120 | T94 T2;
T88: T2 T82 | T120 T63;
T72: T120 T2 | T2 T2;
T76: T77 T120 | T106 T2;
T51: T120 T9 | T2 T35;
T122: T91 T120 | T96 T2;
T109: T2 T119 | T120 T28;
T101: T88 T2 | T70 T120;
T57: T81 T2 | T99 T120;
T83: T98 T120 | T30 T2;
T61: T119 T2;
T68: T120 T3 | T2 T92;
T86: T2 T54 | T120 T77;
T18: T120 T120 | T131 T2;
T80: T120 T123 | T2 T90;
T74: T2 T86 | T120 T101;
T118: T2 T131 | T120 T120;
T91: T2 T120 | T120 T2;
T131: T2 | T120;
T121: T63 T2 | T82 T120;
T43: T120 T50 | T2 T60;
T99: T60 T120 | T91 T2;
T20: T66 T2 | T99 T120;
T73: T29 T120 | T37 T2;
T129: T49 T2 | T21 T120;
T13: T120 T120;
T29: T131 T94;
T87: T2 T13;
T107: T2 T28 | T120 T13;
T66: T50 T131;
T115: T120 T60;
T65: T2 T38 | T120 T119;
T70: T2 T63 | T120 T18;
T47: T2 T108 | T120 T19;
T108: T17 T120 | T116 T2;
T62: T120 T63 | T2 T18;
T125: T120 T93 | T2 T12;
T105: T113 T120 | T114 T2;
T46: T60 T2 | T119 T120;
T54: T120 T91 | T2 T118;
T94: T120 T120 | T2 T2;
T4: T120 T53 | T2 T95;
T23: T103 T120 | T43 T2;
T75: T70 T120 | T127 T2;
T39: T27 T120 | T5 T2;
T90: T128 T120 | T59 T2;
T59: T65 T120 | T36 T2;
T48: T2 T118 | T120 T63;
T81: T2 T82 | T120 T96;
T130: T2 T61 | T120 T48;
T45: T120 T72 | T2 T96;
T93: T131 T28;
T35: T120 T28 | T2 T63;
T40: T2 T118 | T120 T119;
T7: T87 T120 | T9 T2;
T106: T2 T60 | T120 T63;
T41: T120 T9 | T2 T65;
T77: T119 T2 | T38 T120;
T58: T54 T2 | T61 T120;
T33: T2 T29 | T120 T109;
T17: T2 T111 | T120 T58;
T123: T25 T2 | T105 T120;
T84: T82 T120 | T91 T2;
T96: T120 T2;
T56: T33 T120 | T73 T2;
T15: T62 T120 | T24 T2;
T114: T63 T120 | T91 T2;
T112: T122 T120 | T44 T2;
T127: T119 T120 | T91 T2;
T53: T18 T131;
T124: T4 T2 | T20 T120;
T30: T14 T120 | T130 T2;
T25: T121 T2 | T40 T120;
T97: T120 T28;
T52: T2 T71 | T120 T7;
T110: T2 T129 | T120 T125;
T60: T120 T120 | T2 T120;
T42: T120 T16 | T2 T126;
T27: T37 T2 | T104 T120;
T28: T2 T131 | T120 T2;
T126: T2 T83 | T120 T85;
T44: T60 T2 | T94 T120;
T31: T2 T26 | T120 T47;
T98: T41 T2 | T76 T120;
T89: T2 T28 | T120 T91;
T67: T120 T13 | T2 T119;
T14: T120 T97 | T2 T67;
T103: T120 T28 | T2 T38;