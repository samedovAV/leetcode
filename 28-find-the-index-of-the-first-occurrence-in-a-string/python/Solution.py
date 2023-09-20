def get_overlap_index(haystack: str, needle: str) -> int:
    haystack_length: int = haystack.__len__()
    needle_length: int = needle.__len__()

    if haystack_length < needle_length:
        return -1

    for i in range(haystack_length - needle_length):
        if haystack[i:i + needle_length] == needle:
            return i

    return -1
