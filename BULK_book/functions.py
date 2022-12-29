#function to call text underneath heading
def head2txt(document, heading, parnum):
    parlist = []
    paragraphs = list(document.paragraphs)
    for i in range(len(paragraphs)):
        if paragraphs[i].text.startswith(heading):
            for j in range(1,parnum+1):
                parlist.append(paragraphs[i+j].text)
            return parlist
                