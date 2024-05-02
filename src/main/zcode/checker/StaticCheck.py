from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

class Zcode:
    pass

class FuncZcode(Zcode):
    def __init__(self, param = [], typ = None, body = False):
        self.param = param
        self.typ = typ
        self.body = body

class VarZcode(Zcode):
    def __init__(self, typ = None):
        self.typ = typ
# Type: Zcode, ArrayZcode, string, bool, number, arraytype
class ArrayZcode(Type):
    def __init__(self, ele_typ):
        self.eleType = eleType

class StaticChecker(BaseVisitor, Utils):
    def __init__(self,ast, ):
        self.ast = ast
        self.BlockFor = 0
        self.function = None
        self.is_return = False
        self.list_func = [{
                "readNumber" : FuncZcode([], NumberType(), True),
                "readBool" : FuncZcode([], BoolType(), True),
                "readString" : FuncZcode([], StringType(), True),
                "writeNumber" : FuncZcode([NumberType()], VoidType(), True),
                "writeBool" : FuncZcode([BoolType()], VoidType(), True),
                "writeString" : FuncZcode([StringType()], VoidType(), True)
                }]

    def check(self):
        self.visit(self.ast, [{}])
        return None

    def compare_type(self, LHS, RHS):
        if(type(LHS) != type(RHS)):
            return False
        elif(type(LHS) is ArrayType):
            if(len(LHS.size) != len(RHS.size)):
                return False
            elif type(LHS.eleType) != type(RHS.eleType):
                return False
            else:
                for i in range(len(LHS.size)):
                    if LHS.size[i] != RHS.size[i]:
                        return False
        return True

    def compare_list_type(self, list_LHS, list_RHS):
        if (len(list_LHS) != len(list_RHS)):
            return False
        else:
            for i in range(0,len(list_LHS)):
                if(not self.compare_type(list_LHS[i],list_RHS[i])):
                    return False
        return True
    # check TypeCannotBeInferred and TypeMismatchInStatement
    def check_LHS_RHS(self,lhs,rhs,ast,stmt_flag=True):
            if isinstance(lhs,Zcode):
                if isinstance(rhs,Zcode) or isinstance(rhs,ArrayZcode):
                    raise TypeCannotBeInferred(ast)
                # Can be inferred
                else:
                    lhs.typ=rhs
            elif(not isinstance(lhs,Zcode) and isinstance(rhs,ArrayZcode)):
                    if(type(lhs) is ArrayType):
                        if(not self.set_type_arr(lhs, rhs)):
                            if(stmt_flag):
                                raise TypeMismatchInStatement(ast)
                            else:
                                raise TypeMismatchInExpression(ast)
                    # LHS is string, bool, number
                    else:
                        if(stmt_flag):
                            raise TypeMismatchInStatement(ast)
                        else:
                            raise TypeMismatchInExpression(ast)
            # Right inffered
            elif(isinstance(lhs,Type) and isinstance(rhs,Zcode)):
                rhs.typ=lhs
            elif(not self.compare_type(lhs,rhs)):
                if(stmt_flag):
                    raise TypeMismatchInStatement(ast)
                else:
                    raise TypeMismatchInExpression(ast)

    def set_type_arr(self, typeArray, typeArrayZcode):
        if typeArray.size[0] != len(typeArrayZcode.eleType):
            return False
        # normal array
        if len(typeArray.size) == 1:
            for i in range(0,int(typeArray.size[0])):
                if(isinstance(typeArrayZcode.eleType[i],Zcode)):
                    typeArrayZcode.eleType[i].typ = typeArray.eleType
                elif(isinstance(typeArrayZcode.eleType[i],ArrayZcode)):
                    return False
        # array in array
        else:
            for i in range(0,int(typeArray.size[0])):
                if(isinstance(typeArrayZcode.eleType[i],Zcode)):
                    typeArrayZcode.eleType[i].typ = ArrayType(typeArray.size[1:], typeArray.eleType)
                elif(isinstance(typeArrayZcode.eleType[i],ArrayZcode)):
                    check= self.set_type_arr(ArrayType(typeArray.size[1:], typeArray.eleType),typeArrayZcode.eleType[i])
                    if(not check):
                        return False
        return True

    def visitProgram(self, ast, param):
        for decl in ast.decl: self.visit(decl, param)
        for env in self.list_func:
            for name, func in  env.items():
                if func.body == False :
                    raise NoDefinition(name)

        main = self.list_func[-1].get("main")
        if not main or (len(main.param) != 0) or not self.compare_type(main.typ, VoidType()):
            raise NoEntryPoint()
    def visitVarDecl(self, ast, param):
        curr_name = ast.name.name
        # variable
        if (type(param) is list) :
            if curr_name in param[0]:
                raise  Redeclared(Variable(), curr_name)

            param[0][curr_name] = VarZcode(ast.varType)
        # param in func
        elif (type(param) is dict):
            if curr_name in param:
                raise  Redeclared(Parameter(), curr_name)
            param[curr_name] = VarZcode(ast.varType)
        if(ast.varInit):
            lhs = ast.varType if ast.varType else param[0][curr_name]
            rhs = self.visit(ast.varInit, param)
            self.check_LHS_RHS(lhs,rhs,ast,True)

