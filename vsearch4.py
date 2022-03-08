def search4vowels(phrase:str) -> set:
        """Return any vowels found in a supplied word."""
        vowels = set('aeiou')
        return vowels.intersection(set(phrase))
