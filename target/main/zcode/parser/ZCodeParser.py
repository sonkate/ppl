# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\65")
        buf.write("\u01b1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\3\2\5\2f\n\2\3\2\3")
        buf.write("\2\3\2\3\3\3\3\3\3\3\4\3\4\3\4\3\4\5\4r\n\4\3\5\3\5\5")
        buf.write("\5v\n\5\3\6\3\6\3\6\5\6{\n\6\3\6\3\6\3\7\3\7\5\7\u0081")
        buf.write("\n\7\3\b\3\b\3\b\3\b\5\b\u0087\n\b\3\t\3\t\3\t\3\t\3\t")
        buf.write("\5\t\u008e\n\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\5\13")
        buf.write("\u0098\n\13\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\5\16\u00a5\n\16\3\17\3\17\5\17\u00a9\n\17\3\20\3")
        buf.write("\20\3\20\3\20\3\20\3\20\5\20\u00b1\n\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\5\21\u00bb\n\21\3\21\5\21\u00be")
        buf.write("\n\21\3\21\5\21\u00c1\n\21\3\22\3\22\3\22\5\22\u00c6\n")
        buf.write("\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\5\23\u00cf\n\23")
        buf.write("\3\24\3\24\3\24\3\24\5\24\u00d5\n\24\3\25\3\25\3\25\3")
        buf.write("\25\3\25\5\25\u00dc\n\25\3\26\3\26\3\26\3\26\5\26\u00e2")
        buf.write("\n\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\5\27")
        buf.write("\u00ed\n\27\3\30\3\30\5\30\u00f1\n\30\3\30\3\30\3\30\3")
        buf.write("\30\3\31\3\31\5\31\u00f9\n\31\3\31\3\31\3\31\3\31\3\32")
        buf.write("\3\32\3\32\3\32\5\32\u0103\n\32\3\33\3\33\3\33\3\33\3")
        buf.write("\33\5\33\u010a\n\33\3\34\3\34\3\34\3\35\3\35\3\35\3\36")
        buf.write("\3\36\5\36\u0114\n\36\3\36\3\36\3\37\3\37\3\37\3\37\5")
        buf.write("\37\u011c\n\37\3\37\3\37\3\37\3 \3 \3 \3 \5 \u0125\n ")
        buf.write("\3 \3 \3!\3!\3!\3!\3!\5!\u012e\n!\3!\3!\3!\3!\5!\u0134")
        buf.write("\n!\3!\5!\u0137\n!\3\"\3\"\3\"\3\"\5\"\u013d\n\"\3#\3")
        buf.write("#\3#\3#\3#\5#\u0144\n#\3#\3#\3$\3$\3$\3$\3$\3$\3$\5$\u014f")
        buf.write("\n$\3$\3$\3%\3%\3%\3%\3%\5%\u0158\n%\3&\3&\3&\3&\3&\5")
        buf.write("&\u015f\n&\3\'\3\'\3\'\3\'\3\'\3\'\7\'\u0167\n\'\f\'\16")
        buf.write("\'\u016a\13\'\3(\3(\3(\3(\3(\3(\7(\u0172\n(\f(\16(\u0175")
        buf.write("\13(\3)\3)\3)\3)\3)\3)\7)\u017d\n)\f)\16)\u0180\13)\3")
        buf.write("*\3*\3*\5*\u0185\n*\3+\3+\3+\5+\u018a\n+\3,\3,\5,\u018e")
        buf.write("\n,\3-\3-\3-\3-\3-\3-\3-\5-\u0197\n-\3.\3.\3.\3.\3/\6")
        buf.write("/\u019e\n/\r/\16/\u019f\3\60\3\60\3\60\3\60\3\61\3\61")
        buf.write("\3\61\3\61\3\61\5\61\u01ab\n\61\3\62\3\62\5\62\u01af\n")
        buf.write("\62\3\62\2\5LNP\63\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write("\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`b\2\7\3")
        buf.write("\2\4\6\4\2\35\"%%\3\2\33\34\3\2\25\26\3\2\27\31\2\u01b9")
        buf.write("\2e\3\2\2\2\4j\3\2\2\2\6q\3\2\2\2\bu\3\2\2\2\nz\3\2\2")
        buf.write("\2\f\u0080\3\2\2\2\16\u0082\3\2\2\2\20\u0088\3\2\2\2\22")
        buf.write("\u008f\3\2\2\2\24\u0097\3\2\2\2\26\u0099\3\2\2\2\30\u009b")
        buf.write("\3\2\2\2\32\u00a0\3\2\2\2\34\u00a8\3\2\2\2\36\u00aa\3")
        buf.write("\2\2\2 \u00b4\3\2\2\2\"\u00c2\3\2\2\2$\u00ce\3\2\2\2&")
        buf.write("\u00d4\3\2\2\2(\u00db\3\2\2\2*\u00dd\3\2\2\2,\u00ec\3")
        buf.write("\2\2\2.\u00f0\3\2\2\2\60\u00f8\3\2\2\2\62\u0102\3\2\2")
        buf.write("\2\64\u0109\3\2\2\2\66\u010b\3\2\2\28\u010e\3\2\2\2:\u0111")
        buf.write("\3\2\2\2<\u0117\3\2\2\2>\u0120\3\2\2\2@\u0128\3\2\2\2")
        buf.write("B\u013c\3\2\2\2D\u013e\3\2\2\2F\u0147\3\2\2\2H\u0157\3")
        buf.write("\2\2\2J\u015e\3\2\2\2L\u0160\3\2\2\2N\u016b\3\2\2\2P\u0176")
        buf.write("\3\2\2\2R\u0184\3\2\2\2T\u0189\3\2\2\2V\u018d\3\2\2\2")
        buf.write("X\u0196\3\2\2\2Z\u0198\3\2\2\2\\\u019d\3\2\2\2^\u01a1")
        buf.write("\3\2\2\2`\u01aa\3\2\2\2b\u01ae\3\2\2\2df\5\\/\2ed\3\2")
        buf.write("\2\2ef\3\2\2\2fg\3\2\2\2gh\5\4\3\2hi\7\2\2\3i\3\3\2\2")
        buf.write("\2jk\5\b\5\2kl\5\6\4\2l\5\3\2\2\2mn\5\b\5\2no\5\6\4\2")
        buf.write("or\3\2\2\2pr\3\2\2\2qm\3\2\2\2qp\3\2\2\2r\7\3\2\2\2sv")
        buf.write("\5\n\6\2tv\5\34\17\2us\3\2\2\2ut\3\2\2\2v\t\3\2\2\2w{")
        buf.write("\5\f\7\2x{\5\30\r\2y{\5\32\16\2zw\3\2\2\2zx\3\2\2\2zy")
        buf.write("\3\2\2\2{|\3\2\2\2|}\5\\/\2}\13\3\2\2\2~\u0081\5\16\b")
        buf.write("\2\177\u0081\5\20\t\2\u0080~\3\2\2\2\u0080\177\3\2\2\2")
        buf.write("\u0081\r\3\2\2\2\u0082\u0083\5\26\f\2\u0083\u0086\7\62")
        buf.write("\2\2\u0084\u0085\7$\2\2\u0085\u0087\5H%\2\u0086\u0084")
        buf.write("\3\2\2\2\u0086\u0087\3\2\2\2\u0087\17\3\2\2\2\u0088\u0089")
        buf.write("\5\26\f\2\u0089\u008a\7\62\2\2\u008a\u008d\5\22\n\2\u008b")
        buf.write("\u008c\7$\2\2\u008c\u008e\5H%\2\u008d\u008b\3\2\2\2\u008d")
        buf.write("\u008e\3\2\2\2\u008e\21\3\2\2\2\u008f\u0090\7&\2\2\u0090")
        buf.write("\u0091\5\24\13\2\u0091\u0092\7\'\2\2\u0092\23\3\2\2\2")
        buf.write("\u0093\u0094\7\60\2\2\u0094\u0095\7*\2\2\u0095\u0098\5")
        buf.write("\24\13\2\u0096\u0098\7\60\2\2\u0097\u0093\3\2\2\2\u0097")
        buf.write("\u0096\3\2\2\2\u0098\25\3\2\2\2\u0099\u009a\t\2\2\2\u009a")
        buf.write("\27\3\2\2\2\u009b\u009c\7\7\2\2\u009c\u009d\7\62\2\2\u009d")
        buf.write("\u009e\7$\2\2\u009e\u009f\5H%\2\u009f\31\3\2\2\2\u00a0")
        buf.write("\u00a1\7\b\2\2\u00a1\u00a4\7\62\2\2\u00a2\u00a3\7$\2\2")
        buf.write("\u00a3\u00a5\5H%\2\u00a4\u00a2\3\2\2\2\u00a4\u00a5\3\2")
        buf.write("\2\2\u00a5\33\3\2\2\2\u00a6\u00a9\5 \21\2\u00a7\u00a9")
        buf.write("\5\36\20\2\u00a8\u00a6\3\2\2\2\u00a8\u00a7\3\2\2\2\u00a9")
        buf.write("\35\3\2\2\2\u00aa\u00ab\7\n\2\2\u00ab\u00ac\7\62\2\2\u00ac")
        buf.write("\u00ad\7(\2\2\u00ad\u00ae\5&\24\2\u00ae\u00b0\7)\2\2\u00af")
        buf.write("\u00b1\5\\/\2\u00b0\u00af\3\2\2\2\u00b0\u00b1\3\2\2\2")
        buf.write("\u00b1\u00b2\3\2\2\2\u00b2\u00b3\5\"\22\2\u00b3\37\3\2")
        buf.write("\2\2\u00b4\u00b5\7\n\2\2\u00b5\u00b6\7\62\2\2\u00b6\u00b7")
        buf.write("\7(\2\2\u00b7\u00b8\5&\24\2\u00b8\u00ba\7)\2\2\u00b9\u00bb")
        buf.write("\5\\/\2\u00ba\u00b9\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb")
        buf.write("\u00c0\3\2\2\2\u00bc\u00be\5:\36\2\u00bd\u00bc\3\2\2\2")
        buf.write("\u00bd\u00be\3\2\2\2\u00be\u00c1\3\2\2\2\u00bf\u00c1\5")
        buf.write("\\/\2\u00c0\u00bd\3\2\2\2\u00c0\u00bf\3\2\2\2\u00c1!\3")
        buf.write("\2\2\2\u00c2\u00c3\7\23\2\2\u00c3\u00c5\5\\/\2\u00c4\u00c6")
        buf.write("\5$\23\2\u00c5\u00c4\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6")
        buf.write("\u00c7\3\2\2\2\u00c7\u00c8\7\24\2\2\u00c8\u00c9\5\\/\2")
        buf.write("\u00c9#\3\2\2\2\u00ca\u00cb\5,\27\2\u00cb\u00cc\5$\23")
        buf.write("\2\u00cc\u00cf\3\2\2\2\u00cd\u00cf\5,\27\2\u00ce\u00ca")
        buf.write("\3\2\2\2\u00ce\u00cd\3\2\2\2\u00cf%\3\2\2\2\u00d0\u00d1")
        buf.write("\5*\26\2\u00d1\u00d2\5(\25\2\u00d2\u00d5\3\2\2\2\u00d3")
        buf.write("\u00d5\3\2\2\2\u00d4\u00d0\3\2\2\2\u00d4\u00d3\3\2\2\2")
        buf.write("\u00d5\'\3\2\2\2\u00d6\u00d7\7*\2\2\u00d7\u00d8\5*\26")
        buf.write("\2\u00d8\u00d9\5(\25\2\u00d9\u00dc\3\2\2\2\u00da\u00dc")
        buf.write("\3\2\2\2\u00db\u00d6\3\2\2\2\u00db\u00da\3\2\2\2\u00dc")
        buf.write(")\3\2\2\2\u00dd\u00de\5\26\f\2\u00de\u00e1\7\62\2\2\u00df")
        buf.write("\u00e2\5\22\n\2\u00e0\u00e2\3\2\2\2\u00e1\u00df\3\2\2")
        buf.write("\2\u00e1\u00e0\3\2\2\2\u00e2+\3\2\2\2\u00e3\u00ed\5\n")
        buf.write("\6\2\u00e4\u00ed\5.\30\2\u00e5\u00ed\5@!\2\u00e6\u00ed")
        buf.write("\5F$\2\u00e7\u00ed\5\66\34\2\u00e8\u00ed\58\35\2\u00e9")
        buf.write("\u00ed\5:\36\2\u00ea\u00ed\5<\37\2\u00eb\u00ed\5\"\22")
        buf.write("\2\u00ec\u00e3\3\2\2\2\u00ec\u00e4\3\2\2\2\u00ec\u00e5")
        buf.write("\3\2\2\2\u00ec\u00e6\3\2\2\2\u00ec\u00e7\3\2\2\2\u00ec")
        buf.write("\u00e8\3\2\2\2\u00ec\u00e9\3\2\2\2\u00ec\u00ea\3\2\2\2")
        buf.write("\u00ec\u00eb\3\2\2\2\u00ed-\3\2\2\2\u00ee\u00f1\7\62\2")
        buf.write("\2\u00ef\u00f1\5\60\31\2\u00f0\u00ee\3\2\2\2\u00f0\u00ef")
        buf.write("\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2\u00f3\7$\2\2\u00f3")
        buf.write("\u00f4\5H%\2\u00f4\u00f5\5\\/\2\u00f5/\3\2\2\2\u00f6\u00f9")
        buf.write("\7\62\2\2\u00f7\u00f9\5> \2\u00f8\u00f6\3\2\2\2\u00f8")
        buf.write("\u00f7\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa\u00fb\7&\2\2")
        buf.write("\u00fb\u00fc\5\62\32\2\u00fc\u00fd\7\'\2\2\u00fd\61\3")
        buf.write("\2\2\2\u00fe\u00ff\5H%\2\u00ff\u0100\5\64\33\2\u0100\u0103")
        buf.write("\3\2\2\2\u0101\u0103\5H%\2\u0102\u00fe\3\2\2\2\u0102\u0101")
        buf.write("\3\2\2\2\u0103\63\3\2\2\2\u0104\u0105\7*\2\2\u0105\u0106")
        buf.write("\5H%\2\u0106\u0107\5\64\33\2\u0107\u010a\3\2\2\2\u0108")
        buf.write("\u010a\3\2\2\2\u0109\u0104\3\2\2\2\u0109\u0108\3\2\2\2")
        buf.write("\u010a\65\3\2\2\2\u010b\u010c\7\16\2\2\u010c\u010d\5\\")
        buf.write("/\2\u010d\67\3\2\2\2\u010e\u010f\7\17\2\2\u010f\u0110")
        buf.write("\5\\/\2\u01109\3\2\2\2\u0111\u0113\7\t\2\2\u0112\u0114")
        buf.write("\5H%\2\u0113\u0112\3\2\2\2\u0113\u0114\3\2\2\2\u0114\u0115")
        buf.write("\3\2\2\2\u0115\u0116\5\\/\2\u0116;\3\2\2\2\u0117\u0118")
        buf.write("\7\62\2\2\u0118\u011b\7(\2\2\u0119\u011c\5\62\32\2\u011a")
        buf.write("\u011c\3\2\2\2\u011b\u0119\3\2\2\2\u011b\u011a\3\2\2\2")
        buf.write("\u011c\u011d\3\2\2\2\u011d\u011e\7)\2\2\u011e\u011f\5")
        buf.write("\\/\2\u011f=\3\2\2\2\u0120\u0121\7\62\2\2\u0121\u0124")
        buf.write("\7(\2\2\u0122\u0125\5\62\32\2\u0123\u0125\3\2\2\2\u0124")
        buf.write("\u0122\3\2\2\2\u0124\u0123\3\2\2\2\u0125\u0126\3\2\2\2")
        buf.write("\u0126\u0127\7)\2\2\u0127?\3\2\2\2\u0128\u0129\7\20\2")
        buf.write("\2\u0129\u012a\7(\2\2\u012a\u012b\5H%\2\u012b\u012d\7")
        buf.write(")\2\2\u012c\u012e\5\\/\2\u012d\u012c\3\2\2\2\u012d\u012e")
        buf.write("\3\2\2\2\u012e\u012f\3\2\2\2\u012f\u0130\5,\27\2\u0130")
        buf.write("\u0136\5B\"\2\u0131\u0133\7\21\2\2\u0132\u0134\5\\/\2")
        buf.write("\u0133\u0132\3\2\2\2\u0133\u0134\3\2\2\2\u0134\u0135\3")
        buf.write("\2\2\2\u0135\u0137\5,\27\2\u0136\u0131\3\2\2\2\u0136\u0137")
        buf.write("\3\2\2\2\u0137A\3\2\2\2\u0138\u0139\5D#\2\u0139\u013a")
        buf.write("\5B\"\2\u013a\u013d\3\2\2\2\u013b\u013d\3\2\2\2\u013c")
        buf.write("\u0138\3\2\2\2\u013c\u013b\3\2\2\2\u013dC\3\2\2\2\u013e")
        buf.write("\u013f\7\22\2\2\u013f\u0140\7(\2\2\u0140\u0141\5H%\2\u0141")
        buf.write("\u0143\7)\2\2\u0142\u0144\5\\/\2\u0143\u0142\3\2\2\2\u0143")
        buf.write("\u0144\3\2\2\2\u0144\u0145\3\2\2\2\u0145\u0146\5,\27\2")
        buf.write("\u0146E\3\2\2\2\u0147\u0148\7\13\2\2\u0148\u0149\7\62")
        buf.write("\2\2\u0149\u014a\7\f\2\2\u014a\u014b\5H%\2\u014b\u014c")
        buf.write("\7\r\2\2\u014c\u014e\5H%\2\u014d\u014f\5\\/\2\u014e\u014d")
        buf.write("\3\2\2\2\u014e\u014f\3\2\2\2\u014f\u0150\3\2\2\2\u0150")
        buf.write("\u0151\5,\27\2\u0151G\3\2\2\2\u0152\u0153\5J&\2\u0153")
        buf.write("\u0154\7#\2\2\u0154\u0155\5J&\2\u0155\u0158\3\2\2\2\u0156")
        buf.write("\u0158\5J&\2\u0157\u0152\3\2\2\2\u0157\u0156\3\2\2\2\u0158")
        buf.write("I\3\2\2\2\u0159\u015a\5L\'\2\u015a\u015b\t\3\2\2\u015b")
        buf.write("\u015c\5L\'\2\u015c\u015f\3\2\2\2\u015d\u015f\5L\'\2\u015e")
        buf.write("\u0159\3\2\2\2\u015e\u015d\3\2\2\2\u015fK\3\2\2\2\u0160")
        buf.write("\u0161\b\'\1\2\u0161\u0162\5N(\2\u0162\u0168\3\2\2\2\u0163")
        buf.write("\u0164\f\4\2\2\u0164\u0165\t\4\2\2\u0165\u0167\5N(\2\u0166")
        buf.write("\u0163\3\2\2\2\u0167\u016a\3\2\2\2\u0168\u0166\3\2\2\2")
        buf.write("\u0168\u0169\3\2\2\2\u0169M\3\2\2\2\u016a\u0168\3\2\2")
        buf.write("\2\u016b\u016c\b(\1\2\u016c\u016d\5P)\2\u016d\u0173\3")
        buf.write("\2\2\2\u016e\u016f\f\4\2\2\u016f\u0170\t\5\2\2\u0170\u0172")
        buf.write("\5P)\2\u0171\u016e\3\2\2\2\u0172\u0175\3\2\2\2\u0173\u0171")
        buf.write("\3\2\2\2\u0173\u0174\3\2\2\2\u0174O\3\2\2\2\u0175\u0173")
        buf.write("\3\2\2\2\u0176\u0177\b)\1\2\u0177\u0178\5R*\2\u0178\u017e")
        buf.write("\3\2\2\2\u0179\u017a\f\4\2\2\u017a\u017b\t\6\2\2\u017b")
        buf.write("\u017d\5R*\2\u017c\u0179\3\2\2\2\u017d\u0180\3\2\2\2\u017e")
        buf.write("\u017c\3\2\2\2\u017e\u017f\3\2\2\2\u017fQ\3\2\2\2\u0180")
        buf.write("\u017e\3\2\2\2\u0181\u0182\7\32\2\2\u0182\u0185\5R*\2")
        buf.write("\u0183\u0185\5T+\2\u0184\u0181\3\2\2\2\u0184\u0183\3\2")
        buf.write("\2\2\u0185S\3\2\2\2\u0186\u0187\7\26\2\2\u0187\u018a\5")
        buf.write("T+\2\u0188\u018a\5V,\2\u0189\u0186\3\2\2\2\u0189\u0188")
        buf.write("\3\2\2\2\u018aU\3\2\2\2\u018b\u018e\5\60\31\2\u018c\u018e")
        buf.write("\5X-\2\u018d\u018b\3\2\2\2\u018d\u018c\3\2\2\2\u018eW")
        buf.write("\3\2\2\2\u018f\u0197\7\60\2\2\u0190\u0197\7/\2\2\u0191")
        buf.write("\u0197\7\61\2\2\u0192\u0197\7\62\2\2\u0193\u0197\5^\60")
        buf.write("\2\u0194\u0197\5> \2\u0195\u0197\5Z.\2\u0196\u018f\3\2")
        buf.write("\2\2\u0196\u0190\3\2\2\2\u0196\u0191\3\2\2\2\u0196\u0192")
        buf.write("\3\2\2\2\u0196\u0193\3\2\2\2\u0196\u0194\3\2\2\2\u0196")
        buf.write("\u0195\3\2\2\2\u0197Y\3\2\2\2\u0198\u0199\7(\2\2\u0199")
        buf.write("\u019a\5H%\2\u019a\u019b\7)\2\2\u019b[\3\2\2\2\u019c\u019e")
        buf.write("\7\3\2\2\u019d\u019c\3\2\2\2\u019e\u019f\3\2\2\2\u019f")
        buf.write("\u019d\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0]\3\2\2\2\u01a1")
        buf.write("\u01a2\7&\2\2\u01a2\u01a3\5`\61\2\u01a3\u01a4\7\'\2\2")
        buf.write("\u01a4_\3\2\2\2\u01a5\u01a6\5b\62\2\u01a6\u01a7\7*\2\2")
        buf.write("\u01a7\u01a8\5`\61\2\u01a8\u01ab\3\2\2\2\u01a9\u01ab\5")
        buf.write("b\62\2\u01aa\u01a5\3\2\2\2\u01aa\u01a9\3\2\2\2\u01aba")
        buf.write("\3\2\2\2\u01ac\u01af\5^\60\2\u01ad\u01af\5H%\2\u01ae\u01ac")
        buf.write("\3\2\2\2\u01ae\u01ad\3\2\2\2\u01afc\3\2\2\2/equz\u0080")
        buf.write("\u0086\u008d\u0097\u00a4\u00a8\u00b0\u00ba\u00bd\u00c0")
        buf.write("\u00c5\u00ce\u00d4\u00db\u00e1\u00ec\u00f0\u00f8\u0102")
        buf.write("\u0109\u0113\u011b\u0124\u012d\u0133\u0136\u013c\u0143")
        buf.write("\u014e\u0157\u015e\u0168\u0173\u017e\u0184\u0189\u018d")
        buf.write("\u0196\u019f\u01aa\u01ae")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'number'", "'bool'", "'string'", 
                     "'var'", "'dynamic'", "'return'", "'func'", "'for'", 
                     "'until'", "'by'", "'break'", "'continue'", "'if'", 
                     "'else'", "'elif'", "'begin'", "'end'", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'not'", "'and'", "'or'", "'=='", 
                     "'!='", "'<'", "'<='", "'>'", "'>='", "'...'", "'<-'", 
                     "'='", "'['", "']'", "'('", "')'", "','", "':'", "'\"'" ]

    symbolicNames = [ "<INVALID>", "NEWLINE", "TYPE_NUMBER", "TYPE_BOOL", 
                      "TYPE_STRING", "VAR", "DYNAMIC", "RETURN", "FUNC", 
                      "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", "IF", "ELSE", 
                      "ELIF", "BEGIN", "END", "ADD_OP", "SUB_OP", "MUL_OP", 
                      "DIV_OP", "MOD_OP", "NOT_OP", "AND_OP", "OR_OP", "EQ_OP", 
                      "NEQ_OP", "LT_OP", "LEQ_OP", "GT_OP", "GEQ_OP", "CONCAT_OP", 
                      "ASSIGN_OP", "EQ", "LSB", "RSB", "LRB", "RRB", "CM", 
                      "COL", "QUOTES", "LINE_CMT", "WS", "BOOLLIT", "NUMBERLIT", 
                      "STRINGLIT", "IDENTIFIER", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decls = 1
    RULE_decls_tail = 2
    RULE_decl = 3
    RULE_var_decl = 4
    RULE_keyword_var = 5
    RULE_keyword_var_decl = 6
    RULE_keyword_var_array_decl = 7
    RULE_arraydim = 8
    RULE_listdim = 9
    RULE_type_vardecl = 10
    RULE_implicit_var = 11
    RULE_implicit_dynamic = 12
    RULE_func_decl = 13
    RULE_func_decl_complete = 14
    RULE_func_decl_prototype = 15
    RULE_body = 16
    RULE_body_one = 17
    RULE_param_decls = 18
    RULE_param_decl_tail = 19
    RULE_param_decl = 20
    RULE_statement = 21
    RULE_assign_stmt = 22
    RULE_array_index_expr = 23
    RULE_list_expr = 24
    RULE_expr_tail = 25
    RULE_break_stmt = 26
    RULE_continue_stmt = 27
    RULE_return_stmt = 28
    RULE_func_call_stmt = 29
    RULE_func_call = 30
    RULE_if_stmt = 31
    RULE_list_elif = 32
    RULE_elif_one = 33
    RULE_for_stmt = 34
    RULE_expr = 35
    RULE_expr1 = 36
    RULE_expr2 = 37
    RULE_expr3 = 38
    RULE_expr4 = 39
    RULE_expr5 = 40
    RULE_expr6 = 41
    RULE_expr7 = 42
    RULE_factor = 43
    RULE_sub_expr = 44
    RULE_list_newline = 45
    RULE_arraylit = 46
    RULE_itemlist = 47
    RULE_item = 48

    ruleNames =  [ "program", "decls", "decls_tail", "decl", "var_decl", 
                   "keyword_var", "keyword_var_decl", "keyword_var_array_decl", 
                   "arraydim", "listdim", "type_vardecl", "implicit_var", 
                   "implicit_dynamic", "func_decl", "func_decl_complete", 
                   "func_decl_prototype", "body", "body_one", "param_decls", 
                   "param_decl_tail", "param_decl", "statement", "assign_stmt", 
                   "array_index_expr", "list_expr", "expr_tail", "break_stmt", 
                   "continue_stmt", "return_stmt", "func_call_stmt", "func_call", 
                   "if_stmt", "list_elif", "elif_one", "for_stmt", "expr", 
                   "expr1", "expr2", "expr3", "expr4", "expr5", "expr6", 
                   "expr7", "factor", "sub_expr", "list_newline", "arraylit", 
                   "itemlist", "item" ]

    EOF = Token.EOF
    NEWLINE=1
    TYPE_NUMBER=2
    TYPE_BOOL=3
    TYPE_STRING=4
    VAR=5
    DYNAMIC=6
    RETURN=7
    FUNC=8
    FOR=9
    UNTIL=10
    BY=11
    BREAK=12
    CONTINUE=13
    IF=14
    ELSE=15
    ELIF=16
    BEGIN=17
    END=18
    ADD_OP=19
    SUB_OP=20
    MUL_OP=21
    DIV_OP=22
    MOD_OP=23
    NOT_OP=24
    AND_OP=25
    OR_OP=26
    EQ_OP=27
    NEQ_OP=28
    LT_OP=29
    LEQ_OP=30
    GT_OP=31
    GEQ_OP=32
    CONCAT_OP=33
    ASSIGN_OP=34
    EQ=35
    LSB=36
    RSB=37
    LRB=38
    RRB=39
    CM=40
    COL=41
    QUOTES=42
    LINE_CMT=43
    WS=44
    BOOLLIT=45
    NUMBERLIT=46
    STRINGLIT=47
    IDENTIFIER=48
    UNCLOSE_STRING=49
    ILLEGAL_ESCAPE=50
    ERROR_CHAR=51

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decls(self):
            return self.getTypedRuleContext(ZCodeParser.DeclsContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def list_newline(self):
            return self.getTypedRuleContext(ZCodeParser.List_newlineContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 98
                self.list_newline()


            self.state = 101
            self.decls()
            self.state = 102
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(ZCodeParser.DeclContext,0)


        def decls_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Decls_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decls

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecls" ):
                return visitor.visitDecls(self)
            else:
                return visitor.visitChildren(self)




    def decls(self):

        localctx = ZCodeParser.DeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decls)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.decl()
            self.state = 105
            self.decls_tail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decls_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(ZCodeParser.DeclContext,0)


        def decls_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Decls_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decls_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecls_tail" ):
                return visitor.visitDecls_tail(self)
            else:
                return visitor.visitChildren(self)




    def decls_tail(self):

        localctx = ZCodeParser.Decls_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decls_tail)
        try:
            self.state = 111
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.TYPE_NUMBER, ZCodeParser.TYPE_BOOL, ZCodeParser.TYPE_STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 107
                self.decl()
                self.state = 108
                self.decls_tail()
                pass
            elif token in [ZCodeParser.EOF]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Var_declContext,0)


        def func_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Func_declContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = ZCodeParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.TYPE_NUMBER, ZCodeParser.TYPE_BOOL, ZCodeParser.TYPE_STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.state = 113
                self.var_decl()
                pass
            elif token in [ZCodeParser.FUNC]:
                self.state = 114
                self.func_decl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_newline(self):
            return self.getTypedRuleContext(ZCodeParser.List_newlineContext,0)


        def keyword_var(self):
            return self.getTypedRuleContext(ZCodeParser.Keyword_varContext,0)


        def implicit_var(self):
            return self.getTypedRuleContext(ZCodeParser.Implicit_varContext,0)


        def implicit_dynamic(self):
            return self.getTypedRuleContext(ZCodeParser.Implicit_dynamicContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = ZCodeParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.TYPE_NUMBER, ZCodeParser.TYPE_BOOL, ZCodeParser.TYPE_STRING]:
                self.state = 117
                self.keyword_var()
                pass
            elif token in [ZCodeParser.VAR]:
                self.state = 118
                self.implicit_var()
                pass
            elif token in [ZCodeParser.DYNAMIC]:
                self.state = 119
                self.implicit_dynamic()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 122
            self.list_newline()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Keyword_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def keyword_var_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Keyword_var_declContext,0)


        def keyword_var_array_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Keyword_var_array_declContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_keyword_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKeyword_var" ):
                return visitor.visitKeyword_var(self)
            else:
                return visitor.visitChildren(self)




    def keyword_var(self):

        localctx = ZCodeParser.Keyword_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_keyword_var)
        try:
            self.state = 126
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.keyword_var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.keyword_var_array_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Keyword_var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_vardecl(self):
            return self.getTypedRuleContext(ZCodeParser.Type_vardeclContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def ASSIGN_OP(self):
            return self.getToken(ZCodeParser.ASSIGN_OP, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_keyword_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKeyword_var_decl" ):
                return visitor.visitKeyword_var_decl(self)
            else:
                return visitor.visitChildren(self)




    def keyword_var_decl(self):

        localctx = ZCodeParser.Keyword_var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_keyword_var_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.type_vardecl()
            self.state = 129
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN_OP:
                self.state = 130
                self.match(ZCodeParser.ASSIGN_OP)
                self.state = 131
                self.expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Keyword_var_array_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_vardecl(self):
            return self.getTypedRuleContext(ZCodeParser.Type_vardeclContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def arraydim(self):
            return self.getTypedRuleContext(ZCodeParser.ArraydimContext,0)


        def ASSIGN_OP(self):
            return self.getToken(ZCodeParser.ASSIGN_OP, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_keyword_var_array_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKeyword_var_array_decl" ):
                return visitor.visitKeyword_var_array_decl(self)
            else:
                return visitor.visitChildren(self)




    def keyword_var_array_decl(self):

        localctx = ZCodeParser.Keyword_var_array_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_keyword_var_array_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.type_vardecl()
            self.state = 135
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 136
            self.arraydim()
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN_OP:
                self.state = 137
                self.match(ZCodeParser.ASSIGN_OP)
                self.state = 138
                self.expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraydimContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def listdim(self):
            return self.getTypedRuleContext(ZCodeParser.ListdimContext,0)


        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arraydim

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraydim" ):
                return visitor.visitArraydim(self)
            else:
                return visitor.visitChildren(self)




    def arraydim(self):

        localctx = ZCodeParser.ArraydimContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_arraydim)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(ZCodeParser.LSB)
            self.state = 142
            self.listdim()
            self.state = 143
            self.match(ZCodeParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListdimContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBERLIT(self):
            return self.getToken(ZCodeParser.NUMBERLIT, 0)

        def CM(self):
            return self.getToken(ZCodeParser.CM, 0)

        def listdim(self):
            return self.getTypedRuleContext(ZCodeParser.ListdimContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_listdim

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListdim" ):
                return visitor.visitListdim(self)
            else:
                return visitor.visitChildren(self)




    def listdim(self):

        localctx = ZCodeParser.ListdimContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_listdim)
        try:
            self.state = 149
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.match(ZCodeParser.NUMBERLIT)
                self.state = 146
                self.match(ZCodeParser.CM)
                self.state = 147
                self.listdim()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 148
                self.match(ZCodeParser.NUMBERLIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_vardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE_NUMBER(self):
            return self.getToken(ZCodeParser.TYPE_NUMBER, 0)

        def TYPE_BOOL(self):
            return self.getToken(ZCodeParser.TYPE_BOOL, 0)

        def TYPE_STRING(self):
            return self.getToken(ZCodeParser.TYPE_STRING, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_type_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_vardecl" ):
                return visitor.visitType_vardecl(self)
            else:
                return visitor.visitChildren(self)




    def type_vardecl(self):

        localctx = ZCodeParser.Type_vardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_type_vardecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TYPE_NUMBER) | (1 << ZCodeParser.TYPE_BOOL) | (1 << ZCodeParser.TYPE_STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Implicit_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def ASSIGN_OP(self):
            return self.getToken(ZCodeParser.ASSIGN_OP, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_implicit_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplicit_var" ):
                return visitor.visitImplicit_var(self)
            else:
                return visitor.visitChildren(self)




    def implicit_var(self):

        localctx = ZCodeParser.Implicit_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_implicit_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(ZCodeParser.VAR)
            self.state = 154
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 155
            self.match(ZCodeParser.ASSIGN_OP)
            self.state = 156
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Implicit_dynamicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def ASSIGN_OP(self):
            return self.getToken(ZCodeParser.ASSIGN_OP, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_implicit_dynamic

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplicit_dynamic" ):
                return visitor.visitImplicit_dynamic(self)
            else:
                return visitor.visitChildren(self)




    def implicit_dynamic(self):

        localctx = ZCodeParser.Implicit_dynamicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_implicit_dynamic)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(ZCodeParser.DYNAMIC)
            self.state = 159
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN_OP:
                self.state = 160
                self.match(ZCodeParser.ASSIGN_OP)
                self.state = 161
                self.expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_decl_prototype(self):
            return self.getTypedRuleContext(ZCodeParser.Func_decl_prototypeContext,0)


        def func_decl_complete(self):
            return self.getTypedRuleContext(ZCodeParser.Func_decl_completeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_func_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl" ):
                return visitor.visitFunc_decl(self)
            else:
                return visitor.visitChildren(self)




    def func_decl(self):

        localctx = ZCodeParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_func_decl)
        try:
            self.state = 166
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 164
                self.func_decl_prototype()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 165
                self.func_decl_complete()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_decl_completeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LRB(self):
            return self.getToken(ZCodeParser.LRB, 0)

        def param_decls(self):
            return self.getTypedRuleContext(ZCodeParser.Param_declsContext,0)


        def RRB(self):
            return self.getToken(ZCodeParser.RRB, 0)

        def body(self):
            return self.getTypedRuleContext(ZCodeParser.BodyContext,0)


        def list_newline(self):
            return self.getTypedRuleContext(ZCodeParser.List_newlineContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_func_decl_complete

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl_complete" ):
                return visitor.visitFunc_decl_complete(self)
            else:
                return visitor.visitChildren(self)




    def func_decl_complete(self):

        localctx = ZCodeParser.Func_decl_completeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_func_decl_complete)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(ZCodeParser.FUNC)
            self.state = 169
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 170
            self.match(ZCodeParser.LRB)
            self.state = 171
            self.param_decls()
            self.state = 172
            self.match(ZCodeParser.RRB)
            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 173
                self.list_newline()


            self.state = 176
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_decl_prototypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LRB(self):
            return self.getToken(ZCodeParser.LRB, 0)

        def param_decls(self):
            return self.getTypedRuleContext(ZCodeParser.Param_declsContext,0)


        def RRB(self):
            return self.getToken(ZCodeParser.RRB, 0)

        def list_newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.List_newlineContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.List_newlineContext,i)


        def return_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Return_stmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_func_decl_prototype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl_prototype" ):
                return visitor.visitFunc_decl_prototype(self)
            else:
                return visitor.visitChildren(self)




    def func_decl_prototype(self):

        localctx = ZCodeParser.Func_decl_prototypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_func_decl_prototype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(ZCodeParser.FUNC)
            self.state = 179
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 180
            self.match(ZCodeParser.LRB)
            self.state = 181
            self.param_decls()
            self.state = 182
            self.match(ZCodeParser.RRB)
            self.state = 184
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 183
                self.list_newline()


            self.state = 190
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.EOF, ZCodeParser.TYPE_NUMBER, ZCodeParser.TYPE_BOOL, ZCodeParser.TYPE_STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.RETURN, ZCodeParser.FUNC]:
                self.state = 187
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.RETURN:
                    self.state = 186
                    self.return_stmt()


                pass
            elif token in [ZCodeParser.NEWLINE]:
                self.state = 189
                self.list_newline()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def list_newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.List_newlineContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.List_newlineContext,i)


        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def body_one(self):
            return self.getTypedRuleContext(ZCodeParser.Body_oneContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = ZCodeParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.match(ZCodeParser.BEGIN)
            self.state = 193
            self.list_newline()
            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TYPE_NUMBER) | (1 << ZCodeParser.TYPE_BOOL) | (1 << ZCodeParser.TYPE_STRING) | (1 << ZCodeParser.VAR) | (1 << ZCodeParser.DYNAMIC) | (1 << ZCodeParser.RETURN) | (1 << ZCodeParser.FOR) | (1 << ZCodeParser.BREAK) | (1 << ZCodeParser.CONTINUE) | (1 << ZCodeParser.IF) | (1 << ZCodeParser.BEGIN) | (1 << ZCodeParser.IDENTIFIER))) != 0):
                self.state = 194
                self.body_one()


            self.state = 197
            self.match(ZCodeParser.END)
            self.state = 198
            self.list_newline()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Body_oneContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def body_one(self):
            return self.getTypedRuleContext(ZCodeParser.Body_oneContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_body_one

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody_one" ):
                return visitor.visitBody_one(self)
            else:
                return visitor.visitChildren(self)




    def body_one(self):

        localctx = ZCodeParser.Body_oneContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_body_one)
        try:
            self.state = 204
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.statement()
                self.state = 201
                self.body_one()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 203
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_declsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Param_declContext,0)


        def param_decl_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Param_decl_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_param_decls

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_decls" ):
                return visitor.visitParam_decls(self)
            else:
                return visitor.visitChildren(self)




    def param_decls(self):

        localctx = ZCodeParser.Param_declsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_param_decls)
        try:
            self.state = 210
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.TYPE_NUMBER, ZCodeParser.TYPE_BOOL, ZCodeParser.TYPE_STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 206
                self.param_decl()
                self.state = 207
                self.param_decl_tail()
                pass
            elif token in [ZCodeParser.RRB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_decl_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(ZCodeParser.CM, 0)

        def param_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Param_declContext,0)


        def param_decl_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Param_decl_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_param_decl_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_decl_tail" ):
                return visitor.visitParam_decl_tail(self)
            else:
                return visitor.visitChildren(self)




    def param_decl_tail(self):

        localctx = ZCodeParser.Param_decl_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_param_decl_tail)
        try:
            self.state = 217
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 212
                self.match(ZCodeParser.CM)
                self.state = 213
                self.param_decl()
                self.state = 214
                self.param_decl_tail()
                pass
            elif token in [ZCodeParser.RRB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_vardecl(self):
            return self.getTypedRuleContext(ZCodeParser.Type_vardeclContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def arraydim(self):
            return self.getTypedRuleContext(ZCodeParser.ArraydimContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_param_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_decl" ):
                return visitor.visitParam_decl(self)
            else:
                return visitor.visitChildren(self)




    def param_decl(self):

        localctx = ZCodeParser.Param_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_param_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.type_vardecl()
            self.state = 220
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 223
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.LSB]:
                self.state = 221
                self.arraydim()
                pass
            elif token in [ZCodeParser.RRB, ZCodeParser.CM]:
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Var_declContext,0)


        def assign_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Assign_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.For_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Continue_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Return_stmtContext,0)


        def func_call_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Func_call_stmtContext,0)


        def body(self):
            return self.getTypedRuleContext(ZCodeParser.BodyContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ZCodeParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_statement)
        try:
            self.state = 234
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self.assign_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 227
                self.if_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 228
                self.for_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 229
                self.break_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 230
                self.continue_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 231
                self.return_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 232
                self.func_call_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 233
                self.body()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN_OP(self):
            return self.getToken(ZCodeParser.ASSIGN_OP, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def list_newline(self):
            return self.getTypedRuleContext(ZCodeParser.List_newlineContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def array_index_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Array_index_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = ZCodeParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 236
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 237
                self.array_index_expr()
                pass


            self.state = 240
            self.match(ZCodeParser.ASSIGN_OP)
            self.state = 241
            self.expr()
            self.state = 242
            self.list_newline()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_index_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def list_expr(self):
            return self.getTypedRuleContext(ZCodeParser.List_exprContext,0)


        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Func_callContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_index_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_index_expr" ):
                return visitor.visitArray_index_expr(self)
            else:
                return visitor.visitChildren(self)




    def array_index_expr(self):

        localctx = ZCodeParser.Array_index_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_array_index_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 244
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 245
                self.func_call()
                pass


            self.state = 248
            self.match(ZCodeParser.LSB)
            self.state = 249
            self.list_expr()
            self.state = 250
            self.match(ZCodeParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def expr_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_list_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_expr" ):
                return visitor.visitList_expr(self)
            else:
                return visitor.visitChildren(self)




    def list_expr(self):

        localctx = ZCodeParser.List_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_list_expr)
        try:
            self.state = 256
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 252
                self.expr()
                self.state = 253
                self.expr_tail()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 255
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(ZCodeParser.CM, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def expr_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_tail" ):
                return visitor.visitExpr_tail(self)
            else:
                return visitor.visitChildren(self)




    def expr_tail(self):

        localctx = ZCodeParser.Expr_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_expr_tail)
        try:
            self.state = 263
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 258
                self.match(ZCodeParser.CM)
                self.state = 259
                self.expr()
                self.state = 260
                self.expr_tail()
                pass
            elif token in [ZCodeParser.RSB, ZCodeParser.RRB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(ZCodeParser.BREAK, 0)

        def list_newline(self):
            return self.getTypedRuleContext(ZCodeParser.List_newlineContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = ZCodeParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.match(ZCodeParser.BREAK)
            self.state = 266
            self.list_newline()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(ZCodeParser.CONTINUE, 0)

        def list_newline(self):
            return self.getTypedRuleContext(ZCodeParser.List_newlineContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = ZCodeParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.match(ZCodeParser.CONTINUE)
            self.state = 269
            self.list_newline()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def list_newline(self):
            return self.getTypedRuleContext(ZCodeParser.List_newlineContext,0)


        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = ZCodeParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.match(ZCodeParser.RETURN)
            self.state = 273
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.SUB_OP) | (1 << ZCodeParser.NOT_OP) | (1 << ZCodeParser.LSB) | (1 << ZCodeParser.LRB) | (1 << ZCodeParser.BOOLLIT) | (1 << ZCodeParser.NUMBERLIT) | (1 << ZCodeParser.STRINGLIT) | (1 << ZCodeParser.IDENTIFIER))) != 0):
                self.state = 272
                self.expr()


            self.state = 275
            self.list_newline()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_call_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LRB(self):
            return self.getToken(ZCodeParser.LRB, 0)

        def RRB(self):
            return self.getToken(ZCodeParser.RRB, 0)

        def list_newline(self):
            return self.getTypedRuleContext(ZCodeParser.List_newlineContext,0)


        def list_expr(self):
            return self.getTypedRuleContext(ZCodeParser.List_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_func_call_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call_stmt" ):
                return visitor.visitFunc_call_stmt(self)
            else:
                return visitor.visitChildren(self)




    def func_call_stmt(self):

        localctx = ZCodeParser.Func_call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_func_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 278
            self.match(ZCodeParser.LRB)
            self.state = 281
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SUB_OP, ZCodeParser.NOT_OP, ZCodeParser.LSB, ZCodeParser.LRB, ZCodeParser.BOOLLIT, ZCodeParser.NUMBERLIT, ZCodeParser.STRINGLIT, ZCodeParser.IDENTIFIER]:
                self.state = 279
                self.list_expr()
                pass
            elif token in [ZCodeParser.RRB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 283
            self.match(ZCodeParser.RRB)
            self.state = 284
            self.list_newline()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LRB(self):
            return self.getToken(ZCodeParser.LRB, 0)

        def RRB(self):
            return self.getToken(ZCodeParser.RRB, 0)

        def list_expr(self):
            return self.getTypedRuleContext(ZCodeParser.List_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = ZCodeParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 287
            self.match(ZCodeParser.LRB)
            self.state = 290
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SUB_OP, ZCodeParser.NOT_OP, ZCodeParser.LSB, ZCodeParser.LRB, ZCodeParser.BOOLLIT, ZCodeParser.NUMBERLIT, ZCodeParser.STRINGLIT, ZCodeParser.IDENTIFIER]:
                self.state = 288
                self.list_expr()
                pass
            elif token in [ZCodeParser.RRB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 292
            self.match(ZCodeParser.RRB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def LRB(self):
            return self.getToken(ZCodeParser.LRB, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RRB(self):
            return self.getToken(ZCodeParser.RRB, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.StatementContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.StatementContext,i)


        def list_elif(self):
            return self.getTypedRuleContext(ZCodeParser.List_elifContext,0)


        def list_newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.List_newlineContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.List_newlineContext,i)


        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = ZCodeParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.match(ZCodeParser.IF)
            self.state = 295
            self.match(ZCodeParser.LRB)
            self.state = 296
            self.expr()
            self.state = 297
            self.match(ZCodeParser.RRB)
            self.state = 299
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 298
                self.list_newline()


            self.state = 301
            self.statement()
            self.state = 302
            self.list_elif()
            self.state = 308
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 303
                self.match(ZCodeParser.ELSE)
                self.state = 305
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 304
                    self.list_newline()


                self.state = 307
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_elifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elif_one(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_oneContext,0)


        def list_elif(self):
            return self.getTypedRuleContext(ZCodeParser.List_elifContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_list_elif

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_elif" ):
                return visitor.visitList_elif(self)
            else:
                return visitor.visitChildren(self)




    def list_elif(self):

        localctx = ZCodeParser.List_elifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_list_elif)
        try:
            self.state = 314
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 310
                self.elif_one()
                self.state = 311
                self.list_elif()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_oneContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def LRB(self):
            return self.getToken(ZCodeParser.LRB, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RRB(self):
            return self.getToken(ZCodeParser.RRB, 0)

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def list_newline(self):
            return self.getTypedRuleContext(ZCodeParser.List_newlineContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_one

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_one" ):
                return visitor.visitElif_one(self)
            else:
                return visitor.visitChildren(self)




    def elif_one(self):

        localctx = ZCodeParser.Elif_oneContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_elif_one)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self.match(ZCodeParser.ELIF)
            self.state = 317
            self.match(ZCodeParser.LRB)
            self.state = 318
            self.expr()
            self.state = 319
            self.match(ZCodeParser.RRB)
            self.state = 321
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 320
                self.list_newline()


            self.state = 323
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ZCodeParser.FOR, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExprContext,i)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def list_newline(self):
            return self.getTypedRuleContext(ZCodeParser.List_newlineContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = ZCodeParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_for_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.match(ZCodeParser.FOR)
            self.state = 326
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 327
            self.match(ZCodeParser.UNTIL)
            self.state = 328
            self.expr()
            self.state = 329
            self.match(ZCodeParser.BY)
            self.state = 330
            self.expr()
            self.state = 332
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 331
                self.list_newline()


            self.state = 334
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr1Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr1Context,i)


        def CONCAT_OP(self):
            return self.getToken(ZCodeParser.CONCAT_OP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = ZCodeParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_expr)
        try:
            self.state = 341
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 336
                self.expr1()
                self.state = 337
                self.match(ZCodeParser.CONCAT_OP)
                self.state = 338
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 340
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr2Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr2Context,i)


        def EQ(self):
            return self.getToken(ZCodeParser.EQ, 0)

        def EQ_OP(self):
            return self.getToken(ZCodeParser.EQ_OP, 0)

        def NEQ_OP(self):
            return self.getToken(ZCodeParser.NEQ_OP, 0)

        def LT_OP(self):
            return self.getToken(ZCodeParser.LT_OP, 0)

        def GT_OP(self):
            return self.getToken(ZCodeParser.GT_OP, 0)

        def LEQ_OP(self):
            return self.getToken(ZCodeParser.LEQ_OP, 0)

        def GEQ_OP(self):
            return self.getToken(ZCodeParser.GEQ_OP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




    def expr1(self):

        localctx = ZCodeParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 348
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 343
                self.expr2(0)
                self.state = 344
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.EQ_OP) | (1 << ZCodeParser.NEQ_OP) | (1 << ZCodeParser.LT_OP) | (1 << ZCodeParser.LEQ_OP) | (1 << ZCodeParser.GT_OP) | (1 << ZCodeParser.GEQ_OP) | (1 << ZCodeParser.EQ))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 345
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 347
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(ZCodeParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(ZCodeParser.Expr2Context,0)


        def AND_OP(self):
            return self.getToken(ZCodeParser.AND_OP, 0)

        def OR_OP(self):
            return self.getToken(ZCodeParser.OR_OP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 358
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 353
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 354
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND_OP or _la==ZCodeParser.OR_OP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 355
                    self.expr3(0) 
                self.state = 360
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(ZCodeParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(ZCodeParser.Expr3Context,0)


        def ADD_OP(self):
            return self.getToken(ZCodeParser.ADD_OP, 0)

        def SUB_OP(self):
            return self.getToken(ZCodeParser.SUB_OP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 369
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 364
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 365
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.ADD_OP or _la==ZCodeParser.SUB_OP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 366
                    self.expr4(0) 
                self.state = 371
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(ZCodeParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(ZCodeParser.Expr4Context,0)


        def MUL_OP(self):
            return self.getToken(ZCodeParser.MUL_OP, 0)

        def DIV_OP(self):
            return self.getToken(ZCodeParser.DIV_OP, 0)

        def MOD_OP(self):
            return self.getToken(ZCodeParser.MOD_OP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 380
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 375
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 376
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MUL_OP) | (1 << ZCodeParser.DIV_OP) | (1 << ZCodeParser.MOD_OP))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 377
                    self.expr5() 
                self.state = 382
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT_OP(self):
            return self.getToken(ZCodeParser.NOT_OP, 0)

        def expr5(self):
            return self.getTypedRuleContext(ZCodeParser.Expr5Context,0)


        def expr6(self):
            return self.getTypedRuleContext(ZCodeParser.Expr6Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = ZCodeParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_expr5)
        try:
            self.state = 386
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT_OP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 383
                self.match(ZCodeParser.NOT_OP)
                self.state = 384
                self.expr5()
                pass
            elif token in [ZCodeParser.SUB_OP, ZCodeParser.LSB, ZCodeParser.LRB, ZCodeParser.BOOLLIT, ZCodeParser.NUMBERLIT, ZCodeParser.STRINGLIT, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 385
                self.expr6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB_OP(self):
            return self.getToken(ZCodeParser.SUB_OP, 0)

        def expr6(self):
            return self.getTypedRuleContext(ZCodeParser.Expr6Context,0)


        def expr7(self):
            return self.getTypedRuleContext(ZCodeParser.Expr7Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = ZCodeParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_expr6)
        try:
            self.state = 391
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SUB_OP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 388
                self.match(ZCodeParser.SUB_OP)
                self.state = 389
                self.expr6()
                pass
            elif token in [ZCodeParser.LSB, ZCodeParser.LRB, ZCodeParser.BOOLLIT, ZCodeParser.NUMBERLIT, ZCodeParser.STRINGLIT, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 390
                self.expr7()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_index_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Array_index_exprContext,0)


        def factor(self):
            return self.getTypedRuleContext(ZCodeParser.FactorContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)




    def expr7(self):

        localctx = ZCodeParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_expr7)
        try:
            self.state = 395
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 393
                self.array_index_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 394
                self.factor()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBERLIT(self):
            return self.getToken(ZCodeParser.NUMBERLIT, 0)

        def BOOLLIT(self):
            return self.getToken(ZCodeParser.BOOLLIT, 0)

        def STRINGLIT(self):
            return self.getToken(ZCodeParser.STRINGLIT, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def arraylit(self):
            return self.getTypedRuleContext(ZCodeParser.ArraylitContext,0)


        def func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Func_callContext,0)


        def sub_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Sub_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_factor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = ZCodeParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_factor)
        try:
            self.state = 404
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 397
                self.match(ZCodeParser.NUMBERLIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 398
                self.match(ZCodeParser.BOOLLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 399
                self.match(ZCodeParser.STRINGLIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 400
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 401
                self.arraylit()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 402
                self.func_call()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 403
                self.sub_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sub_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LRB(self):
            return self.getToken(ZCodeParser.LRB, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RRB(self):
            return self.getToken(ZCodeParser.RRB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_sub_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSub_expr" ):
                return visitor.visitSub_expr(self)
            else:
                return visitor.visitChildren(self)




    def sub_expr(self):

        localctx = ZCodeParser.Sub_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_sub_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self.match(ZCodeParser.LRB)
            self.state = 407
            self.expr()
            self.state = 408
            self.match(ZCodeParser.RRB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_newlineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_list_newline

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_newline" ):
                return visitor.visitList_newline(self)
            else:
                return visitor.visitChildren(self)




    def list_newline(self):

        localctx = ZCodeParser.List_newlineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_list_newline)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 411 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 410
                    self.match(ZCodeParser.NEWLINE)

                else:
                    raise NoViableAltException(self)
                self.state = 413 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraylitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def itemlist(self):
            return self.getTypedRuleContext(ZCodeParser.ItemlistContext,0)


        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arraylit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraylit" ):
                return visitor.visitArraylit(self)
            else:
                return visitor.visitChildren(self)




    def arraylit(self):

        localctx = ZCodeParser.ArraylitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_arraylit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            self.match(ZCodeParser.LSB)
            self.state = 416
            self.itemlist()
            self.state = 417
            self.match(ZCodeParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ItemlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def item(self):
            return self.getTypedRuleContext(ZCodeParser.ItemContext,0)


        def CM(self):
            return self.getToken(ZCodeParser.CM, 0)

        def itemlist(self):
            return self.getTypedRuleContext(ZCodeParser.ItemlistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_itemlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitItemlist" ):
                return visitor.visitItemlist(self)
            else:
                return visitor.visitChildren(self)




    def itemlist(self):

        localctx = ZCodeParser.ItemlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_itemlist)
        try:
            self.state = 424
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 419
                self.item()
                self.state = 420
                self.match(ZCodeParser.CM)
                self.state = 421
                self.itemlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 423
                self.item()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arraylit(self):
            return self.getTypedRuleContext(ZCodeParser.ArraylitContext,0)


        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_item

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitItem" ):
                return visitor.visitItem(self)
            else:
                return visitor.visitChildren(self)




    def item(self):

        localctx = ZCodeParser.ItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_item)
        try:
            self.state = 428
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 426
                self.arraylit()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 427
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[37] = self.expr2_sempred
        self._predicates[38] = self.expr3_sempred
        self._predicates[39] = self.expr4_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