# Use reduce to apply the function to all parameters in ast.param
    def visitFuncDecl(self, ast, param):
        curr_name = ast.name.name
        if (curr_name in self.list_func[0]) and not(self.list_func[0].get(curr_name).body == False and ast.body):
            raise  Redeclared(Function(), curr_name)

        listParam = {}
        typeParam = []

        for i in ast.param:
            self.visit(i, listParam)
            typeParam.append(i.varType)

        self.Return = False
        is_func_decl=False
        if (curr_name in self.list_func[0]) and (self.list_func[0].get(curr_name).body == False and ast.body):
            lhs=self.list_func[0].get(curr_name).param
            rhs=typeParam
            if not self.compare_list_type(lhs,rhs):
                raise Redeclared(Function(), curr_name)
            self.list_func[0].get(curr_name).body = True
            self.function = self.list_func[0][curr_name]
            self.visit(ast.body,[{}]+[listParam]+param)
        elif (ast.body is None):
            is_func_decl=True
            self.list_func[0][curr_name] = FuncZcode(typeParam, None, False)
        elif (ast.body is not None):
            self.list_func[0][curr_name] = FuncZcode(typeParam,None,True)
            self.function= self.list_func[0][curr_name]
            self.visit(ast.body,[{}]+[listParam]+param)
        if not is_func_decl:
            if not self.Return:
                if not self.list_func[0][curr_name].typ:
                    self.list_func[0][curr_name].typ = VoidType()
                elif not self.compare_type(self.list_func[0][curr_name].typ, VoidType()): 
                    raise TypeMismatchInStatement(Return(None))

    def visitId(self, ast, param):
        for i in param:
            if i.get(ast.name):
                id = i.get(ast.name)
                return id.typ if id.typ else id
        raise Undeclared(Identifier(), ast.name)

    def visitCallExpr(self, ast, param):
        curr_name = ast.name.name
        if (not self.list_func[0].get(curr_name)):
            raise Undeclared(Function(),curr_name)
        list_lhs = self.list_func[0].get(curr_name).param
        list_rhs = ast.args
        if(len(list_lhs) != len(list_rhs)):
            raise TypeMismatchInExpression(ast)
        for i in range(0, len(list_lhs)):
            # check inffer
            lhs=self.visit(list_lhs[i], param)
            rhs=self.visit(list_rhs[i], param)
            self.check_LHS_RHS(lhs, rhs, ast, False)
        call_func = self.list_func[0].get(curr_name)
        if not call_func.typ:
            return self.list_func[0][curr_name]
        if self.compare_type(call_func.typ, VoidType()):
            raise TypeMismatchInExpression(ast)
        return call_func.typ
    def visitCallStmt(self, ast, param):
        curr_name = ast.name.name
        if not self.list_func[0].get(curr_name):
            raise Undeclared(Function(), curr_name)
      
        # check missmatch
        list_lhs=self.list_func[0].get(curr_name).param
        list_rhs=ast.args
        call_func=self.list_func[0].get(curr_name)
        if(len(list_lhs) != len(list_rhs)):
            raise TypeMismatchInStatement(ast)
        for i in range(0, len(list_lhs)):
            lhs=self.visit(list_lhs[i], param)
            rhs=self.visit(list_rhs[i], param)
            self.check_LHS_RHS(lhs, rhs, ast, True)

        if(call_func.typ is None):
            call_func.typ = VoidType()
        elif not self.compare_type(call_func.typ, VoidType()):
            raise TypeMismatchInStatement(ast)
        return call_func.typ

    def visitIf(self, ast, param):
        lhs = BoolType()
        rhs = self.visit(ast.expr, param)
        if isinstance(rhs, Zcode):
            rhs.typ = lhs
        elif not self.compare_type(lhs, rhs):
            raise TypeMismatchInStatement(ast)
        self.visit(ast.thenStmt,[{}]+param)

        for elif_one in ast.elifStmt:
            expr, stmt = elif_one
            lhs = BoolType()
            rhs = self.visit(expr, param)
            if isinstance(rhs, Zcode):
                rhs.typ = lhs
            elif not self.compare_type(lhs, rhs):
                raise TypeMismatchInStatement(ast)
            self.visit(stmt,[{}]+param)
        # else
        if(ast.elseStmt):
            self.visit(ast.elseStmt,[{}]+param)

    def visitFor(self, ast, param):
        name = self.visit(ast.name, param)
        cond_expr = self.visit(ast.condExpr, param)
        up_expr = self.visit(ast.updExpr, param)
        if(isinstance(name, Zcode)):
            name.typ = NumberType()
        elif not self.compare_type(NumberType(), name):
            raise TypeMismatchInStatement(ast)

        if isinstance(cond_expr,Zcode):
            cond_expr.typ = BoolType()
        elif not self.compare_type(BoolType(),cond_expr):
            raise TypeMismatchInStatement(ast)

        if isinstance(up_expr, Zcode):
            up_expr.typ = NumberType()
        elif not self.compare_type(NumberType(), up_expr):
            raise TypeMismatchInStatement(ast)
        # enter block for
        self.BlockFor += 1
        self.visit(ast.body, [{}] + param)
        self.BlockFor -= 1

    def visitReturn(self, ast, param):
        self.Return = True
        if self.function.typ:
            lhs = self.function.typ
        else:
            lhs = self.function
        if ast.expr:
            rhs = self.visit(ast.expr, param)
        else:
            rhs = VoidType()
        self.check_LHS_RHS(lhs, rhs, ast, True)

    def visitAssign(self, ast, param):
        lhs = self.visit(ast.lhs,param)
        rhs = self.visit(ast.rhs,param)
        self.check_LHS_RHS(lhs, rhs, ast, True)

    def visitBinaryOp(self, ast, param):
        left = self.visit(ast.left, param)
        if(ast.op in ['+','-','*','/','%'] ):
            if(isinstance(left,Zcode)):
                left.typ = NumberType()
            elif(not self.compare_type(left, NumberType())):
                raise TypeMismatchInExpression(ast)
            
        elif (ast.op in ['=','!=','<','>','>=','<=']):
            if(isinstance(left,Zcode)):
                left.typ = NumberType()
            elif(not self.compare_type(left, NumberType())):
                raise TypeMismatchInExpression(ast)
            return BoolType()
        
        elif(ast.op in ['and','or']):
            if(isinstance(left,Zcode)):
                left.typ = BoolType()
            elif(not self.compare_type(left, BoolType())):
                raise TypeMismatchInExpression(ast)
            
        elif (ast.op in ['==','...']):
            
            if(isinstance(left,Zcode)):
                left.typ = StringType()
            elif(not self.compare_type(left, StringType())):
                raise TypeMismatchInExpression(ast)

        right = self.visit(ast.right, param)
        if(ast.op in ['+','-','*','/','%']):
            if(isinstance(right,Zcode)):
                right.typ = NumberType()
            elif(not self.compare_type(right, NumberType())):
                raise TypeMismatchInExpression(ast)
            return NumberType()
        
        elif (ast.op in ['=','!=','<','>','>=','<=']):
            if(isinstance(right,Zcode)):
                right.typ = NumberType()
            elif(not self.compare_type(right, NumberType())):
                raise TypeMismatchInExpression(ast)
            return BoolType()
        
        elif(ast.op in ['and','or']):
            if(isinstance(right,Zcode)):
                right.typ = BoolType()
            elif(not self.compare_type(right, BoolType())):
                raise TypeMismatchInExpression(ast)
            return BoolType()
            
        elif (ast.op in ['==','...']):
            if(isinstance(right,Zcode)):
                right.typ= StringType()
            elif(not self.compare_type(right, StringType())):
                raise TypeMismatchInExpression(ast)
            return StringType()
  
    def visitUnaryOp(self, ast, param):
        operand=self.visit(ast.operand,param)
        if(ast.op in ['+','-']):
            if(self.compare_type(operand,NumberType())):
                return NumberType()
            elif(isinstance(operand,Zcode)):
                operand.typ=NumberType()
                return NumberType()
            else:
                raise TypeMismatchInExpression(ast)
        elif(ast.op in ['not']):
            if(self.compare_type(operand,BoolType())):
                return BoolType()
            elif(isinstance(operand,Zcode)):
                operand.typ=BoolType()
                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)

    def visitArrayCell(self, ast, param):
        arr = self.visit(ast.arr,param)
        if type(arr) is not ArrayType:
            raise TypeMismatchInExpression(ast)

        lhs = NumberType()
        list_rhs = ast.idx
        for expr in list_rhs:
            rhs = self.visit(expr,param)
            if(isinstance(rhs, Zcode)):
                rhs.typ = NumberType()
            elif not self.compare_type(lhs,rhs):
                raise TypeMismatchInExpression(ast)
        if(len(arr.size) < len(ast.idx)):
            raise TypeMismatchInExpression(ast)
        elif len(arr.size) == len(ast.idx):
            return arr.eleType
        else:
            start=len(arr.size)-len(ast.idx)
            size=arr.size[start:]
            eleType=arr.eleType
            return ArrayType(size,eleType)

    def visitBlock(self, ast, param):
        for item in ast.stmt:
            if type(item) is Block: self.visit(item, [{}] + param)
            else: self.visit(item, param)

    def visitContinue(self, ast, param):
        if self.BlockFor == 0:
            raise MustInLoop(ast)

    def visitBreak(self, ast, param):
        if self.BlockFor == 0:
            raise MustInLoop(ast)
    def visitNumberType(self, ast, param):
        return ast
    def visitBoolType(self, ast, param):
        return ast
    def visitStringType(self, ast, param):
        return ast
    def visitArrayType(self, ast, param):
        return ast
    def visitNumberLiteral(self, ast, param):
        return NumberType()
    def visitBooleanLiteral(self, ast, param):
        return BoolType()
    def visitStringLiteral(self, ast, param):
        return StringType()