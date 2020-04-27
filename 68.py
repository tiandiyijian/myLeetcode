class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []
        current_length = 0
        row = []
        for word in words:
            if len(word) < maxWidth - current_length:
                row.append(word)
                row.append('')
                print(row)
                current_length += (len(word) + 1)
            elif len(word) == maxWidth - current_length:
                row.append(word)
                res.append(''.join(row))
                print(res[-1])
                row = []
                current_length = 0
            else:
                self.handlerow(row, maxWidth)
                res.append(''.join(row))
                print(res[-1])
                row = []
                current_length = 0
                if len(word) < maxWidth:
                    row.append(word)
                    row.append(' ')
                    current_length = len(word) + 1
                elif len(word) == maxWidth:
                    res.append(word)
        if len(row) == 0:
            return res
        length_of_last_row = 0
        for i in range(len(row) - 1):
            length_of_last_row += len(row[i])
        row[-1] = ' ' * (maxWidth - length_of_last_row)
        res.append(''.join(row))
        return res

    def handlerow(self, row, maxwidth):
        if len(row) == 2:
            row[1] = ' ' * (maxwidth - len(row[0]))
        elif len(row) > 2:
            number_of_blank = int(len(row) / 2 - 1)
            print('number_of_blank: ', number_of_blank)
            row.pop()
            length_of_words = 0
            i = 0
            while i < len(row):
                length_of_words += len(row[i])
                i += 2
            length_of_blanks = maxwidth - length_of_words
            print('length_of_blanks: ', length_of_blanks)
            length_of_each_block = int(length_of_blanks / number_of_blank)
            print('length_of_each_block: ', length_of_each_block)
            left = length_of_blanks % number_of_blank
            print('left: ', left)
            i = 1
            front = 0
            while i < len(row) and front < left:
                row[i] = ' ' * (length_of_each_block + 1)
                i += 2
                front += 1
            while i < len(row):
                row[i] = ' ' * length_of_each_block
                i += 2


