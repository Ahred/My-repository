def areYouPlayingBanjo(name):
    if name[0].lower() == 'r':
        return(name + ' plays banjo')
    else:
        return(name + ' does not play banjo')


#    return ((name + ' plays banjo') if name[0].lower() == 'r' else (name + ' does not play banjo'))