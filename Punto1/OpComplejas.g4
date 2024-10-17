grammar OpComplejas;

program: operation EOF;

operation: complexNumber op=('*' | '/' | '+' | '-') complexNumber;

complexNumber: '(' realPart (op=('+' | '-') imaginaryPart)? 'i'? ')';

realPart: NUMBER;

imaginaryPart: NUMBER;

NUMBER: [0-9]+ ('.' [0-9]+)?;

WS: [ \t\r\n]+ -> skip;
