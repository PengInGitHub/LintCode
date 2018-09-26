/**
 * @param moves: a sequence of its moves
 * @return: if this robot makes a circle
 */
func judgeCircle2(moves string) bool {
	// Write your code here
	x, y := 0, 0
	for _, r := range moves {
		switch r {
		case 'L':
			x -= 1
		case 'R':
			x += 1
		case 'U':
			y -= 1
		default:
			y += 1
		}
	}
	if (x == 0) && (y == 0) {
		return true
	}
	return false
}

func judgeCircle(moves string) bool {
	x, y := 0, 0
	mapX := map[string]int{"L": -1, "R": 1}
	mapY := map[string]int{"U": -1, "D": 1}

	for _, move := range moves {
		x += mapX[string(move)]
		y += mapY[string(move)]
	}
	if (x == 0) && (y == 0) {
		return true
	}
	return false
}
