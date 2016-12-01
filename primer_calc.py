#!usr/bin/env python3
"""Primer Calculator and module

As a script, this program can be used to calculate useful properties
of a DNA primer such as the molecular weight, length, and GC content.
Also, a nicer representation of a primer sequence can be easily created
showing codons and dashes from a long, sequence of nucleotides.

As a module the Primer class is useful to represent DNA primers and access
the attributes of the primer instances.

"""


class Primer(object):

    """Representation of a DNA Primer.

    Create a Primer object using name (str) of the primer and a sequence
    (str) of the primer.

    Primer allows for useful calculations of primer properties as well as
    nice formatting of the primer sequence in codon form.

    """

    def __init__(self, name, sequence):
        """Initialize a primer object.

        name:     string, the name of the primer sequence object
                  eg. 'Gapdh Forward'

        sequence: string, the primer sequence from 5' to 3' (preferably)
                  eg. aaccgtagttctaaacg
                  note - anything besides the four NT bases is removed

        """
        super(Primer, self).__init__()
        self.name = name
        # perform a check on the input sequence
        # self.sequence will only contain 'a', 't', 'c', 'g'
        self.sequence = self.check_seq(sequence)
        # Create and store each NT and # in a dict
        self.nt = {'a': 0, 'c': 0, 'g': 0, 't': 0}
        for nucleotide in self.sequence.lower():
            try:
                self.nt[nucleotide] += 1
            except KeyError:
                pass
        # assign int attributes for each nucleotide
        self.num_a = self.nt['a']
        self.num_c = self.nt['c']
        self.num_g = self.nt['g']
        self.num_t = self.nt['t']
        # TODO add support for uracil? and RNA sequences?

    def check_seq(self, sequence):
        """Validate the sequence, keeeping only NTs.

        Remove anything from the input sequence that is not a nucleotide
        sequence: string, the initial user inputted sequence

        returns: string, the sequence only containing 'a', 'c', 'g', 't' bases

        """
        accept = ['a', 'c', 'g', 't']
        checked_seq = str()
        if type(sequence) == str:
            for char in sequence.lower():
                if char in accept:
                    checked_seq += char
        else:
            return "Invalid sequence entered"
        return checked_seq

    def calc_all(self):
        """Run all Primer property calculations.

        Helper function to perform all calulations of primer properties
        which then creates additional attributes on the primer object.

        returns: None

        """
        self.trip_split()
        self.mol_weight()
        self.gc_content()
        self.standard_tm()

    def trip_split(self):
        """Print sequence in codon, dash, codon format

        returns: None

        """
        s = self.sequence.upper()
        self.trip_upper = str()
        for i in range(0, len(s), 3):
            self.trip_upper += (s[i:i+3] + '-')

    def print_mw(self):
        """Print nice output of the primer's MW

        returns: None

        """
        self.mol_weight()
        print("{} daltons (g/M)".format(self.mw))
        # TODO refactor so that self.mo_weight() runs only if no self.mw
        #      attribute is assigned

    def print_gc(self):
        """Print nice output of the primer's GC % content.

        returns: None

        """
        self.gc_content()
        print("{} % GC".format(self.gc))
        # TODO refactor to only run gc_content calc method if no self.gc
        #      attribute is assigned.

    def print_info(self):
        """Calculate then print Primer info to console.

        Helper function that prints a nicely (for console) formatted info
        display about the primer object. Used when this program is run as
        a script.

        returns: None

        """
        # make sure that all calulations have been done
        self.calc_all()
        # print to console
        print()
        print("=" * 30, "{}".format(self.name), "=" * 30)
        print("Sequence:           5'-{}3'".format(self.trip_upper))
        print("Length:             {} nucleotides".format(self.__len__()))
        print("Molecular Weight:   {} daltons (g/M)".format(self.mw))
        print("GC Content:         {} % GC".format(self.gc))
        print("Standard Tm:        {} ºC".format(self.std_tm))
        print("=" * (62 + len(self.name)))
        print()

    def mol_weight(self):
        """Calculate the molecular weight of the primer.

        returns: self.mw attribute as float if sequence contains >0 NT's
                 self.mw set to string "Invalid" if 0 NT's

        """
        if self.__len__() > 0:
            mw_calc = [313.2 * self.num_a,
                       328.2 * self.num_g,
                       289.2 * self.num_c,
                       304.2 * self.num_t,
                       -60.96]
            self.mw = round(sum(mw_calc), 3)
        else:
            self.mw = "Invalid"

    def gc_content(self):
        """Calculate the % GC content of the primer

        returns: self.gc attribute as float if sequence contains >0 NT's
                 self.gc set to string "Invalid" if 0 NT's

        """
        if self.__len__() > 0:
            self.gc = round(100*((self.num_g+self.num_c)/self.__len__()), 2)
        else:
            self.gc = "Invalid"

    def standard_tm(self):
        """Calculate the standard Tm of the primer

        (not taking in accountsalt concentrations).

        returns: self.std_tm attribute as float if sequence contains >0 NT's
                 self.std_tm set to string "Invalid" if 0 NT's

        """
        if self.__len__() > 0:
            if self.__len__() < 14:
                calc = [2 * (self.num_a + self.num_t),
                        4 * (self.num_g + self.num_c)]
                self.std_tm = round(sum(calc), 2)
            else:
                calc = [64.9,
                        41 * ((self.num_g+self.num_c-16.4)/self.__len__())]
                self.std_tm = round(sum(calc), 2)
        else:
            self.std_tm = "Invalid"

    def __len__(self):
        """returns length (in nucleotides) of the primer sequence."""
        return sum(self.nt.values())

    def __str__(self):
        """Prints: 'Name: 5'-sequence-3'"""
        self.trip_split()
        return "{0}: 5'-{1}3'".format(self.name, self.trip_upper)

    # TODO add different TM calculation options
    #      ability to factor in/change salt conc.


def main():
    """main function, executed if this module is run as a terminal script
    asks for a user to input a primer name and sequence.
    Creates a new primer object and prints to console info about the primer.

    returns: None

    """
    def get_primer():
        """Get user input of the primer's name"""
        primer = input("Enter your primer name, 'exit' or 'q' to quit.\nName > ")
        if primer.lower() in exit_keys:
            return False
        else:
            return primer

    def get_sequence():
        """Get user input of the primer's sequence"""
        seq = input("Enter your primer sequence\nSequence > ")
        return seq

    def primer_script_print(p, s):
        """Create a Primer object and print it's info

        p: string, the primer name
        s: string, the primer's nucleotide sequence

        creates a Primer object named 'p' with sequence 's'
        prints info to console about the primer

        """
        my_primer = Primer(p, s)
        my_primer.print_info()

    # exit keywords, if a primer is named one of these the program terminates
    exit_keys = ["exit", "q"]
    # get user inputted primer name and assign it to primer
    primer = get_primer()
    # if primer is a non-empty string, or not an exit word: while loop runs
    while primer:
        # get the primer's sequence
        sequence = get_sequence()
        # calculate the primer properties and output to console
        primer_script_print(primer, sequence)
        # get a new primer name or allow the user to enter an exit keyword
        primer = get_primer()
    print("Exiting...")


if __name__ == '__main__':
    # only run main function if this program run as a script
    main()
