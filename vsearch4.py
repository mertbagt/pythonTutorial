def search4vowels(phrase:str) -> set:
        """Return any vowels found in a 'phrase'."""
        vowels = set('aeiou')
        return vowels.intersection(set(phrase))
