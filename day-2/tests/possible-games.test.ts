import { describe, expect, test } from '@jest/globals'
import { possibleGames } from '../src/possible-games'

const cubes = {
	'red': 12,
	'green': 13,
	'blue': 14
}

describe('Possible Games', () => {
	test('Test Input', () => {
		expect(possibleGames(cubes, './tests/inputs/test-input.txt')).toBe(8)
	})
})