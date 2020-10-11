# Text Editor
"""
Given a string s representing characters typed into an editor, with "<-" representing a backspace, 
return the current state of the editor.
Example 1
Input
s = "abc<-z"
Output
"abz"
Explanation
The "c" got deleted by the backspace.

Example 2
Input
s = "<-x<-z<-"
Output
""
Explanation
All characters are deleted. Also note you can type backspace when the editor is empty as well.
"""

import unittest


def text_editor(s):
    temp_list=[]
    final_list=[]
    result_string=""
    for i in s:
        temp_list.append(i)
    for i in range(len(temp_list)):
        if (temp_list[i]!='<' and temp_list[i]!="-"):
            final_list.append(temp_list[i])
        elif(temp_list[i]=="-" and temp_list[i-1]!="<"):
            final_list.append(temp_list[i])
        elif(temp_list[i]=="<" and temp_list[i+1]!="-"):
            final_list.append(temp_list[i])
        elif(temp_list[i]=="<" and temp_list[i+1]=="-"):
            if(len(final_list)>=1):
                final_list.pop() 
    result_string="".join(final_list)
    result_string=str(result_string)
    return result_string


class TestTextEditor(unittest.TestCase):

    def test_1(self):
        self.assertEqual(text_editor("abc<-z"), "abz")

    def test_2(self):
        self.assertEqual(text_editor("<-x<-z<-"), "")

    def test_3(self):
        self.assertEqual(text_editor("ab<c<--"), "ab<-")

    def test_4(self):
        self.assertEqual(text_editor("ab<c<--<def<-<-<--"), "ab<-<-")


if __name__ == '__main__':
    unittest.main(verbosity=2)
