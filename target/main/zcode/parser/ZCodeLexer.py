# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\65")
        buf.write("\u0181\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\3\2\5\2q\n\2\3\2\3")
        buf.write("\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24\3\25")
        buf.write("\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\37\3\37\3\37\3 \3 \3!\3!\3!\3\"")
        buf.write("\3\"\3\"\3\"\3#\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(")
        buf.write("\3)\3)\3*\3*\3+\3+\3,\3,\3,\3,\7,\u0114\n,\f,\16,\u0117")
        buf.write("\13,\3,\3,\5,\u011b\n,\3,\3,\3-\6-\u0120\n-\r-\16-\u0121")
        buf.write("\3-\3-\3.\3.\3/\3/\5/\u012a\n/\3\60\3\60\3\60\3\60\3\60")
        buf.write("\5\60\u0131\n\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3")
        buf.write("\61\3\61\5\61\u013c\n\61\3\62\6\62\u013f\n\62\r\62\16")
        buf.write("\62\u0140\3\62\3\62\7\62\u0145\n\62\f\62\16\62\u0148\13")
        buf.write("\62\5\62\u014a\n\62\3\62\3\62\6\62\u014e\n\62\r\62\16")
        buf.write("\62\u014f\5\62\u0152\n\62\3\63\3\63\7\63\u0156\n\63\f")
        buf.write("\63\16\63\u0159\13\63\3\63\3\63\3\63\3\64\3\64\7\64\u0160")
        buf.write("\n\64\f\64\16\64\u0163\13\64\3\65\3\65\7\65\u0167\n\65")
        buf.write("\f\65\16\65\u016a\13\65\3\65\5\65\u016d\n\65\3\65\3\65")
        buf.write("\3\65\3\66\3\66\7\66\u0174\n\66\f\66\16\66\u0177\13\66")
        buf.write("\3\66\3\66\3\66\3\66\3\66\3\66\3\67\3\67\3\67\3\u0115")
        buf.write("\28\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y.[\2]\2_\2a/c\60e\61g\62i\63k\64m\65\3\2")
        buf.write("\f\4\2\13\13\"\"\3\2\62;\4\2GGgg\4\2--//\t\2))^^ddhhp")
        buf.write("pttvv\5\2\f\f$$^^\5\2C\\aac|\6\2\62;C\\aac|\3\3\f\f\n")
        buf.write("\2$$))^^ddhhppttvv\2\u018e\2\3\3\2\2\2\2\5\3\2\2\2\2\7")
        buf.write("\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2")
        buf.write("\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2")
        buf.write("\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2")
        buf.write("\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2")
        buf.write("\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2")
        buf.write("i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\3p\3\2\2\2\5u\3\2\2\2")
        buf.write("\7|\3\2\2\2\t\u0081\3\2\2\2\13\u0088\3\2\2\2\r\u008c\3")
        buf.write("\2\2\2\17\u0094\3\2\2\2\21\u009b\3\2\2\2\23\u00a0\3\2")
        buf.write("\2\2\25\u00a4\3\2\2\2\27\u00aa\3\2\2\2\31\u00ad\3\2\2")
        buf.write("\2\33\u00b3\3\2\2\2\35\u00bc\3\2\2\2\37\u00bf\3\2\2\2")
        buf.write("!\u00c4\3\2\2\2#\u00c9\3\2\2\2%\u00cf\3\2\2\2\'\u00d3")
        buf.write("\3\2\2\2)\u00d5\3\2\2\2+\u00d7\3\2\2\2-\u00d9\3\2\2\2")
        buf.write("/\u00db\3\2\2\2\61\u00dd\3\2\2\2\63\u00e1\3\2\2\2\65\u00e5")
        buf.write("\3\2\2\2\67\u00e8\3\2\2\29\u00eb\3\2\2\2;\u00ee\3\2\2")
        buf.write("\2=\u00f0\3\2\2\2?\u00f3\3\2\2\2A\u00f5\3\2\2\2C\u00f8")
        buf.write("\3\2\2\2E\u00fc\3\2\2\2G\u00ff\3\2\2\2I\u0101\3\2\2\2")
        buf.write("K\u0103\3\2\2\2M\u0105\3\2\2\2O\u0107\3\2\2\2Q\u0109\3")
        buf.write("\2\2\2S\u010b\3\2\2\2U\u010d\3\2\2\2W\u010f\3\2\2\2Y\u011f")
        buf.write("\3\2\2\2[\u0125\3\2\2\2]\u0127\3\2\2\2_\u0130\3\2\2\2")
        buf.write("a\u013b\3\2\2\2c\u013e\3\2\2\2e\u0153\3\2\2\2g\u015d\3")
        buf.write("\2\2\2i\u0164\3\2\2\2k\u0171\3\2\2\2m\u017e\3\2\2\2oq")
        buf.write("\7\17\2\2po\3\2\2\2pq\3\2\2\2qr\3\2\2\2rs\7\f\2\2st\b")
        buf.write("\2\2\2t\4\3\2\2\2uv\7p\2\2vw\7w\2\2wx\7o\2\2xy\7d\2\2")
        buf.write("yz\7g\2\2z{\7t\2\2{\6\3\2\2\2|}\7d\2\2}~\7q\2\2~\177\7")
        buf.write("q\2\2\177\u0080\7n\2\2\u0080\b\3\2\2\2\u0081\u0082\7u")
        buf.write("\2\2\u0082\u0083\7v\2\2\u0083\u0084\7t\2\2\u0084\u0085")
        buf.write("\7k\2\2\u0085\u0086\7p\2\2\u0086\u0087\7i\2\2\u0087\n")
        buf.write("\3\2\2\2\u0088\u0089\7x\2\2\u0089\u008a\7c\2\2\u008a\u008b")
        buf.write("\7t\2\2\u008b\f\3\2\2\2\u008c\u008d\7f\2\2\u008d\u008e")
        buf.write("\7{\2\2\u008e\u008f\7p\2\2\u008f\u0090\7c\2\2\u0090\u0091")
        buf.write("\7o\2\2\u0091\u0092\7k\2\2\u0092\u0093\7e\2\2\u0093\16")
        buf.write("\3\2\2\2\u0094\u0095\7t\2\2\u0095\u0096\7g\2\2\u0096\u0097")
        buf.write("\7v\2\2\u0097\u0098\7w\2\2\u0098\u0099\7t\2\2\u0099\u009a")
        buf.write("\7p\2\2\u009a\20\3\2\2\2\u009b\u009c\7h\2\2\u009c\u009d")
        buf.write("\7w\2\2\u009d\u009e\7p\2\2\u009e\u009f\7e\2\2\u009f\22")
        buf.write("\3\2\2\2\u00a0\u00a1\7h\2\2\u00a1\u00a2\7q\2\2\u00a2\u00a3")
        buf.write("\7t\2\2\u00a3\24\3\2\2\2\u00a4\u00a5\7w\2\2\u00a5\u00a6")
        buf.write("\7p\2\2\u00a6\u00a7\7v\2\2\u00a7\u00a8\7k\2\2\u00a8\u00a9")
        buf.write("\7n\2\2\u00a9\26\3\2\2\2\u00aa\u00ab\7d\2\2\u00ab\u00ac")
        buf.write("\7{\2\2\u00ac\30\3\2\2\2\u00ad\u00ae\7d\2\2\u00ae\u00af")
        buf.write("\7t\2\2\u00af\u00b0\7g\2\2\u00b0\u00b1\7c\2\2\u00b1\u00b2")
        buf.write("\7m\2\2\u00b2\32\3\2\2\2\u00b3\u00b4\7e\2\2\u00b4\u00b5")
        buf.write("\7q\2\2\u00b5\u00b6\7p\2\2\u00b6\u00b7\7v\2\2\u00b7\u00b8")
        buf.write("\7k\2\2\u00b8\u00b9\7p\2\2\u00b9\u00ba\7w\2\2\u00ba\u00bb")
        buf.write("\7g\2\2\u00bb\34\3\2\2\2\u00bc\u00bd\7k\2\2\u00bd\u00be")
        buf.write("\7h\2\2\u00be\36\3\2\2\2\u00bf\u00c0\7g\2\2\u00c0\u00c1")
        buf.write("\7n\2\2\u00c1\u00c2\7u\2\2\u00c2\u00c3\7g\2\2\u00c3 \3")
        buf.write("\2\2\2\u00c4\u00c5\7g\2\2\u00c5\u00c6\7n\2\2\u00c6\u00c7")
        buf.write("\7k\2\2\u00c7\u00c8\7h\2\2\u00c8\"\3\2\2\2\u00c9\u00ca")
        buf.write("\7d\2\2\u00ca\u00cb\7g\2\2\u00cb\u00cc\7i\2\2\u00cc\u00cd")
        buf.write("\7k\2\2\u00cd\u00ce\7p\2\2\u00ce$\3\2\2\2\u00cf\u00d0")
        buf.write("\7g\2\2\u00d0\u00d1\7p\2\2\u00d1\u00d2\7f\2\2\u00d2&\3")
        buf.write("\2\2\2\u00d3\u00d4\7-\2\2\u00d4(\3\2\2\2\u00d5\u00d6\7")
        buf.write("/\2\2\u00d6*\3\2\2\2\u00d7\u00d8\7,\2\2\u00d8,\3\2\2\2")
        buf.write("\u00d9\u00da\7\61\2\2\u00da.\3\2\2\2\u00db\u00dc\7\'\2")
        buf.write("\2\u00dc\60\3\2\2\2\u00dd\u00de\7p\2\2\u00de\u00df\7q")
        buf.write("\2\2\u00df\u00e0\7v\2\2\u00e0\62\3\2\2\2\u00e1\u00e2\7")
        buf.write("c\2\2\u00e2\u00e3\7p\2\2\u00e3\u00e4\7f\2\2\u00e4\64\3")
        buf.write("\2\2\2\u00e5\u00e6\7q\2\2\u00e6\u00e7\7t\2\2\u00e7\66")
        buf.write("\3\2\2\2\u00e8\u00e9\7?\2\2\u00e9\u00ea\7?\2\2\u00ea8")
        buf.write("\3\2\2\2\u00eb\u00ec\7#\2\2\u00ec\u00ed\7?\2\2\u00ed:")
        buf.write("\3\2\2\2\u00ee\u00ef\7>\2\2\u00ef<\3\2\2\2\u00f0\u00f1")
        buf.write("\7>\2\2\u00f1\u00f2\7?\2\2\u00f2>\3\2\2\2\u00f3\u00f4")
        buf.write("\7@\2\2\u00f4@\3\2\2\2\u00f5\u00f6\7@\2\2\u00f6\u00f7")
        buf.write("\7?\2\2\u00f7B\3\2\2\2\u00f8\u00f9\7\60\2\2\u00f9\u00fa")
        buf.write("\7\60\2\2\u00fa\u00fb\7\60\2\2\u00fbD\3\2\2\2\u00fc\u00fd")
        buf.write("\7>\2\2\u00fd\u00fe\7/\2\2\u00feF\3\2\2\2\u00ff\u0100")
        buf.write("\7?\2\2\u0100H\3\2\2\2\u0101\u0102\7]\2\2\u0102J\3\2\2")
        buf.write("\2\u0103\u0104\7_\2\2\u0104L\3\2\2\2\u0105\u0106\7*\2")
        buf.write("\2\u0106N\3\2\2\2\u0107\u0108\7+\2\2\u0108P\3\2\2\2\u0109")
        buf.write("\u010a\7.\2\2\u010aR\3\2\2\2\u010b\u010c\7<\2\2\u010c")
        buf.write("T\3\2\2\2\u010d\u010e\7$\2\2\u010eV\3\2\2\2\u010f\u0110")
        buf.write("\7%\2\2\u0110\u0111\7%\2\2\u0111\u0115\3\2\2\2\u0112\u0114")
        buf.write("\13\2\2\2\u0113\u0112\3\2\2\2\u0114\u0117\3\2\2\2\u0115")
        buf.write("\u0116\3\2\2\2\u0115\u0113\3\2\2\2\u0116\u011a\3\2\2\2")
        buf.write("\u0117\u0115\3\2\2\2\u0118\u011b\5\3\2\2\u0119\u011b\7")
        buf.write("\2\2\3\u011a\u0118\3\2\2\2\u011a\u0119\3\2\2\2\u011b\u011c")
        buf.write("\3\2\2\2\u011c\u011d\b,\3\2\u011dX\3\2\2\2\u011e\u0120")
        buf.write("\t\2\2\2\u011f\u011e\3\2\2\2\u0120\u0121\3\2\2\2\u0121")
        buf.write("\u011f\3\2\2\2\u0121\u0122\3\2\2\2\u0122\u0123\3\2\2\2")
        buf.write("\u0123\u0124\b-\3\2\u0124Z\3\2\2\2\u0125\u0126\t\3\2\2")
        buf.write("\u0126\\\3\2\2\2\u0127\u0129\t\4\2\2\u0128\u012a\t\5\2")
        buf.write("\2\u0129\u0128\3\2\2\2\u0129\u012a\3\2\2\2\u012a^\3\2")
        buf.write("\2\2\u012b\u012c\7^\2\2\u012c\u0131\t\6\2\2\u012d\u012e")
        buf.write("\7)\2\2\u012e\u0131\7$\2\2\u012f\u0131\n\7\2\2\u0130\u012b")
        buf.write("\3\2\2\2\u0130\u012d\3\2\2\2\u0130\u012f\3\2\2\2\u0131")
        buf.write("`\3\2\2\2\u0132\u0133\7v\2\2\u0133\u0134\7t\2\2\u0134")
        buf.write("\u0135\7w\2\2\u0135\u013c\7g\2\2\u0136\u0137\7h\2\2\u0137")
        buf.write("\u0138\7c\2\2\u0138\u0139\7n\2\2\u0139\u013a\7u\2\2\u013a")
        buf.write("\u013c\7g\2\2\u013b\u0132\3\2\2\2\u013b\u0136\3\2\2\2")
        buf.write("\u013cb\3\2\2\2\u013d\u013f\5[.\2\u013e\u013d\3\2\2\2")
        buf.write("\u013f\u0140\3\2\2\2\u0140\u013e\3\2\2\2\u0140\u0141\3")
        buf.write("\2\2\2\u0141\u0149\3\2\2\2\u0142\u0146\7\60\2\2\u0143")
        buf.write("\u0145\5[.\2\u0144\u0143\3\2\2\2\u0145\u0148\3\2\2\2\u0146")
        buf.write("\u0144\3\2\2\2\u0146\u0147\3\2\2\2\u0147\u014a\3\2\2\2")
        buf.write("\u0148\u0146\3\2\2\2\u0149\u0142\3\2\2\2\u0149\u014a\3")
        buf.write("\2\2\2\u014a\u0151\3\2\2\2\u014b\u014d\5]/\2\u014c\u014e")
        buf.write("\5[.\2\u014d\u014c\3\2\2\2\u014e\u014f\3\2\2\2\u014f\u014d")
        buf.write("\3\2\2\2\u014f\u0150\3\2\2\2\u0150\u0152\3\2\2\2\u0151")
        buf.write("\u014b\3\2\2\2\u0151\u0152\3\2\2\2\u0152d\3\2\2\2\u0153")
        buf.write("\u0157\5U+\2\u0154\u0156\5_\60\2\u0155\u0154\3\2\2\2\u0156")
        buf.write("\u0159\3\2\2\2\u0157\u0155\3\2\2\2\u0157\u0158\3\2\2\2")
        buf.write("\u0158\u015a\3\2\2\2\u0159\u0157\3\2\2\2\u015a\u015b\5")
        buf.write("U+\2\u015b\u015c\b\63\4\2\u015cf\3\2\2\2\u015d\u0161\t")
        buf.write("\b\2\2\u015e\u0160\t\t\2\2\u015f\u015e\3\2\2\2\u0160\u0163")
        buf.write("\3\2\2\2\u0161\u015f\3\2\2\2\u0161\u0162\3\2\2\2\u0162")
        buf.write("h\3\2\2\2\u0163\u0161\3\2\2\2\u0164\u0168\5U+\2\u0165")
        buf.write("\u0167\5_\60\2\u0166\u0165\3\2\2\2\u0167\u016a\3\2\2\2")
        buf.write("\u0168\u0166\3\2\2\2\u0168\u0169\3\2\2\2\u0169\u016c\3")
        buf.write("\2\2\2\u016a\u0168\3\2\2\2\u016b\u016d\t\n\2\2\u016c\u016b")
        buf.write("\3\2\2\2\u016d\u016e\3\2\2\2\u016e\u016f\b\65\5\2\u016f")
        buf.write("\u0170\b\65\6\2\u0170j\3\2\2\2\u0171\u0175\5U+\2\u0172")
        buf.write("\u0174\5_\60\2\u0173\u0172\3\2\2\2\u0174\u0177\3\2\2\2")
        buf.write("\u0175\u0173\3\2\2\2\u0175\u0176\3\2\2\2\u0176\u0178\3")
        buf.write("\2\2\2\u0177\u0175\3\2\2\2\u0178\u0179\7^\2\2\u0179\u017a")
        buf.write("\n\13\2\2\u017a\u017b\3\2\2\2\u017b\u017c\b\66\7\2\u017c")
        buf.write("\u017d\b\66\b\2\u017dl\3\2\2\2\u017e\u017f\13\2\2\2\u017f")
        buf.write("\u0180\b\67\t\2\u0180n\3\2\2\2\24\2p\u0115\u011a\u0121")
        buf.write("\u0129\u0130\u013b\u0140\u0146\u0149\u014f\u0151\u0157")
        buf.write("\u0161\u0168\u016c\u0175\n\3\2\2\b\2\2\3\63\3\3\65\4\3")
        buf.write("\65\5\3\66\6\3\66\7\3\67\b")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    NEWLINE = 1
    TYPE_NUMBER = 2
    TYPE_BOOL = 3
    TYPE_STRING = 4
    VAR = 5
    DYNAMIC = 6
    RETURN = 7
    FUNC = 8
    FOR = 9
    UNTIL = 10
    BY = 11
    BREAK = 12
    CONTINUE = 13
    IF = 14
    ELSE = 15
    ELIF = 16
    BEGIN = 17
    END = 18
    ADD_OP = 19
    SUB_OP = 20
    MUL_OP = 21
    DIV_OP = 22
    MOD_OP = 23
    NOT_OP = 24
    AND_OP = 25
    OR_OP = 26
    EQ_OP = 27
    NEQ_OP = 28
    LT_OP = 29
    LEQ_OP = 30
    GT_OP = 31
    GEQ_OP = 32
    CONCAT_OP = 33
    ASSIGN_OP = 34
    EQ = 35
    LSB = 36
    RSB = 37
    LRB = 38
    RRB = 39
    CM = 40
    COL = 41
    QUOTES = 42
    LINE_CMT = 43
    WS = 44
    BOOLLIT = 45
    NUMBERLIT = 46
    STRINGLIT = 47
    IDENTIFIER = 48
    UNCLOSE_STRING = 49
    ILLEGAL_ESCAPE = 50
    ERROR_CHAR = 51

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'number'", "'bool'", "'string'", "'var'", "'dynamic'", "'return'", 
            "'func'", "'for'", "'until'", "'by'", "'break'", "'continue'", 
            "'if'", "'else'", "'elif'", "'begin'", "'end'", "'+'", "'-'", 
            "'*'", "'/'", "'%'", "'not'", "'and'", "'or'", "'=='", "'!='", 
            "'<'", "'<='", "'>'", "'>='", "'...'", "'<-'", "'='", "'['", 
            "']'", "'('", "')'", "','", "':'", "'\"'" ]

    symbolicNames = [ "<INVALID>",
            "NEWLINE", "TYPE_NUMBER", "TYPE_BOOL", "TYPE_STRING", "VAR", 
            "DYNAMIC", "RETURN", "FUNC", "FOR", "UNTIL", "BY", "BREAK", 
            "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", "ADD_OP", 
            "SUB_OP", "MUL_OP", "DIV_OP", "MOD_OP", "NOT_OP", "AND_OP", 
            "OR_OP", "EQ_OP", "NEQ_OP", "LT_OP", "LEQ_OP", "GT_OP", "GEQ_OP", 
            "CONCAT_OP", "ASSIGN_OP", "EQ", "LSB", "RSB", "LRB", "RRB", 
            "CM", "COL", "QUOTES", "LINE_CMT", "WS", "BOOLLIT", "NUMBERLIT", 
            "STRINGLIT", "IDENTIFIER", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "ERROR_CHAR" ]

    ruleNames = [ "NEWLINE", "TYPE_NUMBER", "TYPE_BOOL", "TYPE_STRING", 
                  "VAR", "DYNAMIC", "RETURN", "FUNC", "FOR", "UNTIL", "BY", 
                  "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", 
                  "ADD_OP", "SUB_OP", "MUL_OP", "DIV_OP", "MOD_OP", "NOT_OP", 
                  "AND_OP", "OR_OP", "EQ_OP", "NEQ_OP", "LT_OP", "LEQ_OP", 
                  "GT_OP", "GEQ_OP", "CONCAT_OP", "ASSIGN_OP", "EQ", "LSB", 
                  "RSB", "LRB", "RRB", "CM", "COL", "QUOTES", "LINE_CMT", 
                  "WS", "DIGIT", "EXPONENT", "CHAR", "BOOLLIT", "NUMBERLIT", 
                  "STRINGLIT", "IDENTIFIER", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "ERROR_CHAR" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[0] = self.NEWLINE_action 
            actions[49] = self.STRINGLIT_action 
            actions[51] = self.UNCLOSE_STRING_action 
            actions[52] = self.ILLEGAL_ESCAPE_action 
            actions[53] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('\r','')
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text[1:-1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text[1:]
     

        if actionIndex == 3:
            raise UncloseString(self.text)
            		
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            self.text = self.text[1:]
     

        if actionIndex == 5:
            raise IllegalEscape(self.text)
            		
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:
            raise ErrorToken(self.text)
     


