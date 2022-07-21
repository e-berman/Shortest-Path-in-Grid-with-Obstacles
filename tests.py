import unittest
from Puzzle import *

class TestCase(unittest.TestCase):

    def test_valid_board(self):
        B = [['-','-','-'],
             ['#','_','-'],
             ['-','#','-']]

        # returns tuple of (row_length, col_length)
        row_cols = check_valid_board_dimensions(B)

        self.assertGreaterEqual(
            row_cols[0], 3,
            msg='the row length is not at least 3. Length {}'.format(
                row_cols[0]
            ))
        self.assertGreaterEqual(
            row_cols[1], 3,
            msg='the col length is not at least 3. Length {}'.format(
                row_cols[1]
            ))
    
    def test_invalid_board(self):
        
        B = [['-','-'],
             ['#','-']]

        with self.assertRaises(ValueError):
            check_valid_board_dimensions(B)   

    def test_invalid_source_vertex_index(self):
        B = [['-','-','-','-','-'],
             ['-','-','#','-','-'],
             ['-','-','-','-','-'],
             ['#','-','#','#','-'],
             ['-','#','-','-','-']]

        source = [-1,1]
        destination = [3,3]

        with self.assertRaises(IndexError):
            check_source_destination_vertices(B, source, destination, check_valid_board_dimensions(B))

        source = [6,1]
        destination = [3,3]

        with self.assertRaises(IndexError):
            check_source_destination_vertices(B, source, destination, check_valid_board_dimensions(B))
        
        source = [2,3]
        destination = [3,3]

        with self.assertRaises(ValueError):
            check_source_destination_vertices(B, source, destination, check_valid_board_dimensions(B))
        
    def test_invalid_destination_vertex(self):
        B = [['-','-','-','-','-'],
             ['-','-','#','-','-'],
             ['-','-','-','-','-'],
             ['#','-','#','#','-'],
             ['-','#','-','-','-']]

        source = [1,3]
        destination = [-1,5]

        with self.assertRaises(IndexError):
            check_source_destination_vertices(B, source, destination, check_valid_board_dimensions(B))

        source = [1,3]
        destination = [6,1]

        with self.assertRaises(IndexError):
            check_source_destination_vertices(B, source, destination, check_valid_board_dimensions(B))

        source = [1,1]
        destination = [2,3]

        with self.assertRaises(ValueError):
            check_source_destination_vertices(B, source, destination, check_valid_board_dimensions(B))

    def test_valid_moves(self):
        B = [['-','-','-','-','-'],
             ['-','-','#','-','-'],
             ['-','-','-','-','-'],
             ['#','-','#','#','-'],
             ['-','#','-','-','-']]

        self.assertEqual(
            solve_puzzle(B, [1,3], [3,3]), 3,
            msg='Expected number of moves incorrect. num moves taken {} expected {}'.format(
                solve_puzzle(B, [1,3], [3,3]), 3
            ))
        
        self.assertEqual(
            solve_puzzle(B, [1,1], [5,5]), 7,
            msg='Expected number of moves incorrect. num moves taken {} expected {}'.format(
                solve_puzzle(B, [1,1], [5,5]), 7
            ))

    def test_invalid_move_return_none(self):
        '''In case destination vertex is unable to be reached, returns None'''

        B = [['-','-','-','-','-'],
             ['-','-','#','-','-'],
             ['-','-','-','-','-'],
             ['#','-','#','#','-'],
             ['-','#','-','-','-']]

        self.assertIsNone(
            solve_puzzle(B, [1,1], [5,1]),
            msg='None is not return when expected. Val returned {}'.format(
                solve_puzzle(B, [1,1], [5,1])
            ))

if __name__ == '__main__':
    unittest.main(verbosity=2)