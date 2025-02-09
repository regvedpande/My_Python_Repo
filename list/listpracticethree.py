def ransom_note(magazine, note):
    magazine_words = magazine.split()
    note_words = note.split()
    
    word_count = {}
    
    for word in magazine_words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    for word in note_words:
        if word in word_count and word_count[word] > 0:
            word_count[word] -= 1
        else:
            return False
    
    return True
