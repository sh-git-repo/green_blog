''' module for small helper functions and
    to un-clutter the views script.
'''

def set_active(page_no=0):
    ''' sets the css class active for the respective page. '''
    currently_active = ['active', '', '', '']

    currently_active = (
        currently_active[-page_no:]
        + currently_active[:-page_no]
    )

    return currently_active

def page_title(page_no=0):
    ''' returns the title for current page. '''
    title_list = (
        "HOME",
        "ABOUT",
        "LOGIN",
        "SIGNUP"
    )
    return title_list[page_no]


if __name__ == "__main__":

    def test_active():
        ''' Testing active_list(). '''
        for page in range(3):
            print(active_list(page))
    
    def test_title():
        ''' Test title(). '''
        for page in range(3):
            print(title(page))
    
    test_active()
    test_title()
