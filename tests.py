import unittest
from Puzzle import *

class TestCase(unittest.TestCase):

    def test_valid_board(self):
        B = []
        row_length = len(B[0])
        col_length = len([row[0] for row in B])
        self.assertEqual(
            row_length, col_length,
            msg='the matrix is not a square matrix. cols {} rows {}'.format(
                col_length, row_length
            )
        )

    def test_valid_source_vertex(self):



if __name__ == '__main__':
    unittest.main(verbosity=2)

# if __name__ == "__main__":

#     B = [['-','-','-','-','-'],
#         ['-','-','#','-','-'],
#         ['-','-','-','-','-'],
#         ['#','-','#','#','-'],
#         ['-','#','-','-','-']]

#     print(solve_puzzle(B, [1,1], [5,5]))