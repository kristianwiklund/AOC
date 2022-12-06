-module(nine).

garbage(['!',_|XS]->
	garbage(XS);
	