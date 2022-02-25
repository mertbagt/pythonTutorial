def search4vowels(word):
        """Display a boolean based on any vowels found."""
        vowels = set('aeiou')
        found = vowels.intersection(set(word))
        return bool(found)
