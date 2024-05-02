from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *
# from src.main.zcode.utils.AST import *

class ASTGeneration(ZCodeVisitor):

    def visitProgram(self, ctx: ZCodeParser.ProgramContext):
        return Program(self.visit(ctx.decls()))
    # decls: decl decls_tail;
    def visitDecls(self, ctx: ZCodeParser.DeclsContext):
        return [self.visit(ctx.decl())] + self.visit(ctx.decls_tail())
    # decls_tail: decl decls_tail | ;
    def visitDecls_tail(self, ctx: ZCodeParser.Decls_tailContext):
        if ctx.decls_tail():
            return [self.visit(ctx.decl())] + self.visit(ctx.decls_tail())
        return []
    def visitDecl(self, ctx: ZCodeParser.DeclContext):
        return self.visit(ctx.getChild(0))
    # var_decl: (keyword_var | implicit_var | implicit_dynamic) list_newline;
    def visitVar_decl(self, ctx: ZCodeParser.Var_declContext):
        return self.visit(ctx.getChild(0))
    # keyword_var: keyword_var_decl | keyword_var_array_decl;
    def visitKeyword_var(self, ctx: ZCodeParser.Keyword_varContext):
        return self.visit(ctx.getChild(0))
    # keyword_var_decl: type_vardecl IDENTIFIER (ASSIGN_OP expr)?;
    def visitKeyword_var_decl(self, ctx: ZCodeParser.Keyword_var_declContext):
        if ctx.expr():
            return VarDecl(Id(ctx.IDENTIFIER().getText()),self.visit(ctx.type_vardecl()), None, self.visit(ctx.expr()))
        return VarDecl(Id(ctx.IDENTIFIER().getText()),self.visit(ctx.type_vardecl()))
    # keyword_var_array_decl: type_vardecl IDENTIFIER arraydim (ASSIGN_OP expr)?;
    def visitKeyword_var_array_decl(self, ctx: ZCodeParser.Keyword_var_array_declContext):
        typ = self.visit(ctx.type_vardecl())
        if ctx.expr():
            return VarDecl(Id(ctx.IDENTIFIER().getText()), ArrayType(self.visit(ctx.arraydim()), typ), None, self.visit(ctx.expr()))
        return VarDecl(Id(ctx.IDENTIFIER().getText()), ArrayType(self.visit(ctx.arraydim()), typ))
    # arraydim: LSB listdim RSB;
    def visitArraydim(self, ctx: ZCodeParser.ArraydimContext):
        return self.visit(ctx.listdim())
    # listdim: (NUMBERLIT CM listdim) | NUMBERLIT;
    def visitListdim(self, ctx: ZCodeParser.ListdimContext):
        if ctx.listdim():
            return [float(ctx.NUMBERLIT().getText())] + self.visit(ctx.listdim())
        return [float(ctx.NUMBERLIT().getText())]
    # type_vardecl: TYPE_NUMBER | TYPE_BOOL | TYPE_STRING;
    def visitType_vardecl(self, ctx: ZCodeParser.Type_vardeclContext):
        if ctx.TYPE_NUMBER():
            return NumberType()
        elif ctx.TYPE_BOOL():
            return BoolType()
        else:
            return StringType()
    # implicit_var: VAR IDENTIFIER ASSIGN_OP expr;
    def visitImplicit_var(self, ctx: ZCodeParser.Implicit_varContext):
        modifier = ctx.VAR().getText()
        return VarDecl(Id(ctx.IDENTIFIER().getText()), None, modifier, self.visit(ctx.expr()))
    # implicit_dynamic: DYNAMIC IDENTIFIER (ASSIGN_OP expr)?;
    def visitImplicit_dynamic(self, ctx: ZCodeParser.Implicit_dynamicContext):
        modifier = ctx.DYNAMIC().getText()
        if ctx.expr():
            return VarDecl(Id(ctx.IDENTIFIER().getText()), None, modifier, self.visit(ctx.expr()))
        return VarDecl(Id(ctx.IDENTIFIER().getText()), None, modifier)
    # func_decl: func_decl_prototype | func_decl_complete ;
    def visitFunc_decl(self, ctx: ZCodeParser.Func_declContext):
        return self.visit(ctx.getChild(0))
    # func_decl_complete: FUNC IDENTIFIER LRB param_decls RRB list_newline? body;
    def visitFunc_decl_complete(self, ctx: ZCodeParser.Func_decl_completeContext):
        return FuncDecl(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.param_decls()), self.visit(ctx.body()))
    # func_decl_prototype: FUNC IDENTIFIER LRB param_decls RRB list_newline? (return_stmt?|list_newline);
    def visitFunc_decl_prototype(self, ctx: ZCodeParser.Func_decl_prototypeContext):
        if ctx.return_stmt():
            return FuncDecl(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.param_decls()), self.visit(ctx.return_stmt()))
        else:
            return FuncDecl(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.param_decls()), None)
    # body: BEGIN list_newline body_one? END list_newline;
    def visitBody(self, ctx: ZCodeParser.BodyContext):
        if ctx.body_one():
            return Block(self.visit(ctx.body_one()))
        return Block([])
    # body_one: statement body_one | statement;
    def visitBody_one(self, ctx: ZCodeParser.Body_oneContext):
        if ctx.getChildCount() == 2:
            return [self.visit(ctx.statement())] + self.visit(ctx.body_one())
        return [self.visit(ctx.statement())]
    # param_decls: param_decl param_decl_tail | ;
    def visitParam_decls(self, ctx: ZCodeParser.Param_declsContext):
        if ctx.getChildCount() == 2:
            return [self.visit(ctx.param_decl())] + self.visit(ctx.param_decl_tail())
        return []
    # param_decl_tail: CM param_decl param_decl_tail |;
    def visitParam_decl_tail(self, ctx: ZCodeParser.Param_decl_tailContext):
        if ctx.param_decl_tail():
            return [self.visit(ctx.param_decl())] + self.visit(ctx.param_decl_tail())
        return []
    # param_decl: type_vardecl IDENTIFIER (arraydim |);
    def visitParam_decl(self, ctx: ZCodeParser.Param_declContext):
        typ = self.visit(ctx.type_vardecl())
        if ctx.arraydim():
            return VarDecl(Id(ctx.IDENTIFIER().getText()), ArrayType(self.visit(ctx.arraydim()), typ))
        return VarDecl(Id(ctx.IDENTIFIER().getText()), typ)
    def visitStatement(self, ctx: ZCodeParser.StatementContext):
        return self.visit(ctx.getChild(0))
    # assign_stmt: (IDENTIFIER | array_index_expr) ASSIGN_OP expr list_newline;
    def visitAssign_stmt(self, ctx: ZCodeParser.Assign_stmtContext):
        if ctx.array_index_expr():
            return Assign(self.visit(ctx.array_index_expr()), self.visit(ctx.expr()))
        return Assign(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.expr()))
    # array_index_expr: (IDENTIFIER | func_call) LSB list_expr RSB;
    def visitArray_index_expr(self, ctx: ZCodeParser.Array_index_exprContext):
        if ctx.IDENTIFIER():
            return ArrayCell(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.list_expr()))
        return ArrayCell(self.visit(ctx.func_call()), self.visit(ctx.list_expr()))
    #  list_expr: expr expr_tail | expr;
    def visitList_expr(self, ctx: ZCodeParser.List_exprContext):
        if ctx.expr_tail():
            return [self.visit(ctx.expr())] + self.visit(ctx.expr_tail())
        return [self.visit(ctx.expr())]
    # expr_tail: CM expr expr_tail |;
    def visitExpr_tail(self, ctx: ZCodeParser.Expr_tailContext):
        if ctx.expr_tail():
            return [self.visit(ctx.expr())] + self.visit(ctx.expr_tail())
        return []
    
    def visitBreak_stmt(self, ctx: ZCodeParser.Break_stmtContext):
        return Break()
    def visitContinue_stmt(self, ctx: ZCodeParser.Continue_stmtContext):
        return Continue()
    def visitReturn_stmt(self, ctx: ZCodeParser.Return_stmtContext):
        if ctx.expr():
            return Return(self.visit(ctx.expr()))
        return Return()
    # func_call_stmt: IDENTIFIER LRB (list_expr | ) RRB list_newline;
    def visitFunc_call_stmt(self, ctx: ZCodeParser.Func_call_stmtContext):
        return CallStmt(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.list_expr())) if ctx.list_expr() else CallStmt(Id(ctx.IDENTIFIER().getText()), [])
    # func_call: IDENTIFIER LRB (list_expr | ) RRB;
    def visitFunc_call(self, ctx: ZCodeParser.Func_callContext):
        return CallExpr(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.list_expr())) if ctx.list_expr() else CallExpr(Id(ctx.IDENTIFIER().getText()), [])
    # if_stmt: IF LRB expr RRB list_newline? statement list_elif (ELSE list_newline? statement)?;
    def visitIf_stmt(self, ctx: ZCodeParser.If_stmtContext):
        if ctx.ELSE():
            return If(self.visit(ctx.expr()), self.visit(ctx.statement(0)), self.visit(ctx.list_elif()), self.visit(ctx.statement(1)))
        return If(self.visit(ctx.expr()), self.visit(ctx.statement(0)), self.visit(ctx.list_elif()))
    # list_elif: elif_one list_elif | ;
    def visitList_elif(self, ctx: ZCodeParser.List_elifContext):
        if ctx.elif_one():
            return [self.visit(ctx.elif_one())] + self.visit(ctx.list_elif())
        return []
    # elif_one: ELIF LRB expr RRB list_newline? statement;
    def visitElif_one(self, ctx: ZCodeParser.Elif_oneContext):
        return (self.visit(ctx.expr()), self.visit(ctx.statement()))
    # for_stmt: FOR IDENTIFIER UNTIL expr BY expr list_newline? statement;
    def visitFor_stmt(self, ctx: ZCodeParser.For_stmtContext):
        return For(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.expr(0)), self.visit(ctx.expr(1)), self.visit(ctx.statement()))
    # expr: expr1 CONCAT_OP expr1 | expr1;
    def visitExpr(self, ctx: ZCodeParser.ExprContext):
        if ctx.CONCAT_OP():
            return BinaryOp(ctx.CONCAT_OP().getText(), self.visit(ctx.expr1(0)), self.visit(ctx.expr1(1)))
        return self.visit(ctx.expr1(0))
    # expr1: expr2 (EQ | | EQ_OP | NEQ_OP | LT_OP | GT_OP | LEQ_OP | GEQ_OP) expr2 | expr2;
    def visitExpr1(self, ctx: ZCodeParser.Expr1Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))
        return self.visit(ctx.expr2(0))
    # expr2 : expr2 (AND_OP | OR_OP) expr3 | expr3;
    def visitExpr2(self, ctx: ZCodeParser.Expr2Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expr2()), self.visit(ctx.expr3()))
        return self.visit(ctx.expr3())
    # expr3 : expr3 (ADD_OP | SUB_OP) expr4 | expr4;
    def visitExpr3(self, ctx: ZCodeParser.Expr3Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expr3()), self.visit(ctx.expr4()))
        return self.visit(ctx.expr4())
    # expr4 : expr4 (MUL_OP | DIV_OP | MOD_OP) expr5 | expr5;
    def visitExpr4(self, ctx: ZCodeParser.Expr4Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expr4()), self.visit(ctx.expr5()))
        return self.visit(ctx.expr5())
    # expr5 : NOT_OP expr5 | expr6;
    def visitExpr5(self, ctx: ZCodeParser.Expr5Context):
        if ctx.NOT_OP():
            return UnaryOp(ctx.NOT_OP().getText(), self.visit(ctx.expr5()))
        return self.visit(ctx.expr6())
    # expr6 : SUB_OP expr6 | expr7;
    def visitExpr6(self, ctx: ZCodeParser.Expr6Context):
        if ctx.SUB_OP():
            return UnaryOp(ctx.SUB_OP().getText(), self.visit(ctx.expr6()))
        return self.visit(ctx.expr7())
    # expr7 : array_index_expr | factor;
    def visitExpr7(self, ctx: ZCodeParser.Expr7Context):
        return self.visit(ctx.getChild(0))
    # factor: NUMBERLIT | BOOLLIT | STRINGLIT | IDENTIFIER | arraylit | func_call | sub_expr;
    def visitFactor(self, ctx: ZCodeParser.FactorContext):
        if ctx.NUMBERLIT():
            return NumberLiteral(float(ctx.NUMBERLIT().getText()))
        elif ctx.BOOLLIT():
            return BooleanLiteral(ctx.BOOLLIT().getText() == "true")
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        elif ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        elif ctx.arraylit():
            return self.visit(ctx.arraylit())
        elif ctx.func_call():
            return self.visit(ctx.func_call())
        elif ctx.sub_expr():
            return self.visit(ctx.sub_expr())
    # sub_expr: LRB expr RRB;
    def visitSub_expr(self, ctx: ZCodeParser.Sub_exprContext):
        return self.visit(ctx.expr())
    #arraylit: LSB itemlist RSB;
    def visitArraylit(self, ctx: ZCodeParser.ArraylitContext):
        return ArrayLiteral(self.visit(ctx.itemlist()))
    # itemlist: item CM itemlist | item;
    def visitItemlist(self, ctx: ZCodeParser.ItemlistContext):
        if ctx.itemlist():
            return [self.visit(ctx.item())] + self.visit(ctx.itemlist())
        return [self.visit(ctx.item())]
    # item: arraylit | expr;
    def visitItem(self, ctx: ZCodeParser.ItemContext):
        if ctx.arraylit():
            return self.visit(ctx.arraylit())
        return self.visit(ctx.expr())
