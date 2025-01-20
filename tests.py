import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, animate=False)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )

    def test_maze_small(self):
        num_cols = 5
        num_rows = 3
        m2 = Maze(0, 0, num_rows, num_cols, 20, 20, None, animate=False)
        self.assertEqual(
            len(m2._cells),
            num_rows, 
        )
        self.assertEqual(
            len(m2._cells[0]),
            num_cols,
        )

    def test_maze_large(self):
        num_cols = 100
        num_rows = 50
        m3 = Maze(0, 0, num_rows, num_cols, 5, 5, None, animate=False)
        self.assertEqual(
            len(m3._cells),
            num_rows,
        )
        self.assertEqual(
            len(m3._cells[0]),
            num_cols,
        )

    def test_maze_entrance_and_exit(self):
        num_cols = 5
        num_rows = 3
        m2 = Maze(0, 0, num_rows, num_cols, 20, 20, None, animate=False)
        
        # Test entrance
        entrance = m2._cells[0][0]
        self.assertFalse(
            entrance.has_top_wall,
            "Entrance cell should have its top wall removed.",
        )

        # Test exit
        exit_cell = m2._cells[num_rows - 1][num_cols - 1]
        self.assertFalse(
            exit_cell.has_bottom_wall,
            "Exit cell should have its bottom wall removed.",
        )

    def test_maze_large_with_entrance_exit(self):
        num_cols = 100
        num_rows = 50
        m3 = Maze(0, 0, num_rows, num_cols, 5, 5, None, animate=False)

        # Test entrance
        entrance = m3._cells[0][0]
        self.assertFalse(
            entrance.has_top_wall,
            "Entrance cell should have its top wall removed.",
        )

        # Test exit
        exit_cell = m3._cells[num_rows - 1][num_cols - 1]
        self.assertFalse(
            exit_cell.has_bottom_wall,
            "Exit cell should have its bottom wall removed.",
        )

if __name__ == "__main__":
    unittest.main()

