"""
Create a prefilled ballot with the specified names and footer lines
"""
import os


class Ballot:
    """
    header example 'ABC Corp, 700 20th St, Anytown, NY 11111'
    footer example 'Election Nov 15, 2021 for XXX Corp'
    voter_info example for CoOp 'Unit 4A, John Smith, 450 shares' also used to generate the filename for ballot
    candidates may include zero length strings.

    address may be just the unit number for an one apartment number
    """
    def __init__(self, header='Unnamed CoOp', footer='', voter_info='', signer_info='', candidates=None):
        self.header = header
        self.footer = footer
        self.voter_info = voter_info
        self.signer_info = signer_info
        self.candidates = [x for (i, x) in enumerate(candidates)]

    def save(self, dirpath, file_suffix='.txt'):
        filename = "".join([x for x in self.voter_info.upper() if x in "ABCDEFGHIJKLMNOPQRSTUVWXZ1234567890#_- "])\
            .replace(' ', '-').replace(',', '_') + file_suffix
        with open(os.path.join(dirpath, filename), "w") as f:
            if self.header:
                f.write(f'{self.header}\n\n\n')
            if self.voter_info:
                f.write(f'Voter Info: {self.voter_info}\n\n')
            f.write(f'Votes for:\n\n')
            f.writelines([f'\t({i+1}) {x}\n' for (i, x) in enumerate(self.candidates)])
            if self.footer:
                f.write(f'\n\n{self.footer}\n\n')
            if self.signer_info:
                f.write(f'Signed: {self.signer_info} ____________________________\n\n')
                f.write(f'Signature Date: ________________________\n\n')

