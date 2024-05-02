# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete generic visitor for a parse tree produced by ZCodeParser.

class ZCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ZCodeParser#program.
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#decls.
    def visitDecls(self, ctx:ZCodeParser.DeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#decls_tail.
    def visitDecls_tail(self, ctx:ZCodeParser.Decls_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#decl.
    def visitDecl(self, ctx:ZCodeParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#var_decl.
    def visitVar_decl(self, ctx:ZCodeParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#keyword_var.
    def visitKeyword_var(self, ctx:ZCodeParser.Keyword_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#keyword_var_decl.
    def visitKeyword_var_decl(self, ctx:ZCodeParser.Keyword_var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#keyword_var_array_decl.
    def visitKeyword_var_array_decl(self, ctx:ZCodeParser.Keyword_var_array_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arraydim.
    def visitArraydim(self, ctx:ZCodeParser.ArraydimContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#listdim.
    def visitListdim(self, ctx:ZCodeParser.ListdimContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#type_vardecl.
    def visitType_vardecl(self, ctx:ZCodeParser.Type_vardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#implicit_var.
    def visitImplicit_var(self, ctx:ZCodeParser.Implicit_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#implicit_dynamic.
    def visitImplicit_dynamic(self, ctx:ZCodeParser.Implicit_dynamicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#func_decl.
    def visitFunc_decl(self, ctx:ZCodeParser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#func_decl_complete.
    def visitFunc_decl_complete(self, ctx:ZCodeParser.Func_decl_completeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#func_decl_prototype.
    def visitFunc_decl_prototype(self, ctx:ZCodeParser.Func_decl_prototypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#body.
    def visitBody(self, ctx:ZCodeParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#body_one.
    def visitBody_one(self, ctx:ZCodeParser.Body_oneContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#param_decls.
    def visitParam_decls(self, ctx:ZCodeParser.Param_declsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#param_decl_tail.
    def visitParam_decl_tail(self, ctx:ZCodeParser.Param_decl_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#param_decl.
    def visitParam_decl(self, ctx:ZCodeParser.Param_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#statement.
    def visitStatement(self, ctx:ZCodeParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#assign_stmt.
    def visitAssign_stmt(self, ctx:ZCodeParser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_index_expr.
    def visitArray_index_expr(self, ctx:ZCodeParser.Array_index_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#list_expr.
    def visitList_expr(self, ctx:ZCodeParser.List_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr_tail.
    def visitExpr_tail(self, ctx:ZCodeParser.Expr_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#break_stmt.
    def visitBreak_stmt(self, ctx:ZCodeParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#continue_stmt.
    def visitContinue_stmt(self, ctx:ZCodeParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#return_stmt.
    def visitReturn_stmt(self, ctx:ZCodeParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#func_call_stmt.
    def visitFunc_call_stmt(self, ctx:ZCodeParser.Func_call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#func_call.
    def visitFunc_call(self, ctx:ZCodeParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#if_stmt.
    def visitIf_stmt(self, ctx:ZCodeParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#list_elif.
    def visitList_elif(self, ctx:ZCodeParser.List_elifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elif_one.
    def visitElif_one(self, ctx:ZCodeParser.Elif_oneContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#for_stmt.
    def visitFor_stmt(self, ctx:ZCodeParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr.
    def visitExpr(self, ctx:ZCodeParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr1.
    def visitExpr1(self, ctx:ZCodeParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr2.
    def visitExpr2(self, ctx:ZCodeParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr3.
    def visitExpr3(self, ctx:ZCodeParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr4.
    def visitExpr4(self, ctx:ZCodeParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr5.
    def visitExpr5(self, ctx:ZCodeParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr6.
    def visitExpr6(self, ctx:ZCodeParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr7.
    def visitExpr7(self, ctx:ZCodeParser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#factor.
    def visitFactor(self, ctx:ZCodeParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#sub_expr.
    def visitSub_expr(self, ctx:ZCodeParser.Sub_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#list_newline.
    def visitList_newline(self, ctx:ZCodeParser.List_newlineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arraylit.
    def visitArraylit(self, ctx:ZCodeParser.ArraylitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#itemlist.
    def visitItemlist(self, ctx:ZCodeParser.ItemlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#item.
    def visitItem(self, ctx:ZCodeParser.ItemContext):
        return self.visitChildren(ctx)



del ZCodeParser