class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}

        for word in strs:
            # Anagrams have the same letters when sorted
            key = "".join(sorted(word))

            # Create a new group if this key hasn't appeared yet
            if key not in groups:
                groups[key] = []

            # Add the original word to its group
            groups[key].append(word)

        return list(groups.values())