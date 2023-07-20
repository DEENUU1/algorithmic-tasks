class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        curr_line = []
        curr_len = 0

        for word in words:
            if curr_len + len(curr_line) + len(word) <= maxWidth:
                curr_line.append(word)
                curr_len += len(word)
            else:
                spaces_to_distribute = maxWidth - curr_len
                num_words = len(curr_line)

                if num_words == 1:
                    line = curr_line[0] + " " * spaces_to_distribute
                else:
                    spaces_between_words = spaces_to_distribute // (num_words - 1)
                    extra_spaces = spaces_to_distribute % (num_words - 1)
                    line = curr_line[0]
                    for i in range(1, num_words):
                        num_spaces = spaces_between_words + (1 if i <= extra_spaces else 0)
                        line += " " * num_spaces + curr_line[i]

                lines.append(line)
                curr_line = [word]
                curr_len = len(word)

        last_line = " ".join(curr_line)
        last_line += " " * (maxWidth - len(last_line))
        lines.append(last_line)

        return lines
