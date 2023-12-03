import { describe, expect, test } from '@jest/globals'
import { requiredCubes } from '../src/required-cubes'

describe('Required Cubes', () => {
	test('Test Input', () => {
		expect(requiredCubes('./tests/inputs/test-input.txt')).toBe(2286)
	})
})