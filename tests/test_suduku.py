from sudoku.sudoku import Grid


class TestGrid:
    def test_it_accepts_a_complete_grid(self):
        grid = Grid([[1, 2, 3, 4], [4, 3, 2, 1]])
        assert grid.grid[0] == [1, 2, 3, 4]
        assert grid.grid[1] == [4, 3, 2, 1]

    def test_it_accepts_an_incomplete_grid(self):
        grid = Grid([[1, 2, None, None], [None, None, None, 1]])
        assert grid.grid[0] == [1, 2, None, None]
        assert grid.grid[1] == [None, None, None, 1]

    def test_it_can_set_a_cell(self):
        grid = Grid([[1, 2, None, None], [None, None, None, 1]])
        grid.set_cell(0, 2, 3)
        assert grid.grid[0] == [1, 2, 3, None]
        assert grid.grid[1] == [None, None, None, 1]

    def test_it_can_get_a_row(self):
        grid = Grid([[1, 2, None, 3], [None, None, None, 1]])
        assert grid.get_row(0) == [1, 2, None, 3]

    def test_it_can_get_a_column(self):
        grid = Grid([[1, 2, None, 3], [None, None, None, 1]])
        assert grid.get_col(1) == [2, None]

    def test_it_can_get_a_section(self):
        grid = Grid([
            [1, 2, 3, 4],
            [2, 3, 4, 1],
            [3, 4, 1, 2],
            [4, 1, 2, 3]
        ])
        assert grid.get_section(0, 2) == [[3, 4], [4, 1]]
