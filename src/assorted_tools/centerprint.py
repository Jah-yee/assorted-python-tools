"""Print a string centered on the terminal, word wrapped and balanced across lines."""


import shutil

__all__ = ["centerprint"]


def _split_long_words(text, width):
    """Split text into words, breaking any word longer than width into equal pieces.

    :param text: the text to split.
    :param width: the longest a word or piece may be.
    :return: a tuple of the word list and a set of indexes. Each index marks a piece that
        continues a broken word, which must start a new line.
    """
    words = []
    breaks = set()
    for word in text.split():
        if len(word) <= width:
            words.append(word)
            continue

        pieces = -(-len(word) // width)
        size = -(-len(word) // pieces)
        for start in range(0, len(word), size):
            if start:
                breaks.add(len(words))
            words.append(word[start:start + size])
    return words, breaks


def _fits(breaks, start, end):
    """Return whether words start through end - 1 may share a line.

    :param breaks: indexes of words that must start a new line.
    :param start: index of the first word on the line.
    :param end: index one past the last word on the line.
    :return: true if no word after the first is a forced line start.
    """
    return not any(index in breaks for index in range(start + 1, end))


def _joined_width(words, start, end):
    """Return the width of words start through end - 1 joined by single spaces.

    :param words: the full word list.
    :param start: index of the first word.
    :param end: index one past the last word.
    """
    return sum(len(word) for word in words[start:end]) + (end - start - 1)


def _greedy_lines(words, breaks, width):
    """Wrap words into as few lines as possible.

    :param words: the full word list.
    :param breaks: indexes of words that must start a new line.
    :param width: the widest a line may be.
    :return: a list of lines.
    """
    lines = []
    start = 0
    end = 1
    while end <= len(words):
        if (end < len(words) and end not in breaks
                and _joined_width(words, start, end + 1) <= width):
            end += 1
            continue
        lines.append(" ".join(words[start:end]))
        start = end
        end += 1
    return lines


def _balanced_lines(words, breaks, count, limit):
    """Wrap words into exactly count lines with widths as even as possible.

    Uses dynamic programming to minimize the sum of squared line widths. Falls back to
    greedy wrapping if no layout with count lines fits.

    :param words: the full word list.
    :param breaks: indexes of words that must start a new line.
    :param count: the number of lines to produce.
    :param limit: the widest a line may be.
    :return: a list of lines.
    """
    total = len(words)
    huge = float("inf")
    best = [[huge] * (total + 1) for _ in range(count + 1)]
    cut = [[0] * (total + 1) for _ in range(count + 1)]

    for start in range(total):
        width = _joined_width(words, start, total)
        if width <= limit and _fits(breaks, start, total):
            best[1][start] = width ** 2

    for lines_left in range(2, count + 1):
        for start in range(total):
            for end in range(start + 1, total - lines_left + 2):
                width = _joined_width(words, start, end)
                if width > limit or not _fits(breaks, start, end):
                    break
                score = width ** 2 + best[lines_left - 1][end]
                if score < best[lines_left][start]:
                    best[lines_left][start] = score
                    cut[lines_left][start] = end

    if best[count][0] == huge:
        return _greedy_lines(words, breaks, limit)

    lines = []
    start = 0
    for lines_left in range(count, 0, -1):
        end = total if lines_left == 1 else cut[lines_left][start]
        lines.append(" ".join(words[start:end]))
        start = end
    return lines


def centerprint(string, whitespace="-", extra=" ", ret=False):
    """Print a string centered on the terminal.

    Text is wrapped to about three quarters of the terminal width across an odd number of
    lines, so that one line sits in the middle.

    :param string: the string to be printed.
    :param whitespace: the character to bound the middle-most line of text. Only the first
        character is used.
    :param extra: the character to bound all other lines of text. Only the first character
        is used.
    :param ret: if true, return the formatted string instead of printing it.
    :return: the formatted string if ret is true, otherwise None.
    """
    whitespace_to_text = 0.75

    columns = shutil.get_terminal_size().columns
    whitespace = (whitespace or " ")[0]
    extra = (extra or " ")[0]

    gap = " " if columns >= 3 else ""
    if gap:
        max_text = max(1, min(int(columns * whitespace_to_text), columns - 2))
    else:
        max_text = max(1, columns)

    chunk = max_text
    words, breaks = _split_long_words(string, chunk)

    if not words:
        line = whitespace * columns
        if ret:
            return line
        else:
            print(line)
        return None

    while True:
        fewest = len(_greedy_lines(words, breaks, max_text))
        count = fewest if fewest % 2 else fewest + 1
        if count <= len(words) or chunk <= 1:
            break
        chunk -= 1
        words, breaks = _split_long_words(string, chunk)

    lines = _balanced_lines(words, breaks, count, max_text)

    middle = len(lines) // 2
    built = []
    for index, line in enumerate(lines):
        fill = whitespace if index == middle else extra
        padding = max(0, columns - len(line) - 2 * len(gap))
        left = padding // 2
        right = padding - left
        built.append(f"{fill * left}{gap}{line}{gap}{fill * right}")

    text = "\n".join(built)
    if ret:
        return text
    else:
        print(text)
    return None
