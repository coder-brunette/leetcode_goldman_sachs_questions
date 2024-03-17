# Given a C++ program, remove comments from it. The program source is an array of strings source where source[i] is the ith 
# line of the source code. This represents the result of splitting the original source code string by the newline character 
# '\n'.

# Input: source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]
# Output: ["int main()","{ ","  ","int a, b, c;","a = b + c;","}"]
# Explanation: The line by line code is visualized as below:
# /*Test program */
# int main()
# { 
#   // variable declaration 
# int a, b, c;
# /* This is a test
#    multiline  
#    comment for 
#    testing */
# a = b + c;
# }
# The string /* denotes a block comment, including line 1 and lines 6-9. The string // denotes line 4 as comments.
# The line by line output code is visualized as below:
# int main()
# { 
  
# int a, b, c;
# a = b + c;
# }


class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        final = []
        in_block_comment = False
        current_line = ""

        for line in source:
            i = 0
            while i < len(line):
                if not in_block_comment and line[i:i+2] == '/*':
                    in_block_comment = True
                    i += 1
                elif in_block_comment and line[i:i+2] == '*/':
                    in_block_comment = False
                    i += 1
                elif not in_block_comment and line[i:i+2] == '//':
                    break
                elif not in_block_comment:
                    current_line += line[i]
                i += 1
            if not in_block_comment and current_line:
                final.append(current_line)
                current_line = ""
        return final