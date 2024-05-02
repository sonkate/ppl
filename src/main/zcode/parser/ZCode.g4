// Tran Thanh Son - 2053405
grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: list_newline? decls EOF;
decls: decl decls_tail;
decls_tail: decl decls_tail | ;
decl: (var_decl | func_decl);

// class members can be null
var_decl: (keyword_var | implicit_var | implicit_dynamic) list_newline;

keyword_var: keyword_var_decl | keyword_var_array_decl;
keyword_var_decl: type_vardecl IDENTIFIER (ASSIGN_OP expr)?;
keyword_var_array_decl:
	type_vardecl IDENTIFIER arraydim (ASSIGN_OP expr)?;

arraydim: LSB listdim RSB;
listdim: (NUMBERLIT CM listdim) | NUMBERLIT;

type_vardecl: TYPE_NUMBER | TYPE_BOOL | TYPE_STRING;

implicit_var: VAR IDENTIFIER ASSIGN_OP expr;
implicit_dynamic: DYNAMIC IDENTIFIER (ASSIGN_OP expr)?;

// attribute_decl: (CONST | VAR) (no_assign_attr | value_attr) SC; no_assign_attr: listID COL
// (element_type | obj_type); value_attr: (IDENTIFIER | AT_IDENTIFIER) CM value_attr CM expr |
// (IDENTIFIER|AT_IDENTIFIER) COL (element_type | obj_type) EQ expr;

func_decl: func_decl_prototype | func_decl_complete ;
func_decl_complete:
	FUNC IDENTIFIER LRB param_decls RRB list_newline? body;
func_decl_prototype:
	FUNC IDENTIFIER LRB param_decls RRB list_newline? (return_stmt?|list_newline);

body: BEGIN list_newline body_one? END list_newline;
body_one: statement body_one | statement;

// params in function
param_decls: param_decl param_decl_tail | ;
param_decl_tail: CM param_decl param_decl_tail |;
param_decl: type_vardecl IDENTIFIER (arraydim |);
// listID: IDENTIFIER CM listID | IDENTIFIER;

// statements
statement:
	 var_decl
	| assign_stmt
	| if_stmt
	| for_stmt
	| break_stmt
	| continue_stmt
	| return_stmt
	| func_call_stmt
	| body;

assign_stmt: (IDENTIFIER | array_index_expr) ASSIGN_OP expr list_newline;
array_index_expr: (IDENTIFIER | func_call) LSB list_expr RSB;
list_expr: expr expr_tail | expr;
expr_tail: CM expr expr_tail |;

break_stmt: BREAK list_newline;
continue_stmt: CONTINUE list_newline;
return_stmt: RETURN expr? list_newline;
func_call_stmt: IDENTIFIER LRB (list_expr | ) RRB list_newline;
func_call: IDENTIFIER LRB (list_expr | ) RRB;


if_stmt: IF LRB expr RRB list_newline? statement list_elif (ELSE list_newline? statement)?;
list_elif: elif_one list_elif | ;
elif_one: ELIF LRB expr RRB list_newline? statement;

for_stmt: FOR IDENTIFIER UNTIL expr BY expr list_newline? statement;

// expr
expr
	: expr1 CONCAT_OP expr1
	| expr1;
expr1
	: expr2 (EQ | EQ_OP | NEQ_OP | LT_OP | GT_OP | LEQ_OP | GEQ_OP) expr2
	| expr2;
expr2
	: expr2 (AND_OP | OR_OP) expr3
	| expr3;
expr3
	: expr3 (ADD_OP | SUB_OP) expr4
	| expr4;
expr4
	: expr4 (MUL_OP | DIV_OP | MOD_OP) expr5
	| expr5;
expr5
	: NOT_OP expr5
	| expr6;
expr6
	: SUB_OP expr6
	| expr7;
expr7
	: array_index_expr
	| factor;

factor: NUMBERLIT | BOOLLIT | STRINGLIT | IDENTIFIER | arraylit | func_call | sub_expr;
sub_expr: LRB expr RRB;

list_newline: NEWLINE+;
NEWLINE: '\r'? '\n' {self.text = self.text.replace('\r','')};

// Keywords
TYPE_NUMBER: 'number';
TYPE_BOOL: 'bool';
TYPE_STRING: 'string';
VAR: 'var';
DYNAMIC: 'dynamic';
RETURN: 'return';
FUNC: 'func';
FOR: 'for';
UNTIL: 'until';
BY: 'by';
BREAK: 'break';
CONTINUE: 'continue';
IF: 'if';
ELSE: 'else';
ELIF: 'elif';
BEGIN: 'begin';
END: 'end';
//Operators
ADD_OP: '+';
SUB_OP: '-';
MUL_OP: '*';
DIV_OP: '/';
MOD_OP: '%';
NOT_OP: 'not';
AND_OP: 'and';
OR_OP: 'or';
EQ_OP: '==';
NEQ_OP: '!=';
LT_OP: '<';
LEQ_OP: '<=';
GT_OP: '>';
GEQ_OP: '>=';
CONCAT_OP: '...';
ASSIGN_OP: '<-';
EQ: '=';

//Seperators
LSB: '[';
RSB: ']';
LRB: '(';
RRB: ')';
CM: ',';
COL: ':';
QUOTES: '"';

// comments
LINE_CMT: ('##' .*? (NEWLINE | EOF)) -> skip;
WS: [ \t]+ -> skip; // skip spaces, tabs, newlines

//fragments
fragment DIGIT: [0-9];
fragment EXPONENT: [eE] [+-]?;
fragment CHAR: ('\\' [\\bfrnt'] | '\'"' | ~["\\\n]);
// literal
BOOLLIT: ('true' | 'false');
NUMBERLIT: DIGIT+ ('.' DIGIT*)? (EXPONENT DIGIT+)?;
STRINGLIT: QUOTES CHAR* QUOTES {self.text = self.text[1:-1]};
arraylit: LSB itemlist RSB;
itemlist: item CM itemlist | item;
item: arraylit | expr;
// identifiers
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;

UNCLOSE_STRING:
	QUOTES CHAR* ('\n' | EOF) {self.text = self.text[1:]} {raise UncloseString(self.text)
		};
ILLEGAL_ESCAPE:
	QUOTES CHAR* ('\\' ~[bfrnt'"\\]) {self.text = self.text[1:]} {raise IllegalEscape(self.text)
		};
ERROR_CHAR: . {raise ErrorToken(self.text)};
