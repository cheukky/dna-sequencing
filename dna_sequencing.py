import sys


def dna_sequencing(sequence):
    '''This function calculates the statistics of the string and returns a
    dictionary of the output.'''
    result = dict()

    a_counter = 0
    c_counter = 0
    g_counter = 0
    t_counter = 0
    other_counter = 0

    a_consec = 0
    a_maxconsec = 0
    c_consec = 0
    c_maxconsec = 0
    g_consec = 0
    g_maxconsec = 0
    t_consec = 0
    t_maxconsec = 0

    a_percent = 0.0
    c_percent = 0.0
    g_percent = 0.0
    t_percent = 0.0
    other_percent = 0.0

    for letter in sequence:
        if letter == "A" or letter == 'a':
            a_counter += 1
            a_consec += 1

            if(c_consec > c_maxconsec):
                c_maxconsec = c_consec
            c_consec = 0

            if(g_consec > g_maxconsec):
                g_maxconsec = g_consec
            g_consec = 0

            if(t_consec > t_maxconsec):
                t_maxconsec = t_consec
            t_consec = 0
        else:
            if(a_consec > a_maxconsec):
                a_maxconsec = a_consec
            a_consec = 0

    # consecutive
    if(a_consec > a_maxconsec):
        a_maxconsec = a_consec
    if(c_consec > c_maxconsec):
        c_maxconsec = c_consec
    if(g_consec > g_maxconsec):
        g_maxconsec = g_consec
    if(t_consec > t_maxconsec):
        t_maxconsec = t_consec

    # percentages
    if len(sequence) > 0:
        a_percent = a_counter/len(sequence)

    result["A"] = a_counter
    result["C"] = c_counter
    result["G"] = g_counter
    result["T"] = t_counter
    result["Other"] = other_counter

    result["Max consecutive As"] = a_maxconsec
    result["Max consecutive Cs"] = c_maxconsec
    result["Max consecutive Gs"] = g_maxconsec
    result["Max consecutive Ts"] = t_maxconsec

    result["Percentage of As"] = a_percent
    result["Percentage of Cs"] = c_percent
    result["Percentage of Gs"] = g_percent
    result["Percentage of Ts"] = t_percent
    result["Percentage of other characters"] = other_percent

    print("Number of As: "+str(result["A"]))

    print("Greatest number of consecutive As: " + str(result["Max consecutive As"]))

    print("Percentage of As:"+str(result["Percentage of As"]))

    return result


dna_sequencing(sys.argv[1])
