def search4vowels(word):
        """Return any vowels found in a supplied word."""
        vowels = set('aeiou')
        return vowels.intersection(set(word))
