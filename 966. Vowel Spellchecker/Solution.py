class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        exact_words = set(wordlist)
        case_map = {}
        vowel_map = {}

        def mask_vowels(word: str) -> str:
            return ''.join('*' if c in "aeiou" else c for c in word)

        # Build maps
        for word in wordlist:
            lower = word.lower()
            case_map.setdefault(lower, word)          # only first occurrence
            vowel_map.setdefault(mask_vowels(lower), word)

        result = []
        for query in queries:
            if query in exact_words:                        # exact match
                result.append(query)
            elif query.lower() in case_map:                 # case-insensitive match
                result.append(case_map[query.lower()])
            elif mask_vowels(query.lower()) in vowel_map:   # vowel-error match
                result.append(vowel_map[mask_vowels(query.lower())])
            else:
                result.append("")                           # no match
        return result
